# How To: Large Archive

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test large archive

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

### Step 1: Assign shape = value

```python
shape = (2 ** 30, 2)
```

**Verification:**
```python
assert new_a.shape == shape
```

### Step 2: Assign fname = os.path.join(...)

```python
fname = os.path.join(tmpdir, 'large_archive')
```

**Verification:**
```python
assert new_a.shape == shape
```

### Step 3: Assign a = np.empty(...)

```python
a = np.empty(shape, dtype=np.uint8)
```

### Step 4: Call np.savez()

```python
np.savez(f, arr=a)
```

### Step 5: Assign new_a = value

```python
new_a = np.load(f)['arr']
```

### Step 6: Call pytest.skip()

```python
pytest.skip('Could not create large file')
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
shape = (2 ** 30, 2)
try:
    a = np.empty(shape, dtype=np.uint8)
except MemoryError:
    pytest.skip('Could not create large file')
fname = os.path.join(tmpdir, 'large_archive')
with open(fname, 'wb') as f:
    np.savez(f, arr=a)
del a
with open(fname, 'rb') as f:
    new_a = np.load(f)['arr']
assert new_a.shape == shape
```

## Next Steps


---

*Source: test_format.py:961 | Complexity: Advanced | Last updated: 2026-06-02*