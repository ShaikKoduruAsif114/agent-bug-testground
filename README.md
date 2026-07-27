# Agent Bug Test Repository 🤖

This repository is a **test playground** for the [Autonomous GitHub Issue Agent](https://github.com/ShaikKoduruAsif114/Multi_Agent_orchrastat).

It contains Python modules with **intentionally planted bugs** to test whether the AI agent can:
1. Correctly identify the bug from the issue description
2. Generate an accurate code fix using Llama 3.2
3. Write meaningful pytest unit tests that verify the fix
4. Open a valid Pull Request on GitHub

---

## 🐛 Intentional Bugs

### Issue #1 — `src/calculator.py`
- `divide(a, b)` crashes with `ZeroDivisionError` when `b=0`
- `percentage(value, percent)` divides by 10 instead of 100
- `factorial(0)` hits infinite recursion (missing base case)

### Issue #2 — `src/user_manager.py`
- `get_user()` returns key `username` instead of `name` — breaks API consumers
- `update_email()` accepts invalid emails without `@`

### Issue #3 — `src/shopping_cart.py`
- `get_total()` ignores item quantity
- `apply_discount()` subtracts raw number instead of applying percentage
- `remove_item()` crashes with `StopIteration` if item not found

### Issue #4 — `src/string_utils.py`
- `is_palindrome()` fails for mixed-case strings like `'Racecar'`
- `count_words()` miscounts with multiple consecutive spaces
- `truncate()` always appends `'...'` even for short strings

### Issue #5 — `src/bank_account.py`
- `withdraw()` allows balance to go negative (no overdraft protection)
- `transfer()` doesn't validate sender has sufficient funds
- `apply_interest()` uses simple interest formula instead of compound interest

---

## 📁 Project Structure
```
test-buggy-app/
├── src/
│   ├── calculator.py      # Issue #1
│   ├── user_manager.py    # Issue #2
│   ├── shopping_cart.py   # Issue #3
│   ├── string_utils.py    # Issue #4
│   └── bank_account.py    # Issue #5
└── README.md
```

---

*Powered by: Autonomous GitHub Issue Agent — LangGraph + Llama 3.2 + Docker*
