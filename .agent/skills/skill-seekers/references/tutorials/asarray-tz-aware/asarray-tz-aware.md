# How To: Asarray Tz Aware

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asarray tz aware

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`


## Step-by-Step Guide

### Step 1: Assign tz = 'US/Central'

```python
tz = 'US/Central'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(date_range('2000', periods=2, tz=tz))
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array(['2000-01-01T06', '2000-01-02T06'], dtype='M8[ns]')
```

### Step 4: Assign result = np.asarray(...)

```python
result = np.asarray(ser, dtype='datetime64[ns]')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = np.asarray(...)

```python
result = np.asarray(ser, dtype='M8[ns]')
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
tz = 'US/Central'
ser = Series(date_range('2000', periods=2, tz=tz))
expected = np.array(['2000-01-01T06', '2000-01-02T06'], dtype='M8[ns]')
result = np.asarray(ser, dtype='datetime64[ns]')
tm.assert_numpy_array_equal(result, expected)
result = np.asarray(ser, dtype='M8[ns]')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_conversion.py:585 | Complexity: Intermediate | Last updated: 2026-06-02*