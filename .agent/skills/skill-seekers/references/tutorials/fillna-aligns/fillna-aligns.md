# How To: Fillna Aligns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna aligns

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([0, 1, 2], list('abc'))
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([0, np.nan, 2], list('bac'))
```

### Step 3: Assign result = s2.fillna(...)

```python
result = s2.fillna(s1)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0, 0, 2.0], list('bac'))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([0, 1, 2], list('abc'))
s2 = Series([0, np.nan, 2], list('bac'))
result = s2.fillna(s1)
expected = Series([0, 0, 2.0], list('bac'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*