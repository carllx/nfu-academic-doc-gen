# How To: Drop Fields

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop fields

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.lib.recfunctions`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([(1, (2, 3.0)), (4, (5, 6.0))], dtype=[('a', int), ('b', [('ba', float), ('bb', int)])])
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 2: Assign test = drop_fields(...)

```python
test = drop_fields(a, 'a')
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 3: Assign control = np.array(...)

```python
control = np.array([((2, 3.0),), ((5, 6.0),)], dtype=[('b', [('ba', float), ('bb', int)])])
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 4: Call assert_equal()

```python
assert_equal(test, control)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 5: Assign test = drop_fields(...)

```python
test = drop_fields(a, 'b')
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 6: Assign control = np.array(...)

```python
control = np.array([(1,), (4,)], dtype=[('a', int)])
```

### Step 7: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 8: Assign test = drop_fields(...)

```python
test = drop_fields(a, ['ba'])
```

### Step 9: Assign control = np.array(...)

```python
control = np.array([(1, (3.0,)), (4, (6.0,))], dtype=[('a', int), ('b', [('bb', int)])])
```

### Step 10: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 11: Assign test = drop_fields(...)

```python
test = drop_fields(a, ['ba', 'bb'])
```

### Step 12: Assign control = np.array(...)

```python
control = np.array([(1,), (4,)], dtype=[('a', int)])
```

### Step 13: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 14: Assign test = drop_fields(...)

```python
test = drop_fields(a, ['a', 'b'])
```

### Step 15: Assign control = np.array(...)

```python
control = np.array([(), ()], dtype=[])
```

### Step 16: Call assert_equal()

```python
assert_equal(test, control)
```


## Complete Example

```python
# Workflow
a = np.array([(1, (2, 3.0)), (4, (5, 6.0))], dtype=[('a', int), ('b', [('ba', float), ('bb', int)])])
test = drop_fields(a, 'a')
control = np.array([((2, 3.0),), ((5, 6.0),)], dtype=[('b', [('ba', float), ('bb', int)])])
assert_equal(test, control)
test = drop_fields(a, 'b')
control = np.array([(1,), (4,)], dtype=[('a', int)])
assert_equal(test, control)
test = drop_fields(a, ['ba'])
control = np.array([(1, (3.0,)), (4, (6.0,))], dtype=[('a', int), ('b', [('bb', int)])])
assert_equal(test, control)
test = drop_fields(a, ['ba', 'bb'])
control = np.array([(1,), (4,)], dtype=[('a', int)])
assert_equal(test, control)
test = drop_fields(a, ['a', 'b'])
control = np.array([(), ()], dtype=[])
assert_equal(test, control)
```

## Next Steps


---

*Source: test_recfunctions.py:73 | Complexity: Advanced | Last updated: 2026-06-02*