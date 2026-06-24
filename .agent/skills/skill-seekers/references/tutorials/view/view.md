# How To: View

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test view

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

### Step 1: Assign fp = memmap(...)

```python
fp = memmap(self.tmpfp, dtype=self.dtype, shape=self.shape)
```

**Verification:**
```python
assert_(new1.base is fp)
```

### Step 2: Assign new1 = fp.view(...)

```python
new1 = fp.view()
```

**Verification:**
```python
assert_(new2.base is fp)
```

### Step 3: Assign new2 = new1.view(...)

```python
new2 = new1.view()
```

**Verification:**
```python
assert_(new_array.base is fp)
```

### Step 4: Call assert_()

```python
assert_(new1.base is fp)
```

### Step 5: Call assert_()

```python
assert_(new2.base is fp)
```

### Step 6: Assign new_array = asarray(...)

```python
new_array = asarray(fp)
```

### Step 7: Call assert_()

```python
assert_(new_array.base is fp)
```


## Complete Example

```python
# Workflow
fp = memmap(self.tmpfp, dtype=self.dtype, shape=self.shape)
new1 = fp.view()
new2 = new1.view()
assert_(new1.base is fp)
assert_(new2.base is fp)
new_array = asarray(fp)
assert_(new_array.base is fp)
```

## Next Steps


---

*Source: test_memmap.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*