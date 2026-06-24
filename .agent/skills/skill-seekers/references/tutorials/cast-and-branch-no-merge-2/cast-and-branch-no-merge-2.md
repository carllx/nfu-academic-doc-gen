# How To: Cast And Branch No Merge 2

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test cast and branch no merge 2

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
self.registers: list[Register] = []

def add_local(name: str, rtype: RType) -> Register:
    reg = Register(rtype, name)
    self.registers.append(reg)
    return reg
self.n = add_local('n', int_rprimitive)
self.m = add_local('m', int_rprimitive)
self.k = add_local('k', int_rprimitive)
self.l = add_local('l', list_rprimitive)
self.ll = add_local('ll', list_rprimitive)
self.o = add_local('o', object_rprimitive)
self.o2 = add_local('o2', object_rprimitive)
self.d = add_local('d', dict_rprimitive)
self.b = add_local('b', bool_rprimitive)
self.s1 = add_local('s1', short_int_rprimitive)
self.s2 = add_local('s2', short_int_rprimitive)
self.i32 = add_local('i32', int32_rprimitive)
self.i32_1 = add_local('i32_1', int32_rprimitive)
self.i64 = add_local('i64', int64_rprimitive)
self.i64_1 = add_local('i64_1', int64_rprimitive)
self.ptr = add_local('ptr', pointer_rprimitive)
self.t = add_local('t', RTuple([int_rprimitive, bool_rprimitive]))
self.tt = add_local('tt', RTuple([RTuple([int_rprimitive, bool_rprimitive]), bool_rprimitive]))
ir = ClassIR('A', 'mod')
ir.attributes = {'x': bool_rprimitive, 'y': int_rprimitive, 'i1': int64_rprimitive, 'i2': int32_rprimitive, 't': RTuple([object_rprimitive, object_rprimitive])}
ir.bitmap_attrs = ['i1', 'i2']
compute_vtable(ir)
ir.mro = [ir]
self.r = add_local('r', RInstance(ir))
self.none = add_local('none', none_rprimitive)
self.struct_type = RStruct('Foo', ['b', 'x', 'y'], [bool_rprimitive, int32_rprimitive, int64_rprimitive])
self.st = add_local('st', self.struct_type)
self.context = EmitterContext(NameGenerator([['mod']]))
```

## Step-by-Step Guide

### Step 1: Assign op = Cast(...)

```python
op = Cast(self.r, dict_rprimitive, 1)
```

### Step 2: Assign next_block = BasicBlock(...)

```python
next_block = BasicBlock(9)
```

### Step 3: Assign branch = Branch(...)

```python
branch = Branch(op, BasicBlock(8), next_block, Branch.IS_ERROR)
```

### Step 4: Assign branch.negated = True

```python
branch.negated = True
```

### Step 5: Assign branch.traceback_entry = value

```python
branch.traceback_entry = ('foobar', 123)
```

### Step 6: Call self.assert_emit()

```python
self.assert_emit(op, '            if (likely(PyDict_Check(cpy_r_r)))\n                cpy_r_r0 = cpy_r_r;\n            else {\n                CPy_TypeError("dict", cpy_r_r);\n                cpy_r_r0 = NULL;\n            }\n            ', next_block=next_block, next_branch=branch)
```


## Complete Example

```python
# Setup
self.registers: list[Register] = []

def add_local(name: str, rtype: RType) -> Register:
    reg = Register(rtype, name)
    self.registers.append(reg)
    return reg
self.n = add_local('n', int_rprimitive)
self.m = add_local('m', int_rprimitive)
self.k = add_local('k', int_rprimitive)
self.l = add_local('l', list_rprimitive)
self.ll = add_local('ll', list_rprimitive)
self.o = add_local('o', object_rprimitive)
self.o2 = add_local('o2', object_rprimitive)
self.d = add_local('d', dict_rprimitive)
self.b = add_local('b', bool_rprimitive)
self.s1 = add_local('s1', short_int_rprimitive)
self.s2 = add_local('s2', short_int_rprimitive)
self.i32 = add_local('i32', int32_rprimitive)
self.i32_1 = add_local('i32_1', int32_rprimitive)
self.i64 = add_local('i64', int64_rprimitive)
self.i64_1 = add_local('i64_1', int64_rprimitive)
self.ptr = add_local('ptr', pointer_rprimitive)
self.t = add_local('t', RTuple([int_rprimitive, bool_rprimitive]))
self.tt = add_local('tt', RTuple([RTuple([int_rprimitive, bool_rprimitive]), bool_rprimitive]))
ir = ClassIR('A', 'mod')
ir.attributes = {'x': bool_rprimitive, 'y': int_rprimitive, 'i1': int64_rprimitive, 'i2': int32_rprimitive, 't': RTuple([object_rprimitive, object_rprimitive])}
ir.bitmap_attrs = ['i1', 'i2']
compute_vtable(ir)
ir.mro = [ir]
self.r = add_local('r', RInstance(ir))
self.none = add_local('none', none_rprimitive)
self.struct_type = RStruct('Foo', ['b', 'x', 'y'], [bool_rprimitive, int32_rprimitive, int64_rprimitive])
self.st = add_local('st', self.struct_type)
self.context = EmitterContext(NameGenerator([['mod']]))

# Workflow
op = Cast(self.r, dict_rprimitive, 1)
next_block = BasicBlock(9)
branch = Branch(op, BasicBlock(8), next_block, Branch.IS_ERROR)
branch.negated = True
branch.traceback_entry = ('foobar', 123)
self.assert_emit(op, '            if (likely(PyDict_Check(cpy_r_r)))\n                cpy_r_r0 = cpy_r_r;\n            else {\n                CPy_TypeError("dict", cpy_r_r);\n                cpy_r_r0 = NULL;\n            }\n            ', next_block=next_block, next_branch=branch)
```

## Next Steps


---

*Source: test_emitfunc.py:766 | Complexity: Advanced | Last updated: 2026-06-02*