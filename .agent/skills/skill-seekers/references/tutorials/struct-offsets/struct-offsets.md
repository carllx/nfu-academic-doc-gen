# How To: Struct Offsets

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test struct offsets

## Prerequisites

**Required Modules:**
- `__future__`
- `unittest`
- `mypyc.ir.rtypes`
- `mypyc.rt_subtype`


## Step-by-Step Guide

### Step 1: Assign r = RStruct(...)

```python
r = RStruct('', [], [bool_rprimitive, int32_rprimitive, int64_rprimitive])
```

**Verification:**
```python
assert r.size == 16
```

### Step 2: Assign r1 = RStruct(...)

```python
r1 = RStruct('', [], [bool_rprimitive, bool_rprimitive])
```

**Verification:**
```python
assert r.offsets == [0, 4, 8]
```

### Step 3: Assign r2 = RStruct(...)

```python
r2 = RStruct('', [], [int32_rprimitive, bool_rprimitive])
```

**Verification:**
```python
assert r1.size == 2
```

### Step 4: Assign r3 = RStruct(...)

```python
r3 = RStruct('', [], [int64_rprimitive, bool_rprimitive])
```

**Verification:**
```python
assert r1.offsets == [0, 1]
```

### Step 5: Assign r4 = RStruct(...)

```python
r4 = RStruct('', [], [bool_rprimitive, bool_rprimitive, bool_rprimitive, int32_rprimitive])
```

**Verification:**
```python
assert r2.offsets == [0, 4]
```

### Step 6: Assign r5 = RStruct(...)

```python
r5 = RStruct('', [], [bool_rprimitive, r])
```

**Verification:**
```python
assert r3.offsets == [0, 8]
```

### Step 7: Assign r6 = RStruct(...)

```python
r6 = RStruct('', [], [int32_rprimitive, r5])
```

**Verification:**
```python
assert r2.size == 8
```

### Step 8: Assign r7 = RStruct(...)

```python
r7 = RStruct('', [], [bool_rprimitive, r4])
```

**Verification:**
```python
assert r3.size == 16
```


## Complete Example

```python
# Workflow
r = RStruct('', [], [bool_rprimitive, int32_rprimitive, int64_rprimitive])
assert r.size == 16
assert r.offsets == [0, 4, 8]
r1 = RStruct('', [], [bool_rprimitive, bool_rprimitive])
assert r1.size == 2
assert r1.offsets == [0, 1]
r2 = RStruct('', [], [int32_rprimitive, bool_rprimitive])
r3 = RStruct('', [], [int64_rprimitive, bool_rprimitive])
assert r2.offsets == [0, 4]
assert r3.offsets == [0, 8]
assert r2.size == 8
assert r3.size == 16
r4 = RStruct('', [], [bool_rprimitive, bool_rprimitive, bool_rprimitive, int32_rprimitive])
assert r4.size == 8
assert r4.offsets == [0, 1, 2, 4]
r5 = RStruct('', [], [bool_rprimitive, r])
assert r5.offsets == [0, 8]
assert r5.size == 24
r6 = RStruct('', [], [int32_rprimitive, r5])
assert r6.offsets == [0, 8]
assert r6.size == 32
r7 = RStruct('', [], [bool_rprimitive, r4])
assert r7.offsets == [0, 4]
assert r7.size == 12
```

## Next Steps


---

*Source: test_struct.py:17 | Complexity: Advanced | Last updated: 2026-06-02*