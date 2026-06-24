# How To: Distutils Parse Env Order

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test distutils parse env order

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `pytest`
- `tempfile`
- `subprocess`
- `importlib.metadata`
- `distutils.errors`
- `numpy.testing`
- `numpy.distutils`
- `numpy.distutils.system_info`
- `numpy.distutils.system_info`
- `numpy.distutils.system_info`
- `numpy.distutils`
- `numpy.distutils.system_info`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign env = 'NPY_TESTS_DISTUTILS_PARSE_ENV_ORDER'

```python
env = 'NPY_TESTS_DISTUTILS_PARSE_ENV_ORDER'
```

**Verification:**
```python
assert len(order) == 3
```

### Step 2: Assign base_order = list(...)

```python
base_order = list('abcdef')
```

**Verification:**
```python
assert order == list('bef')
```

### Step 3: Call monkeypatch.setenv()

```python
monkeypatch.setenv(env, 'b,i,e,f')
```

**Verification:**
```python
assert len(unknown) == 1
```

### Step 4: Assign unknown = _parse_env_order(...)

```python
order, unknown = _parse_env_order(base_order, env)
```

**Verification:**
```python
assert len(order) == 0
```

### Step 5: Call monkeypatch.setenv()

```python
monkeypatch.setenv(env, '')
```

**Verification:**
```python
assert len(unknown) == 0
```

### Step 6: Assign unknown = _parse_env_order(...)

```python
order, unknown = _parse_env_order(base_order, env)
```

**Verification:**
```python
assert len(order) == 4
```

### Step 7: Call monkeypatch.setenv()

```python
monkeypatch.setenv(env, f'{prefix}b,i,e')
```

**Verification:**
```python
assert order == list('acdf')
```

### Step 8: Assign unknown = _parse_env_order(...)

```python
order, unknown = _parse_env_order(base_order, env)
```

**Verification:**
```python
assert len(unknown) == 1
```

### Step 9: Call monkeypatch.setenv()

```python
monkeypatch.setenv(env, 'b,^e,i')
```

### Step 10: Call _parse_env_order()

```python
_parse_env_order(base_order, env)
```

### Step 11: Call monkeypatch.setenv()

```python
monkeypatch.setenv(env, '!b,^e,i')
```

### Step 12: Call _parse_env_order()

```python
_parse_env_order(base_order, env)
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
from numpy.distutils.system_info import _parse_env_order
env = 'NPY_TESTS_DISTUTILS_PARSE_ENV_ORDER'
base_order = list('abcdef')
monkeypatch.setenv(env, 'b,i,e,f')
order, unknown = _parse_env_order(base_order, env)
assert len(order) == 3
assert order == list('bef')
assert len(unknown) == 1
monkeypatch.setenv(env, '')
order, unknown = _parse_env_order(base_order, env)
assert len(order) == 0
assert len(unknown) == 0
for prefix in '^!':
    monkeypatch.setenv(env, f'{prefix}b,i,e')
    order, unknown = _parse_env_order(base_order, env)
    assert len(order) == 4
    assert order == list('acdf')
    assert len(unknown) == 1
with pytest.raises(ValueError):
    monkeypatch.setenv(env, 'b,^e,i')
    _parse_env_order(base_order, env)
with pytest.raises(ValueError):
    monkeypatch.setenv(env, '!b,^e,i')
    _parse_env_order(base_order, env)
```

## Next Steps


---

*Source: test_system_info.py:303 | Complexity: Advanced | Last updated: 2026-06-02*