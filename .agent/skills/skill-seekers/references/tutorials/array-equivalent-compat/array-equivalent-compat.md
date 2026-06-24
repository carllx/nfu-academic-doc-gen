# How To: Array Equivalent Compat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array equivalent compat

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign m = np.array(...)

```python
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
```

**Verification:**
```python
assert array_equivalent(m, n, strict_nan=True)
```

### Step 2: Assign n = np.array(...)

```python
n = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
```

**Verification:**
```python
assert array_equivalent(m, n, strict_nan=False)
```

### Step 3: Assign m = np.array(...)

```python
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
```

**Verification:**
```python
assert not array_equivalent(m, n, strict_nan=True)
```

### Step 4: Assign n = np.array(...)

```python
n = np.array([(1, 2), (4, 3)], dtype=[('a', int), ('b', float)])
```

**Verification:**
```python
assert not array_equivalent(m, n, strict_nan=False)
```

### Step 5: Assign m = np.array(...)

```python
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
```

**Verification:**
```python
assert not array_equivalent(m, n, strict_nan=True)
```

### Step 6: Assign n = np.array(...)

```python
n = np.array([(1, 2), (3, 4)], dtype=[('b', int), ('a', float)])
```

**Verification:**
```python
assert not array_equivalent(m, n, strict_nan=False)
```


## Complete Example

```python
# Workflow
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
n = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
assert array_equivalent(m, n, strict_nan=True)
assert array_equivalent(m, n, strict_nan=False)
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
n = np.array([(1, 2), (4, 3)], dtype=[('a', int), ('b', float)])
assert not array_equivalent(m, n, strict_nan=True)
assert not array_equivalent(m, n, strict_nan=False)
m = np.array([(1, 2), (3, 4)], dtype=[('a', int), ('b', float)])
n = np.array([(1, 2), (3, 4)], dtype=[('b', int), ('a', float)])
assert not array_equivalent(m, n, strict_nan=True)
assert not array_equivalent(m, n, strict_nan=False)
```

## Next Steps


---

*Source: test_missing.py:548 | Complexity: Intermediate | Last updated: 2026-06-02*