# How To: Attributepropagation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attributepropagation

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = array(...)

```python
x = array(arange(5), mask=[0] + [1] * 4)
```

**Verification:**
```python
assert_(isinstance(z, MaskedArray))
```

### Step 2: Assign my = masked_array(...)

```python
my = masked_array(subarray(x))
```

**Verification:**
```python
assert_(not isinstance(z, MSubArray))
```

### Step 3: Assign ym = msubarray(...)

```python
ym = msubarray(x)
```

**Verification:**
```python
assert_(isinstance(z._data, SubArray))
```

### Step 4: Assign z = value

```python
z = my + 1
```

**Verification:**
```python
assert_equal(z._data.info, {})
```

### Step 5: Call assert_()

```python
assert_(isinstance(z, MaskedArray))
```

**Verification:**
```python
assert_(isinstance(z, MaskedArray))
```

### Step 6: Call assert_()

```python
assert_(not isinstance(z, MSubArray))
```

**Verification:**
```python
assert_(isinstance(z, MSubArray))
```

### Step 7: Call assert_()

```python
assert_(isinstance(z._data, SubArray))
```

**Verification:**
```python
assert_(isinstance(z._data, SubArray))
```

### Step 8: Call assert_equal()

```python
assert_equal(z._data.info, {})
```

**Verification:**
```python
assert_(z._data.info['added'] > 0)
```

### Step 9: Assign z = value

```python
z = ym + 1
```

**Verification:**
```python
assert_(isinstance(ym, MaskedArray))
```

### Step 10: Call assert_()

```python
assert_(isinstance(z, MaskedArray))
```

**Verification:**
```python
assert_(isinstance(ym, MSubArray))
```

### Step 11: Call assert_()

```python
assert_(isinstance(z, MSubArray))
```

**Verification:**
```python
assert_(isinstance(ym._data, SubArray))
```

### Step 12: Call assert_()

```python
assert_(isinstance(z._data, SubArray))
```

**Verification:**
```python
assert_(ym._data.info['iadded'] > 0)
```

### Step 13: Call assert_()

```python
assert_(z._data.info['added'] > 0)
```

**Verification:**
```python
assert_equal(ym._mask, [1, 0, 0, 0, 1])
```

### Step 14: Call assert_()

```python
assert_(isinstance(ym, MaskedArray))
```

**Verification:**
```python
assert_equal(ym._mask, [0, 0, 0, 0, 1])
```

### Step 15: Call assert_()

```python
assert_(isinstance(ym, MSubArray))
```

**Verification:**
```python
assert_(hasattr(mxsub, 'info'))
```

### Step 16: Call assert_()

```python
assert_(isinstance(ym._data, SubArray))
```

**Verification:**
```python
assert_equal(mxsub.info, xsub.info)
```

### Step 17: Call assert_()

```python
assert_(ym._data.info['iadded'] > 0)
```

### Step 18: Call ym._set_mask()

```python
ym._set_mask([1, 0, 0, 0, 1])
```

### Step 19: Call assert_equal()

```python
assert_equal(ym._mask, [1, 0, 0, 0, 1])
```

### Step 20: Call ym._series._set_mask()

```python
ym._series._set_mask([0, 0, 0, 0, 1])
```

### Step 21: Call assert_equal()

```python
assert_equal(ym._mask, [0, 0, 0, 0, 1])
```

### Step 22: Assign xsub = subarray(...)

```python
xsub = subarray(x, info={'name': 'x'})
```

### Step 23: Assign mxsub = masked_array(...)

```python
mxsub = masked_array(xsub)
```

### Step 24: Call assert_()

```python
assert_(hasattr(mxsub, 'info'))
```

### Step 25: Call assert_equal()

```python
assert_equal(mxsub.info, xsub.info)
```


## Complete Example

```python
# Workflow
x = array(arange(5), mask=[0] + [1] * 4)
my = masked_array(subarray(x))
ym = msubarray(x)
z = my + 1
assert_(isinstance(z, MaskedArray))
assert_(not isinstance(z, MSubArray))
assert_(isinstance(z._data, SubArray))
assert_equal(z._data.info, {})
z = ym + 1
assert_(isinstance(z, MaskedArray))
assert_(isinstance(z, MSubArray))
assert_(isinstance(z._data, SubArray))
assert_(z._data.info['added'] > 0)
ym += 1
assert_(isinstance(ym, MaskedArray))
assert_(isinstance(ym, MSubArray))
assert_(isinstance(ym._data, SubArray))
assert_(ym._data.info['iadded'] > 0)
ym._set_mask([1, 0, 0, 0, 1])
assert_equal(ym._mask, [1, 0, 0, 0, 1])
ym._series._set_mask([0, 0, 0, 0, 1])
assert_equal(ym._mask, [0, 0, 0, 0, 1])
xsub = subarray(x, info={'name': 'x'})
mxsub = masked_array(xsub)
assert_(hasattr(mxsub, 'info'))
assert_equal(mxsub.info, xsub.info)
```

## Next Steps


---

*Source: test_subclassing.py:239 | Complexity: Advanced | Last updated: 2026-06-02*