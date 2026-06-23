# 003 — Python Statements

- Source: https://www.w3schools.com/python/python_statements.asp
- Date: 2026-06-19

## Key ideas

- A **statement** is a single instruction that Python executes — one "thing to
  do". A program is just a list of statements run by the computer.
- In Python a statement **normally ends at the end of the line** — no semicolon
  needed (unlike Java or C, where every statement ends with `;`).
- A program usually has **many statements**, and they run **in order, top to
  bottom** — the sequence you write them in is the sequence they happen in.
- **Semicolons are optional and rarely used.** You *can* put several statements
  on one line by separating them with `;`, but it hurts readability, so the
  normal style is **one statement per line**.

## Examples

```python
# A single statement
print("Python is fun!")
```

```python
# Many statements — they run in the order written
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
```

```python
# Allowed but discouraged: several statements on one line using semicolons
print("Hello"); print("How are you?"); print("Bye bye!")
```

## Gotchas

- Two statements on the same line **without** a separating semicolon is an
  error:

  ```python
  print("Python is fun!") print("Really!")   # SyntaxError: invalid syntax
  ```

- Just because semicolons are *allowed* doesn't mean I should use them — one
  statement per line is the readable, normal way.

## Practice

Make `practical/We3Schools/003_statements.py` with three `print()` statements on
separate lines, run it, and confirm they appear in order:

```powershell
python practical/We3Schools/003_statements.py
```

Then try squeezing two of them onto one line with `;`, and again *without* the
`;`, to see the `SyntaxError`.

## Takeaways

1. A statement = one instruction; statements run top to bottom in order.
2. No semicolons needed in Python — line endings end statements.
3. One statement per line is the clean, standard style.
