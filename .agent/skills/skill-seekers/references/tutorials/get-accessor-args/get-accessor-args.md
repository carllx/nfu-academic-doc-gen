# How To: Get Accessor Args

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get accessor args

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting._matplotlib.style`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `pandas.plotting._matplotlib.style`
- `matplotlib.text`
- `matplotlib.text`
- `matplotlib.text`


## Step-by-Step Guide

### Step 1: Assign func = value

```python
func = plotting._core.PlotAccessor._get_call_args
```

**Verification:**
```python
assert x == 'x'
```

### Step 2: Assign msg = 'Called plot accessor for type list, expected Series or DataFrame'

```python
msg = 'Called plot accessor for type list, expected Series or DataFrame'
```

**Verification:**
```python
assert y == 'y'
```

### Step 3: Assign msg = 'should not be called with positional arguments'

```python
msg = 'should not be called with positional arguments'
```

**Verification:**
```python
assert kind == 'bar'
```

### Step 4: Assign unknown = func(...)

```python
x, y, kind, kwargs = func(backend_name='', data=DataFrame(), args=['x'], kwargs={'y': 'y', 'kind': 'bar', 'grid': False})
```

**Verification:**
```python
assert kwargs == {'grid': False}
```

### Step 5: Assign unknown = func(...)

```python
x, y, kind, kwargs = func(backend_name='pandas.plotting._matplotlib', data=Series(dtype=object), args=[], kwargs={})
```

**Verification:**
```python
assert x is None
```

### Step 6: Call func()

```python
func(backend_name='', data=[], args=[], kwargs={})
```

**Verification:**
```python
assert y is None
```

### Step 7: Call func()

```python
func(backend_name='', data=Series(dtype=object), args=['line', None], kwargs={})
```

**Verification:**
```python
assert kind == 'line'
```


## Complete Example

```python
# Workflow
func = plotting._core.PlotAccessor._get_call_args
msg = 'Called plot accessor for type list, expected Series or DataFrame'
with pytest.raises(TypeError, match=msg):
    func(backend_name='', data=[], args=[], kwargs={})
msg = 'should not be called with positional arguments'
with pytest.raises(TypeError, match=msg):
    func(backend_name='', data=Series(dtype=object), args=['line', None], kwargs={})
x, y, kind, kwargs = func(backend_name='', data=DataFrame(), args=['x'], kwargs={'y': 'y', 'kind': 'bar', 'grid': False})
assert x == 'x'
assert y == 'y'
assert kind == 'bar'
assert kwargs == {'grid': False}
x, y, kind, kwargs = func(backend_name='pandas.plotting._matplotlib', data=Series(dtype=object), args=[], kwargs={})
assert x is None
assert y is None
assert kind == 'line'
assert len(kwargs) == 24
```

## Next Steps


---

*Source: test_misc.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*