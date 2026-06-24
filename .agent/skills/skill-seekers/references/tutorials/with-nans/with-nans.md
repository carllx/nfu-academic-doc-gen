# How To: With Nans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: Assign index = self.create_index(...)

```python
index = self.create_index(closed=closed)
```

**Verification:**
```python
assert index.hasnans is False
```

### Step 2: Assign result = index.isna(...)

```python
result = index.isna()
```

**Verification:**
```python
assert index.hasnans is True
```

### Step 3: Assign expected = np.zeros(...)

```python
expected = np.zeros(len(index), dtype=bool)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = index.notna(...)

```python
result = index.notna()
```

### Step 6: Assign expected = np.ones(...)

```python
expected = np.ones(len(index), dtype=bool)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign index = self.create_index_with_nan(...)

```python
index = self.create_index_with_nan(closed=closed)
```

**Verification:**
```python
assert index.hasnans is True
```

### Step 9: Assign result = index.isna(...)

```python
result = index.isna()
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([False, True] + [False] * (len(index) - 2))
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 12: Assign result = index.notna(...)

```python
result = index.notna()
```

### Step 13: Assign expected = np.array(...)

```python
expected = np.array([True, False] + [True] * (len(index) - 2))
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
index = self.create_index(closed=closed)
assert index.hasnans is False
result = index.isna()
expected = np.zeros(len(index), dtype=bool)
tm.assert_numpy_array_equal(result, expected)
result = index.notna()
expected = np.ones(len(index), dtype=bool)
tm.assert_numpy_array_equal(result, expected)
index = self.create_index_with_nan(closed=closed)
assert index.hasnans is True
result = index.isna()
expected = np.array([False, True] + [False] * (len(index) - 2))
tm.assert_numpy_array_equal(result, expected)
result = index.notna()
expected = np.array([True, False] + [True] * (len(index) - 2))
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:110 | Complexity: Advanced | Last updated: 2026-06-02*