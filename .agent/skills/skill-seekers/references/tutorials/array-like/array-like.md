# How To: Array Like

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, pytest, workflow, integration

## Overview

Workflow: test array like

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
# Fixtures: function, args, kwargs, numpy_ref
```

## Step-by-Step Guide

### Step 1: Assign MyArray = self._create_MyArray(...)

```python
MyArray = self._create_MyArray()
```

**Verification:**
```python
assert type(array_like) is np.ndarray
```

### Step 2: Call self.add_method()

```python
self.add_method('array', MyArray)
```

**Verification:**
```python
assert_equal(array_like, np_arr)
```

### Step 3: Call self.add_method()

```python
self.add_method(function, MyArray)
```

**Verification:**
```python
assert type(array_like) is MyArray
```

### Step 4: Assign np_func = getattr(...)

```python
np_func = getattr(np, function)
```

**Verification:**
```python
assert array_like.function is my_func
```

### Step 5: Assign my_func = getattr(...)

```python
my_func = getattr(MyArray, function)
```

### Step 6: Assign like_args = tuple(...)

```python
like_args = tuple((a() if callable(a) else a for a in args))
```

### Step 7: Assign array_like = np_func(...)

```python
array_like = np_func(*like_args, **kwargs, like=ref)
```

### Step 8: Assign ref = np.array(...)

```python
ref = np.array(1)
```

### Step 9: Assign ref = MyArray.array(...)

```python
ref = MyArray.array()
```

**Verification:**
```python
assert type(array_like) is np.ndarray
```

### Step 10: Assign np_args = tuple(...)

```python
np_args = tuple((a() if callable(a) else a for a in args))
```

### Step 11: Assign np_arr = np_func(...)

```python
np_arr = np_func(*np_args, **kwargs)
```

### Step 12: Call assert_equal()

```python
assert_equal(array_like, np_arr)
```

**Verification:**
```python
assert type(array_like) is MyArray
```

### Step 13: Call np_arr.fill()

```python
np_arr.fill(1)
```

### Step 14: Call array_like.fill()

```python
array_like.fill(1)
```


## Complete Example

```python
# Setup
# Fixtures: function, args, kwargs, numpy_ref

# Workflow
MyArray = self._create_MyArray()
self.add_method('array', MyArray)
self.add_method(function, MyArray)
np_func = getattr(np, function)
my_func = getattr(MyArray, function)
if numpy_ref is True:
    ref = np.array(1)
else:
    ref = MyArray.array()
like_args = tuple((a() if callable(a) else a for a in args))
array_like = np_func(*like_args, **kwargs, like=ref)
if numpy_ref is True:
    assert type(array_like) is np.ndarray
    np_args = tuple((a() if callable(a) else a for a in args))
    np_arr = np_func(*np_args, **kwargs)
    if function == 'empty':
        np_arr.fill(1)
        array_like.fill(1)
    assert_equal(array_like, np_arr)
else:
    assert type(array_like) is MyArray
    assert array_like.function is my_func
```

## Next Steps


---

*Source: test_overrides.py:651 | Complexity: Advanced | Last updated: 2026-06-02*