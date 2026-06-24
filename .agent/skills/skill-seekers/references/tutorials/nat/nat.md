# How To: Nat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_without_na
```

## Step-by-Step Guide

### Step 1: Assign empty_index = value

```python
empty_index = index_without_na[:0]
```

**Verification:**
```python
assert empty_index._na_value is NaT
```

### Step 2: Assign index_with_na = index_without_na.copy(...)

```python
index_with_na = index_without_na.copy(deep=True)
```

**Verification:**
```python
assert index_with_na._na_value is NaT
```

### Step 3: Assign unknown = NaT

```python
index_with_na._data[1] = NaT
```

**Verification:**
```python
assert index_without_na._na_value is NaT
```

### Step 4: Assign idx = index_without_na

```python
idx = index_without_na
```

**Verification:**
```python
assert idx._can_hold_na
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
```

**Verification:**
```python
assert idx.hasnans is False
```

### Step 6: Assign idx = index_with_na

```python
idx = index_with_na
```

**Verification:**
```python
assert idx._can_hold_na
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
```

**Verification:**
```python
assert idx.hasnans is True
```


## Complete Example

```python
# Setup
# Fixtures: index_without_na

# Workflow
empty_index = index_without_na[:0]
index_with_na = index_without_na.copy(deep=True)
index_with_na._data[1] = NaT
assert empty_index._na_value is NaT
assert index_with_na._na_value is NaT
assert index_without_na._na_value is NaT
idx = index_without_na
assert idx._can_hold_na
tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
assert idx.hasnans is False
idx = index_with_na
assert idx._can_hold_na
tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
assert idx.hasnans is True
```

## Next Steps


---

*Source: test_nat.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*