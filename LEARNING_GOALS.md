# Python + OOP Roadmap — Rene

- **Owner:** Rene Kolednik
- **Mentors:** Jakob (lead) · Tadej (manager / co-mentor)
- **Created:** 2026-06-22
- **Priority:** #1 — Python + OOP fundamentals
- **Plan:** 30 days · ~8 h/day · **CS50P (Harvard)** + **Exercism** + practice in this repo
- **Target window:** 2026-06-22 → 2026-07-21 (dates are targets — I'll shift for rest days)

> I can explain and defend every goal, estimate, and line of code here without AI.

---

## How I work each day (~8 h)
- **~3 h** new material — CS50P lecture + take notes.
- **~4 h** hands-on — CS50P problem set + Exercism exercises + a practice script in this repo.
- **~1 h** review — write notes in `docs/` and explain the day's concept in my own words.
- **Rule:** every script I write, I can walk through line-by-line without AI.

## Resources
- **Course:** CS50P — https://cs50.harvard.edu/python/
- **Practice:** Exercism Python track — https://exercism.org/tracks/python
- **Reference:** W3Schools — https://www.w3schools.com/python/ · deep dives: https://realpython.com
- **Testing:** pytest — https://docs.pytest.org (CS50P Week 5)

## Starting self-assessment — 2026-06-22 (Conf 1–5)
| Area | Lowest-confidence topics (my weak spots) |
| --- | --- |
| Core syntax | loops (1), lists/tuples/sets/dicts (1), if/elif/else (2) |
| Functions/toolkit | functions, scope, files, idioms (0) |
| OOP | almost everything (0–1) — concepts known from C++, Python syntax is new |
| Testing | pytest (0) |

---

## The 30-Day Roadmap

### Week 1 — Python core (Days 1–7 · Jun 22–28)
**Goal:** comfortably write small scripts with variables, conditionals, loops, and collections.

| Day | Focus | CS50P | Practice (Exercism + repo) | Output |
| --- | --- | --- | --- | --- |
| 1 (Jun 22) | Setup + Functions & Variables | Lecture 0 | 1–2 intro exercises; rewrite small functions | `docs/004` + practice file |
| 2 (Jun 23) | Conditionals | Lecture 1 + pset | conditionals exercises | practice file |
| 3 (Jun 24) | Data types, casting, operators | — | W3Schools + Real Python; small drills | notes |
| 4 (Jun 25) | Loops (for, while, range) | Lecture 2 + pset | loop exercises | practice file |
| 5 (Jun 26) | Lists & tuples | — | iterate/build lists; Exercism list track | practice file |
| 6 (Jun 27) | Dicts & sets | — | small program using a dict | practice file |
| 7 (Jun 28) | **Review + mini-project** | finish psets | menu/text program combining all of Week 1 | mini-project + notes |

### Week 2 — Functions, errors, libraries, files, idioms (Days 8–14 · Jun 29–Jul 5)
**Goal:** write reusable functions, handle errors, use modules, read/write files, start thinking Pythonic.

| Day | Focus | CS50P | Practice (Exercism + repo) | Output |
| --- | --- | --- | --- | --- |
| 8 (Jun 29) | Functions deep: params, defaults, return, `*args/**kwargs` | review L0 | refactor Day-7 project into functions | practice file |
| 9 (Jun 30) | Scope (local/global) | — | scope drills | notes |
| 10 (Jul 1) | Exceptions | Lecture 3 + pset | `try/except/raise` exercises | practice file |
| 11 (Jul 2) | Libraries, modules, pip | Lecture 4 + pset | use `random`/`statistics`; write own module | practice file |
| 12 (Jul 3) | File I/O | Lecture 6 + pset | read/write a text + CSV file | practice file |
| 13 (Jul 4) | Pythonic idioms: comprehensions, f-strings, `enumerate`, `zip`, unpacking | — | rewrite earlier loops as comprehensions | practice file |
| 14 (Jul 5) | **Review + mini-project** | finish psets | read file → process with functions + exceptions → write output | mini-project + notes |

### Week 3 — Testing + OOP (Days 15–21 · Jul 6–12)
**Goal:** write & read tests, and build classes confidently. *(Goal 3 + exit criteria.)*

| Day | Focus | CS50P | Practice (Exercism + repo) | Output |
| --- | --- | --- | --- | --- |
| 15 (Jul 6) | **Unit testing with pytest** | Lecture 5 + pset | write tests for Week-2 functions | tests in repo |
| 16 (Jul 7) | More pytest; read & explain existing tests | — | TDD a small function | tests + notes |
| 17 (Jul 8) | OOP: classes, `__init__`, `self`, instance vs class attrs | Lecture 8 (pt 1) | map C++ → Python; first class | practice file |
| 18 (Jul 9) | Methods, `@classmethod`/`@staticmethod`, `@property`, encapsulation | Lecture 8 (pt 2) | build `BankAccount` class **with tests** | class + tests |
| 19 (Jul 10) | Inheritance, `super()`, overriding; composition vs inheritance | — | small class hierarchy | practice file |
| 20 (Jul 11) | Dunder methods (`__str__`, `__repr__`, `__eq__`, operators), duck typing | — | add dunders to your classes | practice file |
| 21 (Jul 12) | ABCs (`abc`), `@dataclass` + **OOP mini-project** | — | deck of cards / inventory **with pytest** | mini-project + tests |

### Week 4 — Project-driven capstone: CLI Banking System (Days 22–28 · Jul 13–19)
**Goal:** build one real OOP app end-to-end so every Week 1–3 concept gets used for a purpose. Remaining CS50P topics (regex, et-cetera) are learned *inside* the project where I actually need them.

**What it exercises:** inheritance (account types) · custom exceptions (overdraft) · composition (`Bank` holds accounts) · file I/O (persistence) · CLI (`sys.argv` / menu loop) · regex (input validation) · `pytest`.

| Day | Focus | CS50P | Build milestone | Output |
| --- | --- | --- | --- | --- |
| 22 (Jul 13) | **Design first** — features, classes & responsibilities, file format | — | write a short spec/plan before any code | design doc |
| 23 (Jul 14) | Project setup + `Account` base class | Lecture 9 (et-cetera: `sys.argv`, packages, type hints) | `Account` with `deposit`/`withdraw` + custom exceptions | account module |
| 24 (Jul 15) | Account types via inheritance | — | `SavingsAccount` / `CheckingAccount` overriding behavior (interest, overdraft) | account types |
| 25 (Jul 16) | `Bank` class (composition) + dunders | — | manage many accounts; `__str__`/`__repr__` | bank module |
| 26 (Jul 17) | Persistence + CLI | Lecture 7 (regex for ID/input validation) | save/load to JSON; menu loop | working CLI |
| 27 (Jul 18) | **Tests** | — | `pytest` suite for account + bank logic | test suite |
| 28 (Jul 19) | Polish + explain | — | README; **read a reference Python project & explain it**; rehearse walking through my own code line-by-line without AI | README + written walkthrough |

### Buffer / review (Days 29–30 · Jul 20–21)
Catch-up, revisit lowest-confidence topics, and a final self-review against the exit criteria below.

---

## Definition of done (exit criteria — from Rules of Engagement)
- [ ] I can read unfamiliar code and explain it  → trained Day 28 + capstone
- [ ] I can write and read tests  → Week 3 (Days 15–16) + every mini-project after
- [ ] I can explain every line I commit — without AI  → daily review habit + Day 28 rehearsal

## Open questions for Jakob / Tadej
-
