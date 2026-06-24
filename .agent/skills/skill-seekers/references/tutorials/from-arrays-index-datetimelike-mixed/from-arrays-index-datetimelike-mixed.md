# How To: From Arrays Index Datetimelike Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from arrays index datetimelike mixed

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = date_range(...)

```python
idx1 = date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern')
```

### Step 2: Assign idx2 = date_range(...)

```python
idx2 = date_range('2015-01-01 10:00', freq='h', periods=3)
```

### Step 3: Assign idx3 = pd.timedelta_range(...)

```python
idx3 = pd.timedelta_range('1 days', freq='D', periods=3)
```

### Step 4: Assign idx4 = pd.period_range(...)

```python
idx4 = pd.period_range('2011-01-01', freq='D', periods=3)
```

### Step 5: Assign result = MultiIndex.from_arrays(...)

```python
result = MultiIndex.from_arrays([idx1, idx2, idx3, idx4])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(0), idx1)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(1), idx2)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(2), idx3)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(3), idx4)
```

### Step 10: Assign result2 = MultiIndex.from_arrays(...)

```python
result2 = MultiIndex.from_arrays([Series(idx1), Series(idx2), Series(idx3), Series(idx4)])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(0), idx1)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(1), idx2)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(2), idx3)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(3), idx4)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, result2)
```


## Complete Example

```python
# Workflow
idx1 = date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern')
idx2 = date_range('2015-01-01 10:00', freq='h', periods=3)
idx3 = pd.timedelta_range('1 days', freq='D', periods=3)
idx4 = pd.period_range('2011-01-01', freq='D', periods=3)
result = MultiIndex.from_arrays([idx1, idx2, idx3, idx4])
tm.assert_index_equal(result.get_level_values(0), idx1)
tm.assert_index_equal(result.get_level_values(1), idx2)
tm.assert_index_equal(result.get_level_values(2), idx3)
tm.assert_index_equal(result.get_level_values(3), idx4)
result2 = MultiIndex.from_arrays([Series(idx1), Series(idx2), Series(idx3), Series(idx4)])
tm.assert_index_equal(result2.get_level_values(0), idx1)
tm.assert_index_equal(result2.get_level_values(1), idx2)
tm.assert_index_equal(result2.get_level_values(2), idx3)
tm.assert_index_equal(result2.get_level_values(3), idx4)
tm.assert_index_equal(result, result2)
```

## Next Steps


---

*Source: test_constructors.py:228 | Complexity: Advanced | Last updated: 2026-06-02*