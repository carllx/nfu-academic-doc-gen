# How To: Td Add Sub Td64 Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td add sub td64 ndarray

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta('1 day')
```

### Step 2: Assign other = np.array(...)

```python
other = np.array([td.to_timedelta64()])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([Timedelta('2 Days').to_timedelta64()])
```

### Step 4: Assign result = value

```python
result = td + other
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = other + td
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = td - other
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected * 0)
```

### Step 10: Assign result = value

```python
result = other - td
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected * 0)
```


## Complete Example

```python
# Workflow
td = Timedelta('1 day')
other = np.array([td.to_timedelta64()])
expected = np.array([Timedelta('2 Days').to_timedelta64()])
result = td + other
tm.assert_numpy_array_equal(result, expected)
result = other + td
tm.assert_numpy_array_equal(result, expected)
result = td - other
tm.assert_numpy_array_equal(result, expected * 0)
result = other - td
tm.assert_numpy_array_equal(result, expected * 0)
```

## Next Steps


---

*Source: test_arithmetic.py:294 | Complexity: Advanced | Last updated: 2026-06-02*