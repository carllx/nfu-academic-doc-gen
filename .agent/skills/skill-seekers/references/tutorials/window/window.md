# How To: Window

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test window

## Prerequisites

**Required Modules:**
- `lib`
- `smmap.util`
- `os`
- `sys`


## Step-by-Step Guide

### Step 1: Assign wl = MapWindow(...)

```python
wl = MapWindow(0, 1)
```

**Verification:**
```python
assert wl.ofs_end() == 1
```

### Step 2: Assign wc = MapWindow(...)

```python
wc = MapWindow(1, 1)
```

**Verification:**
```python
assert wc.ofs_end() == 2
```

### Step 3: Assign wc2 = MapWindow(...)

```python
wc2 = MapWindow(10, 5)
```

**Verification:**
```python
assert wr.ofs_end() == 8050
```

### Step 4: Assign wr = MapWindow(...)

```python
wr = MapWindow(8000, 50)
```

**Verification:**
```python
assert wc.ofs == 1 and wc.size == 1
```

### Step 5: Assign maxsize = 100

```python
maxsize = 100
```

**Verification:**
```python
assert wl.ofs == 0 and wl.size == 1
```

### Step 6: Call wc.extend_left_to()

```python
wc.extend_left_to(wl, maxsize)
```

**Verification:**
```python
assert wc2.ofs == wc.ofs_end() and pofs_end == wc2.ofs_end()
```

### Step 7: Call wl.extend_right_to()

```python
wl.extend_right_to(wc, maxsize)
```

**Verification:**
```python
assert wc.ofs == 1 and wc.size == maxsize
```

### Step 8: Call wl.extend_right_to()

```python
wl.extend_right_to(wc, maxsize)
```

**Verification:**
```python
assert wc.ofs == 1 and wc.size == maxsize
```

### Step 9: Assign pofs_end = wc2.ofs_end(...)

```python
pofs_end = wc2.ofs_end()
```

**Verification:**
```python
assert wc.ofs_end() == wr.ofs and wc.ofs == 1
```

### Step 10: Call wc2.extend_left_to()

```python
wc2.extend_left_to(wc, maxsize)
```

**Verification:**
```python
assert wr.size == maxsize
```

### Step 11: Call wc.extend_right_to()

```python
wc.extend_right_to(wr, maxsize)
```

**Verification:**
```python
assert wr.ofs == wc2.ofs_end()
```

### Step 12: Call wc.extend_right_to()

```python
wc.extend_right_to(wr, maxsize)
```

**Verification:**
```python
assert wc.ofs == 0 and wc.size == align_to_mmap(wc.size, True)
```

### Step 13: Call wc.extend_right_to()

```python
wc.extend_right_to(wr, sys.maxsize)
```

**Verification:**
```python
assert wc.ofs_end() == wr.ofs and wc.ofs == 1
```

### Step 14: Call wr.extend_left_to()

```python
wr.extend_left_to(wc2, maxsize)
```

### Step 15: Call wr.extend_left_to()

```python
wr.extend_left_to(wc2, maxsize)
```

**Verification:**
```python
assert wr.size == maxsize
```

### Step 16: Call wr.extend_left_to()

```python
wr.extend_left_to(wc2, sys.maxsize)
```

**Verification:**
```python
assert wr.ofs == wc2.ofs_end()
```

### Step 17: Call wc.align()

```python
wc.align()
```

**Verification:**
```python
assert wc.ofs == 0 and wc.size == align_to_mmap(wc.size, True)
```


## Complete Example

```python
# Workflow
wl = MapWindow(0, 1)
wc = MapWindow(1, 1)
wc2 = MapWindow(10, 5)
wr = MapWindow(8000, 50)
assert wl.ofs_end() == 1
assert wc.ofs_end() == 2
assert wr.ofs_end() == 8050
maxsize = 100
wc.extend_left_to(wl, maxsize)
assert wc.ofs == 1 and wc.size == 1
wl.extend_right_to(wc, maxsize)
wl.extend_right_to(wc, maxsize)
assert wl.ofs == 0 and wl.size == 1
pofs_end = wc2.ofs_end()
wc2.extend_left_to(wc, maxsize)
assert wc2.ofs == wc.ofs_end() and pofs_end == wc2.ofs_end()
wc.extend_right_to(wr, maxsize)
assert wc.ofs == 1 and wc.size == maxsize
wc.extend_right_to(wr, maxsize)
assert wc.ofs == 1 and wc.size == maxsize
wc.extend_right_to(wr, sys.maxsize)
assert wc.ofs_end() == wr.ofs and wc.ofs == 1
wr.extend_left_to(wc2, maxsize)
wr.extend_left_to(wc2, maxsize)
assert wr.size == maxsize
wr.extend_left_to(wc2, sys.maxsize)
assert wr.ofs == wc2.ofs_end()
wc.align()
assert wc.ofs == 0 and wc.size == align_to_mmap(wc.size, True)
```

## Next Steps


---

*Source: test_util.py:18 | Complexity: Advanced | Last updated: 2026-06-02*