# How To: Xs Partial

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs partial

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data, multiindex_year_month_day_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

### Step 2: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

### Step 3: Assign result = frame.xs(...)

```python
result = frame.xs('foo')
```

### Step 4: Assign result2 = value

```python
result2 = frame.loc['foo']
```

### Step 5: Assign expected = value

```python
expected = frame.T['foo'].T
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, result2)
```

### Step 8: Assign result = ymd.xs(...)

```python
result = ymd.xs((2000, 4))
```

### Step 9: Assign expected = value

```python
expected = ymd.loc[2000, 4]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[['foo', 'bar'], ['one', 'two'], [-1, 1]], codes=[[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]])
```

### Step 12: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((8, 4)), index=index, columns=list('abcd'))
```

### Step 13: Assign result = df.xs(...)

```python
result = df.xs(('foo', 'one'))
```

### Step 14: Assign expected = value

```python
expected = df.loc['foo', 'one']
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data, multiindex_year_month_day_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
ymd = multiindex_year_month_day_dataframe_random_data
result = frame.xs('foo')
result2 = frame.loc['foo']
expected = frame.T['foo'].T
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result, result2)
result = ymd.xs((2000, 4))
expected = ymd.loc[2000, 4]
tm.assert_frame_equal(result, expected)
index = MultiIndex(levels=[['foo', 'bar'], ['one', 'two'], [-1, 1]], codes=[[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1]])
df = DataFrame(np.random.default_rng(2).standard_normal((8, 4)), index=index, columns=list('abcd'))
result = df.xs(('foo', 'one'))
expected = df.loc['foo', 'one']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial.py:42 | Complexity: Advanced | Last updated: 2026-06-02*