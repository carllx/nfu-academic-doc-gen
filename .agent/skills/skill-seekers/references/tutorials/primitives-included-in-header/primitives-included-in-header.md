# How To: Primitives Included In Header

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test primitives included in header

## Prerequisites

**Required Modules:**
- `__future__`
- `glob`
- `os`
- `re`
- `unittest`
- `mypyc.primitives`


## Step-by-Step Guide

### Step 1: Assign base_dir = os.path.join(...)

```python
base_dir = os.path.join(os.path.dirname(__file__), '..', 'lib-rt')
```

**Verification:**
```python
assert re.search(f'\\b{name}\\b', header), f'"{name}" is used in mypyc.primitives but not declared in CPy.h'
```

### Step 2: Assign primitives_path = os.path.join(...)

```python
primitives_path = os.path.join(os.path.dirname(__file__), '..', 'primitives')
```

### Step 3: Assign header = f.read(...)

```python
header = f.read()
```

**Verification:**
```python
assert re.search(f'\\b{name}\\b', header), f'"{name}" is used in mypyc.primitives but not declared in CPy.h'
```

### Step 4: Assign content = f.read(...)

```python
content = f.read()
```

### Step 5: Call check_name()

```python
check_name(name)
```

### Step 6: Call check_name()

```python
check_name(op.c_function_name)
```


## Complete Example

```python
# Workflow
base_dir = os.path.join(os.path.dirname(__file__), '..', 'lib-rt')
with open(os.path.join(base_dir, 'CPy.h')) as f:
    header = f.read()
with open(os.path.join(base_dir, 'pythonsupport.h')) as f:
    header += f.read()

def check_name(name: str) -> None:
    if name.startswith('CPy'):
        assert re.search(f'\\b{name}\\b', header), f'"{name}" is used in mypyc.primitives but not declared in CPy.h'
for values in [registry.method_call_ops.values(), registry.binary_ops.values(), registry.unary_ops.values(), registry.function_ops.values()]:
    for ops in values:
        for op in ops:
            if op.c_function_name is not None:
                check_name(op.c_function_name)
primitives_path = os.path.join(os.path.dirname(__file__), '..', 'primitives')
for fnam in glob.glob(f'{primitives_path}/*.py'):
    with open(fnam) as f:
        content = f.read()
    for name in re.findall('c_function_name=["\\\'](CPy[A-Z_a-z0-9]+)', content):
        check_name(name)
```

## Next Steps


---

*Source: test_cheader.py:14 | Complexity: Advanced | Last updated: 2026-06-02*