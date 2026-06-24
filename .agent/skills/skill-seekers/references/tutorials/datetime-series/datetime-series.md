# How To: Datetime Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetime series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, func
```

## Step-by-Step Guide

### Step 1: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(func(datetime_series).values, func(np.array(datetime_series)), check_dtype=True)
```

### Step 2: Assign ts = datetime_series.copy(...)

```python
ts = datetime_series.copy()
```

### Step 3: Assign unknown = value

```python
ts[::2] = np.nan
```

### Step 4: Assign result = value

```python
result = func(ts)[1::2]
```

### Step 5: Assign expected = func(...)

```python
expected = func(np.array(ts.dropna()))
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result.values, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, func

# Workflow
tm.assert_numpy_array_equal(func(datetime_series).values, func(np.array(datetime_series)), check_dtype=True)
ts = datetime_series.copy()
ts[::2] = np.nan
result = func(ts)[1::2]
expected = func(np.array(ts.dropna()))
tm.assert_numpy_array_equal(result.values, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_cumulative.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*