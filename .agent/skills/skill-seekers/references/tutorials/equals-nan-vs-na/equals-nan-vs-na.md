# How To: Equals Nan Vs Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals nan vs na

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arrays.masked_shared`


## Step-by-Step Guide

### Step 1: Assign mask = np.zeros(...)

```python
mask = np.zeros(3, dtype=bool)
```

**Verification:**
```python
assert left.equals(left)
```

### Step 2: Assign data = np.array(...)

```python
data = np.array([1.0, np.nan, 3.0], dtype=np.float64)
```

**Verification:**
```python
assert left.equals(left.copy())
```

### Step 3: Assign left = FloatingArray(...)

```python
left = FloatingArray(data, mask)
```

**Verification:**
```python
assert left.equals(FloatingArray(data.copy(), mask.copy()))
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(left, left)
```

**Verification:**
```python
assert right.equals(right)
```

### Step 5: Assign mask2 = np.array(...)

```python
mask2 = np.array([False, True, False], dtype=bool)
```

**Verification:**
```python
assert not left.equals(right)
```

### Step 6: Assign data2 = np.array(...)

```python
data2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
```

**Verification:**
```python
assert left.equals(right)
```

### Step 7: Assign right = FloatingArray(...)

```python
right = FloatingArray(data2, mask2)
```

**Verification:**
```python
assert right.equals(right)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(right, right)
```

**Verification:**
```python
assert not left.equals(right)
```

### Step 9: Assign unknown = True

```python
mask[1] = True
```

**Verification:**
```python
assert left.equals(right)
```


## Complete Example

```python
# Workflow
mask = np.zeros(3, dtype=bool)
data = np.array([1.0, np.nan, 3.0], dtype=np.float64)
left = FloatingArray(data, mask)
assert left.equals(left)
tm.assert_extension_array_equal(left, left)
assert left.equals(left.copy())
assert left.equals(FloatingArray(data.copy(), mask.copy()))
mask2 = np.array([False, True, False], dtype=bool)
data2 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
right = FloatingArray(data2, mask2)
assert right.equals(right)
tm.assert_extension_array_equal(right, right)
assert not left.equals(right)
mask[1] = True
assert left.equals(right)
```

## Next Steps


---

*Source: test_comparison.py:41 | Complexity: Advanced | Last updated: 2026-06-02*