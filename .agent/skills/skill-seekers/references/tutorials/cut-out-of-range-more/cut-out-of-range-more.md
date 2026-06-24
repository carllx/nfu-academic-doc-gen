# How To: Cut Out Of Range More

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cut out of range more

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign name = 'x'

```python
name = 'x'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([0, -1, 0, 1, -3], name=name)
```

### Step 3: Assign ind = cut(...)

```python
ind = cut(ser, [0, 1], labels=False)
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([np.nan, np.nan, np.nan, 0, np.nan], name=name)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ind, exp)
```


## Complete Example

```python
# Workflow
name = 'x'
ser = Series([0, -1, 0, 1, -3], name=name)
ind = cut(ser, [0, 1], labels=False)
exp = Series([np.nan, np.nan, np.nan, 0, np.nan], name=name)
tm.assert_series_equal(ind, exp)
```

## Next Steps


---

*Source: test_cut.py:214 | Complexity: Intermediate | Last updated: 2026-06-02*