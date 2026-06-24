# How To: Data Subclassing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test data subclassing

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.arange(...)

```python
x = np.arange(5)
```

**Verification:**
```python
assert_(isinstance(xmsub, MaskedArray))
```

### Step 2: Assign m = value

```python
m = [0, 0, 1, 0, 0]
```

**Verification:**
```python
assert_equal(xmsub._data, xsub)
```

### Step 3: Assign xsub = SubArray(...)

```python
xsub = SubArray(x)
```

**Verification:**
```python
assert_(isinstance(xmsub._data, SubArray))
```

### Step 4: Assign xmsub = masked_array(...)

```python
xmsub = masked_array(xsub, mask=m)
```

### Step 5: Call assert_()

```python
assert_(isinstance(xmsub, MaskedArray))
```

### Step 6: Call assert_equal()

```python
assert_equal(xmsub._data, xsub)
```

### Step 7: Call assert_()

```python
assert_(isinstance(xmsub._data, SubArray))
```


## Complete Example

```python
# Workflow
x = np.arange(5)
m = [0, 0, 1, 0, 0]
xsub = SubArray(x)
xmsub = masked_array(xsub, mask=m)
assert_(isinstance(xmsub, MaskedArray))
assert_equal(xmsub._data, xsub)
assert_(isinstance(xmsub._data, SubArray))
```

## Next Steps


---

*Source: test_subclassing.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*