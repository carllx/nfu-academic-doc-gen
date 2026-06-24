# How To: Region

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test region

## Prerequisites

**Required Modules:**
- `lib`
- `smmap.util`
- `os`
- `sys`


## Step-by-Step Guide

### Step 1: Assign rfull2 = rfull

```python
rfull2 = rfull
```

**Verification:**
```python
assert rfull.ofs_begin() == 0 and rfull.size() == fc.size
```

### Step 2: Assign w = MapWindow.from_region(...)

```python
w = MapWindow.from_region(rfull)
```

**Verification:**
```python
assert rfull.ofs_end() == fc.size
```

### Step 3: Assign half_size = value

```python
half_size = fc.size // 2
```

**Verification:**
```python
assert rhalfofs.ofs_begin() == rofs and rhalfofs.size() == fc.size - rofs
```

### Step 4: Assign rofs = align_to_mmap(...)

```python
rofs = align_to_mmap(4200, False)
```

**Verification:**
```python
assert rhalfsize.ofs_begin() == 0 and rhalfsize.size() == half_size
```

### Step 5: Assign rfull = MapRegion(...)

```python
rfull = MapRegion(fc.path, 0, fc.size)
```

**Verification:**
```python
assert rfull.includes_ofs(0) and rfull.includes_ofs(fc.size - 1) and rfull.includes_ofs(half_size)
```

### Step 6: Assign rhalfofs = MapRegion(...)

```python
rhalfofs = MapRegion(fc.path, rofs, fc.size)
```

**Verification:**
```python
assert not rfull.includes_ofs(-1) and (not rfull.includes_ofs(sys.maxsize))
```

### Step 7: Assign rhalfsize = MapRegion(...)

```python
rhalfsize = MapRegion(fc.path, 0, half_size)
```

**Verification:**
```python
assert rfull.client_count() == 1
```


## Complete Example

```python
# Workflow
with FileCreator(self.k_window_test_size, 'window_test') as fc:
    half_size = fc.size // 2
    rofs = align_to_mmap(4200, False)
    rfull = MapRegion(fc.path, 0, fc.size)
    rhalfofs = MapRegion(fc.path, rofs, fc.size)
    rhalfsize = MapRegion(fc.path, 0, half_size)
    assert rfull.ofs_begin() == 0 and rfull.size() == fc.size
    assert rfull.ofs_end() == fc.size
    assert rhalfofs.ofs_begin() == rofs and rhalfofs.size() == fc.size - rofs
    assert rhalfsize.ofs_begin() == 0 and rhalfsize.size() == half_size
    assert rfull.includes_ofs(0) and rfull.includes_ofs(fc.size - 1) and rfull.includes_ofs(half_size)
    assert not rfull.includes_ofs(-1) and (not rfull.includes_ofs(sys.maxsize))
assert rfull.client_count() == 1
rfull2 = rfull
assert rfull.client_count() == 1, 'no auto-counting'
w = MapWindow.from_region(rfull)
assert w.ofs == rfull.ofs_begin() and w.ofs_end() == rfull.ofs_end()
```

## Next Steps


---

*Source: test_util.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*