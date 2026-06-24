# How To: Int Op

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test int op

## Prerequisites

**Required Modules:**
- `__future__`
- `unittest`
- `mypyc.ir.ops`
- `mypyc.ir.pprint`
- `mypyc.ir.rtypes`


## Step-by-Step Guide

### Step 1: Assign n1 = Integer(...)

```python
n1 = Integer(2)
```

**Verification:**
```python
assert generate_names_for_ir([], [block]) == {op1: 'r0', op2: 'r1'}
```

### Step 2: Assign n2 = Integer(...)

```python
n2 = Integer(4)
```

### Step 3: Assign op1 = IntOp(...)

```python
op1 = IntOp(int_rprimitive, n1, n2, IntOp.ADD)
```

### Step 4: Assign op2 = IntOp(...)

```python
op2 = IntOp(int_rprimitive, op1, n2, IntOp.ADD)
```

### Step 5: Assign block = make_block(...)

```python
block = make_block([op1, op2, Unreachable()])
```

**Verification:**
```python
assert generate_names_for_ir([], [block]) == {op1: 'r0', op2: 'r1'}
```


## Complete Example

```python
# Workflow
n1 = Integer(2)
n2 = Integer(4)
op1 = IntOp(int_rprimitive, n1, n2, IntOp.ADD)
op2 = IntOp(int_rprimitive, op1, n2, IntOp.ADD)
block = make_block([op1, op2, Unreachable()])
assert generate_names_for_ir([], [block]) == {op1: 'r0', op2: 'r1'}
```

## Next Steps


---

*Source: test_pprint.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*