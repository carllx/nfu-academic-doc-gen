# How To: Asarray Tz Naive

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asarray tz naive

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2000', periods=2)
```

### Step 2: Assign result = np.asarray(...)

```python
result = np.asarray(idx)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array(['2000-01-01', '2000-01-02'], dtype='M8[ns]')
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = np.asarray(...)

```python
result = np.asarray(idx, dtype=object)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([Timestamp('2000-01-01'), Timestamp('2000-01-02')])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = date_range('2000', periods=2)
result = np.asarray(idx)
expected = np.array(['2000-01-01', '2000-01-02'], dtype='M8[ns]')
tm.assert_numpy_array_equal(result, expected)
result = np.asarray(idx, dtype=object)
expected = np.array([Timestamp('2000-01-01'), Timestamp('2000-01-02')])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*