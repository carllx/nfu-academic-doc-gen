# How To: Transform Axis 1

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform axis 1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: request, transformation_func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, index=['x', 'y'])
```

### Step 2: Assign args = get_groupby_method_args(...)

```python
args = get_groupby_method_args(transformation_func, df)
```

### Step 3: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 4: Assign warn = value

```python
warn = FutureWarning if transformation_func == 'fillna' else None
```

### Step 5: Assign msg = 'DataFrameGroupBy.fillna is deprecated'

```python
msg = 'DataFrameGroupBy.fillna is deprecated'
```

### Step 6: Assign msg = 'DataFrameGroupBy.fillna is deprecated'

```python
msg = 'DataFrameGroupBy.fillna is deprecated'
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign gb = df.groupby(...)

```python
gb = df.groupby([0, 0, 1], axis=1)
```

### Step 9: Assign result = gb.transform(...)

```python
result = gb.transform(transformation_func, *args)
```

### Step 10: Assign expected = value

```python
expected = df.T.groupby([0, 0, 1]).transform(transformation_func, *args).T
```

### Step 11: Assign unknown = unknown.astype(...)

```python
expected['b'] = expected['b'].astype('int64')
```


## Complete Example

```python
# Setup
# Fixtures: request, transformation_func

# Workflow
df = DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, index=['x', 'y'])
args = get_groupby_method_args(transformation_func, df)
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby([0, 0, 1], axis=1)
warn = FutureWarning if transformation_func == 'fillna' else None
msg = 'DataFrameGroupBy.fillna is deprecated'
with tm.assert_produces_warning(warn, match=msg):
    result = gb.transform(transformation_func, *args)
msg = 'DataFrameGroupBy.fillna is deprecated'
with tm.assert_produces_warning(warn, match=msg):
    expected = df.T.groupby([0, 0, 1]).transform(transformation_func, *args).T
if transformation_func in ['diff', 'shift']:
    expected['b'] = expected['b'].astype('int64')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:189 | Complexity: Advanced | Last updated: 2026-06-02*