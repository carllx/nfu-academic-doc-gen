# How To: Eq And Hash

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test eq and hash

## Prerequisites

**Required Modules:**
- `__future__`
- `unittest`
- `mypyc.ir.rtypes`
- `mypyc.rt_subtype`


## Step-by-Step Guide

### Step 1: Assign r = RStruct(...)

```python
r = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert hash(r) == hash(r1)
```

### Step 2: Assign r1 = RStruct(...)

```python
r1 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert r == r1
```

### Step 3: Assign r2 = RStruct(...)

```python
r2 = RStruct('Foq', ['a', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert hash(r) != hash(r2)
```

### Step 4: Assign r3 = RStruct(...)

```python
r3 = RStruct('Foo', ['a', 'c'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert r != r2
```

### Step 5: Assign r4 = RStruct(...)

```python
r4 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive, bool_rprimitive])
```

**Verification:**
```python
assert hash(r) != hash(r3)
```


## Complete Example

```python
# Workflow
r = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
r1 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
assert hash(r) == hash(r1)
assert r == r1
r2 = RStruct('Foq', ['a', 'b'], [bool_rprimitive, int_rprimitive])
assert hash(r) != hash(r2)
assert r != r2
r3 = RStruct('Foo', ['a', 'c'], [bool_rprimitive, int_rprimitive])
assert hash(r) != hash(r3)
assert r != r3
r4 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive, bool_rprimitive])
assert hash(r) != hash(r4)
assert r != r4
```

## Next Steps


---

*Source: test_struct.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*