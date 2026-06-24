# How To: Instances

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test instances

## Prerequisites

**Required Modules:**
- `types`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign class_iinfo = iinfo(...)

```python
class_iinfo = iinfo(c)
```

**Verification:**
```python
assert_iinfo_equal(class_iinfo, instance_iinfo)
```

### Step 2: Assign instance_iinfo = iinfo(...)

```python
instance_iinfo = iinfo(c(12))
```

**Verification:**
```python
assert_finfo_equal(class_finfo, instance_finfo)
```

### Step 3: Call assert_iinfo_equal()

```python
assert_iinfo_equal(class_iinfo, instance_iinfo)
```

### Step 4: Assign class_finfo = finfo(...)

```python
class_finfo = finfo(c)
```

### Step 5: Assign instance_finfo = finfo(...)

```python
instance_finfo = finfo(c(1.2))
```

### Step 6: Call assert_finfo_equal()

```python
assert_finfo_equal(class_finfo, instance_finfo)
```

### Step 7: Call iinfo()

```python
iinfo(10.0)
```

### Step 8: Call iinfo()

```python
iinfo('hi')
```

### Step 9: Call finfo()

```python
finfo(np.int64(1))
```


## Complete Example

```python
# Workflow
for c in [int, np.int16, np.int32, np.int64]:
    class_iinfo = iinfo(c)
    instance_iinfo = iinfo(c(12))
    assert_iinfo_equal(class_iinfo, instance_iinfo)
for c in [float, np.float16, np.float32, np.float64]:
    class_finfo = finfo(c)
    instance_finfo = finfo(c(1.2))
    assert_finfo_equal(class_finfo, instance_finfo)
with pytest.raises(ValueError):
    iinfo(10.0)
with pytest.raises(ValueError):
    iinfo('hi')
with pytest.raises(ValueError):
    finfo(np.int64(1))
```

## Next Steps


---

*Source: test_getlimits.py:116 | Complexity: Advanced | Last updated: 2026-06-02*