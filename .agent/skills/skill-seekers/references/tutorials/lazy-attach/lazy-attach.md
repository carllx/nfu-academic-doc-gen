# How To: Lazy Attach

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lazy attach

## Prerequisites

**Required Modules:**
- `sys`
- `types`
- `pytest`
- `networkx.lazy_imports`


## Step-by-Step Guide

### Step 1: Assign name = 'mymod'

```python
name = 'mymod'
```

**Verification:**
```python
assert locls.keys() == expected.keys()
```

### Step 2: Assign submods = value

```python
submods = ['mysubmodule', 'anothersubmodule']
```

**Verification:**
```python
assert locls[k] == v
```

### Step 3: Assign myall = value

```python
myall = {'not_real_submod': ['some_var_or_func']}
```

### Step 4: Assign locls = value

```python
locls = {'attach': lazy.attach, 'name': name, 'submods': submods, 'myall': myall}
```

### Step 5: Assign s = '__getattr__, __lazy_dir__, __all__ = attach(name, submods, myall)'

```python
s = '__getattr__, __lazy_dir__, __all__ = attach(name, submods, myall)'
```

### Step 6: Call exec()

```python
exec(s, {}, locls)
```

### Step 7: Assign expected = value

```python
expected = {'attach': lazy.attach, 'name': name, 'submods': submods, 'myall': myall, '__getattr__': None, '__lazy_dir__': None, '__all__': None}
```

**Verification:**
```python
assert locls.keys() == expected.keys()
```


## Complete Example

```python
# Workflow
name = 'mymod'
submods = ['mysubmodule', 'anothersubmodule']
myall = {'not_real_submod': ['some_var_or_func']}
locls = {'attach': lazy.attach, 'name': name, 'submods': submods, 'myall': myall}
s = '__getattr__, __lazy_dir__, __all__ = attach(name, submods, myall)'
exec(s, {}, locls)
expected = {'attach': lazy.attach, 'name': name, 'submods': submods, 'myall': myall, '__getattr__': None, '__lazy_dir__': None, '__all__': None}
assert locls.keys() == expected.keys()
for k, v in expected.items():
    if v is not None:
        assert locls[k] == v
```

## Next Steps


---

*Source: test_lazy_imports.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*