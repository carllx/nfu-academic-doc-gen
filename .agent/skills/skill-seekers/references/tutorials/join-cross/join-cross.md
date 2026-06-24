# How To: Join Cross

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join cross

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: input_col, output_cols
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'a': [1, 3]})
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({input_col: [3, 4]})
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, how='cross', lsuffix='_x', rsuffix='_y')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({output_cols[0]: [1, 1, 3, 3], output_cols[1]: [3, 4, 3, 4]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: input_col, output_cols

# Workflow
left = DataFrame({'a': [1, 3]})
right = DataFrame({input_col: [3, 4]})
result = left.join(right, how='cross', lsuffix='_x', rsuffix='_y')
expected = DataFrame({output_cols[0]: [1, 1, 3, 3], output_cols[1]: [3, 4, 3, 4]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:939 | Complexity: Intermediate | Last updated: 2026-06-02*