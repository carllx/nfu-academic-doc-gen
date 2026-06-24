# How To: Sum On Mock Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test sum on mock array

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign proxy = ArrayProxy(...)

```python
proxy = ArrayProxy(mock.Mock(spec=ArrayProxy))
```

**Verification:**
```python
assert_equal(result, 1)
```

### Step 2: Assign proxy.value.__array_function__.return_value = 1

```python
proxy.value.__array_function__.return_value = 1
```

### Step 3: Assign result = np.sum(...)

```python
result = np.sum(proxy)
```

### Step 4: Call assert_equal()

```python
assert_equal(result, 1)
```

### Step 5: Call proxy.value.__array_function__.assert_called_once_with()

```python
proxy.value.__array_function__.assert_called_once_with(np.sum, (ArrayProxy,), (proxy,), {})
```

### Step 6: Call proxy.value.__array__.assert_not_called()

```python
proxy.value.__array__.assert_not_called()
```

### Step 7: Assign self.value = value

```python
self.value = value
```


## Complete Example

```python
# Workflow
class ArrayProxy:

    def __init__(self, value):
        self.value = value

    def __array_function__(self, *args, **kwargs):
        return self.value.__array_function__(*args, **kwargs)

    def __array__(self, *args, **kwargs):
        return self.value.__array__(*args, **kwargs)
proxy = ArrayProxy(mock.Mock(spec=ArrayProxy))
proxy.value.__array_function__.return_value = 1
result = np.sum(proxy)
assert_equal(result, 1)
proxy.value.__array_function__.assert_called_once_with(np.sum, (ArrayProxy,), (proxy,), {})
proxy.value.__array__.assert_not_called()
```

## Next Steps


---

*Source: test_overrides.py:515 | Complexity: Intermediate | Last updated: 2026-06-02*