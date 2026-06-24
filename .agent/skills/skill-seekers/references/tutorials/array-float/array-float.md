# How To: Array Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array float

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `decimal`
- `json`
- `locale`
- `math`
- `re`
- `time`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.json`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = np.float32
```

### Step 2: Assign arr = np.arange(...)

```python
arr = np.arange(100.202, 200.202, 1, dtype=dtype)
```

### Step 3: Assign arr = arr.reshape(...)

```python
arr = arr.reshape((5, 5, 4))
```

### Step 4: Assign arr_out = np.array(...)

```python
arr_out = np.array(ujson.ujson_loads(ujson.ujson_dumps(arr)), dtype=dtype)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(arr, arr_out)
```


## Complete Example

```python
# Workflow
dtype = np.float32
arr = np.arange(100.202, 200.202, 1, dtype=dtype)
arr = arr.reshape((5, 5, 4))
arr_out = np.array(ujson.ujson_loads(ujson.ujson_dumps(arr)), dtype=dtype)
tm.assert_almost_equal(arr, arr_out)
```

## Next Steps


---

*Source: test_ujson.py:806 | Complexity: Intermediate | Last updated: 2026-06-02*