# 001 — Python Intro

- Source: https://www.w3schools.com/python/python_intro.asp
- Date: 2026-06-19

## Key ideas

- **Python** is a popular general-purpose programming language, created by
  **Guido van Rossum** and released in **1991**.
- It's used for:
  - **Web / server-side** development (back-end of websites).
  - **Software development** and scripting (automating tasks).
  - **Math & data** work.
  - **System scripting** (telling the computer to do jobs for you).
- Why people like Python:
  - Runs on many platforms (Windows, Mac, Linux, Raspberry Pi…).
  - **Simple, English-like syntax** — easy to read and write.
  - Lets you write programs in **fewer lines** than many other languages.
  - Runs on an **interpreter**, so code executes line by line — you can test
    ideas quickly without a separate "compile" step.

## How Python runs (my terminal notes)

- Python is **interpreted**: a program called the interpreter reads my file and
  runs it top to bottom, one line at a time.
- To run a script on my machine (Windows + PowerShell):

  ```powershell
  python hello.py
  ```

  `pip` is NOT for running code — it only installs extra libraries.

## Examples

```python
print("Hello, World!")
```

My own first program in [`../../practical/hello.py`](../../practical/hello.py):

```python
print("dobro jutro življenje, lahko noč negativa")
```

`print()` sends text to the screen (standard output).

## Gotchas

- Tried `pip hello.py` first — wrong tool. `pip` = package installer,
  `python` = the thing that actually runs my code.
- The terminal has to be in the same folder as the file (or I give the full
  path), otherwise Python can't find it.

## Practice

- [`../../practical/hello.py`](../../practical/hello.py) — first `print()` statement.

## Takeaways

1. Python = simple, readable, interpreted language.
2. Run a file with `python file.py` (not `pip`).
3. `print()` is how I show output.
