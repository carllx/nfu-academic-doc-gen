# How To: Lazy Import Impact On Sys Modules

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lazy import impact on sys modules

## Prerequisites

**Required Modules:**
- `sys`
- `types`
- `pytest`
- `networkx.lazy_imports`


## Step-by-Step Guide

### Step 1: Assign math = lazy._lazy_import(...)

```python
math = lazy._lazy_import('math')
```

**Verification:**
```python
assert isinstance(math, types.ModuleType)
```

### Step 2: Assign anything_not_real = lazy._lazy_import(...)

```python
anything_not_real = lazy._lazy_import('anything_not_real')
```

**Verification:**
```python
assert 'math' in sys.modules
```

### Step 3: Assign np_test = pytest.importorskip(...)

```python
np_test = pytest.importorskip('numpy')
```

**Verification:**
```python
assert type(anything_not_real) is lazy.DelayedImportErrorModule
```

### Step 4: Assign np = lazy._lazy_import(...)

```python
np = lazy._lazy_import('numpy')
```

**Verification:**
```python
assert 'anything_not_real' not in sys.modules
```

### Step 5: np.pi

```python
np.pi
```

**Verification:**
```python
assert isinstance(np, types.ModuleType)
```


## Complete Example

```python
# Workflow
math = lazy._lazy_import('math')
anything_not_real = lazy._lazy_import('anything_not_real')
assert isinstance(math, types.ModuleType)
assert 'math' in sys.modules
assert type(anything_not_real) is lazy.DelayedImportErrorModule
assert 'anything_not_real' not in sys.modules
np_test = pytest.importorskip('numpy')
np = lazy._lazy_import('numpy')
assert isinstance(np, types.ModuleType)
assert 'numpy' in sys.modules
np.pi
assert isinstance(np, types.ModuleType)
assert 'numpy' in sys.modules
```

## Next Steps


---

*Source: test_lazy_imports.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*