# How To: Void From Byteslike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test void from byteslike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: bytes_
```

## Step-by-Step Guide

### Step 1: Assign res = np.void(...)

```python
res = np.void(bytes_)
```

**Verification:**
```python
assert type(res) is np.void
```

### Step 2: Assign expected = bytes(...)

```python
expected = bytes(bytes_)
```

**Verification:**
```python
assert res.item() == expected
```

### Step 3: Assign res = np.void(...)

```python
res = np.void(bytes_, dtype='V100')
```

**Verification:**
```python
assert type(res) is np.void
```

### Step 4: Assign res = np.void(...)

```python
res = np.void(bytes_, dtype='V4')
```

**Verification:**
```python
assert res.item()[:len(expected)] == expected
```


## Complete Example

```python
# Setup
# Fixtures: bytes_

# Workflow
res = np.void(bytes_)
expected = bytes(bytes_)
assert type(res) is np.void
assert res.item() == expected
res = np.void(bytes_, dtype='V100')
assert type(res) is np.void
assert res.item()[:len(expected)] == expected
assert res.item()[len(expected):] == b'\x00' * (res.nbytes - len(expected))
res = np.void(bytes_, dtype='V4')
assert type(res) is np.void
assert res.item() == expected[:4]
```

## Next Steps


---

*Source: test_scalar_ctors.py:146 | Complexity: Intermediate | Last updated: 2026-06-02*