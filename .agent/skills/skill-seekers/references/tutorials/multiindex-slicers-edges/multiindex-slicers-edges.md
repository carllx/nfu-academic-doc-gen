# How To: Multiindex Slicers Edges

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex slicers edges

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['A0'] * 5 + ['A1'] * 5 + ['A2'] * 5, 'B': ['B0', 'B0', 'B1', 'B1', 'B2'] * 3, 'DATE': ['2013-06-11', '2013-07-02', '2013-07-09', '2013-07-30', '2013-08-06', '2013-06-11', '2013-07-02', '2013-07-09', '2013-07-30', '2013-08-06', '2013-09-03', '2013-10-01', '2013-07-09', '2013-08-06', '2013-09-03'], 'VALUES': [22, 35, 14, 9, 4, 40, 18, 4, 2, 5, 1, 2, 3, 4, 2]})
```

### Step 2: Assign unknown = pd.to_datetime(...)

```python
df['DATE'] = pd.to_datetime(df['DATE'])
```

### Step 3: Assign df1 = df.set_index(...)

```python
df1 = df.set_index(['A', 'B', 'DATE'])
```

### Step 4: Assign df1 = df1.sort_index(...)

```python
df1 = df1.sort_index()
```

### Step 5: Assign result = value

```python
result = df1.loc[slice('A1'), :]
```

### Step 6: Assign expected = value

```python
expected = df1.iloc[0:10]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df1.loc[slice('A2'), :]
```

### Step 9: Assign expected = df1

```python
expected = df1
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = df1.loc[(slice(None), slice('B1', 'B2')), :]
```

### Step 12: Assign expected = value

```python
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13, 14]]
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = value

```python
result = df1.loc[(slice(None), slice(None), slice('20130702', '20130709')), :]
```

### Step 15: Assign expected = value

```python
expected = df1.iloc[[1, 2, 6, 7, 12]]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = value

```python
result = df1.loc[(slice('A2'), slice('B0')), :]
```

### Step 18: Assign expected = value

```python
expected = df1.iloc[[0, 1, 5, 6, 10, 11]]
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 20: Assign result = value

```python
result = df1.loc[(slice(None), slice('B2')), :]
```

### Step 21: Assign expected = df1

```python
expected = df1
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 23: Assign result = value

```python
result = df1.loc[(slice(None), slice('B1', 'B2'), slice('2013-08-06')), :]
```

### Step 24: Assign expected = value

```python
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13]]
```

### Step 25: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 26: Assign result = value

```python
result = df1.loc[(slice(None), slice(None), slice('20130701', '20130709')), :]
```

### Step 27: Assign expected = value

```python
expected = df1.iloc[[1, 2, 6, 7, 12]]
```

### Step 28: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['A0'] * 5 + ['A1'] * 5 + ['A2'] * 5, 'B': ['B0', 'B0', 'B1', 'B1', 'B2'] * 3, 'DATE': ['2013-06-11', '2013-07-02', '2013-07-09', '2013-07-30', '2013-08-06', '2013-06-11', '2013-07-02', '2013-07-09', '2013-07-30', '2013-08-06', '2013-09-03', '2013-10-01', '2013-07-09', '2013-08-06', '2013-09-03'], 'VALUES': [22, 35, 14, 9, 4, 40, 18, 4, 2, 5, 1, 2, 3, 4, 2]})
df['DATE'] = pd.to_datetime(df['DATE'])
df1 = df.set_index(['A', 'B', 'DATE'])
df1 = df1.sort_index()
result = df1.loc[slice('A1'), :]
expected = df1.iloc[0:10]
tm.assert_frame_equal(result, expected)
result = df1.loc[slice('A2'), :]
expected = df1
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice(None), slice('B1', 'B2')), :]
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13, 14]]
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice(None), slice(None), slice('20130702', '20130709')), :]
expected = df1.iloc[[1, 2, 6, 7, 12]]
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice('A2'), slice('B0')), :]
expected = df1.iloc[[0, 1, 5, 6, 10, 11]]
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice(None), slice('B2')), :]
expected = df1
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice(None), slice('B1', 'B2'), slice('2013-08-06')), :]
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13]]
tm.assert_frame_equal(result, expected)
result = df1.loc[(slice(None), slice(None), slice('20130701', '20130709')), :]
expected = df1.iloc[[1, 2, 6, 7, 12]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:311 | Complexity: Advanced | Last updated: 2026-06-02*