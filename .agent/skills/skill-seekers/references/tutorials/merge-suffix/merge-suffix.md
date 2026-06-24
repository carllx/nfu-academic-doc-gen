# How To: Merge Suffix

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge suffix

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: col1, col2, kwargs, expected_cols
```

## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame({col1: [1, 2, 3]})
```

### Step 2: Assign b = DataFrame(...)

```python
b = DataFrame({col2: [4, 5, 6]})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=expected_cols)
```

### Step 4: Assign result = a.merge(...)

```python
result = a.merge(b, left_index=True, right_index=True, **kwargs)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = merge(...)

```python
result = merge(a, b, left_index=True, right_index=True, **kwargs)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: col1, col2, kwargs, expected_cols

# Workflow
a = DataFrame({col1: [1, 2, 3]})
b = DataFrame({col2: [4, 5, 6]})
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=expected_cols)
result = a.merge(b, left_index=True, right_index=True, **kwargs)
tm.assert_frame_equal(result, expected)
result = merge(a, b, left_index=True, right_index=True, **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2331 | Complexity: Intermediate | Last updated: 2026-06-02*