# How To: Getitem Periodindex Duplicates String Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem periodindex duplicates string slice

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([2000, 2007, 2007, 2009, 2009], freq='Y-JUN')
```

**Verification:**
```python
assert (ts[1:3] == 1).all()
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
```

### Step 3: Assign original = ts.copy(...)

```python
original = ts.copy()
```

### Step 4: Assign result = value

```python
result = ts['2007']
```

### Step 5: Assign expected = value

```python
expected = ts[1:3]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([2000, 2007, 2007, 2009, 2007], freq='Y-JUN')
```

### Step 8: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
```

### Step 9: Assign result = value

```python
result = ts['2007']
```

### Step 10: Assign expected = value

```python
expected = ts[idx == '2007']
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign unknown = 1

```python
result[:] = 1
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts, original)
```

**Verification:**
```python
assert (ts[1:3] == 1).all()
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
idx = PeriodIndex([2000, 2007, 2007, 2009, 2009], freq='Y-JUN')
ts = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
original = ts.copy()
result = ts['2007']
expected = ts[1:3]
tm.assert_series_equal(result, expected)
with tm.assert_cow_warning(warn_copy_on_write):
    result[:] = 1
if using_copy_on_write:
    tm.assert_series_equal(ts, original)
else:
    assert (ts[1:3] == 1).all()
idx = PeriodIndex([2000, 2007, 2007, 2009, 2007], freq='Y-JUN')
ts = Series(np.random.default_rng(2).standard_normal(len(idx)), index=idx)
result = ts['2007']
expected = ts[idx == '2007']
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_partial_slicing.py:15 | Complexity: Advanced | Last updated: 2026-06-02*