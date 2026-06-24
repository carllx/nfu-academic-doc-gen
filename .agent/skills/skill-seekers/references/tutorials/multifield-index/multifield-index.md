# How To: Multifield Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multifield index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `ctypes`
- `gc`
- `inspect`
- `operator`
- `pickle`
- `sys`
- `types`
- `itertools`
- `typing`
- `hypothesis`
- `pytest`
- `hypothesis.extra`
- `numpy`
- `numpy.dtypes`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: align_flag
```

## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([(('title', 'col1'), '<U20'), ('A', '<f8'), ('B', '<f8')], align=align_flag)
```

**Verification:**
```python
assert_equal(dt_sub, np.dtype({'names': ['B', 'col1'], 'formats': ['<f8', '<U20'], 'offsets': [88, 0], 'titles': [None, 'title'], 'itemsize': 96}))
```

### Step 2: Assign dt_sub = value

```python
dt_sub = dt[['B', 'col1']]
```

**Verification:**
```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

### Step 3: Call assert_equal()

```python
assert_equal(dt_sub, np.dtype({'names': ['B', 'col1'], 'formats': ['<f8', '<U20'], 'offsets': [88, 0], 'titles': [None, 'title'], 'itemsize': 96}))
```

**Verification:**
```python
assert_equal(dt_sub, np.dtype({'names': ['B'], 'formats': ['<f8'], 'offsets': [88], 'itemsize': 96}))
```

### Step 4: Call assert_equal()

```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

**Verification:**
```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

### Step 5: Assign dt_sub = value

```python
dt_sub = dt[['B']]
```

**Verification:**
```python
assert_equal(dt_sub, np.dtype({'names': [], 'formats': [], 'offsets': [], 'itemsize': 96}))
```

### Step 6: Call assert_equal()

```python
assert_equal(dt_sub, np.dtype({'names': ['B'], 'formats': ['<f8'], 'offsets': [88], 'itemsize': 96}))
```

**Verification:**
```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

### Step 7: Call assert_equal()

```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

**Verification:**
```python
assert_raises(TypeError, operator.getitem, dt, ())
```

### Step 8: Assign dt_sub = value

```python
dt_sub = dt[[]]
```

**Verification:**
```python
assert_raises(TypeError, operator.getitem, dt, [1, 2, 3])
```

### Step 9: Call assert_equal()

```python
assert_equal(dt_sub, np.dtype({'names': [], 'formats': [], 'offsets': [], 'itemsize': 96}))
```

**Verification:**
```python
assert_raises(TypeError, operator.getitem, dt, ['col1', 2])
```

### Step 10: Call assert_equal()

```python
assert_equal(dt_sub.isalignedstruct, align_flag)
```

**Verification:**
```python
assert_raises(KeyError, operator.getitem, dt, ['fake'])
```

### Step 11: Call assert_raises()

```python
assert_raises(TypeError, operator.getitem, dt, ())
```

**Verification:**
```python
assert_raises(KeyError, operator.getitem, dt, ['title'])
```

### Step 12: Call assert_raises()

```python
assert_raises(TypeError, operator.getitem, dt, [1, 2, 3])
```

**Verification:**
```python
assert_raises(ValueError, operator.getitem, dt, ['col1', 'col1'])
```

### Step 13: Call assert_raises()

```python
assert_raises(TypeError, operator.getitem, dt, ['col1', 2])
```

### Step 14: Call assert_raises()

```python
assert_raises(KeyError, operator.getitem, dt, ['fake'])
```

### Step 15: Call assert_raises()

```python
assert_raises(KeyError, operator.getitem, dt, ['title'])
```

### Step 16: Call assert_raises()

```python
assert_raises(ValueError, operator.getitem, dt, ['col1', 'col1'])
```


## Complete Example

```python
# Setup
# Fixtures: align_flag

# Workflow
dt = np.dtype([(('title', 'col1'), '<U20'), ('A', '<f8'), ('B', '<f8')], align=align_flag)
dt_sub = dt[['B', 'col1']]
assert_equal(dt_sub, np.dtype({'names': ['B', 'col1'], 'formats': ['<f8', '<U20'], 'offsets': [88, 0], 'titles': [None, 'title'], 'itemsize': 96}))
assert_equal(dt_sub.isalignedstruct, align_flag)
dt_sub = dt[['B']]
assert_equal(dt_sub, np.dtype({'names': ['B'], 'formats': ['<f8'], 'offsets': [88], 'itemsize': 96}))
assert_equal(dt_sub.isalignedstruct, align_flag)
dt_sub = dt[[]]
assert_equal(dt_sub, np.dtype({'names': [], 'formats': [], 'offsets': [], 'itemsize': 96}))
assert_equal(dt_sub.isalignedstruct, align_flag)
assert_raises(TypeError, operator.getitem, dt, ())
assert_raises(TypeError, operator.getitem, dt, [1, 2, 3])
assert_raises(TypeError, operator.getitem, dt, ['col1', 2])
assert_raises(KeyError, operator.getitem, dt, ['fake'])
assert_raises(KeyError, operator.getitem, dt, ['title'])
assert_raises(ValueError, operator.getitem, dt, ['col1', 'col1'])
```

## Next Steps


---

*Source: test_dtype.py:543 | Complexity: Advanced | Last updated: 2026-06-02*