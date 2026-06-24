# How To: Func Dir

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test func dir

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `gc`
- `logging`
- `os`
- `os.path`
- `pickle`
- `shutil`
- `sys`
- `textwrap`
- `time`
- `pathlib`
- `pytest`
- `joblib._store_backends`
- `joblib.hashing`
- `joblib.memory`
- `joblib.parallel`
- `joblib.test.common`
- `joblib.testing`
- `functools`
- `tmp_joblib_`
- `tmp_joblib_`
- `datetime`
- `time`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=0)
```

**Verification:**
```python
assert location == path
```

### Step 2: Assign path = __name__.split(...)

```python
path = __name__.split('.')
```

**Verification:**
```python
assert os.path.exists(path)
```

### Step 3: Call path.append()

```python
path.append('f')
```

**Verification:**
```python
assert memory.location == os.path.dirname(g.store_backend.location)
```

### Step 4: Assign path = value

```python
path = tmpdir.join('joblib', *path).strpath
```

**Verification:**
```python
assert not g._check_previous_func_code()
```

### Step 5: Assign g = memory.cache(...)

```python
g = memory.cache(f)
```

**Verification:**
```python
assert os.path.exists(os.path.join(path, 'func_code.py'))
```

### Step 6: Assign func_id = _build_func_identifier(...)

```python
func_id = _build_func_identifier(f)
```

**Verification:**
```python
assert g._check_previous_func_code()
```

### Step 7: Assign location = os.path.join(...)

```python
location = os.path.join(g.store_backend.location, func_id)
```

**Verification:**
```python
assert os.path.exists(output_dir)
```

### Step 8: Call _FUNCTION_HASHES.clear()

```python
_FUNCTION_HASHES.clear()
```

**Verification:**
```python
assert a == g(1)
```

### Step 9: Assign args_id = g._get_args_id(...)

```python
args_id = g._get_args_id(1)
```

### Step 10: Assign output_dir = os.path.join(...)

```python
output_dir = os.path.join(g.store_backend.location, g.func_id, args_id)
```

### Step 11: Assign a = g(...)

```python
a = g(1)
```

**Verification:**
```python
assert os.path.exists(output_dir)
```

### Step 12: Call os.remove()

```python
os.remove(os.path.join(output_dir, 'output.pkl'))
```

**Verification:**
```python
assert a == g(1)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
memory = Memory(location=tmpdir.strpath, verbose=0)
path = __name__.split('.')
path.append('f')
path = tmpdir.join('joblib', *path).strpath
g = memory.cache(f)
func_id = _build_func_identifier(f)
location = os.path.join(g.store_backend.location, func_id)
assert location == path
assert os.path.exists(path)
assert memory.location == os.path.dirname(g.store_backend.location)
_FUNCTION_HASHES.clear()
assert not g._check_previous_func_code()
assert os.path.exists(os.path.join(path, 'func_code.py'))
assert g._check_previous_func_code()
args_id = g._get_args_id(1)
output_dir = os.path.join(g.store_backend.location, g.func_id, args_id)
a = g(1)
assert os.path.exists(output_dir)
os.remove(os.path.join(output_dir, 'output.pkl'))
assert a == g(1)
```

## Next Steps


---

*Source: test_memory.py:560 | Complexity: Advanced | Last updated: 2026-06-02*