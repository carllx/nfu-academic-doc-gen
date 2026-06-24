# How To: Iterrows Corner

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test iterrows corner

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = Series(...)

```python
expected = Series([datetime.datetime(2015, 1, 1), None, None, '', [], set(), {}], index=list('abcdefg'), name=0, dtype='object')
```


## Complete Example

```python
# Workflow
expected = Series([datetime.datetime(2015, 1, 1), None, None, '', [], set(), {}], index=list('abcdefg'), name=0, dtype='object')
```

## Next Steps


---

*Source: test_iteration.py:79 | Complexity: Beginner | Last updated: 2026-06-02*