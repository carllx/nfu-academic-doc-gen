# How To: No Array Function Like

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, pytest, workflow, integration

## Overview

Workflow: test no array function like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `os`
- `pickle`
- `sys`
- `tempfile`
- `io`
- `unittest`
- `pytest`
- `numpy`
- `numpy._core.overrides`
- `numpy.testing`
- `numpy.testing.overrides`

**Setup Required:**
```python
# Fixtures: function, args, kwargs, ref
```

## Step-by-Step Guide

### Step 1: Assign MyNoArrayFunctionArray = self._create_MyNoArrayFunctionArray(...)

```python
MyNoArrayFunctionArray = self._create_MyNoArrayFunctionArray()
```

### Step 2: Call self.add_method()

```python
self.add_method('array', MyNoArrayFunctionArray)
```

### Step 3: Call self.add_method()

```python
self.add_method(function, MyNoArrayFunctionArray)
```

### Step 4: Assign np_func = getattr(...)

```python
np_func = getattr(np, function)
```

### Step 5: Assign like_args = tuple(...)

```python
like_args = tuple((a() if callable(a) else a for a in args))
```

### Step 6: Assign ref = MyNoArrayFunctionArray.array(...)

```python
ref = MyNoArrayFunctionArray.array()
```

### Step 7: Call np_func()

```python
np_func(*like_args, **kwargs, like=ref)
```


## Complete Example

```python
# Setup
# Fixtures: function, args, kwargs, ref

# Workflow
MyNoArrayFunctionArray = self._create_MyNoArrayFunctionArray()
self.add_method('array', MyNoArrayFunctionArray)
self.add_method(function, MyNoArrayFunctionArray)
np_func = getattr(np, function)
if ref == 'MyNoArrayFunctionArray':
    ref = MyNoArrayFunctionArray.array()
like_args = tuple((a() if callable(a) else a for a in args))
with assert_raises_regex(TypeError, 'The `like` argument must be an array-like that implements'):
    np_func(*like_args, **kwargs, like=ref)
```

## Next Steps


---

*Source: test_overrides.py:684 | Complexity: Intermediate | Last updated: 2026-06-02*