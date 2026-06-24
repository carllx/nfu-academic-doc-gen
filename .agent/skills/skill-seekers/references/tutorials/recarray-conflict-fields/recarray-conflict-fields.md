# How To: Recarray Conflict Fields

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray conflict fields

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign ra = np.rec.array(...)

```python
ra = np.rec.array([(1, 'abc', 2.3), (2, 'xyz', 4.2), (3, 'wrs', 1.3)], names='field, shape, mean')
```

**Verification:**
```python
assert_array_almost_equal(ra['mean'], [1.1, 2.2, 3.3])
```

### Step 2: Assign ra.mean = value

```python
ra.mean = [1.1, 2.2, 3.3]
```

**Verification:**
```python
assert_(type(ra.mean) is type(ra.var))
```

### Step 3: Call assert_array_almost_equal()

```python
assert_array_almost_equal(ra['mean'], [1.1, 2.2, 3.3])
```

**Verification:**
```python
assert_(ra.shape == (1, 3))
```

### Step 4: Call assert_()

```python
assert_(type(ra.mean) is type(ra.var))
```

**Verification:**
```python
assert_array_equal(ra['shape'], [['A', 'B', 'C']])
```

### Step 5: Assign ra.shape = value

```python
ra.shape = (1, 3)
```

**Verification:**
```python
assert_array_equal(ra['field'], [[5, 5, 5]])
```

### Step 6: Call assert_()

```python
assert_(ra.shape == (1, 3))
```

**Verification:**
```python
assert_(isinstance(ra.field, collections.abc.Callable))
```

### Step 7: Assign ra.shape = value

```python
ra.shape = ['A', 'B', 'C']
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(ra['shape'], [['A', 'B', 'C']])
```

### Step 9: Assign ra.field = 5

```python
ra.field = 5
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(ra['field'], [[5, 5, 5]])
```

### Step 11: Call assert_()

```python
assert_(isinstance(ra.field, collections.abc.Callable))
```


## Complete Example

```python
# Workflow
ra = np.rec.array([(1, 'abc', 2.3), (2, 'xyz', 4.2), (3, 'wrs', 1.3)], names='field, shape, mean')
ra.mean = [1.1, 2.2, 3.3]
assert_array_almost_equal(ra['mean'], [1.1, 2.2, 3.3])
assert_(type(ra.mean) is type(ra.var))
ra.shape = (1, 3)
assert_(ra.shape == (1, 3))
ra.shape = ['A', 'B', 'C']
assert_array_equal(ra['shape'], [['A', 'B', 'C']])
ra.field = 5
assert_array_equal(ra['field'], [[5, 5, 5]])
assert_(isinstance(ra.field, collections.abc.Callable))
```

## Next Steps


---

*Source: test_records.py:265 | Complexity: Advanced | Last updated: 2026-06-02*