# How To: Isna For Inf

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isna for inf

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', np.inf, np.nan, pd.NA, 1.0])
```

### Step 2: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

### Step 3: Assign e = Series(...)

```python
e = Series([False, True, True, True, False])
```

### Step 4: Assign de = Series(...)

```python
de = Series(['a', 1.0], index=[0, 4])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(r, e)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(dr, de)
```

### Step 7: Assign r = s.isna(...)

```python
r = s.isna()
```

### Step 8: Assign dr = s.dropna(...)

```python
dr = s.dropna()
```


## Complete Example

```python
# Workflow
s = Series(['a', np.inf, np.nan, pd.NA, 1.0])
msg = 'use_inf_as_na option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.use_inf_as_na', True):
        r = s.isna()
        dr = s.dropna()
e = Series([False, True, True, True, False])
de = Series(['a', 1.0], index=[0, 4])
tm.assert_series_equal(r, e)
tm.assert_series_equal(dr, de)
```

## Next Steps


---

*Source: test_missing.py:28 | Complexity: Advanced | Last updated: 2026-06-02*