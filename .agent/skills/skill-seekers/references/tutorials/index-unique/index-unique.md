# How To: Index Unique

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DatetimeIndex: test index unique

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: rand_series_with_duplicate_datetimeindex
```

## Step-by-Step Guide

### Step 1: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([datetime(2000, 1, 2), datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5)], dtype=index.dtype)
```


## Complete Example

```python
# Setup
# Fixtures: rand_series_with_duplicate_datetimeindex

# Workflow
expected = DatetimeIndex([datetime(2000, 1, 2), datetime(2000, 1, 3), datetime(2000, 1, 4), datetime(2000, 1, 5)], dtype=index.dtype)
```

## Next Steps


---

*Source: test_unique.py:30 | Complexity: Beginner | Last updated: 2026-06-02*