# How To: Merge Index Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge index types

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
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'left_data': [1, 2]}, index=index)
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'right_data': [1.0, 2.0]}, index=index)
```

### Step 3: Assign result = left.merge(...)

```python
result = left.merge(right, on=['index_col'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'left_data': [1, 2], 'right_data': [1.0, 2.0]}, index=index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
left = DataFrame({'left_data': [1, 2]}, index=index)
right = DataFrame({'right_data': [1.0, 2.0]}, index=index)
result = left.merge(right, on=['index_col'])
expected = DataFrame({'left_data': [1, 2], 'right_data': [1.0, 2.0]}, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2230 | Complexity: Intermediate | Last updated: 2026-06-02*