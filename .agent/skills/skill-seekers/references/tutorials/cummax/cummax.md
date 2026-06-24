# How To: Cummax

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cummax

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtypes_for_minmax
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = dtypes_for_minmax[0]
```

### Step 2: Assign max_val = value

```python
max_val = dtypes_for_minmax[2]
```

### Step 3: Assign base_df = DataFrame(...)

```python
base_df = DataFrame({'A': [1, 1, 1, 1, 2, 2, 2, 2], 'B': [3, 4, 3, 2, 2, 3, 2, 1]})
```

### Step 4: Assign expected_maxs = value

```python
expected_maxs = [3, 4, 4, 4, 2, 3, 3, 3]
```

### Step 5: Assign df = base_df.astype(...)

```python
df = base_df.astype(dtype)
```

### Step 6: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame({'B': expected_maxs}).astype(dtype)
```

### Step 7: Assign result = df.groupby.cummax(...)

```python
result = df.groupby('A').cummax()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.groupby.B.apply.to_frame(...)

```python
result = df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign unknown = max_val

```python
df.loc[[2, 6], 'B'] = max_val
```

### Step 12: Assign unknown = max_val

```python
expected.loc[[2, 3, 6, 7], 'B'] = max_val
```

### Step 13: Assign result = df.groupby.cummax(...)

```python
result = df.groupby('A').cummax()
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign expected = df.groupby.B.apply.to_frame(...)

```python
expected = df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign base_df = base_df.astype(...)

```python
base_df = base_df.astype({'B': 'float'})
```

### Step 18: Assign unknown = value

```python
base_df.loc[[0, 2, 4, 6], 'B'] = np.nan
```

### Step 19: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': [np.nan, 4, np.nan, 4, np.nan, 3, np.nan, 3]})
```

### Step 20: Assign result = base_df.groupby.cummax(...)

```python
result = base_df.groupby('A').cummax()
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 22: Assign expected = base_df.groupby.B.apply.to_frame(...)

```python
expected = base_df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 24: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1], 'b': pd.to_datetime(['2001'])})
```

### Step 25: Assign expected = Series(...)

```python
expected = Series(pd.to_datetime('2001'), index=[0], name='b')
```

### Step 26: Assign result = unknown.cummax(...)

```python
result = df.groupby('a')['b'].cummax()
```

### Step 27: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 28: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 1], 'b': [2, 1, 1]})
```

### Step 29: Assign result = df.groupby.b.cummax(...)

```python
result = df.groupby('a').b.cummax()
```

### Step 30: Assign expected = Series(...)

```python
expected = Series([2, 1, 2], name='b')
```

### Step 31: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtypes_for_minmax

# Workflow
dtype = dtypes_for_minmax[0]
max_val = dtypes_for_minmax[2]
base_df = DataFrame({'A': [1, 1, 1, 1, 2, 2, 2, 2], 'B': [3, 4, 3, 2, 2, 3, 2, 1]})
expected_maxs = [3, 4, 4, 4, 2, 3, 3, 3]
df = base_df.astype(dtype)
expected = DataFrame({'B': expected_maxs}).astype(dtype)
result = df.groupby('A').cummax()
tm.assert_frame_equal(result, expected)
result = df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
tm.assert_frame_equal(result, expected)
df.loc[[2, 6], 'B'] = max_val
expected.loc[[2, 3, 6, 7], 'B'] = max_val
result = df.groupby('A').cummax()
tm.assert_frame_equal(result, expected)
expected = df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
tm.assert_frame_equal(result, expected)
base_df = base_df.astype({'B': 'float'})
base_df.loc[[0, 2, 4, 6], 'B'] = np.nan
expected = DataFrame({'B': [np.nan, 4, np.nan, 4, np.nan, 3, np.nan, 3]})
result = base_df.groupby('A').cummax()
tm.assert_frame_equal(result, expected)
expected = base_df.groupby('A', group_keys=False).B.apply(lambda x: x.cummax()).to_frame()
tm.assert_frame_equal(result, expected)
df = DataFrame({'a': [1], 'b': pd.to_datetime(['2001'])})
expected = Series(pd.to_datetime('2001'), index=[0], name='b')
result = df.groupby('a')['b'].cummax()
tm.assert_series_equal(expected, result)
df = DataFrame({'a': [1, 2, 1], 'b': [2, 1, 1]})
result = df.groupby('a').b.cummax()
expected = Series([2, 1, 2], name='b')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:164 | Complexity: Advanced | Last updated: 2026-06-02*