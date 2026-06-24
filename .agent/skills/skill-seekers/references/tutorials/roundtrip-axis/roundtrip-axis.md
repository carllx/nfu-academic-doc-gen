# How To: Roundtrip Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: bitorder, count
```

## Step-by-Step Guide

### Step 1: Assign packed0 = np.packbits(...)

```python
packed0 = np.packbits(self.x, axis=0, bitorder=bitorder)
```

**Verification:**
```python
assert_equal(unpacked0.dtype, np.uint8)
```

### Step 2: Assign unpacked0 = np.unpackbits(...)

```python
unpacked0 = np.unpackbits(packed0, axis=0, count=count, bitorder=bitorder)
```

**Verification:**
```python
assert_array_equal(unpacked0, self.padded2[:cutoff, :self.x.shape[1]])
```

### Step 3: Call assert_equal()

```python
assert_equal(unpacked0.dtype, np.uint8)
```

**Verification:**
```python
assert_equal(unpacked1.dtype, np.uint8)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(unpacked0, self.padded2[:cutoff, :self.x.shape[1]])
```

**Verification:**
```python
assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :cutoff])
```

### Step 5: Assign packed1 = np.packbits(...)

```python
packed1 = np.packbits(self.x, axis=1, bitorder=bitorder)
```

### Step 6: Assign unpacked1 = np.unpackbits(...)

```python
unpacked1 = np.unpackbits(packed1, axis=1, count=count, bitorder=bitorder)
```

### Step 7: Call assert_equal()

```python
assert_equal(unpacked1.dtype, np.uint8)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :cutoff])
```

### Step 9: Assign cutoff = value

```python
cutoff = count - 1
```

### Step 10: Assign cutoff = count

```python
cutoff = count
```


## Complete Example

```python
# Setup
# Fixtures: bitorder, count

# Workflow
if count < 0:
    cutoff = count - 1
else:
    cutoff = count
packed0 = np.packbits(self.x, axis=0, bitorder=bitorder)
unpacked0 = np.unpackbits(packed0, axis=0, count=count, bitorder=bitorder)
assert_equal(unpacked0.dtype, np.uint8)
assert_array_equal(unpacked0, self.padded2[:cutoff, :self.x.shape[1]])
packed1 = np.packbits(self.x, axis=1, bitorder=bitorder)
unpacked1 = np.unpackbits(packed1, axis=1, count=count, bitorder=bitorder)
assert_equal(unpacked1.dtype, np.uint8)
assert_array_equal(unpacked1, self.padded2[:self.x.shape[0], :cutoff])
```

## Next Steps


---

*Source: test_packbits.py:328 | Complexity: Advanced | Last updated: 2026-06-02*