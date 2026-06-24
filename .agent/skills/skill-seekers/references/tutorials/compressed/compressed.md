# How To: Compressed

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compressed

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign a = masked_array(...)

```python
a = masked_array(np.matrix([1, 2, 3, 4]), mask=[0, 0, 0, 0])
```

**Verification:**
```python
assert_equal(b, a)
```

### Step 2: Assign b = a.compressed(...)

```python
b = a.compressed()
```

**Verification:**
```python
assert_(isinstance(b, np.matrix))
```

### Step 3: Call assert_equal()

```python
assert_equal(b, a)
```

**Verification:**
```python
assert_equal(b, [[2, 3, 4]])
```

### Step 4: Call assert_()

```python
assert_(isinstance(b, np.matrix))
```

### Step 5: Assign unknown = masked

```python
a[0, 0] = masked
```

### Step 6: Assign b = a.compressed(...)

```python
b = a.compressed()
```

### Step 7: Call assert_equal()

```python
assert_equal(b, [[2, 3, 4]])
```


## Complete Example

```python
# Workflow
a = masked_array(np.matrix([1, 2, 3, 4]), mask=[0, 0, 0, 0])
b = a.compressed()
assert_equal(b, a)
assert_(isinstance(b, np.matrix))
a[0, 0] = masked
b = a.compressed()
assert_equal(b, [[2, 3, 4]])
```

## Next Steps


---

*Source: test_masked_matrix.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*