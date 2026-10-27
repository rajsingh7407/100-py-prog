"""Self-checking helpers for the exercises in the Python course notebooks.

Typical use, at the top of a notebook::

    import sys
    sys.path.insert(0, "../src")
    from course_tools import check, check_output

Then, after an exercise::

    check(total, 42, hint="Did you add all three numbers?")
    check_output("Hello, Ada!", inputs=["Ada"])

Nothing here is meant to be clever: each helper prints a short, friendly
verdict and never raises, so a wrong answer never stops "Run All".
"""

import builtins
import contextlib
import io
import linecache
import math
import random
import re
import sys

__all__ = ["check", "check_output"]

_PASS = "✅ Correct!"


def _show(value):
    """repr() for display, shortened if it is very long."""
    text = repr(value)
    return text if len(text) <= 300 else text[:300] + "..."


def _fail(lines, hint, label=None):
    print(f"❌ {label}: not quite." if label else "❌ Not quite.")
    for line in lines:
        print("   " + line)
    if hint:
        print("💡 Hint:", hint)


def _caller_label(depth=2):
    """The text of the first argument in the line that called check(), e.g. 'total'."""
    try:
        frame = sys._getframe(depth)
        line = linecache.getline(frame.f_code.co_filename, frame.f_lineno)
        match = re.search(r"\bcheck\(\s*([A-Za-z_][\w.\[\]]*)\s*,", line)
        return match.group(1) if match else None
    except Exception:  # noqa: BLE001 - a missing label is never worth an error
        return None


def check(actual, expected, hint=None, tol=1e-9):
    """Compare ``actual`` (your answer) with ``expected`` and say how it went.

    Types matter: ``5`` and ``5.0`` are different answers, and so are ``5`` and
    ``"5"``. Floats are compared with a tolerance of ``tol`` so that tiny
    rounding noise (see the Numbers notebook) does not count as a mistake.
    """
    label = _caller_label()
    if actual is None and expected is not None:
        _fail(["Your answer is still None. Replace the placeholder with your solution."], hint, label)
        return

    # Exact types matter: 5 vs 5.0, 5 vs "5" and True vs 1 are all different answers.
    if type(actual) is not type(expected):
        _fail(
            [
                f"Expected a value of type {type(expected).__name__}.",
                f"Your answer has type {type(actual).__name__}: {_show(actual)}",
            ],
            hint,
            label,
        )
        return

    if isinstance(actual, float):
        ok = math.isclose(actual, expected, rel_tol=tol, abs_tol=tol)
    else:
        ok = actual == expected

    if ok:
        print(f"✅ {label} is correct!" if label else _PASS)
    else:
        _fail([f"Expected: {_show(expected)}", f"You got:  {_show(actual)}"], hint, label)


def _last_cell_source():
    """Source of the most recent cell that ran before the current one and is not a check cell."""
    try:
        ip = get_ipython()  # noqa: F821  (defined inside Jupyter/IPython)
    except NameError:
        return None, None
    history = ip.user_ns.get("In", [])
    for source in reversed(history[:-1]):
        stripped = source.strip()
        if stripped and not stripped.startswith("check"):
            return ip, source
    return ip, None


def _normalise(text):
    lines = [line.rstrip() for line in text.rstrip().split("\n")]
    return "\n".join(lines)


def check_output(expected, inputs=None, hint=None, seed=None):
    """Re-run your most recent code cell and compare what it prints with ``expected``.

    - ``inputs``: answers handed to ``input()``, in order, so you do not have to type them.
      (The prompt text itself is not part of the captured output.)
    - ``seed``: seeds the ``random`` module first, so programs that use random numbers
      behave predictably.

    Trailing spaces and trailing blank lines are ignored; everything else must match.
    """
    ip, source = _last_cell_source()
    if ip is None:
        print("⚠️  check_output only works inside a Jupyter notebook.")
        return
    if source is None:
        print("⚠️  Run the cell with your code first, then run this check cell.")
        return

    queue = list(inputs or [])

    def fake_input(prompt=""):
        if not queue:
            raise EOFError("your program asked for more input than the check supplied")
        return queue.pop(0)

    buffer = io.StringIO()
    real_input = builtins.input
    problem = None
    builtins.input = fake_input
    try:
        if seed is not None:
            random.seed(seed)
        code = compile(ip.transform_cell(source), "<your cell>", "exec")
        with contextlib.redirect_stdout(buffer):
            exec(code, ip.user_ns)
    except BaseException as error:  # noqa: BLE001 - we want to report anything the student's code raised
        problem = f"{type(error).__name__}: {error}"
    finally:
        builtins.input = real_input

    first_line = source.strip().split("\n")[0]
    got = _normalise(buffer.getvalue())
    want = _normalise(expected)

    if problem is None and got == want:
        print(_PASS)
        return

    print("❌ Not quite.")
    print(f"   (I ran your most recent code cell, the one starting with: {first_line[:60]!r})")
    if inputs:
        print(f"   Inputs supplied: {list(inputs)}")
    if problem:
        print(f"   Your code stopped with an error: {problem}")
    print("   Expected output:")
    print(_indent(want))
    print("   Your output:")
    print(_indent(got))
    if problem is None:
        expected_lines, got_lines = want.split("\n"), got.split("\n")
        for number, (a, b) in enumerate(zip(expected_lines, got_lines), start=1):
            if a != b:
                print(f"   First difference is on output line {number}.")
                break
        else:
            print("   The outputs differ in length: one has extra or missing lines.")
    if hint:
        print("💡 Hint:", hint)


def _indent(text):
    if not text:
        return "      (nothing was printed)"
    return "\n".join("      |" + line for line in text.split("\n"))
