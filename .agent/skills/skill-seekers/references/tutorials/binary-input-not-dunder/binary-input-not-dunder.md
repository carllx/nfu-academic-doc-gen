# How To: Binary Input Not Dunder

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test binary input not dunder

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3])
```

**Verification:**
```python
assert np.logaddexp(NA, NA) is NA
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([NA, NA, NA], dtype=object)
```

**Verification:**
```python
assert len(result) == 2
```

### Step 3: Assign result = np.logaddexp(...)

```python
result = np.logaddexp(a, NA)
```

**Verification:**
```python
assert all((x is NA for x in result))
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = np.logaddexp(...)

```python
result = np.logaddexp(NA, a)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

**Verification:**
```python
assert np.logaddexp(NA, NA) is NA
```

### Step 7: Assign result = np.modf(...)

```python
result = np.modf(NA, NA)
```

**Verification:**
```python
assert len(result) == 2
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3])
expected = np.array([NA, NA, NA], dtype=object)
result = np.logaddexp(a, NA)
tm.assert_numpy_array_equal(result, expected)
result = np.logaddexp(NA, a)
tm.assert_numpy_array_equal(result, expected)
assert np.logaddexp(NA, NA) is NA
result = np.modf(NA, NA)
assert len(result) == 2
assert all((x is NA for x in result))
```

## Next Steps


---

*Source: test_na_scalar.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*