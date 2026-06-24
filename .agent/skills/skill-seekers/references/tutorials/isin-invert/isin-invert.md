# How To: Isin Invert

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test isin's invert parameter

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.dtypes`
- `numpy.exceptions`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: "Test isin's invert parameter"

```python
"Test isin's invert parameter"
```

**Verification:**
```python
assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
```

### Step 2: Assign a = np.array(...)

```python
a = np.array([5, 4, 5, 3, 4, 4, 3, 4, 3, 5, 2, 1, 5, 5])
```

**Verification:**
```python
assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
```

### Step 3: Assign b = value

```python
b = [2, 3, 4] * mult
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
```

### Step 5: Assign a = np.array(...)

```python
a = np.array([5, 4, 5, 3, 4, 4, 3, 4, 3, 5, 2, 1, 5, 5], dtype=np.float32)
```

### Step 6: Assign b = value

```python
b = [2, 3, 4] * mult
```

### Step 7: Assign b = np.array(...)

```python
b = np.array(b, dtype=np.float32)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
"Test isin's invert parameter"
for mult in (1, 10):
    a = np.array([5, 4, 5, 3, 4, 4, 3, 4, 3, 5, 2, 1, 5, 5])
    b = [2, 3, 4] * mult
    assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
if kind in {None, 'sort'}:
    for mult in (1, 10):
        a = np.array([5, 4, 5, 3, 4, 4, 3, 4, 3, 5, 2, 1, 5, 5], dtype=np.float32)
        b = [2, 3, 4] * mult
        b = np.array(b, dtype=np.float32)
        assert_array_equal(np.invert(isin(a, b, kind=kind)), isin(a, b, invert=True, kind=kind))
```

## Next Steps


---

*Source: test_arraysetops.py:347 | Complexity: Advanced | Last updated: 2026-06-02*