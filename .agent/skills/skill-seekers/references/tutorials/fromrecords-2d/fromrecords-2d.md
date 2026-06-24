# How To: Fromrecords 2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fromrecords 2d

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

### Step 1: Assign data = value

```python
data = [[(1, 2), (3, 4), (5, 6)], [(6, 5), (4, 3), (2, 1)]]
```

**Verification:**
```python
assert_equal(r1['a'], expected_a)
```

### Step 2: Assign expected_a = value

```python
expected_a = [[1, 3, 5], [6, 4, 2]]
```

**Verification:**
```python
assert_equal(r1['b'], expected_b)
```

### Step 3: Assign expected_b = value

```python
expected_b = [[2, 4, 6], [5, 3, 1]]
```

**Verification:**
```python
assert_equal(r2['a'], expected_a)
```

### Step 4: Assign r1 = np.rec.fromrecords(...)

```python
r1 = np.rec.fromrecords(data, dtype=[('a', int), ('b', int)])
```

**Verification:**
```python
assert_equal(r2['b'], expected_b)
```

### Step 5: Call assert_equal()

```python
assert_equal(r1['a'], expected_a)
```

**Verification:**
```python
assert_equal(r1, r2)
```

### Step 6: Call assert_equal()

```python
assert_equal(r1['b'], expected_b)
```

### Step 7: Assign r2 = np.rec.fromrecords(...)

```python
r2 = np.rec.fromrecords(data, names=['a', 'b'])
```

### Step 8: Call assert_equal()

```python
assert_equal(r2['a'], expected_a)
```

### Step 9: Call assert_equal()

```python
assert_equal(r2['b'], expected_b)
```

### Step 10: Call assert_equal()

```python
assert_equal(r1, r2)
```


## Complete Example

```python
# Workflow
data = [[(1, 2), (3, 4), (5, 6)], [(6, 5), (4, 3), (2, 1)]]
expected_a = [[1, 3, 5], [6, 4, 2]]
expected_b = [[2, 4, 6], [5, 3, 1]]
r1 = np.rec.fromrecords(data, dtype=[('a', int), ('b', int)])
assert_equal(r1['a'], expected_a)
assert_equal(r1['b'], expected_b)
r2 = np.rec.fromrecords(data, names=['a', 'b'])
assert_equal(r2['a'], expected_a)
assert_equal(r2['b'], expected_b)
assert_equal(r1, r2)
```

## Next Steps


---

*Source: test_records.py:37 | Complexity: Advanced | Last updated: 2026-06-02*