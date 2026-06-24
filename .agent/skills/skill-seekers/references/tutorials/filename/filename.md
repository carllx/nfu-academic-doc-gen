# How To: Filename

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filename

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `mmap`
- `os`
- `sys`
- `warnings`
- `pathlib`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign tmpname = value

```python
tmpname = tmp_path / 'mmap'
```

**Verification:**
```python
assert_equal(abspath, fp.filename)
```

### Step 2: Assign fp = memmap(...)

```python
fp = memmap(tmpname, dtype=self.dtype, mode='w+', shape=self.shape)
```

**Verification:**
```python
assert_equal(abspath, b.filename)
```

### Step 3: Assign abspath = Path(...)

```python
abspath = Path(os.path.abspath(tmpname))
```

### Step 4: Assign unknown = value

```python
fp[:] = self.data[:]
```

### Step 5: Call assert_equal()

```python
assert_equal(abspath, fp.filename)
```

### Step 6: Assign b = value

```python
b = fp[:1]
```

### Step 7: Call assert_equal()

```python
assert_equal(abspath, b.filename)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
tmpname = tmp_path / 'mmap'
fp = memmap(tmpname, dtype=self.dtype, mode='w+', shape=self.shape)
abspath = Path(os.path.abspath(tmpname))
fp[:] = self.data[:]
assert_equal(abspath, fp.filename)
b = fp[:1]
assert_equal(abspath, b.filename)
del b
del fp
```

## Next Steps


---

*Source: test_memmap.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*