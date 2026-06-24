# How To: Pairwise With Self

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pairwise with self

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: pairwise_frames, pairwise_target_frame, f
```

## Step-by-Step Guide

### Step 1: Assign result = f(...)

```python
result = f(pairwise_frames)
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index.levels[0], pairwise_frames.index, check_names=False)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(safe_sort(result.index.levels[1]), safe_sort(pairwise_frames.columns.unique()))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, pairwise_frames.columns)
```

### Step 5: Assign expected = f(...)

```python
expected = f(pairwise_target_frame)
```

### Step 6: Assign result = value

```python
result = result.dropna().values
```

### Step 7: Assign expected = value

```python
expected = expected.dropna().values
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: pairwise_frames, pairwise_target_frame, f

# Workflow
result = f(pairwise_frames)
tm.assert_index_equal(result.index.levels[0], pairwise_frames.index, check_names=False)
tm.assert_index_equal(safe_sort(result.index.levels[1]), safe_sort(pairwise_frames.columns.unique()))
tm.assert_index_equal(result.columns, pairwise_frames.columns)
expected = f(pairwise_target_frame)
result = result.dropna().values
expected = expected.dropna().values
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_pairwise.py:248 | Complexity: Advanced | Last updated: 2026-06-02*