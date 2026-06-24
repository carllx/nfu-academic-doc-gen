# How To: C String

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test c string

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

### Step 1: Assign s = Register(...)

```python
s = Register(cstring_rprimitive, 's')
```

### Step 2: Call self.assert_emit()

```python
self.assert_emit(Assign(s, CString(b'foo')), 'cpy_r_s = "foo";')
```

### Step 3: Call self.assert_emit()

```python
self.assert_emit(Assign(s, CString(b'foo "o')), 'cpy_r_s = "foo \\"o";')
```

### Step 4: Call self.assert_emit()

```python
self.assert_emit(Assign(s, CString(b'\x00')), 'cpy_r_s = "\\x00";')
```

### Step 5: Call self.assert_emit()

```python
self.assert_emit(Assign(s, CString(b'\\')), 'cpy_r_s = "\\\\";')
```

### Step 6: Assign b = bytes(...)

```python
b = bytes([i])
```

### Step 7: Call self.assert_emit()

```python
self.assert_emit(Assign(s, CString(b)), f'cpy_r_s = "{target}";')
```

### Step 8: Assign target = '\\n'

```python
target = '\\n'
```

### Step 9: Assign target = '\\r'

```python
target = '\\r'
```

### Step 10: Assign target = '\\t'

```python
target = '\\t'
```

### Step 11: Assign target = '\\"'

```python
target = '\\"'
```

### Step 12: Assign target = '\\\\'

```python
target = '\\\\'
```

### Step 13: Assign target = value

```python
target = '\\x%.2x' % i
```

### Step 14: Assign target = b.decode(...)

```python
target = b.decode('ascii')
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
s = Register(cstring_rprimitive, 's')
self.assert_emit(Assign(s, CString(b'foo')), 'cpy_r_s = "foo";')
self.assert_emit(Assign(s, CString(b'foo "o')), 'cpy_r_s = "foo \\"o";')
self.assert_emit(Assign(s, CString(b'\x00')), 'cpy_r_s = "\\x00";')
self.assert_emit(Assign(s, CString(b'\\')), 'cpy_r_s = "\\\\";')
for i in range(256):
    b = bytes([i])
    if b == b'\n':
        target = '\\n'
    elif b == b'\r':
        target = '\\r'
    elif b == b'\t':
        target = '\\t'
    elif b == b'"':
        target = '\\"'
    elif b == b'\\':
        target = '\\\\'
    elif i < 32 or i >= 127:
        target = '\\x%.2x' % i
    else:
        target = b.decode('ascii')
    self.assert_emit(Assign(s, CString(b)), f'cpy_r_s = "{target}";')
```

## Next Steps


---

*Source: test_emitfunc.py:859 | Complexity: Advanced | Last updated: 2026-06-02*