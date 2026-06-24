# How To: Xs Datetimelike Wrapping

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs datetimelike wrapping

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = date_range('2016-01-01', periods=3)._data._ndarray
```

**Verification:**
```python
assert ser.dtype == object
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(arr, dtype=object)
```

**Verification:**
```python
assert isinstance(ser[0], np.datetime64)
```

### Step 3: Assign result = ser.xs(...)

```python
result = ser.xs(0)
```

**Verification:**
```python
assert isinstance(result, np.datetime64)
```

### Step 4: Assign unknown = value

```python
ser.iloc[i] = arr[i]
```


## Complete Example

```python
# Workflow
arr = date_range('2016-01-01', periods=3)._data._ndarray
ser = Series(arr, dtype=object)
for i in range(len(ser)):
    ser.iloc[i] = arr[i]
assert ser.dtype == object
assert isinstance(ser[0], np.datetime64)
result = ser.xs(0)
assert isinstance(result, np.datetime64)
```

## Next Steps


---

*Source: test_xs.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*