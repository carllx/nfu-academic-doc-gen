# How To: Subclass Str

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str with subclass that has overridden str, setitem

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.lib.mixins`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'test str with subclass that has overridden str, setitem'

```python
'test str with subclass that has overridden str, setitem'
```

**Verification:**
```python
assert_equal(str(mxsub), '[-- 1 -- 3 4]')
```

### Step 2: Assign x = np.arange(...)

```python
x = np.arange(5)
```

**Verification:**
```python
assert_raises(ValueError, xcsub.__setitem__, 0, np.ma.core.masked_print_option)
```

### Step 3: Assign xsub = SubArray(...)

```python
xsub = SubArray(x)
```

**Verification:**
```python
assert_equal(str(mxcsub), 'myprefix [-- 1 -- 3 4] mypostfix')
```

### Step 4: Assign mxsub = masked_array(...)

```python
mxsub = masked_array(xsub, mask=[True, False, True, False, False])
```

### Step 5: Call assert_equal()

```python
assert_equal(str(mxsub), '[-- 1 -- 3 4]')
```

### Step 6: Assign xcsub = ComplicatedSubArray(...)

```python
xcsub = ComplicatedSubArray(x)
```

### Step 7: Call assert_raises()

```python
assert_raises(ValueError, xcsub.__setitem__, 0, np.ma.core.masked_print_option)
```

### Step 8: Assign mxcsub = masked_array(...)

```python
mxcsub = masked_array(xcsub, mask=[True, False, True, False, False])
```

### Step 9: Call assert_equal()

```python
assert_equal(str(mxcsub), 'myprefix [-- 1 -- 3 4] mypostfix')
```


## Complete Example

```python
# Workflow
'test str with subclass that has overridden str, setitem'
x = np.arange(5)
xsub = SubArray(x)
mxsub = masked_array(xsub, mask=[True, False, True, False, False])
assert_equal(str(mxsub), '[-- 1 -- 3 4]')
xcsub = ComplicatedSubArray(x)
assert_raises(ValueError, xcsub.__setitem__, 0, np.ma.core.masked_print_option)
mxcsub = masked_array(xcsub, mask=[True, False, True, False, False])
assert_equal(str(mxcsub), 'myprefix [-- 1 -- 3 4] mypostfix')
```

## Next Steps


---

*Source: test_subclassing.py:358 | Complexity: Advanced | Last updated: 2026-06-02*