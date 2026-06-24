# How To: Getitem

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: Assign idx = IntervalIndex.from_arrays(...)

```python
idx = IntervalIndex.from_arrays((0, 1, np.nan), (1, 2, np.nan), closed=closed)
```

**Verification:**
```python
assert idx[0] == Interval(0.0, 1.0, closed=closed)
```

### Step 2: Assign result = value

```python
result = idx[0:1]
```

**Verification:**
```python
assert idx[1] == Interval(1.0, 2.0, closed=closed)
```

### Step 3: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays((0.0,), (1.0,), closed=closed)
```

**Verification:**
```python
assert isna(idx[2])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = idx[0:2]
```

### Step 6: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays((0.0, 1), (1.0, 2.0), closed=closed)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = idx[1:3]
```

### Step 9: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays((1.0, np.nan), (2.0, np.nan), closed=closed)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
idx = IntervalIndex.from_arrays((0, 1, np.nan), (1, 2, np.nan), closed=closed)
assert idx[0] == Interval(0.0, 1.0, closed=closed)
assert idx[1] == Interval(1.0, 2.0, closed=closed)
assert isna(idx[2])
result = idx[0:1]
expected = IntervalIndex.from_arrays((0.0,), (1.0,), closed=closed)
tm.assert_index_equal(result, expected)
result = idx[0:2]
expected = IntervalIndex.from_arrays((0.0, 1), (1.0, 2.0), closed=closed)
tm.assert_index_equal(result, expected)
result = idx[1:3]
expected = IntervalIndex.from_arrays((1.0, np.nan), (2.0, np.nan), closed=closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:30 | Complexity: Advanced | Last updated: 2026-06-02*