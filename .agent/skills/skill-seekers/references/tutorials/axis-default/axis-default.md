# How To: Axis Default

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test axis default

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma.core`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign data1d = np.ma.arange(...)

```python
data1d = np.ma.arange(6)
```

**Verification:**
```python
assert_equal(result, ma_max(data2d, axis=None))
```

### Step 2: Assign data2d = data1d.reshape(...)

```python
data2d = data1d.reshape(2, 3)
```

**Verification:**
```python
assert_equal(result, ma_min(data2d, axis=None))
```

### Step 3: Assign ma_min = value

```python
ma_min = np.ma.minimum.reduce
```

**Verification:**
```python
assert_equal(result, ma_min(data1d, axis=None))
```

### Step 4: Assign ma_max = value

```python
ma_max = np.ma.maximum.reduce
```

**Verification:**
```python
assert_equal(result, ma_min(data1d, axis=0))
```

### Step 5: Assign result = pytest.warns(...)

```python
result = pytest.warns(MaskedArrayFutureWarning, ma_max, data2d)
```

**Verification:**
```python
assert_equal(result, ma_max(data1d, axis=None))
```

### Step 6: Call assert_equal()

```python
assert_equal(result, ma_max(data2d, axis=None))
```

**Verification:**
```python
assert_equal(result, ma_max(data1d, axis=0))
```

### Step 7: Assign result = pytest.warns(...)

```python
result = pytest.warns(MaskedArrayFutureWarning, ma_min, data2d)
```

### Step 8: Call assert_equal()

```python
assert_equal(result, ma_min(data2d, axis=None))
```

### Step 9: Assign result = ma_min(...)

```python
result = ma_min(data1d)
```

### Step 10: Call assert_equal()

```python
assert_equal(result, ma_min(data1d, axis=None))
```

### Step 11: Call assert_equal()

```python
assert_equal(result, ma_min(data1d, axis=0))
```

### Step 12: Assign result = ma_max(...)

```python
result = ma_max(data1d)
```

### Step 13: Call assert_equal()

```python
assert_equal(result, ma_max(data1d, axis=None))
```

### Step 14: Call assert_equal()

```python
assert_equal(result, ma_max(data1d, axis=0))
```


## Complete Example

```python
# Workflow
data1d = np.ma.arange(6)
data2d = data1d.reshape(2, 3)
ma_min = np.ma.minimum.reduce
ma_max = np.ma.maximum.reduce
result = pytest.warns(MaskedArrayFutureWarning, ma_max, data2d)
assert_equal(result, ma_max(data2d, axis=None))
result = pytest.warns(MaskedArrayFutureWarning, ma_min, data2d)
assert_equal(result, ma_min(data2d, axis=None))
result = ma_min(data1d)
assert_equal(result, ma_min(data1d, axis=None))
assert_equal(result, ma_min(data1d, axis=0))
result = ma_max(data1d)
assert_equal(result, ma_max(data1d, axis=None))
assert_equal(result, ma_max(data1d, axis=0))
```

## Next Steps


---

*Source: test_deprecations.py:42 | Complexity: Advanced | Last updated: 2026-06-02*