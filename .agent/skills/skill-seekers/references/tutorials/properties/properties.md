# How To: Properties

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test properties

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
assert len(index) == 10
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.left, Index(np.arange(10, dtype=np.int64)))
```

**Verification:**
```python
assert index.size == 10
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.right, Index(np.arange(1, 11, dtype=np.int64)))
```

**Verification:**
```python
assert index.shape == (10,)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.mid, Index(np.arange(0.5, 10.5, dtype=np.float64)))
```

**Verification:**
```python
assert index.closed == closed
```

### Step 5: Assign ivs = value

```python
ivs = [Interval(left, right, closed) for left, right in zip(range(10), range(1, 11))]
```

**Verification:**
```python
assert len(index) == 10
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array(ivs, dtype=object)
```

**Verification:**
```python
assert index.size == 10
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.asarray(index), expected)
```

**Verification:**
```python
assert index.shape == (10,)
```

### Step 8: Assign index = self.create_index_with_nan(...)

```python
index = self.create_index_with_nan(closed=closed)
```

**Verification:**
```python
assert index.closed == closed
```

### Step 9: Assign expected_left = Index(...)

```python
expected_left = Index([0, np.nan, 2, 3, 4, 5, 6, 7, 8, 9])
```

### Step 10: Assign expected_right = value

```python
expected_right = expected_left + 1
```

### Step 11: Assign expected_mid = value

```python
expected_mid = expected_left + 0.5
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.left, expected_left)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.right, expected_right)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.mid, expected_mid)
```

**Verification:**
```python
assert index.closed == closed
```

### Step 15: Assign ivs = value

```python
ivs = [Interval(left, right, closed) if notna(left) else np.nan for left, right in zip(expected_left, expected_right)]
```

### Step 16: Assign expected = np.array(...)

```python
expected = np.array(ivs, dtype=object)
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.asarray(index), expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
index = self.create_index(closed=closed)
assert len(index) == 10
assert index.size == 10
assert index.shape == (10,)
tm.assert_index_equal(index.left, Index(np.arange(10, dtype=np.int64)))
tm.assert_index_equal(index.right, Index(np.arange(1, 11, dtype=np.int64)))
tm.assert_index_equal(index.mid, Index(np.arange(0.5, 10.5, dtype=np.float64)))
assert index.closed == closed
ivs = [Interval(left, right, closed) for left, right in zip(range(10), range(1, 11))]
expected = np.array(ivs, dtype=object)
tm.assert_numpy_array_equal(np.asarray(index), expected)
index = self.create_index_with_nan(closed=closed)
assert len(index) == 10
assert index.size == 10
assert index.shape == (10,)
expected_left = Index([0, np.nan, 2, 3, 4, 5, 6, 7, 8, 9])
expected_right = expected_left + 1
expected_mid = expected_left + 0.5
tm.assert_index_equal(index.left, expected_left)
tm.assert_index_equal(index.right, expected_right)
tm.assert_index_equal(index.mid, expected_mid)
assert index.closed == closed
ivs = [Interval(left, right, closed) if notna(left) else np.nan for left, right in zip(expected_left, expected_right)]
expected = np.array(ivs, dtype=object)
tm.assert_numpy_array_equal(np.asarray(index), expected)
```

## Next Steps


---

*Source: test_interval.py:43 | Complexity: Advanced | Last updated: 2026-06-02*