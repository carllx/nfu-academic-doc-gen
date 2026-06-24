# How To: Bad Version

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test bad version

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
assert result is module
```

### Step 2: Assign module = types.ModuleType(...)

```python
module = types.ModuleType(name)
```

**Verification:**
```python
assert result is None
```

### Step 3: Assign module.__version__ = '0.9.0'

```python
module.__version__ = '0.9.0'
```

**Verification:**
```python
assert result is module
```

### Step 4: Assign unknown = module

```python
sys.modules[name] = module
```

**Verification:**
```python
assert result is None
```

### Step 5: Call monkeypatch.setitem()

```python
monkeypatch.setitem(VERSIONS, name, '1.0.0')
```

**Verification:**
```python
assert result is None
```

### Step 6: Assign match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"

```python
match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"
```

### Step 7: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule', min_version='0.8')
```

**Verification:**
```python
assert result is module
```

### Step 8: Assign module.__version__ = '1.0.0'

```python
module.__version__ = '1.0.0'
```

### Step 9: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule')
```

**Verification:**
```python
assert result is module
```

### Step 10: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule', errors='ignore', min_version='1.1.0')
```

**Verification:**
```python
assert result is None
```

### Step 11: Call import_optional_dependency()

```python
import_optional_dependency('fakemodule')
```

### Step 12: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule', errors='warn')
```

### Step 13: Call import_optional_dependency()

```python
import_optional_dependency('fakemodule', min_version='1.1.0')
```

### Step 14: Assign result = import_optional_dependency(...)

```python
result = import_optional_dependency('fakemodule', errors='warn', min_version='1.1.0')
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
monkeypatch.setitem(VERSIONS, name, '1.0.0')
match = "Pandas requires .*1.0.0.* of .fakemodule.*'0.9.0'"
with pytest.raises(ImportError, match=match):
    import_optional_dependency('fakemodule')
result = import_optional_dependency('fakemodule', min_version='0.8')
assert result is module
with tm.assert_produces_warning(UserWarning):
    result = import_optional_dependency('fakemodule', errors='warn')
assert result is None
module.__version__ = '1.0.0'
result = import_optional_dependency('fakemodule')
assert result is module
with pytest.raises(ImportError, match="Pandas requires version '1.1.0'"):
    import_optional_dependency('fakemodule', min_version='1.1.0')
with tm.assert_produces_warning(UserWarning):
    result = import_optional_dependency('fakemodule', errors='warn', min_version='1.1.0')
assert result is None
result = import_optional_dependency('fakemodule', errors='ignore', min_version='1.1.0')
assert result is None
```

## Next Steps


---

*Source: test_optional_dependency.py:30 | Complexity: Advanced | Last updated: 2026-06-02*