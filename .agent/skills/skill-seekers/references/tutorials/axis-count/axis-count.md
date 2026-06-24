# How To: Axis Count

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test axis count

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: kwargs
```

## Step-by-Step Guide

### Step 1: Assign packed0 = np.packbits(...)

```python
packed0 = np.packbits(self.x, axis=0)
```

**Verification:**
```python
assert_equal(unpacked0.dtype, np.uint8)
```

### Step 2: Assign unpacked0 = np.unpackbits(...)

```python
unpacked0 = np.unpackbits(packed0, axis=0, **kwargs)
```

**Verification:**
```python
assert_array_equal(unpacked0, self.padded2[:-1, :self.x.shape[1]])
```

### Step 3: Call assert_equal()

```python
assert_equal(unpacked0.dtype, np.uint8)
```

**Verification:**
```python
assert_array_equal(unpacked0[::-1, :], self.padded2[:-1, :self.x.shape[1]])
```

### Step 4: Assign packed1 = np.packbits(...)

```python
packed1 = np.packbits(self.x, axis=1)
```

**Verification:**
```python
assert_equal(unpacked1.dtype, np.uint8)
```

### Step 5: Assign unpacked1 = np.unpackbits(...)

```python
unpacked1 = np.unpackbits(packed1, axis=1, **kwargs)
```

**Verification:**
```python
assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :-1])
```

### Step 6: Call assert_equal()

```python
assert_equal(unpacked1.dtype, np.uint8)
```

**Verification:**
```python
assert_array_equal(unpacked1[:, ::-1], self.padded2[:self.x.shape[0], :-1])
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(unpacked0, self.padded2[:-1, :self.x.shape[1]])
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(unpacked0[::-1, :], self.padded2[:-1, :self.x.shape[1]])
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :-1])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(unpacked1[:, ::-1], self.padded2[:self.x.shape[0], :-1])
```


## Complete Example

```python
# Setup
# Fixtures: kwargs

# Workflow
packed0 = np.packbits(self.x, axis=0)
unpacked0 = np.unpackbits(packed0, axis=0, **kwargs)
assert_equal(unpacked0.dtype, np.uint8)
if kwargs.get('bitorder', 'big') == 'big':
    assert_array_equal(unpacked0, self.padded2[:-1, :self.x.shape[1]])
else:
    assert_array_equal(unpacked0[::-1, :], self.padded2[:-1, :self.x.shape[1]])
packed1 = np.packbits(self.x, axis=1)
unpacked1 = np.unpackbits(packed1, axis=1, **kwargs)
assert_equal(unpacked1.dtype, np.uint8)
if kwargs.get('bitorder', 'big') == 'big':
    assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :-1])
else:
    assert_array_equal(unpacked1[:, ::-1], self.padded2[:self.x.shape[0], :-1])
```

## Next Steps


---

*Source: test_packbits.py:353 | Complexity: Advanced | Last updated: 2026-06-02*