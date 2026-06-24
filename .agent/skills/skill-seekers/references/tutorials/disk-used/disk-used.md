# How To: Disk Used

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test disk used

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `array`
- `os`
- `joblib.disk`
- `joblib.testing`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign cachedir = value

```python
cachedir = tmpdir.strpath
```

**Verification:**
```python
assert disk_used(cachedir) >= target_size
```

### Step 2: Assign a = array.array(...)

```python
a = array.array('i')
```

**Verification:**
```python
assert disk_used(cachedir) < target_size + 12
```

### Step 3: Assign sizeof_i = value

```python
sizeof_i = a.itemsize
```

### Step 4: Assign target_size = 1024

```python
target_size = 1024
```

### Step 5: Assign n = int(...)

```python
n = int(target_size * 1024 / sizeof_i)
```

### Step 6: Assign a = array.array(...)

```python
a = array.array('i', n * (1,))
```

**Verification:**
```python
assert disk_used(cachedir) >= target_size
```

### Step 7: Call a.tofile()

```python
a.tofile(output)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
cachedir = tmpdir.strpath
a = array.array('i')
sizeof_i = a.itemsize
target_size = 1024
n = int(target_size * 1024 / sizeof_i)
a = array.array('i', n * (1,))
with open(os.path.join(cachedir, 'test'), 'wb') as output:
    a.tofile(output)
assert disk_used(cachedir) >= target_size
assert disk_used(cachedir) < target_size + 12
```

## Next Steps


---

*Source: test_disk.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*