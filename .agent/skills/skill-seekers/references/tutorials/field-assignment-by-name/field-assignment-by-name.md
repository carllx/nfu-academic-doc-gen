# How To: Field Assignment By Name

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test field assignment by name

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

### Step 1: Assign a = np.ones(...)

```python
a = np.ones(2, dtype=[('a', 'i4'), ('b', 'f8'), ('c', 'u1')])
```

**Verification:**
```python
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
```

### Step 2: Assign newdt = value

```python
newdt = [('b', 'f4'), ('c', 'u1')]
```

**Verification:**
```python
assert_equal(a, np.array([(1, 1, 2), (1, 3, 4)], dtype=a.dtype))
```

### Step 3: Call assert_equal()

```python
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
```

**Verification:**
```python
assert_equal(a, np.array([(0, 1, 2), (0, 3, 4)], dtype=a.dtype))
```

### Step 4: Assign b = np.array(...)

```python
b = np.array([(1, 2), (3, 4)], dtype=newdt)
```

**Verification:**
```python
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
```

### Step 5: Call assign_fields_by_name()

```python
assign_fields_by_name(a, b, zero_unassigned=False)
```

**Verification:**
```python
assert_equal(a, np.array([((1, 2),), ((1, 3),)], dtype=a.dtype))
```

### Step 6: Call assert_equal()

```python
assert_equal(a, np.array([(1, 1, 2), (1, 3, 4)], dtype=a.dtype))
```

**Verification:**
```python
assert_equal(a, np.array([((0, 2),), ((0, 3),)], dtype=a.dtype))
```

### Step 7: Call assign_fields_by_name()

```python
assign_fields_by_name(a, b)
```

**Verification:**
```python
assert_equal(b[()], 3)
```

### Step 8: Call assert_equal()

```python
assert_equal(a, np.array([(0, 1, 2), (0, 3, 4)], dtype=a.dtype))
```

### Step 9: Assign a = np.ones(...)

```python
a = np.ones(2, dtype=[('a', [('b', 'f8'), ('c', 'u1')])])
```

### Step 10: Assign newdt = value

```python
newdt = [('a', [('c', 'u1')])]
```

### Step 11: Call assert_equal()

```python
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
```

### Step 12: Assign b = np.array(...)

```python
b = np.array([((2,),), ((3,),)], dtype=newdt)
```

### Step 13: Call assign_fields_by_name()

```python
assign_fields_by_name(a, b, zero_unassigned=False)
```

### Step 14: Call assert_equal()

```python
assert_equal(a, np.array([((1, 2),), ((1, 3),)], dtype=a.dtype))
```

### Step 15: Call assign_fields_by_name()

```python
assign_fields_by_name(a, b)
```

### Step 16: Call assert_equal()

```python
assert_equal(a, np.array([((0, 2),), ((0, 3),)], dtype=a.dtype))
```

### Step 17: Assign unknown = value

```python
a, b = (np.array(3), np.array(0))
```

### Step 18: Call assign_fields_by_name()

```python
assign_fields_by_name(b, a)
```

### Step 19: Call assert_equal()

```python
assert_equal(b[()], 3)
```


## Complete Example

```python
# Workflow
a = np.ones(2, dtype=[('a', 'i4'), ('b', 'f8'), ('c', 'u1')])
newdt = [('b', 'f4'), ('c', 'u1')]
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
b = np.array([(1, 2), (3, 4)], dtype=newdt)
assign_fields_by_name(a, b, zero_unassigned=False)
assert_equal(a, np.array([(1, 1, 2), (1, 3, 4)], dtype=a.dtype))
assign_fields_by_name(a, b)
assert_equal(a, np.array([(0, 1, 2), (0, 3, 4)], dtype=a.dtype))
a = np.ones(2, dtype=[('a', [('b', 'f8'), ('c', 'u1')])])
newdt = [('a', [('c', 'u1')])]
assert_equal(require_fields(a, newdt), np.ones(2, newdt))
b = np.array([((2,),), ((3,),)], dtype=newdt)
assign_fields_by_name(a, b, zero_unassigned=False)
assert_equal(a, np.array([((1, 2),), ((1, 3),)], dtype=a.dtype))
assign_fields_by_name(a, b)
assert_equal(a, np.array([((0, 2),), ((0, 3),)], dtype=a.dtype))
a, b = (np.array(3), np.array(0))
assign_fields_by_name(b, a)
assert_equal(b[()], 3)
```

## Next Steps


---

*Source: test_recfunctions.py:394 | Complexity: Advanced | Last updated: 2026-06-02*