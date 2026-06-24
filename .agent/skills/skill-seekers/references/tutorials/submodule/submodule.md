# How To: Submodule

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test submodule

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sys`
- `types`
- `pytest`
- `pandas.compat._optional`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign name = 'fakemodule'

```python
name = 'fakemodule'
```

**Verification:**
```python
assert result is None
```

### Step 2: Assign module = types.ModuleType(...)

```python
module = types.ModuleType(name)
```

**Verification:**
```python
assert result is submodule
```

### Step 3: Assign module.__version__ = '0.9.0'

```python
module.__version__ = '0.9.0'
```

### Step 4: Assign unknown = module

```python
sys.modules[name] = module
```

### Step 5: Assign sub_name = 'submodule'

```python
sub_name = 'submodule'
```

### Step 6: Assign submodule = types.ModuleType(...)

```python
submodule = types.ModuleType(sub_name)
```

### Step 7: Call setattr()

```python
setattr(module, sub_name, submodule)
```

### Step 8: Assign unknown = submodule

```python
sys.modules[f'{name}.{sub_name}'] = submodule
```

### Step 9: Call monkeypatch.setitem()

```python
monkeypatch.setitem(VERSIONS, name, '1.0.0')
```

### Step 10: Assign match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"

```python
match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"
```

**Verification:**
```python
assert result is None
```

### Step 11: Assign module.__version__ = '1.0.0'

```python
module.__version__ = '1.0.0'
```

### Step 12: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule.submodule')
```

**Verification:**
```python
assert result is submodule
```

### Step 13: Call import_optional_dependency()

```python
import_optional_dependency('fakemodule.submodule')
```

### Step 14: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule.submodule', errors='warn')
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
name = 'fakemodule'
module = types.ModuleType(name)
module.__version__ = '0.9.0'
sys.modules[name] = module
sub_name = 'submodule'
submodule = types.ModuleType(sub_name)
setattr(module, sub_name, submodule)
sys.modules[f'{name}.{sub_name}'] = submodule
monkeypatch.setitem(VERSIONS, name, '1.0.0')
match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"
with pytest.raises(ImportError, match=match):
    import_optional_dependency('fakemodule.submodule')
with tm.assert_produces_warning(UserWarning):
    result = import_optional_dependency('fakemodule.submodule', errors='warn')
assert result is None
module.__version__ = '1.0.0'
result = import_optional_dependency('fakemodule.submodule')
assert result is submodule
```

## Next Steps


---

*Source: test_optional_dependency.py:68 | Complexity: Advanced | Last updated: 2026-06-02*