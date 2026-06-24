# How To: Runtime Subtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test runtime subtype

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
assert is_runtime_subtype(r1, r) is True
```

### Step 2: Assign r1 = RStruct(...)

```python
r1 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert is_runtime_subtype(r2, r) is False
```

### Step 3: Assign r2 = RStruct(...)

```python
r2 = RStruct('Bar', ['c', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert is_runtime_subtype(r3, r) is False
```

### Step 4: Assign r3 = RStruct(...)

```python
r3 = RStruct('Baz', ['a', 'b'], [bool_rprimitive, int_rprimitive])
```

**Verification:**
```python
assert is_runtime_subtype(r4, r) is False
```

### Step 5: Assign r4 = RStruct(...)

```python
r4 = RStruct('FooBar', ['a', 'b'], [bool_rprimitive, int32_rprimitive])
```

**Verification:**
```python
assert is_runtime_subtype(r5, r) is False
```

### Step 6: Assign r5 = RStruct(...)

```python
r5 = RStruct('FooBarBaz', ['a', 'b', 'c'], [bool_rprimitive, int_rprimitive, bool_rprimitive])
```

**Verification:**
```python
assert is_runtime_subtype(r1, r) is True
```


## Complete Example

```python
# Workflow
r = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
r1 = RStruct('Foo', ['a', 'b'], [bool_rprimitive, int_rprimitive])
r2 = RStruct('Bar', ['c', 'b'], [bool_rprimitive, int_rprimitive])
r3 = RStruct('Baz', ['a', 'b'], [bool_rprimitive, int_rprimitive])
r4 = RStruct('FooBar', ['a', 'b'], [bool_rprimitive, int32_rprimitive])
r5 = RStruct('FooBarBaz', ['a', 'b', 'c'], [bool_rprimitive, int_rprimitive, bool_rprimitive])
assert is_runtime_subtype(r1, r) is True
assert is_runtime_subtype(r2, r) is False
assert is_runtime_subtype(r3, r) is False
assert is_runtime_subtype(r4, r) is False
assert is_runtime_subtype(r5, r) is False
```

## Next Steps


---

*Source: test_struct.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*