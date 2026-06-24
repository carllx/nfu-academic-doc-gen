# How To: Ftype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ftype

## Prerequisites

**Required Modules:**
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign ftype = value

```python
ftype = self.module
```

**Verification:**
```python
assert_equal(ftype.data.a, 0)
```

### Step 2: Call ftype.foo()

```python
ftype.foo()
```

**Verification:**
```python
assert_equal(ftype.data.a, 3)
```

### Step 3: Call assert_equal()

```python
assert_equal(ftype.data.a, 0)
```

**Verification:**
```python
assert_array_equal(ftype.data.x, np.array([1, 2, 3], dtype=np.float32))
```

### Step 4: Assign ftype.data.a = 3

```python
ftype.data.a = 3
```

**Verification:**
```python
assert_array_equal(ftype.data.x, np.array([1, 45, 3], dtype=np.float32))
```

### Step 5: Assign ftype.data.x = value

```python
ftype.data.x = [1, 2, 3]
```

### Step 6: Call assert_equal()

```python
assert_equal(ftype.data.a, 3)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(ftype.data.x, np.array([1, 2, 3], dtype=np.float32))
```

### Step 8: Assign unknown = 45

```python
ftype.data.x[1] = 45
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(ftype.data.x, np.array([1, 45, 3], dtype=np.float32))
```

### Step 10: Assign ftype.data.a = 0

```python
ftype.data.a = 0
```


## Complete Example

```python
# Workflow
ftype = self.module
ftype.foo()
assert_equal(ftype.data.a, 0)
ftype.data.a = 3
ftype.data.x = [1, 2, 3]
assert_equal(ftype.data.a, 3)
assert_array_equal(ftype.data.x, np.array([1, 2, 3], dtype=np.float32))
ftype.data.x[1] = 45
assert_array_equal(ftype.data.x, np.array([1, 45, 3], dtype=np.float32))
ftype.data.a = 0
```

## Next Steps


---

*Source: test_docs.py:51 | Complexity: Advanced | Last updated: 2026-06-02*