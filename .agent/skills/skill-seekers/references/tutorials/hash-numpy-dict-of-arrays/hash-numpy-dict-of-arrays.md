# How To: Hash Numpy Dict Of Arrays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hash numpy dict of arrays

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `gc`
- `hashlib`
- `io`
- `itertools`
- `pickle`
- `random`
- `sys`
- `time`
- `concurrent.futures`
- `decimal`
- `joblib.func_inspect`
- `joblib.hashing`
- `joblib.memory`
- `joblib.test.common`
- `joblib.testing`

**Setup Required:**
```python
# Fixtures: three_np_arrays
```

## Step-by-Step Guide

### Step 1: Assign unknown = three_np_arrays

```python
arr1, arr2, arr3 = three_np_arrays
```

**Verification:**
```python
assert hash(d1) == hash(d2)
```

### Step 2: Assign d1 = value

```python
d1 = {1: arr1, 2: arr2}
```

**Verification:**
```python
assert hash(d1) != hash(d3)
```

### Step 3: Assign d2 = value

```python
d2 = {1: arr2, 2: arr1}
```

### Step 4: Assign d3 = value

```python
d3 = {1: arr2, 2: arr3}
```

**Verification:**
```python
assert hash(d1) == hash(d2)
```


## Complete Example

```python
# Setup
# Fixtures: three_np_arrays

# Workflow
arr1, arr2, arr3 = three_np_arrays
d1 = {1: arr1, 2: arr2}
d2 = {1: arr2, 2: arr1}
d3 = {1: arr2, 2: arr3}
assert hash(d1) == hash(d2)
assert hash(d1) != hash(d3)
```

## Next Steps


---

*Source: test_hashing.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*