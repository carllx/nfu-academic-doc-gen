# How To: Empty Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(['a', 'b', 'c'], ordered=True)
```

**Verification:**
```python
assert isinstance(result, Categorical)
```

### Step 2: Assign dtype = value

```python
dtype = ci.dtype
```

**Verification:**
```python
assert result.shape == shape
```

### Step 3: Assign shape = value

```python
shape = (4,)
```

**Verification:**
```python
assert result._ndarray.dtype == np.int8
```

### Step 4: Assign result = Categorical._empty(...)

```python
result = Categorical._empty(shape, dtype=dtype)
```

**Verification:**
```python
assert isinstance(result, Categorical)
```

### Step 5: Assign result = Categorical._empty(...)

```python
result = Categorical._empty((4096,), dtype=dtype)
```

**Verification:**
```python
assert result.shape == (4096,)
```

### Step 6: Call repr()

```python
repr(result)
```

**Verification:**
```python
assert result._ndarray.dtype == np.int8
```

### Step 7: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list(range(512)) * 4, ordered=False)
```

**Verification:**
```python
assert isinstance(result, Categorical)
```

### Step 8: Assign dtype = value

```python
dtype = ci.dtype
```

**Verification:**
```python
assert result.shape == shape
```

### Step 9: Assign result = Categorical._empty(...)

```python
result = Categorical._empty(shape, dtype=dtype)
```

**Verification:**
```python
assert result._ndarray.dtype == np.int16
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(['a', 'b', 'c'], ordered=True)
dtype = ci.dtype
shape = (4,)
result = Categorical._empty(shape, dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == shape
assert result._ndarray.dtype == np.int8
result = Categorical._empty((4096,), dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == (4096,)
assert result._ndarray.dtype == np.int8
repr(result)
ci = CategoricalIndex(list(range(512)) * 4, ordered=False)
dtype = ci.dtype
result = Categorical._empty(shape, dtype=dtype)
assert isinstance(result, Categorical)
assert result.shape == shape
assert result._ndarray.dtype == np.int16
```

## Next Steps


---

*Source: test_ndarray_backed.py:19 | Complexity: Advanced | Last updated: 2026-06-02*