# How To: Apply Reduce To Dict

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply reduce to dict

## Prerequisites

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame([[1, 2], [3, 4]], columns=['c0', 'c1'], index=['i0', 'i1'])
```

### Step 2: Assign result = data.apply(...)

```python
result = data.apply(dict, axis=0)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([{'i0': 1, 'i1': 3}, {'i0': 2, 'i1': 4}], index=data.columns)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = data.apply(...)

```python
result = data.apply(dict, axis=1)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([{'c0': 1, 'c1': 2}, {'c0': 3, 'c1': 4}], index=data.index)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = DataFrame([[1, 2], [3, 4]], columns=['c0', 'c1'], index=['i0', 'i1'])
result = data.apply(dict, axis=0)
expected = Series([{'i0': 1, 'i1': 3}, {'i0': 2, 'i1': 4}], index=data.columns)
tm.assert_series_equal(result, expected)
result = data.apply(dict, axis=1)
expected = Series([{'c0': 1, 'c1': 2}, {'c0': 3, 'c1': 4}], index=data.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:416 | Complexity: Intermediate | Last updated: 2026-06-02*