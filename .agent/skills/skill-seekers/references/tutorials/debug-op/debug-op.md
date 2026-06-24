# How To: Debug Op

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test debug op

## Prerequisites

**Required Modules:**
- `__future__`
- `unittest`
- `mypyc.ir.ops`
- `mypyc.ir.pprint`
- `mypyc.irbuild.ll_builder`
- `mypyc.options`


## Step-by-Step Guide

### Step 1: Assign block = BasicBlock(...)

```python
block = BasicBlock()
```

**Verification:**
```python
assert code[:-1] == ['L0:', "    r0 = 'foo'", '    CPyDebug_PrintObject(r0)']
```

### Step 2: Assign builder = LowLevelIRBuilder(...)

```python
builder = LowLevelIRBuilder(errors=None, options=CompilerOptions())
```

### Step 3: Call builder.activate_block()

```python
builder.activate_block(block)
```

### Step 4: Call builder.debug_print()

```python
builder.debug_print('foo')
```

### Step 5: Assign names = generate_names_for_ir(...)

```python
names = generate_names_for_ir([], [block])
```

### Step 6: Assign code = format_blocks(...)

```python
code = format_blocks([block], names, {})
```

**Verification:**
```python
assert code[:-1] == ['L0:', "    r0 = 'foo'", '    CPyDebug_PrintObject(r0)']
```


## Complete Example

```python
# Workflow
block = BasicBlock()
builder = LowLevelIRBuilder(errors=None, options=CompilerOptions())
builder.activate_block(block)
builder.debug_print('foo')
names = generate_names_for_ir([], [block])
code = format_blocks([block], names, {})
assert code[:-1] == ['L0:', "    r0 = 'foo'", '    CPyDebug_PrintObject(r0)']
```

## Next Steps


---

*Source: test_misc.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*