# Burnout Guide App

This README is intentionally rough so you can improve it with GitHub Copilot CLI.

A Python app for exploring five common types of burnout and the first steps toward healing.
It can add, remove, and list burnout types. It can also search for burnout guidance by healing keyword.

---

## Current Features

* Reads burnout types from a JSON file
* Includes starter guidance for five burnout patterns
* Some tests exist but probably not enough

---

## Files

* `burnout_app.py` - Main CLI entry point
* `burnout_types.py` - BurnoutCollection class with data logic
* `utils.py` - Helper functions for UI and input
* `data.json` - Sample burnout data
* `tests/test_burnout_types.py` - Starter pytest tests

---

## Running the App

```bash
python burnout_app.py list
python burnout_app.py add
python burnout_app.py find
python burnout_app.py remove
python burnout_app.py help
```

## Running Tests

```bash
python -m pytest tests/
```

---

## Notes

* Not production-ready
* Some code could be improved
* Could add more commands later