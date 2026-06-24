# How To: Array No Inheritance

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array no inheritance

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign data_masked = np.ma.array(...)

```python
data_masked = np.ma.array([1, 2, 3], mask=[True, False, True])
```

**Verification:**
```python
assert_equal(data_masked.data, new_array.data)
```

### Step 2: Assign data_masked_units = ArrayNoInheritance(...)

```python
data_masked_units = ArrayNoInheritance(data_masked, 'meters')
```

**Verification:**
```python
assert_equal(data_masked.mask, new_array.mask)
```

### Step 3: Assign new_array = np.ma.array(...)

```python
new_array = np.ma.array(data_masked_units)
```

**Verification:**
```python
assert_equal(data_masked.mask, new_array.mask)
```

### Step 4: Call assert_equal()

```python
assert_equal(data_masked.data, new_array.data)
```

**Verification:**
```python
assert_(new_array.sharedmask)
```

### Step 5: Call assert_equal()

```python
assert_equal(data_masked.mask, new_array.mask)
```

**Verification:**
```python
assert_equal(data_masked.data, new_array.data)
```

### Step 6: Assign data_masked.mask = value

```python
data_masked.mask = [True, False, False]
```

**Verification:**
```python
assert_equal(data_masked.mask, new_array.mask)
```

### Step 7: Call assert_equal()

```python
assert_equal(data_masked.mask, new_array.mask)
```

**Verification:**
```python
assert_equal([True, False, False], new_array.mask)
```

### Step 8: Call assert_()

```python
assert_(new_array.sharedmask)
```

**Verification:**
```python
assert_(not new_array.sharedmask)
```

### Step 9: Assign new_array = np.ma.array(...)

```python
new_array = np.ma.array(data_masked_units, copy=True)
```

**Verification:**
```python
assert_equal(data_masked.data, new_array.data)
```

### Step 10: Call assert_equal()

```python
assert_equal(data_masked.data, new_array.data)
```

**Verification:**
```python
assert_equal(data_masked.mask, [True, False, True])
```

### Step 11: Call assert_equal()

```python
assert_equal(data_masked.mask, new_array.mask)
```

**Verification:**
```python
assert_(not new_array.mask)
```

### Step 12: Assign data_masked.mask = value

```python
data_masked.mask = [True, False, True]
```

**Verification:**
```python
assert_(not new_array.sharedmask)
```

### Step 13: Call assert_equal()

```python
assert_equal([True, False, False], new_array.mask)
```

### Step 14: Call assert_()

```python
assert_(not new_array.sharedmask)
```

### Step 15: Assign new_array = np.ma.array(...)

```python
new_array = np.ma.array(data_masked_units, keep_mask=False)
```

### Step 16: Call assert_equal()

```python
assert_equal(data_masked.data, new_array.data)
```

### Step 17: Call assert_equal()

```python
assert_equal(data_masked.mask, [True, False, True])
```

### Step 18: Call assert_()

```python
assert_(not new_array.mask)
```

### Step 19: Call assert_()

```python
assert_(not new_array.sharedmask)
```


## Complete Example

```python
# Workflow
data_masked = np.ma.array([1, 2, 3], mask=[True, False, True])
data_masked_units = ArrayNoInheritance(data_masked, 'meters')
new_array = np.ma.array(data_masked_units)
assert_equal(data_masked.data, new_array.data)
assert_equal(data_masked.mask, new_array.mask)
data_masked.mask = [True, False, False]
assert_equal(data_masked.mask, new_array.mask)
assert_(new_array.sharedmask)
new_array = np.ma.array(data_masked_units, copy=True)
assert_equal(data_masked.data, new_array.data)
assert_equal(data_masked.mask, new_array.mask)
data_masked.mask = [True, False, True]
assert_equal([True, False, False], new_array.mask)
assert_(not new_array.sharedmask)
new_array = np.ma.array(data_masked_units, keep_mask=False)
assert_equal(data_masked.data, new_array.data)
assert_equal(data_masked.mask, [True, False, True])
assert_(not new_array.mask)
assert_(not new_array.sharedmask)
```

## Next Steps


---

*Source: test_subclassing.py:395 | Complexity: Advanced | Last updated: 2026-06-02*