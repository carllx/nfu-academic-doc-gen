# How To:   Module   Attribute

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test   module   attribute

## Prerequisites

**Required Modules:**
- `functools`
- `importlib`
- `inspect`
- `pkgutil`
- `subprocess`
- `sys`
- `sysconfig`
- `types`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `ctypes`
- `numpy.core`
- `collections.abc`
- `typing`
- `numpy._core._multiarray_umath`


## Step-by-Step Guide

### Step 1: Assign modules_queue = value

```python
modules_queue = [np]
```

**Verification:**
```python
assert len(incorrect_entries) == 0, incorrect_entries
```

### Step 2: Assign visited_modules = value

```python
visited_modules = {np}
```

### Step 3: Assign visited_functions = set(...)

```python
visited_functions = set()
```

### Step 4: Assign incorrect_entries = value

```python
incorrect_entries = []
```

### Step 5: Assign module = modules_queue.pop(...)

```python
module = modules_queue.pop()
```

**Verification:**
```python
assert len(incorrect_entries) == 0, incorrect_entries
```

### Step 6: Assign member = getattr(...)

```python
member = getattr(module, member_name)
```

### Step 7: Call modules_queue.append()

```python
modules_queue.append(member)
```

### Step 8: Call visited_modules.add()

```python
visited_modules.add(member)
```

### Step 9: Call incorrect_entries.append()

```python
incorrect_entries.append({'Func': member.__name__, 'actual': member.__module__, 'expected': module.__name__})
```

### Step 10: Call visited_functions.add()

```python
visited_functions.add(member)
```


## Complete Example

```python
# Workflow
modules_queue = [np]
visited_modules = {np}
visited_functions = set()
incorrect_entries = []
while len(modules_queue) > 0:
    module = modules_queue.pop()
    for member_name in dir(module):
        member = getattr(module, member_name)
        if inspect.ismodule(member) and 'numpy' in member.__name__ and (not member_name.startswith('_')) and ('numpy._core' not in member.__name__) and (member_name not in ['char', 'core', 'f2py', 'ma', 'lapack_lite', 'mrecords', 'testing', 'tests', 'polynomial', 'typing', 'mtrand', 'bit_generator']) and (member not in visited_modules):
            modules_queue.append(member)
            visited_modules.add(member)
        elif not inspect.ismodule(member) and hasattr(member, '__name__') and (not member.__name__.startswith('_')) and (member.__module__ != module.__name__) and (member not in visited_functions):
            if member.__name__ in ('add', 'equal', 'not_equal', 'greater', 'greater_equal', 'less', 'less_equal') and module.__name__ == 'numpy.strings':
                continue
            if member.__name__ == 'recarray' and module.__name__ == 'numpy' or (member.__name__ == 'record' and module.__name__ == 'numpy.rec'):
                continue
            if member.__name__ in ('c_long', 'c_longlong') and module.__name__ == 'numpy.ctypeslib':
                continue
            if member.__name__ in ('BitGenerator', 'Generator', 'MT19937', 'PCG64', 'PCG64DXSM', 'Philox', 'RandomState', 'SFC64', 'SeedSequence'):
                continue
            incorrect_entries.append({'Func': member.__name__, 'actual': member.__module__, 'expected': module.__name__})
            visited_functions.add(member)
if incorrect_entries:
    assert len(incorrect_entries) == 0, incorrect_entries
```

## Next Steps


---

*Source: test_public_api.py:673 | Complexity: Advanced | Last updated: 2026-06-02*