# How To: Combine First Empty Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first empty columns

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame(columns=['a', 'b'])
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame(columns=['a', 'c'])
```

### Step 3: Assign result = left.combine_first(...)

```python
result = left.combine_first(right)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame(columns=['a', 'b'])
right = DataFrame(columns=['a', 'c'])
result = left.combine_first(right)
expected = DataFrame(columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:551 | Complexity: Intermediate | Last updated: 2026-06-02*