# How To: Cursor

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cursor

## Prerequisites

**Required Modules:**
- `lib`
- `smmap.mman`
- `smmap.util`
- `random`
- `time`
- `os`
- `sys`
- `copy`


## Step-by-Step Guide

### Step 1: Assign cio = copy(...)

```python
cio = copy(cv)
```

**Verification:**
```python
assert not ci.is_valid()
```

### Step 2: Call ci.assign()

```python
ci.assign(cv)
```

**Verification:**
```python
assert not ci.is_associated()
```

### Step 3: Call cv.unuse_region()

```python
cv.unuse_region()
```

**Verification:**
```python
assert ci.size() == 0
```

### Step 4: Call cv.unuse_region()

```python
cv.unuse_region()
```

**Verification:**
```python
assert not cv.is_valid()
```

### Step 5: Call cv._destroy()

```python
cv._destroy()
```

**Verification:**
```python
assert cv.is_associated()
```

### Step 6: Call WindowCursor._destroy()

```python
WindowCursor(man)._destroy()
```

**Verification:**
```python
assert cv.file_size() == fc.size
```

### Step 7: Assign man = SlidingWindowMapManager(...)

```python
man = SlidingWindowMapManager()
```

**Verification:**
```python
assert cv.path() == fc.path
```

### Step 8: Assign ci = WindowCursor(...)

```python
ci = WindowCursor(man)
```

**Verification:**
```python
assert not cio.is_valid() and cio.is_associated()
```

### Step 9: Assign cv = man.make_cursor(...)

```python
cv = man.make_cursor(fc.path)
```

**Verification:**
```python
assert not ci.is_associated()
```


## Complete Example

```python
# Workflow
with FileCreator(self.k_window_test_size, 'cursor_test') as fc:
    man = SlidingWindowMapManager()
    ci = WindowCursor(man)
    assert not ci.is_valid()
    assert not ci.is_associated()
    assert ci.size() == 0
    cv = man.make_cursor(fc.path)
    assert not cv.is_valid()
    assert cv.is_associated()
    assert cv.file_size() == fc.size
    assert cv.path() == fc.path
cio = copy(cv)
assert not cio.is_valid() and cio.is_associated()
assert not ci.is_associated()
ci.assign(cv)
assert not ci.is_valid() and ci.is_associated()
cv.unuse_region()
cv.unuse_region()
cv._destroy()
WindowCursor(man)._destroy()
```

## Next Steps


---

*Source: test_mman.py:19 | Complexity: Advanced | Last updated: 2026-06-02*