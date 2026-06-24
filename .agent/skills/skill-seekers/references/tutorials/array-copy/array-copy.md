# How To: Array Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array copy

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.arrays`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2])
```

**Verification:**
```python
assert not tm.shares_memory(a, b)
```

### Step 2: Assign b = pd.array(...)

```python
b = pd.array(a, dtype=a.dtype)
```

**Verification:**
```python
assert not tm.shares_memory(a, b)
```

### Step 3: Assign b = pd.array(...)

```python
b = pd.array(a, dtype=a.dtype, copy=True)
```

**Verification:**
```python
assert tm.shares_memory(a, b)
```

### Step 4: Assign b = pd.array(...)

```python
b = pd.array(a, dtype=a.dtype, copy=False)
```

**Verification:**
```python
assert tm.shares_memory(a, b)
```


## Complete Example

```python
# Workflow
a = np.array([1, 2])
b = pd.array(a, dtype=a.dtype)
assert not tm.shares_memory(a, b)
b = pd.array(a, dtype=a.dtype, copy=True)
assert not tm.shares_memory(a, b)
b = pd.array(a, dtype=a.dtype, copy=False)
assert tm.shares_memory(a, b)
```

## Next Steps


---

*Source: test_array.py:294 | Complexity: Intermediate | Last updated: 2026-06-02*