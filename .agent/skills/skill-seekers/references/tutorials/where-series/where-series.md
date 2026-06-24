# How To: Where Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data, na_value
```

## Step-by-Step Guide

### Step 1: Assign cls = type(...)

```python
cls = type(data)
```

**Verification:**
```python
assert data[0] != data[1]
```

### Step 2: Assign unknown = value

```python
a, b = data[:2]
```

### Step 3: Assign ser = pd.Series(...)

```python
ser = pd.Series(cls._from_sequence([a, a, b, b], dtype=data.dtype))
```

### Step 4: Assign cond = np.array(...)

```python
cond = np.array([True, True, False, False])
```

### Step 5: Assign result = ser.where(...)

```python
result = ser.where(cond)
```

### Step 6: Assign new_dtype = SparseDtype(...)

```python
new_dtype = SparseDtype('float', 0.0)
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series(cls._from_sequence([a, a, na_value, na_value], dtype=new_dtype))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign other = cls._from_sequence(...)

```python
other = cls._from_sequence([a, b, a, b], dtype=data.dtype)
```

### Step 10: Assign cond = np.array(...)

```python
cond = np.array([True, False, True, True])
```

### Step 11: Assign result = ser.where(...)

```python
result = ser.where(cond, other)
```

### Step 12: Assign expected = pd.Series(...)

```python
expected = pd.Series(cls._from_sequence([a, b, b, b], dtype=data.dtype))
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, na_value

# Workflow
assert data[0] != data[1]
cls = type(data)
a, b = data[:2]
ser = pd.Series(cls._from_sequence([a, a, b, b], dtype=data.dtype))
cond = np.array([True, True, False, False])
result = ser.where(cond)
new_dtype = SparseDtype('float', 0.0)
expected = pd.Series(cls._from_sequence([a, a, na_value, na_value], dtype=new_dtype))
tm.assert_series_equal(result, expected)
other = cls._from_sequence([a, b, a, b], dtype=data.dtype)
cond = np.array([True, False, True, True])
result = ser.where(cond, other)
expected = pd.Series(cls._from_sequence([a, b, b, b], dtype=data.dtype))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sparse.py:312 | Complexity: Advanced | Last updated: 2026-06-02*