# How To: Register

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test register

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `unittest`
- `mypy.test.helpers`
- `mypyc.codegen.emit`
- `mypyc.codegen.emitfunc`
- `mypyc.common`
- `mypyc.ir.class_ir`
- `mypyc.ir.func_ir`
- `mypyc.ir.ops`
- `mypyc.ir.pprint`
- `mypyc.ir.rtypes`
- `mypyc.irbuild.vtable`
- `mypyc.namegen`
- `mypyc.primitives.dict_ops`
- `mypyc.primitives.int_ops`
- `mypyc.primitives.list_ops`
- `mypyc.primitives.misc_ops`
- `mypyc.primitives.registry`
- `mypyc.subtype`

**Setup Required:**
```python
self.arg = RuntimeArg('arg', int_rprimitive)
self.reg = Register(int_rprimitive, 'arg')
self.block = BasicBlock(0)
```

## Step-by-Step Guide

### Step 1: Assign reg = Register(...)

```python
reg = Register(int_rprimitive)
```

**Verification:**
```python
assert_string_arrays_equal(['PyObject *CPyDef_myfunc(CPyTagged cpy_r_arg) {\n', '    CPyTagged cpy_r_r0;\n', '    cpy_r_r0 = 10;\n', '    CPy_Unreachable();\n', '}\n'], result, msg='Generated code invalid')
```

### Step 2: Assign op = Assign(...)

```python
op = Assign(reg, Integer(5))
```

### Step 3: Call self.block.ops.append()

```python
self.block.ops.append(op)
```

### Step 4: Call self.block.ops.append()

```python
self.block.ops.append(Unreachable())
```

### Step 5: Assign fn = FuncIR(...)

```python
fn = FuncIR(FuncDecl('myfunc', None, 'mod', FuncSignature([self.arg], list_rprimitive)), [self.reg], [self.block])
```

### Step 6: Assign value_names = generate_names_for_ir(...)

```python
value_names = generate_names_for_ir(fn.arg_regs, fn.blocks)
```

### Step 7: Assign emitter = Emitter(...)

```python
emitter = Emitter(EmitterContext(NameGenerator([['mod']])), value_names)
```

### Step 8: Call generate_native_function()

```python
generate_native_function(fn, emitter, 'prog.py', 'prog')
```

### Step 9: Assign result = value

```python
result = emitter.fragments
```

### Step 10: Call assert_string_arrays_equal()

```python
assert_string_arrays_equal(['PyObject *CPyDef_myfunc(CPyTagged cpy_r_arg) {\n', '    CPyTagged cpy_r_r0;\n', '    cpy_r_r0 = 10;\n', '    CPy_Unreachable();\n', '}\n'], result, msg='Generated code invalid')
```


## Complete Example

```python
# Setup
self.arg = RuntimeArg('arg', int_rprimitive)
self.reg = Register(int_rprimitive, 'arg')
self.block = BasicBlock(0)

# Workflow
reg = Register(int_rprimitive)
op = Assign(reg, Integer(5))
self.block.ops.append(op)
self.block.ops.append(Unreachable())
fn = FuncIR(FuncDecl('myfunc', None, 'mod', FuncSignature([self.arg], list_rprimitive)), [self.reg], [self.block])
value_names = generate_names_for_ir(fn.arg_regs, fn.blocks)
emitter = Emitter(EmitterContext(NameGenerator([['mod']])), value_names)
generate_native_function(fn, emitter, 'prog.py', 'prog')
result = emitter.fragments
assert_string_arrays_equal(['PyObject *CPyDef_myfunc(CPyTagged cpy_r_arg) {\n', '    CPyTagged cpy_r_r0;\n', '    cpy_r_r0 = 10;\n', '    CPy_Unreachable();\n', '}\n'], result, msg='Generated code invalid')
```

## Next Steps


---

*Source: test_emitfunc.py:986 | Complexity: Advanced | Last updated: 2026-06-02*