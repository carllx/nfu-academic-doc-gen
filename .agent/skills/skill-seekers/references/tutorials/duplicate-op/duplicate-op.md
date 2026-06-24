# How To: Duplicate Op

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test duplicate op

## Prerequisites

**Required Modules:**
- `__future__`
- `unittest`
- `mypyc.analysis.ircheck`
- `mypyc.ir.class_ir`
- `mypyc.ir.func_ir`
- `mypyc.ir.ops`
- `mypyc.ir.pprint`
- `mypyc.ir.rtypes`


## Step-by-Step Guide

### Step 1: Assign arg_reg = Register(...)

```python
arg_reg = Register(type=int32_rprimitive, name='r1')
```

**Verification:**
```python
assert_has_error(fn, FnError(source=assign, desc='Func has a duplicate op'))
```

### Step 2: Assign assign = Assign(...)

```python
assign = Assign(dest=arg_reg, src=Integer(value=5, rtype=int32_rprimitive))
```

### Step 3: Assign block = self.basic_block(...)

```python
block = self.basic_block([assign, assign, Return(value=NONE_VALUE)])
```

### Step 4: Assign fn = FuncIR(...)

```python
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[], blocks=[block])
```

### Step 5: Call assert_has_error()

```python
assert_has_error(fn, FnError(source=assign, desc='Func has a duplicate op'))
```


## Complete Example

```python
# Workflow
arg_reg = Register(type=int32_rprimitive, name='r1')
assign = Assign(dest=arg_reg, src=Integer(value=5, rtype=int32_rprimitive))
block = self.basic_block([assign, assign, Return(value=NONE_VALUE)])
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[], blocks=[block])
assert_has_error(fn, FnError(source=assign, desc='Func has a duplicate op'))
```

## Next Steps


---

*Source: test_ircheck.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*