# How To: Nxconfig

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nxconfig

## Prerequisites

**Required Modules:**
- `collections`
- `pickle`
- `pytest`
- `networkx`
- `networkx.utils.configs`


## Step-by-Step Guide

### Step 1: Assign prev = value

```python
prev = nx.config.backend_priority
```

**Verification:**
```python
assert isinstance(nx.config.backend_priority, BackendPriorities)
```

### Step 2: Assign nx.config.backend_priority.algos = 'nx_loopback'

```python
nx.config.backend_priority.algos = 'nx_loopback'
```

**Verification:**
```python
assert isinstance(nx.config.backend_priority.algos, list)
```

### Step 3: Assign nx.config.backend_priority.algos = value

```python
nx.config.backend_priority.algos = ['this_almost_certainly_is_not_a_backend']
```

**Verification:**
```python
assert isinstance(nx.config.backends, Config)
```

### Step 4: Assign nx.config.backends = value

```python
nx.config.backends = {}
```

**Verification:**
```python
assert isinstance(nx.config.backend_priority, BackendPriorities)
```

### Step 5: Assign nx.config.backends = Config(...)

```python
nx.config.backends = Config(plausible_backend_name={})
```

**Verification:**
```python
assert nx.config.backend_priority.algos == ['networkx']
```

### Step 6: Assign nx.config.backends = Config(...)

```python
nx.config.backends = Config(this_almost_certainly_is_not_a_backend=Config())
```

### Step 7: Assign nx.config.cache_converted_graphs = 'bad value'

```python
nx.config.cache_converted_graphs = 'bad value'
```

### Step 8: Assign nx.config.warnings_to_ignore = 7

```python
nx.config.warnings_to_ignore = 7
```

### Step 9: Assign nx.config.warnings_to_ignore = value

```python
nx.config.warnings_to_ignore = {'bad value'}
```

### Step 10: Assign nx.config.backend_priority = value

```python
nx.config.backend_priority = ['networkx']
```

**Verification:**
```python
assert isinstance(nx.config.backend_priority, BackendPriorities)
```

### Step 11: Assign nx.config.backend_priority = prev

```python
nx.config.backend_priority = prev
```


## Complete Example

```python
# Workflow
assert isinstance(nx.config.backend_priority, BackendPriorities)
assert isinstance(nx.config.backend_priority.algos, list)
assert isinstance(nx.config.backends, Config)
with pytest.raises(TypeError, match='must be a list of backend names'):
    nx.config.backend_priority.algos = 'nx_loopback'
with pytest.raises(ValueError, match='Unknown backend when setting'):
    nx.config.backend_priority.algos = ['this_almost_certainly_is_not_a_backend']
with pytest.raises(TypeError, match='must be a Config of backend configs'):
    nx.config.backends = {}
with pytest.raises(TypeError, match='must be a Config of backend configs'):
    nx.config.backends = Config(plausible_backend_name={})
with pytest.raises(ValueError, match='Unknown backend when setting'):
    nx.config.backends = Config(this_almost_certainly_is_not_a_backend=Config())
with pytest.raises(TypeError, match='must be True or False'):
    nx.config.cache_converted_graphs = 'bad value'
with pytest.raises(TypeError, match='must be a set of '):
    nx.config.warnings_to_ignore = 7
with pytest.raises(ValueError, match='Unknown warning '):
    nx.config.warnings_to_ignore = {'bad value'}
prev = nx.config.backend_priority
try:
    nx.config.backend_priority = ['networkx']
    assert isinstance(nx.config.backend_priority, BackendPriorities)
    assert nx.config.backend_priority.algos == ['networkx']
finally:
    nx.config.backend_priority = prev
```

## Next Steps


---

*Source: test_config.py:119 | Complexity: Advanced | Last updated: 2026-06-02*