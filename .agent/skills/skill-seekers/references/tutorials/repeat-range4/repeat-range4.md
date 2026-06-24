# How To: Repeat Range4

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate as_unit: test repeat range4

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture, unit
```

## Step-by-Step Guide

### Step 1: Assign exp = DatetimeIndex.as_unit(...)

```python
exp = DatetimeIndex(['2001-01-01', '2001-01-01', '2001-01-01', 'NaT', 'NaT', 'NaT', '2003-01-01', '2003-01-01', '2003-01-01'], tz=tz).as_unit(unit)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, unit

# Workflow
exp = DatetimeIndex(['2001-01-01', '2001-01-01', '2001-01-01', 'NaT', 'NaT', 'NaT', '2003-01-01', '2003-01-01', '2003-01-01'], tz=tz).as_unit(unit)
```

## Next Steps


---

*Source: test_repeat.py:43 | Complexity: Beginner | Last updated: 2026-06-02*