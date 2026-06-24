# How To: Pprint

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test pprint

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

### Step 1: Assign block_1 = self.basic_block(...)

```python
block_1 = self.basic_block([Return(value=NONE_VALUE)])
```

**Verification:**
```python
assert formatted == ['def func_1():', 'L0:', '    goto L1', '  ERR: Invalid control operation target: 1']
```

### Step 2: Assign goto = Goto(...)

```python
goto = Goto(label=block_1)
```

### Step 3: Assign block_2 = self.basic_block(...)

```python
block_2 = self.basic_block([goto])
```

### Step 4: Assign fn = FuncIR(...)

```python
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[], blocks=[block_2])
```

### Step 5: Assign errors = value

```python
errors = [(goto, 'Invalid control operation target: 1')]
```

### Step 6: Assign formatted = format_func(...)

```python
formatted = format_func(fn, errors)
```

**Verification:**
```python
assert formatted == ['def func_1():', 'L0:', '    goto L1', '  ERR: Invalid control operation target: 1']
```


## Complete Example

```python
# Workflow
block_1 = self.basic_block([Return(value=NONE_VALUE)])
goto = Goto(label=block_1)
block_2 = self.basic_block([goto])
fn = FuncIR(decl=self.func_decl(name='func_1'), arg_regs=[], blocks=[block_2])
errors = [(goto, 'Invalid control operation target: 1')]
formatted = format_func(fn, errors)
assert formatted == ['def func_1():', 'L0:', '    goto L1', '  ERR: Invalid control operation target: 1']
```

## Next Steps


---

*Source: test_ircheck.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*