# How To: Merge On Cat And Ext Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge on cat and ext array

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign right = DataFrame(...)

```python
right = DataFrame({'a': Series([pd.Interval(0, 1), pd.Interval(1, 2)], dtype='interval')})
```

### Step 2: Assign left = right.copy(...)

```python
left = right.copy()
```

### Step 3: Assign unknown = unknown.astype(...)

```python
left['a'] = left['a'].astype('category')
```

### Step 4: Assign result = merge(...)

```python
result = merge(left, right, how='inner', on='a')
```

### Step 5: Assign expected = right.copy(...)

```python
expected = right.copy()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
right = DataFrame({'a': Series([pd.Interval(0, 1), pd.Interval(1, 2)], dtype='interval')})
left = right.copy()
left['a'] = left['a'].astype('category')
result = merge(left, right, how='inner', on='a')
expected = right.copy()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2481 | Complexity: Intermediate | Last updated: 2026-06-02*