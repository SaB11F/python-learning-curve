# 002 — Python Syntax

- Source: https://www.w3schools.com/python/python_syntax.asp
- Date: 2026-06-19

## Key ideas

- **Two ways to run Python code:**
  1. Directly in the command line / interactive prompt (lines start with `>>>`).
  2. By saving code in a `.py` file and running it, e.g. `python myfile.py`.
- **Indentation matters in Python.** In most languages indentation is just for
  looks; in Python it's part of the syntax — it's how Python knows which lines
  belong to a block of code.
  - You need **at least one space**, but **4 spaces is the common standard**.
  - The indentation must be **consistent within the same block** — every line
    in the block uses the same number of spaces.
- **Variables** are created the moment you assign a value. There's no separate
  "declare a variable" command like in some languages — `x = 5` is all it takes.
- **Comments** start with `#`. Everything after `#` on that line is ignored by
  Python; it's just notes for humans reading the code.

## Examples

```python
# Indentation marks the block that belongs to the if-statement
if 5 > 2:
    print("Five is greater than two!")
```

```python
# Creating variables (no declaration needed)
x = 5
y = "Hello, World!"
```

```python
#This is a comment.
print("Hello, World!")
```

## Gotchas

- **Forgetting to indent** the body of an `if` (or any block) is an error:

  ```python
  if 5 > 2:
  print("Five is greater than two!")   # IndentationError / SyntaxError
  ```

- **Mixing indent sizes in the same block** (e.g. 2 spaces on one line, 4 on the
  next) also errors out. Pick one — I'm using 4 — and stick to it.

## Practice

Make `practical/We3Schools/002_syntax.py` with an `if`-block, a variable, and a
comment, then run it:

```powershell
python practical/We3Schools/002_syntax.py
```

Then **break it on purpose**: remove the indentation and re-run it to see the
`IndentationError` for yourself.

## Takeaways

1. Indentation isn't optional in Python — it defines code blocks (use 4 spaces).
2. Variables just need a value assigned: `x = 5`. No declaration step.
3. `#` starts a comment.
