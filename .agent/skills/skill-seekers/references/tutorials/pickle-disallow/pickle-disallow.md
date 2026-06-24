# How To: Pickle Disallow

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickle disallow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `warnings`
- `io`
- `pytest`
- `numpy`
- `numpy.lib`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy.lib._utils_impl`
- `random`
- `subprocess`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign data_dir = os.path.join(...)

```python
data_dir = os.path.join(os.path.dirname(__file__), 'data')
```

**Verification:**
```python
assert_raises(ValueError, np.load, path, allow_pickle=False, encoding='latin1')
```

### Step 2: Assign path = os.path.join(...)

```python
path = os.path.join(data_dir, 'py2-objarr.npy')
```

**Verification:**
```python
assert_raises(ValueError, f.__getitem__, 'x')
```

### Step 3: Call assert_raises()

```python
assert_raises(ValueError, np.load, path, allow_pickle=False, encoding='latin1')
```

**Verification:**
```python
assert_raises(ValueError, np.save, path, np.array([None], dtype=object), allow_pickle=False)
```

### Step 4: Assign path = os.path.join(...)

```python
path = os.path.join(data_dir, 'py2-objarr.npz')
```

### Step 5: Assign path = os.path.join(...)

```python
path = os.path.join(tmpdir, 'pickle-disabled.npy')
```

### Step 6: Call assert_raises()

```python
assert_raises(ValueError, np.save, path, np.array([None], dtype=object), allow_pickle=False)
```

### Step 7: Call assert_raises()

```python
assert_raises(ValueError, f.__getitem__, 'x')
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
data_dir = os.path.join(os.path.dirname(__file__), 'data')
path = os.path.join(data_dir, 'py2-objarr.npy')
assert_raises(ValueError, np.load, path, allow_pickle=False, encoding='latin1')
path = os.path.join(data_dir, 'py2-objarr.npz')
with np.load(path, allow_pickle=False, encoding='latin1') as f:
    assert_raises(ValueError, f.__getitem__, 'x')
path = os.path.join(tmpdir, 'pickle-disabled.npy')
assert_raises(ValueError, np.save, path, np.array([None], dtype=object), allow_pickle=False)
```

## Next Steps


---

*Source: test_format.py:614 | Complexity: Intermediate | Last updated: 2026-06-02*