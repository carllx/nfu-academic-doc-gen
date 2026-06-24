# How To: Function Like

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test function like

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

### Step 1: Assign m = MyClass(...)

```python
m = MyClass()
```

**Verification:**
```python
assert type(np.mean) is np._core._multiarray_umath._ArrayFunctionDispatcher
```

### Step 2: Assign bound = np.mean.__get__(...)

```python
bound = np.mean.__get__(m, MyClass)
```

**Verification:**
```python
assert m.func1([10]) == 10
```

### Step 3: Assign bound = np.mean.__get__(...)

```python
bound = np.mean.__get__(None, MyClass)
```

**Verification:**
```python
assert m.func2() == 1
```

### Step 4: Assign bound = np.mean.__get__(...)

```python
bound = np.mean.__get__(MyClass)
```

**Verification:**
```python
assert bound() == 1
```

### Step 5: Assign func1 = staticmethod(...)

```python
func1 = staticmethod(np.mean)
```

**Verification:**
```python
assert bound([10]) == 10
```

### Step 6: Assign func2 = value

```python
func2 = np.mean
```

### Step 7: Assign func3 = classmethod(...)

```python
func3 = classmethod(np.mean)
```

### Step 8: Call m.func3()

```python
m.func3()
```

### Step 9: Call bound()

```python
bound()
```


## Complete Example

```python
# Workflow
assert type(np.mean) is np._core._multiarray_umath._ArrayFunctionDispatcher

class MyClass:

    def __array__(self, dtype=None, copy=None):
        return np.arange(3)
    func1 = staticmethod(np.mean)
    func2 = np.mean
    func3 = classmethod(np.mean)
m = MyClass()
assert m.func1([10]) == 10
assert m.func2() == 1
with pytest.raises(TypeError, match='unsupported operand type'):
    m.func3()
bound = np.mean.__get__(m, MyClass)
assert bound() == 1
bound = np.mean.__get__(None, MyClass)
assert bound([10]) == 10
bound = np.mean.__get__(MyClass)
with pytest.raises(TypeError, match='unsupported operand type'):
    bound()
```

## Next Steps


---

*Source: test_overrides.py:771 | Complexity: Advanced | Last updated: 2026-06-02*