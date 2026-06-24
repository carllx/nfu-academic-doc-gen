# How To: Branch Rare

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test branch rare

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

### Step 1: Call self.assert_emit()

```python
self.assert_emit(Branch(self.b, BasicBlock(8), BasicBlock(9), Branch.BOOL, rare=True), 'if (unlikely(cpy_r_b)) {\n                                goto CPyL8;\n                            } else\n                                goto CPyL9;\n                         ')
```

### Step 2: Assign next_block = BasicBlock(...)

```python
next_block = BasicBlock(9)
```

### Step 3: Call self.assert_emit()

```python
self.assert_emit(Branch(self.b, BasicBlock(8), next_block, Branch.BOOL, rare=True), 'if (unlikely(cpy_r_b)) goto CPyL8;', next_block=next_block)
```

### Step 4: Assign next_block = BasicBlock(...)

```python
next_block = BasicBlock(8)
```

### Step 5: Assign b = Branch(...)

```python
b = Branch(self.b, next_block, BasicBlock(9), Branch.BOOL, rare=True)
```

### Step 6: Call self.assert_emit()

```python
self.assert_emit(b, 'if (likely(!cpy_r_b)) goto CPyL9;', next_block=next_block)
```

### Step 7: Assign next_block = BasicBlock(...)

```python
next_block = BasicBlock(8)
```

### Step 8: Assign b = Branch(...)

```python
b = Branch(self.b, next_block, BasicBlock(9), Branch.BOOL, rare=True)
```

### Step 9: Assign b.negated = True

```python
b.negated = True
```

### Step 10: Call self.assert_emit()

```python
self.assert_emit(b, 'if (likely(cpy_r_b)) goto CPyL9;', next_block=next_block)
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
self.assert_emit(Branch(self.b, BasicBlock(8), BasicBlock(9), Branch.BOOL, rare=True), 'if (unlikely(cpy_r_b)) {\n                                goto CPyL8;\n                            } else\n                                goto CPyL9;\n                         ')
next_block = BasicBlock(9)
self.assert_emit(Branch(self.b, BasicBlock(8), next_block, Branch.BOOL, rare=True), 'if (unlikely(cpy_r_b)) goto CPyL8;', next_block=next_block)
next_block = BasicBlock(8)
b = Branch(self.b, next_block, BasicBlock(9), Branch.BOOL, rare=True)
self.assert_emit(b, 'if (likely(!cpy_r_b)) goto CPyL9;', next_block=next_block)
next_block = BasicBlock(8)
b = Branch(self.b, next_block, BasicBlock(9), Branch.BOOL, rare=True)
b.negated = True
self.assert_emit(b, 'if (likely(cpy_r_b)) goto CPyL9;', next_block=next_block)
```

## Next Steps


---

*Source: test_emitfunc.py:252 | Complexity: Advanced | Last updated: 2026-06-02*