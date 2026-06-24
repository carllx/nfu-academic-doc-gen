# How To: Reset Index Rename

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index rename

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign result = float_frame.reset_index(...)

```python
result = float_frame.reset_index(names='new_name')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(float_frame.index.values, name='new_name')
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result['new_name'], expected)
```

### Step 4: Assign result = float_frame.reset_index(...)

```python
result = float_frame.reset_index(names=123)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(float_frame.index.values, name=123)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[123], expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
result = float_frame.reset_index(names='new_name')
expected = Series(float_frame.index.values, name='new_name')
tm.assert_series_equal(result['new_name'], expected)
result = float_frame.reset_index(names=123)
expected = Series(float_frame.index.values, name=123)
tm.assert_series_equal(result[123], expected)
```

## Next Steps


---

*Source: test_reset_index.py:731 | Complexity: Intermediate | Last updated: 2026-06-02*