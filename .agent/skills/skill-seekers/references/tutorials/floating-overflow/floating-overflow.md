# How To: Floating Overflow

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Strings containing an unrepresentable float overflow 

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: ' Strings containing an unrepresentable float overflow '

```python
' Strings containing an unrepresentable float overflow '
```

**Verification:**
```python
assert_equal(fhalf, np.inf)
```

### Step 2: Assign fhalf = np.half(...)

```python
fhalf = np.half('1e10000')
```

**Verification:**
```python
assert_equal(fsingle, np.inf)
```

### Step 3: Call assert_equal()

```python
assert_equal(fhalf, np.inf)
```

**Verification:**
```python
assert_equal(fdouble, np.inf)
```

### Step 4: Assign fsingle = np.single(...)

```python
fsingle = np.single('1e10000')
```

**Verification:**
```python
assert_equal(flongdouble, np.inf)
```

### Step 5: Call assert_equal()

```python
assert_equal(fsingle, np.inf)
```

**Verification:**
```python
assert_equal(fhalf, -np.inf)
```

### Step 6: Assign fdouble = np.double(...)

```python
fdouble = np.double('1e10000')
```

**Verification:**
```python
assert_equal(fsingle, -np.inf)
```

### Step 7: Call assert_equal()

```python
assert_equal(fdouble, np.inf)
```

**Verification:**
```python
assert_equal(fdouble, -np.inf)
```

### Step 8: Assign flongdouble = pytest.warns(...)

```python
flongdouble = pytest.warns(RuntimeWarning, np.longdouble, '1e10000')
```

**Verification:**
```python
assert_equal(flongdouble, -np.inf)
```

### Step 9: Call assert_equal()

```python
assert_equal(flongdouble, np.inf)
```

### Step 10: Assign fhalf = np.half(...)

```python
fhalf = np.half('-1e10000')
```

### Step 11: Call assert_equal()

```python
assert_equal(fhalf, -np.inf)
```

### Step 12: Assign fsingle = np.single(...)

```python
fsingle = np.single('-1e10000')
```

### Step 13: Call assert_equal()

```python
assert_equal(fsingle, -np.inf)
```

### Step 14: Assign fdouble = np.double(...)

```python
fdouble = np.double('-1e10000')
```

### Step 15: Call assert_equal()

```python
assert_equal(fdouble, -np.inf)
```

### Step 16: Assign flongdouble = pytest.warns(...)

```python
flongdouble = pytest.warns(RuntimeWarning, np.longdouble, '-1e10000')
```

### Step 17: Call assert_equal()

```python
assert_equal(flongdouble, -np.inf)
```


## Complete Example

```python
# Workflow
' Strings containing an unrepresentable float overflow '
fhalf = np.half('1e10000')
assert_equal(fhalf, np.inf)
fsingle = np.single('1e10000')
assert_equal(fsingle, np.inf)
fdouble = np.double('1e10000')
assert_equal(fdouble, np.inf)
flongdouble = pytest.warns(RuntimeWarning, np.longdouble, '1e10000')
assert_equal(flongdouble, np.inf)
fhalf = np.half('-1e10000')
assert_equal(fhalf, -np.inf)
fsingle = np.single('-1e10000')
assert_equal(fsingle, -np.inf)
fdouble = np.double('-1e10000')
assert_equal(fdouble, -np.inf)
flongdouble = pytest.warns(RuntimeWarning, np.longdouble, '-1e10000')
assert_equal(flongdouble, -np.inf)
```

## Next Steps


---

*Source: test_scalar_ctors.py:20 | Complexity: Advanced | Last updated: 2026-06-02*