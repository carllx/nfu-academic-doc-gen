# How To: Persistence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test persistence

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
assert os.path.exists(output_dir)
```

### Step 2: Assign g = memory.cache(...)

```python
g = memory.cache(f)
```

**Verification:**
```python
assert output == h.store_backend.load_item([h.func_id, args_id])
```

### Step 3: Assign output = g(...)

```python
output = g(1)
```

**Verification:**
```python
assert memory.store_backend.location == memory2.store_backend.location
```

### Step 4: Assign h = pickle.loads(...)

```python
h = pickle.loads(pickle.dumps(g))
```

### Step 5: Assign args_id = h._get_args_id(...)

```python
args_id = h._get_args_id(1)
```

### Step 6: Assign output_dir = os.path.join(...)

```python
output_dir = os.path.join(h.store_backend.location, h.func_id, args_id)
```

**Verification:**
```python
assert os.path.exists(output_dir)
```

### Step 7: Assign memory2 = pickle.loads(...)

```python
memory2 = pickle.loads(pickle.dumps(memory))
```

**Verification:**
```python
assert memory.store_backend.location == memory2.store_backend.location
```

### Step 8: Assign memory = Memory(...)

```python
memory = Memory(location=None, verbose=0)
```

### Step 9: Call pickle.loads()

```python
pickle.loads(pickle.dumps(memory))
```

### Step 10: Assign g = memory.cache(...)

```python
g = memory.cache(f)
```

### Step 11: Assign gp = pickle.loads(...)

```python
gp = pickle.loads(pickle.dumps(g))
```

### Step 12: Call gp()

```python
gp(1)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
memory = Memory(location=tmpdir.strpath, verbose=0)
g = memory.cache(f)
output = g(1)
h = pickle.loads(pickle.dumps(g))
args_id = h._get_args_id(1)
output_dir = os.path.join(h.store_backend.location, h.func_id, args_id)
assert os.path.exists(output_dir)
assert output == h.store_backend.load_item([h.func_id, args_id])
memory2 = pickle.loads(pickle.dumps(memory))
assert memory.store_backend.location == memory2.store_backend.location
memory = Memory(location=None, verbose=0)
pickle.loads(pickle.dumps(memory))
g = memory.cache(f)
gp = pickle.loads(pickle.dumps(g))
gp(1)
```

## Next Steps


---

*Source: test_memory.py:592 | Complexity: Advanced | Last updated: 2026-06-02*