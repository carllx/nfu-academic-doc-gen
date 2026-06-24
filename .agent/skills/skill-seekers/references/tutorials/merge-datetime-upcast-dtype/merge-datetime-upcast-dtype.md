# How To: Merge Datetime Upcast Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge datetime upcast dtype

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'x': ['a', 'b', 'c'], 'y': ['1', '2', '4']})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'y': ['1', '2', '3'], 'z': pd.to_datetime(['2000', '2001', '2002'])})
```

### Step 3: Assign result = merge(...)

```python
result = merge(df1, df2, how='left', on='y')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': ['a', 'b', 'c'], 'y': ['1', '2', '4'], 'z': pd.to_datetime(['2000', '2001', 'NaT'])})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'x': ['a', 'b', 'c'], 'y': ['1', '2', '4']})
df2 = DataFrame({'y': ['1', '2', '3'], 'z': pd.to_datetime(['2000', '2001', '2002'])})
result = merge(df1, df2, how='left', on='y')
expected = DataFrame({'x': ['a', 'b', 'c'], 'y': ['1', '2', '4'], 'z': pd.to_datetime(['2000', '2001', 'NaT'])})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2525 | Complexity: Intermediate | Last updated: 2026-06-02*