# How To: Merge Asof Extension Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge asof extension dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'join_col': [1, 3, 5], 'left_val': [1, 2, 3]})
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'join_col': [2, 3, 4], 'right_val': [1, 2, 3]})
```

### Step 3: Assign left = left.astype(...)

```python
left = left.astype({'join_col': dtype})
```

### Step 4: Assign right = right.astype(...)

```python
right = right.astype({'join_col': dtype})
```

### Step 5: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, on='join_col')
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'join_col': [1, 3, 5], 'left_val': [1, 2, 3], 'right_val': [np.nan, 2.0, 3.0]})
```

### Step 7: Assign expected = expected.astype(...)

```python
expected = expected.astype({'join_col': dtype})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
left = pd.DataFrame({'join_col': [1, 3, 5], 'left_val': [1, 2, 3]})
right = pd.DataFrame({'join_col': [2, 3, 4], 'right_val': [1, 2, 3]})
left = left.astype({'join_col': dtype})
right = right.astype({'join_col': dtype})
result = merge_asof(left, right, on='join_col')
expected = pd.DataFrame({'join_col': [1, 3, 5], 'left_val': [1, 2, 3], 'right_val': [np.nan, 2.0, 3.0]})
expected = expected.astype({'join_col': dtype})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3556 | Complexity: Advanced | Last updated: 2026-06-02*