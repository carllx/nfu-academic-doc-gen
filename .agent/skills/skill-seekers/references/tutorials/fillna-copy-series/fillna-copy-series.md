# How To: Fillna Copy Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna copy series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_missing, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign arr = data_missing.take(...)

```python
arr = data_missing.take([1, 1])
```

**Verification:**
```python
assert ser._values is result._values
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(arr, copy=False)
```

**Verification:**
```python
assert ser._values is not result._values
```

### Step 3: Assign filled_val = value

```python
filled_val = ser[0]
```

**Verification:**
```python
assert ser._values.to_dense() is arr.to_dense()
```

### Step 4: Assign result = ser.fillna(...)

```python
result = ser.fillna(filled_val)
```

**Verification:**
```python
assert ser._values.to_dense() is arr.to_dense()
```


## Complete Example

```python
# Setup
# Fixtures: data_missing, using_copy_on_write

# Workflow
arr = data_missing.take([1, 1])
ser = pd.Series(arr, copy=False)
filled_val = ser[0]
result = ser.fillna(filled_val)
if using_copy_on_write:
    assert ser._values is result._values
else:
    assert ser._values is not result._values
assert ser._values.to_dense() is arr.to_dense()
```

## Next Steps


---

*Source: test_sparse.py:294 | Complexity: Intermediate | Last updated: 2026-06-02*