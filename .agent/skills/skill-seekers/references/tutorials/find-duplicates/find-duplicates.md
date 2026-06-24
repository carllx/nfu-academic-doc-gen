# How To: Find Duplicates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find duplicates

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

### Step 1: Assign a = ma.array(...)

```python
a = ma.array([(2, (2.0, 'B')), (1, (2.0, 'B')), (2, (2.0, 'B')), (1, (1.0, 'B')), (2, (2.0, 'B')), (2, (2.0, 'C'))], mask=[(0, (0, 0)), (0, (0, 0)), (0, (0, 0)), (0, (0, 0)), (1, (0, 0)), (0, (1, 0))], dtype=[('A', int), ('B', [('BA', float), ('BB', '|S1')])])
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 2: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, ignoremask=False, return_index=True)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 3: Assign control = value

```python
control = [0, 2]
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 4: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 5: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 6: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, key='A', return_index=True)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 7: Assign control = value

```python
control = [0, 1, 2, 3, 5]
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 8: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 9: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 10: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, key='B', return_index=True)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 11: Assign control = value

```python
control = [0, 1, 2, 4]
```

### Step 12: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

### Step 13: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```

### Step 14: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, key='BA', return_index=True)
```

### Step 15: Assign control = value

```python
control = [0, 1, 2, 4]
```

### Step 16: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

### Step 17: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```

### Step 18: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, key='BB', return_index=True)
```

### Step 19: Assign control = value

```python
control = [0, 1, 2, 3, 4]
```

### Step 20: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

### Step 21: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```


## Complete Example

```python
# Workflow
a = ma.array([(2, (2.0, 'B')), (1, (2.0, 'B')), (2, (2.0, 'B')), (1, (1.0, 'B')), (2, (2.0, 'B')), (2, (2.0, 'C'))], mask=[(0, (0, 0)), (0, (0, 0)), (0, (0, 0)), (0, (0, 0)), (1, (0, 0)), (0, (1, 0))], dtype=[('A', int), ('B', [('BA', float), ('BB', '|S1')])])
test = find_duplicates(a, ignoremask=False, return_index=True)
control = [0, 2]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
test = find_duplicates(a, key='A', return_index=True)
control = [0, 1, 2, 3, 5]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
test = find_duplicates(a, key='B', return_index=True)
control = [0, 1, 2, 4]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
test = find_duplicates(a, key='BA', return_index=True)
control = [0, 1, 2, 4]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
test = find_duplicates(a, key='BB', return_index=True)
control = [0, 1, 2, 3, 4]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
```

## Next Steps


---

*Source: test_recfunctions.py:179 | Complexity: Advanced | Last updated: 2026-06-02*