# How To: Date Range Index Comparison

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range index comparison

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`
- `pandas.tseries.holiday`
- `pandas._libs.tslibs.timezones`
- `pandas._libs.tslibs.timezones`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('2011-01-01', periods=3, tz='US/Eastern')
```

### Step 2: Assign df = Series.to_frame(...)

```python
df = Series(rng).to_frame()
```

### Step 3: Assign arr = value

```python
arr = np.array([rng.to_list()]).T
```

### Step 4: Assign arr2 = value

```python
arr2 = np.array([rng]).T
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([True, True, True])
```

### Step 6: Assign results = value

```python
results = df == arr2
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(results, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([True, True, True], name=0)
```

### Step 9: Assign results = value

```python
results = df[0] == arr2[:, 0]
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(results, expected)
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([[True, False, False], [False, True, False], [False, False, True]])
```

### Step 12: Assign results = value

```python
results = rng == arr
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(results, expected)
```

### Step 14: rng == df

```python
rng == df
```

### Step 15: df == rng

```python
df == rng
```


## Complete Example

```python
# Workflow
rng = date_range('2011-01-01', periods=3, tz='US/Eastern')
df = Series(rng).to_frame()
arr = np.array([rng.to_list()]).T
arr2 = np.array([rng]).T
with pytest.raises(ValueError, match='Unable to coerce to Series'):
    rng == df
with pytest.raises(ValueError, match='Unable to coerce to Series'):
    df == rng
expected = DataFrame([True, True, True])
results = df == arr2
tm.assert_frame_equal(results, expected)
expected = Series([True, True, True], name=0)
results = df[0] == arr2[:, 0]
tm.assert_series_equal(results, expected)
expected = np.array([[True, False, False], [False, True, False], [False, False, True]])
results = rng == arr
tm.assert_numpy_array_equal(results, expected)
```

## Next Steps


---

*Source: test_date_range.py:352 | Complexity: Advanced | Last updated: 2026-06-02*