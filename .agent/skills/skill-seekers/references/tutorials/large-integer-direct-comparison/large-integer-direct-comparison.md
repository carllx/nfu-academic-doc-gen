# How To: Large Integer Direct Comparison

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test large integer direct comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`

**Setup Required:**
```python
# Fixtures: dtypes, py_comp, np_comp, vals
```

## Step-by-Step Guide

### Step 1: Assign a1 = np.array(...)

```python
a1 = np.array([2 ** 60], dtype=dtypes[0])
```

**Verification:**
```python
assert py_comp(a1, a2) == expected
```

### Step 2: Assign a2 = np.array(...)

```python
a2 = np.array([2 ** 60 + 1], dtype=dtypes[1])
```

**Verification:**
```python
assert np_comp(a1, a2) == expected
```

### Step 3: Assign expected = py_comp(...)

```python
expected = py_comp(2 ** 60, 2 ** 60 + 1)
```

**Verification:**
```python
assert isinstance(s1, np.integer)
```

### Step 4: Assign s1 = value

```python
s1 = a1[0]
```

**Verification:**
```python
assert isinstance(s2, np.integer)
```

### Step 5: Assign s2 = value

```python
s2 = a2[0]
```

**Verification:**
```python
assert py_comp(s1, s2) == expected
```


## Complete Example

```python
# Setup
# Fixtures: dtypes, py_comp, np_comp, vals

# Workflow
a1 = np.array([2 ** 60], dtype=dtypes[0])
a2 = np.array([2 ** 60 + 1], dtype=dtypes[1])
expected = py_comp(2 ** 60, 2 ** 60 + 1)
assert py_comp(a1, a2) == expected
assert np_comp(a1, a2) == expected
s1 = a1[0]
s2 = a2[0]
assert isinstance(s1, np.integer)
assert isinstance(s2, np.integer)
assert py_comp(s1, s2) == expected
assert np_comp(s1, s2) == expected
```

## Next Steps


---

*Source: test_umath.py:406 | Complexity: Intermediate | Last updated: 2026-06-02*