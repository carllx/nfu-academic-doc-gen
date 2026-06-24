# How To: Ndindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ndindex

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._index_tricks_impl`
- `numpy.testing`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign x = list(...)

```python
x = list(ndindex(1, 2, 3))
```

**Verification:**
```python
assert_array_equal(x, expected)
```

### Step 2: Assign expected = value

```python
expected = [ix for ix, e in ndenumerate(np.zeros((1, 2, 3)))]
```

**Verification:**
```python
assert_array_equal(x, expected)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(x, expected)
```

**Verification:**
```python
assert_array_equal(x, list(ndindex(3)))
```

### Step 4: Assign x = list(...)

```python
x = list(ndindex((1, 2, 3)))
```

**Verification:**
```python
assert_equal(x, [()])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(x, expected)
```

**Verification:**
```python
assert_equal(x, [()])
```

### Step 6: Assign x = list(...)

```python
x = list(ndindex((3,)))
```

**Verification:**
```python
assert_equal(x, [])
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(x, list(ndindex(3)))
```

### Step 8: Assign x = list(...)

```python
x = list(ndindex())
```

### Step 9: Call assert_equal()

```python
assert_equal(x, [()])
```

### Step 10: Assign x = list(...)

```python
x = list(ndindex(()))
```

### Step 11: Call assert_equal()

```python
assert_equal(x, [()])
```

### Step 12: Assign x = list(...)

```python
x = list(ndindex(*[0]))
```

### Step 13: Call assert_equal()

```python
assert_equal(x, [])
```


## Complete Example

```python
# Workflow
x = list(ndindex(1, 2, 3))
expected = [ix for ix, e in ndenumerate(np.zeros((1, 2, 3)))]
assert_array_equal(x, expected)
x = list(ndindex((1, 2, 3)))
assert_array_equal(x, expected)
x = list(ndindex((3,)))
assert_array_equal(x, list(ndindex(3)))
x = list(ndindex())
assert_equal(x, [()])
x = list(ndindex(()))
assert_equal(x, [()])
x = list(ndindex(*[0]))
assert_equal(x, [])
```

## Next Steps


---

*Source: test_index_tricks.py:552 | Complexity: Advanced | Last updated: 2026-06-02*