# How To: Memory Manager

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memory manager

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

### Step 1: Assign slide_man = SlidingWindowMapManager(...)

```python
slide_man = SlidingWindowMapManager()
```

**Verification:**
```python
assert man.num_file_handles() == 0
```

### Step 2: Assign static_man = StaticWindowMapManager(...)

```python
static_man = StaticWindowMapManager()
```

**Verification:**
```python
assert man.num_open_files() == 0
```

### Step 3: Assign winsize_cmp_val = 0

```python
winsize_cmp_val = 0
```

**Verification:**
```python
assert man.window_size() > winsize_cmp_val
```

### Step 4: Call man._collect_lru_region()

```python
man._collect_lru_region(0)
```

**Verification:**
```python
assert man.mapped_memory_size() == 0
```

### Step 5: Call man._collect_lru_region()

```python
man._collect_lru_region(10)
```

**Verification:**
```python
assert man.max_mapped_memory_size() > 0
```

### Step 6: Assign winsize_cmp_val = value

```python
winsize_cmp_val = -1
```

**Verification:**
```python
assert man._collect_lru_region(sys.maxsize) == 0
```

### Step 7: Assign fd = os.open(...)

```python
fd = os.open(fc.path, os.O_RDONLY)
```

**Verification:**
```python
assert c.path_or_fd() is item
```

### Step 8: Call os.close()

```python
os.close(fd)
```

**Verification:**
```python
assert c.use_region(10, 10).is_valid()
```

### Step 9: Assign c = man.make_cursor(...)

```python
c = man.make_cursor(item)
```

**Verification:**
```python
assert c.ofs_begin() == 10
```

### Step 10: Call self.assertRaises()

```python
self.assertRaises(ValueError, c.path)
```

**Verification:**
```python
assert c.size() == 10
```

### Step 11: Call self.assertRaises()

```python
self.assertRaises(ValueError, c.fd)
```

**Verification:**
```python
assert c.buffer()[:] == fp.read(20)[10:]
```


## Complete Example

```python
# Workflow
slide_man = SlidingWindowMapManager()
static_man = StaticWindowMapManager()
for man in (static_man, slide_man):
    assert man.num_file_handles() == 0
    assert man.num_open_files() == 0
    winsize_cmp_val = 0
    if isinstance(man, StaticWindowMapManager):
        winsize_cmp_val = -1
    assert man.window_size() > winsize_cmp_val
    assert man.mapped_memory_size() == 0
    assert man.max_mapped_memory_size() > 0
    man._collect_lru_region(0)
    man._collect_lru_region(10)
    assert man._collect_lru_region(sys.maxsize) == 0
    with FileCreator(self.k_window_test_size, 'manager_test') as fc:
        fd = os.open(fc.path, os.O_RDONLY)
        try:
            for item in (fc.path, fd):
                c = man.make_cursor(item)
                assert c.path_or_fd() is item
                assert c.use_region(10, 10).is_valid()
                assert c.ofs_begin() == 10
                assert c.size() == 10
                with open(fc.path, 'rb') as fp:
                    assert c.buffer()[:] == fp.read(20)[10:]
            if isinstance(item, int):
                self.assertRaises(ValueError, c.path)
            else:
                self.assertRaises(ValueError, c.fd)
        finally:
            os.close(fd)
```

## Next Steps


---

*Source: test_mman.py:50 | Complexity: Advanced | Last updated: 2026-06-02*