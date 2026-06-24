# How To: Invalid Assign

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test invalid assign

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
arg_reg = Register(type=int64_rprimitive, name='r1')
```

**Verification:**
```python
assert_has_error(fn, FnError(source=assign, desc='Cannot coerce source type i32 to dest type i64'))
```

### Step 2: Assign assign = Assign(...)

```python
assign = Assign(dest=arg_reg, src=Integer(value=5, rtype=int32_rprimitive))
```

### Step 3: Assign ret = Return(...)

```python
ret = Return(value=NONE_VALUE)
```

### Step 4: Assign fn = FuncIR(...)

```python
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[arg_reg], blocks=[self.basic_block([assign, ret])])
```

### Step 5: Call assert_has_error()

```python
assert_has_error(fn, FnError(source=assign, desc='Cannot coerce source type i32 to dest type i64'))
```


## Complete Example

```python
# Workflow
arg_reg = Register(type=int64_rprimitive, name='r1')
assign = Assign(dest=arg_reg, src=Integer(value=5, rtype=int32_rprimitive))
ret = Return(value=NONE_VALUE)
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[arg_reg], blocks=[self.basic_block([assign, ret])])
assert_has_error(fn, FnError(source=assign, desc='Cannot coerce source type i32 to dest type i64'))
```

## Next Steps


---

*Source: test_ircheck.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*