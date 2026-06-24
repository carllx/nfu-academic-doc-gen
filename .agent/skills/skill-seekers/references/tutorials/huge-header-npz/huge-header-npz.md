# How To: Huge Header Npz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test huge header npz

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

### Step 1: Assign f = os.path.join(...)

```python
f = os.path.join(tmpdir, 'large_header.npz')
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

### Step 3: Assign res = value

```python
res = np.load(f, allow_pickle=True)['arr']
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(res, arr)
```

### Step 5: Assign res = value

```python
res = np.load(f, max_header_size=180000)['arr']
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, arr)
```

### Step 7: Call np.savez()

```python
np.savez(f, arr=arr)
```

### Step 8: np.load(f)['arr']

```python
np.load(f)['arr']
```

### Step 9: np.load(f, max_header_size=20000)['arr']

```python
np.load(f, max_header_size=20000)['arr']
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
f = os.path.join(tmpdir, 'large_header.npz')
arr = np.array(1, dtype='i,' * 10000 + 'i')
with pytest.warns(UserWarning, match='.*format 2.0'):
    np.savez(f, arr=arr)
with pytest.raises(ValueError, match='Header.*large'):
    np.load(f)['arr']
with pytest.raises(ValueError, match='Header.*large'):
    np.load(f, max_header_size=20000)['arr']
res = np.load(f, allow_pickle=True)['arr']
assert_array_equal(res, arr)
res = np.load(f, max_header_size=180000)['arr']
assert_array_equal(res, arr)
```

## Next Steps


---

*Source: test_format.py:761 | Complexity: Advanced | Last updated: 2026-06-02*