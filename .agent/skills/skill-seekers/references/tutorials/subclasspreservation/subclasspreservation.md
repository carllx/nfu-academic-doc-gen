# How To: Subclasspreservation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclasspreservation

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
assert_(not isinstance(mxsub, MSubArray))
```

### Step 2: Assign m = value

```python
m = [0, 0, 1, 0, 0]
```

**Verification:**
```python
assert_(isinstance(mxsub, MaskedArray))
```

### Step 3: Assign xinfo = list(...)

```python
xinfo = list(zip(x, m))
```

**Verification:**
```python
assert_equal(mxsub._mask, m)
```

### Step 4: Assign xsub = MSubArray(...)

```python
xsub = MSubArray(x, mask=m, info={'xsub': xinfo})
```

**Verification:**
```python
assert_(not isinstance(mxsub, MSubArray))
```

### Step 5: Assign mxsub = masked_array(...)

```python
mxsub = masked_array(xsub, subok=False)
```

**Verification:**
```python
assert_(isinstance(mxsub, MaskedArray))
```

### Step 6: Call assert_()

```python
assert_(not isinstance(mxsub, MSubArray))
```

**Verification:**
```python
assert_equal(mxsub._mask, m)
```

### Step 7: Call assert_()

```python
assert_(isinstance(mxsub, MaskedArray))
```

**Verification:**
```python
assert_(isinstance(mxsub, MSubArray))
```

### Step 8: Call assert_equal()

```python
assert_equal(mxsub._mask, m)
```

**Verification:**
```python
assert_equal(mxsub.info, xsub.info)
```

### Step 9: Assign mxsub = asarray(...)

```python
mxsub = asarray(xsub)
```

**Verification:**
```python
assert_equal(mxsub._mask, xsub._mask)
```

### Step 10: Call assert_()

```python
assert_(not isinstance(mxsub, MSubArray))
```

**Verification:**
```python
assert_(isinstance(mxsub, MSubArray))
```

### Step 11: Call assert_()

```python
assert_(isinstance(mxsub, MaskedArray))
```

**Verification:**
```python
assert_equal(mxsub.info, xsub.info)
```

### Step 12: Call assert_equal()

```python
assert_equal(mxsub._mask, m)
```

**Verification:**
```python
assert_equal(mxsub._mask, m)
```

### Step 13: Assign mxsub = masked_array(...)

```python
mxsub = masked_array(xsub, subok=True)
```

### Step 14: Call assert_()

```python
assert_(isinstance(mxsub, MSubArray))
```

### Step 15: Call assert_equal()

```python
assert_equal(mxsub.info, xsub.info)
```

### Step 16: Call assert_equal()

```python
assert_equal(mxsub._mask, xsub._mask)
```

### Step 17: Assign mxsub = asanyarray(...)

```python
mxsub = asanyarray(xsub)
```

### Step 18: Call assert_()

```python
assert_(isinstance(mxsub, MSubArray))
```

### Step 19: Call assert_equal()

```python
assert_equal(mxsub.info, xsub.info)
```

### Step 20: Call assert_equal()

```python
assert_equal(mxsub._mask, m)
```


## Complete Example

```python
# Workflow
x = np.arange(5)
m = [0, 0, 1, 0, 0]
xinfo = list(zip(x, m))
xsub = MSubArray(x, mask=m, info={'xsub': xinfo})
mxsub = masked_array(xsub, subok=False)
assert_(not isinstance(mxsub, MSubArray))
assert_(isinstance(mxsub, MaskedArray))
assert_equal(mxsub._mask, m)
mxsub = asarray(xsub)
assert_(not isinstance(mxsub, MSubArray))
assert_(isinstance(mxsub, MaskedArray))
assert_equal(mxsub._mask, m)
mxsub = masked_array(xsub, subok=True)
assert_(isinstance(mxsub, MSubArray))
assert_equal(mxsub.info, xsub.info)
assert_equal(mxsub._mask, xsub._mask)
mxsub = asanyarray(xsub)
assert_(isinstance(mxsub, MSubArray))
assert_equal(mxsub.info, xsub.info)
assert_equal(mxsub._mask, m)
```

## Next Steps


---

*Source: test_subclassing.py:272 | Complexity: Advanced | Last updated: 2026-06-02*