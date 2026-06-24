# How To: No Pairwise With Self

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test no pairwise with self

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
tm.assert_index_equal(result.index, pairwise_frames.index)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, pairwise_frames.columns)
```

### Step 4: Assign expected = f(...)

```python
expected = f(pairwise_target_frame)
```

### Step 5: Assign result = value

```python
result = result.dropna().values
```

### Step 6: Assign expected = value

```python
expected = expected.dropna().values
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: pairwise_frames, pairwise_target_frame, f

# Workflow
result = f(pairwise_frames)
tm.assert_index_equal(result.index, pairwise_frames.index)
tm.assert_index_equal(result.columns, pairwise_frames.columns)
expected = f(pairwise_target_frame)
result = result.dropna().values
expected = expected.dropna().values
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_pairwise.py:280 | Complexity: Intermediate | Last updated: 2026-06-02*