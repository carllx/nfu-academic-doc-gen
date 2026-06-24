# How To: Dataframe Multiple Numpy Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe multiple numpy dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': 1.5})
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign arr = np.asarray(...)

```python
arr = np.asarray(df)
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array(df, copy=True)
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 4: Assign msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"

```python
msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"
```

### Step 5: Assign arr = np.array(...)

```python
arr = np.array(df, copy=False)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': 1.5})
arr = np.asarray(df)
assert not np.shares_memory(arr, get_array(df, 'a'))
assert arr.flags.writeable is True
if np_version_gt2:
    msg = "Starting with NumPy 2.0, the behavior of the 'copy' keyword has changed"
    with pytest.raises(FutureWarning, match=msg):
        arr = np.array(df, copy=False)
arr = np.array(df, copy=True)
assert arr.flags.writeable is True
```

## Next Steps


---

*Source: test_array.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*