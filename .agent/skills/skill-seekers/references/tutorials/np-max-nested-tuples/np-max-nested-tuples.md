# How To: Np Max Nested Tuples

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test np max nested tuples

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = [(('j', 'k'), ('l', 'm')), (('l', 'm'), ('o', 'p')), (('o', 'p'), ('j', 'k'))]
```

**Verification:**
```python
assert arr.max() is arr[2]
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(vals)
```

**Verification:**
```python
assert ser.max() is arr[2]
```

### Step 3: Assign arr = value

```python
arr = ser.array
```

**Verification:**
```python
assert result == arr[2]
```

### Step 4: Assign result = np.maximum.reduce(...)

```python
result = np.maximum.reduce(arr)
```

**Verification:**
```python
assert result == arr[2]
```

### Step 5: Assign result = np.maximum.reduce(...)

```python
result = np.maximum.reduce(ser)
```

**Verification:**
```python
assert result == arr[2]
```


## Complete Example

```python
# Workflow
vals = [(('j', 'k'), ('l', 'm')), (('l', 'm'), ('o', 'p')), (('o', 'p'), ('j', 'k'))]
ser = pd.Series(vals)
arr = ser.array
assert arr.max() is arr[2]
assert ser.max() is arr[2]
result = np.maximum.reduce(arr)
assert result == arr[2]
result = np.maximum.reduce(ser)
assert result == arr[2]
```

## Next Steps


---

*Source: test_numpy.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*