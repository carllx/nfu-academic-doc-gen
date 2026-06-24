# How To: Usecols With Unicode Strings

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: test usecols with unicode strings

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign exp_data = value

```python
exp_data = {'AAA': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'BBB': {0: 8, 1: 2, 2: 7}}
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
exp_data = {'AAA': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'BBB': {0: 8, 1: 2, 2: 7}}
```

## Next Steps


---

*Source: test_strings.py:25 | Complexity: Beginner | Last updated: 2026-06-02*