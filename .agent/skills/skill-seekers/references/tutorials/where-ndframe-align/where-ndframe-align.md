# How To: Where Ndframe Align

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where ndframe align

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'Array conditional must be same shape as self'

```python
msg = 'Array conditional must be same shape as self'
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 3: Assign cond = value

```python
cond = [True]
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, np.nan, np.nan])
```

### Step 5: Assign out = s.where(...)

```python
out = s.where(Series(cond))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out, expected)
```

### Step 7: Assign cond = np.array(...)

```python
cond = np.array([False, True, False, True])
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([np.nan, 2, np.nan])
```

### Step 9: Assign out = s.where(...)

```python
out = s.where(Series(cond))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out, expected)
```

### Step 11: Call s.where()

```python
s.where(cond)
```

### Step 12: Call s.where()

```python
s.where(cond)
```


## Complete Example

```python
# Workflow
msg = 'Array conditional must be same shape as self'
s = Series([1, 2, 3])
cond = [True]
with pytest.raises(ValueError, match=msg):
    s.where(cond)
expected = Series([1, np.nan, np.nan])
out = s.where(Series(cond))
tm.assert_series_equal(out, expected)
cond = np.array([False, True, False, True])
with pytest.raises(ValueError, match=msg):
    s.where(cond)
expected = Series([np.nan, 2, np.nan])
out = s.where(Series(cond))
tm.assert_series_equal(out, expected)
```

## Next Steps


---

*Source: test_where.py:210 | Complexity: Advanced | Last updated: 2026-06-02*