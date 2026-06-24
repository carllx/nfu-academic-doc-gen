# How To: Merge Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge series

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
# Fixtures: on, left_on, right_on, left_index, right_index, nm
```

## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame({'A': [1, 2, 3, 4]}, index=MultiIndex.from_product([['a', 'b'], [0, 1]], names=['outer', 'inner']))
```

### Step 2: Assign b = Series(...)

```python
b = Series([1, 2, 3, 4], index=MultiIndex.from_product([['a', 'b'], [1, 2]], names=['outer', 'inner']), name=nm)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [2, 4], 'B': [1, 3]}, index=MultiIndex.from_product([['a', 'b'], [1]], names=['outer', 'inner']))
```

### Step 4: Assign result = merge(...)

```python
result = merge(a, b, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = 'Cannot merge a Series without a name'

```python
msg = 'Cannot merge a Series without a name'
```

### Step 7: Assign result = merge(...)

```python
result = merge(a, b, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index)
```


## Complete Example

```python
# Setup
# Fixtures: on, left_on, right_on, left_index, right_index, nm

# Workflow
a = DataFrame({'A': [1, 2, 3, 4]}, index=MultiIndex.from_product([['a', 'b'], [0, 1]], names=['outer', 'inner']))
b = Series([1, 2, 3, 4], index=MultiIndex.from_product([['a', 'b'], [1, 2]], names=['outer', 'inner']), name=nm)
expected = DataFrame({'A': [2, 4], 'B': [1, 3]}, index=MultiIndex.from_product([['a', 'b'], [1]], names=['outer', 'inner']))
if nm is not None:
    result = merge(a, b, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index)
    tm.assert_frame_equal(result, expected)
else:
    msg = 'Cannot merge a Series without a name'
    with pytest.raises(ValueError, match=msg):
        result = merge(a, b, on=on, left_on=left_on, right_on=right_on, left_index=left_index, right_index=right_index)
```

## Next Steps


---

*Source: test_merge.py:2255 | Complexity: Intermediate | Last updated: 2026-06-02*