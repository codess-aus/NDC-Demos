# Burnout App - Buggy Version

This directory contains an intentionally buggy version of the burnout guide app for debugging exercises.

Do NOT fix these bugs directly. They exist so learners can practice using GitHub Copilot to identify and debug issues.

---

## Intentional Bugs

### burnout_types_buggy.py

| # | Bug | Symptom |
|---|-----|---------|
| 1 | `find_burnout_type_by_title()` uses exact case match | Searching for `emotional burnout` returns nothing even though `Emotional Burnout` exists |
| 2 | `save_burnout_types()` does not use a context manager | File handle leak and weak error handling |
| 3 | `add_burnout_type()` has no validation | Empty titles, empty signs, and empty healing steps are accepted |
| 4 | `remove_burnout_type()` uses `in` substring check | Removing `Mental Burnout` can also match longer titles |
| 5 | `mark_as_reviewed()` marks all entries as reviewed | One update changes every burnout type |
| 6 | `find_by_healing_keyword()` requires exact full-text match | Searching for `purpose` does not find guidance containing that keyword |

### burnout_app_buggy.py

| # | Bug | Symptom |
|---|-----|---------|
| 7 | `show_burnout_types()` numbering starts at 0 | Entries display as `0.`, `1.`, `2.` |
| 8 | `handle_add()` accepts blank content | Can add incomplete burnout entries |
| 9 | `handle_remove()` always prints success | Says an item was removed even when nothing matched |

---

## Example Prompts

```bash
copilot

> @"samples 2/burnout-app-buggy/burnout_types_buggy.py" Users report that searching for
> "emotional burnout" returns no results even though it exists in the guide. Debug why.

> @"samples 2/burnout-app-buggy/burnout_app_buggy.py" When I remove a burnout type that
> doesn't exist, the app says it was removed. Help me find why.
```