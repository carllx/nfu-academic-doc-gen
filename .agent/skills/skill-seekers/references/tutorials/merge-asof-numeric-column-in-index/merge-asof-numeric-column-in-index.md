# How To: Merge Asof Numeric Column In Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof numeric column in index

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'b': [10, 11, 12]}, index=Index([1, 2, 3], name='a'))
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'c': [20, 21, 22]}, index=Index([0, 2, 3], name='a'))
```

### Step 3: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, left_on='a', right_on='a')
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1, 2, 3], 'b': [10, 11, 12], 'c': [20, 21, 22]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = pd.DataFrame({'b': [10, 11, 12]}, index=Index([1, 2, 3], name='a'))
right = pd.DataFrame({'c': [20, 21, 22]}, index=Index([0, 2, 3], name='a'))
result = merge_asof(left, right, left_on='a', right_on='a')
expected = pd.DataFrame({'a': [1, 2, 3], 'b': [10, 11, 12], 'c': [20, 21, 22]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3442 | Complexity: Intermediate | Last updated: 2026-06-02*