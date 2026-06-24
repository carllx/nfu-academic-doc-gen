# How To: Int From Long

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int from long

## Prerequisites

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign l = value

```python
l = [1000000.0, 1000000000000.0, 1e+18, -1000000.0, -1000000000000.0, -1e+18]
```

**Verification:**
```python
assert_equal([int(_m) for _m in a], li)
```

### Step 2: Assign li = value

```python
li = [10 ** 6, 10 ** 12, 10 ** 18, -10 ** 6, -10 ** 12, -10 ** 18]
```

**Verification:**
```python
assert_equal([int(_m) for _m in a], li[:3])
```

### Step 3: Assign a = np.array(...)

```python
a = np.array(l[:3], dtype=np.uint64)
```

### Step 4: Call assert_equal()

```python
assert_equal([int(_m) for _m in a], li[:3])
```

### Step 5: Assign a = np.array(...)

```python
a = np.array(l, dtype=T)
```

### Step 6: Call assert_equal()

```python
assert_equal([int(_m) for _m in a], li)
```


## Complete Example

```python
# Workflow
l = [1000000.0, 1000000000000.0, 1e+18, -1000000.0, -1000000000000.0, -1e+18]
li = [10 ** 6, 10 ** 12, 10 ** 18, -10 ** 6, -10 ** 12, -10 ** 18]
for T in [None, np.float64, np.int64]:
    a = np.array(l, dtype=T)
    assert_equal([int(_m) for _m in a], li)
a = np.array(l[:3], dtype=np.uint64)
assert_equal([int(_m) for _m in a], li[:3])
```

## Next Steps


---

*Source: test_scalarmath.py:483 | Complexity: Intermediate | Last updated: 2026-06-02*