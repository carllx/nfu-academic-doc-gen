# How To: Huge Header

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test huge header

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
# Fixtures: tmpdir, mmap_mode
```

## Step-by-Step Guide

### Step 1: Assign f = os.path.join(...)

```python
f = os.path.join(tmpdir, 'large_header.npy')
```

**Verification:**
```python
assert_array_equal(res, arr)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array(1, dtype='i,' * 10000 + 'i')
```

**Verification:**
```python
assert_array_equal(res, arr)
```

### Step 3: Assign res = np.load(...)

```python
res = np.load(f, mmap_mode=mmap_mode, allow_pickle=True)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(res, arr)
```

### Step 5: Assign res = np.load(...)

```python
res = np.load(f, mmap_mode=mmap_mode, max_header_size=180000)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, arr)
```

### Step 7: Call np.save()

```python
np.save(f, arr)
```

### Step 8: Call np.load()

```python
np.load(f, mmap_mode=mmap_mode)
```

### Step 9: Call np.load()

```python
np.load(f, mmap_mode=mmap_mode, max_header_size=20000)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir, mmap_mode

# Workflow
f = os.path.join(tmpdir, 'large_header.npy')
arr = np.array(1, dtype='i,' * 10000 + 'i')
with pytest.warns(UserWarning, match='.*format 2.0'):
    np.save(f, arr)
with pytest.raises(ValueError, match='Header.*large'):
    np.load(f, mmap_mode=mmap_mode)
with pytest.raises(ValueError, match='Header.*large'):
    np.load(f, mmap_mode=mmap_mode, max_header_size=20000)
res = np.load(f, mmap_mode=mmap_mode, allow_pickle=True)
assert_array_equal(res, arr)
res = np.load(f, mmap_mode=mmap_mode, max_header_size=180000)
assert_array_equal(res, arr)
```

## Next Steps


---

*Source: test_format.py:742 | Complexity: Advanced | Last updated: 2026-06-02*