# How To: Del

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test del

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign fp_base = memmap(...)

```python
fp_base = memmap(self.tmpfp, dtype=self.dtype, mode='w+', shape=self.shape)
```

**Verification:**
```python
assert_equal(fp_view[0], 5)
```

### Step 2: Assign unknown = 5

```python
fp_base[0] = 5
```

**Verification:**
```python
assert_equal(fp_base[0], 5)
```

### Step 3: Assign fp_view = value

```python
fp_view = fp_base[0:1]
```

**Verification:**
```python
assert_equal(fp_base[0], 6)
```

### Step 4: Call assert_equal()

```python
assert_equal(fp_view[0], 5)
```

### Step 5: Call assert_equal()

```python
assert_equal(fp_base[0], 5)
```

### Step 6: Assign unknown = 6

```python
fp_base[0] = 6
```

### Step 7: Call assert_equal()

```python
assert_equal(fp_base[0], 6)
```


## Complete Example

```python
# Workflow
fp_base = memmap(self.tmpfp, dtype=self.dtype, mode='w+', shape=self.shape)
fp_base[0] = 5
fp_view = fp_base[0:1]
assert_equal(fp_view[0], 5)
del fp_view
assert_equal(fp_base[0], 5)
fp_base[0] = 6
assert_equal(fp_base[0], 6)
```

## Next Steps


---

*Source: test_memmap.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*