# How To: Array Equivalent Array Mismatched Shape

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array equivalent array mismatched shape

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

### Step 1: Assign first = np.array(...)

```python
first = np.array([1, 2, 3])
```

**Verification:**
```python
assert not array_equivalent(left, right)
```

### Step 2: Assign second = np.array(...)

```python
second = np.array([1, 2])
```

### Step 3: Assign left = Series(...)

```python
left = Series([first, 'a'], dtype=object)
```

### Step 4: Assign right = Series(...)

```python
right = Series([second, 'a'], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right)
```


## Complete Example

```python
# Workflow
first = np.array([1, 2, 3])
second = np.array([1, 2])
left = Series([first, 'a'], dtype=object)
right = Series([second, 'a'], dtype=object)
assert not array_equivalent(left, right)
```

## Next Steps


---

*Source: test_missing.py:499 | Complexity: Intermediate | Last updated: 2026-06-02*