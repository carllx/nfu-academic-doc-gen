# How To: Frame Getitem Not Sorted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame getitem not sorted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

### Step 2: Assign df = value

```python
df = frame.T
```

### Step 3: Assign unknown = 'foo'

```python
df['foo', 'four'] = 'foo'
```

### Step 4: Assign arrays = value

```python
arrays = [np.array(x) for x in zip(*df.columns.values)]
```

### Step 5: Assign result = value

```python
result = df['foo']
```

### Step 6: Assign result2 = value

```python
result2 = df.loc[:, 'foo']
```

### Step 7: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=df.columns[arrays[0] == 'foo'])
```

### Step 8: Assign expected.columns = expected.columns.droplevel(...)

```python
expected.columns = expected.columns.droplevel(0)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```

### Step 11: Assign df = value

```python
df = df.T
```

### Step 12: Assign result = df.xs(...)

```python
result = df.xs('foo')
```

### Step 13: Assign result2 = value

```python
result2 = df.loc['foo']
```

### Step 14: Assign expected = df.reindex(...)

```python
expected = df.reindex(df.index[arrays[0] == 'foo'])
```

### Step 15: Assign expected.index = expected.index.droplevel(...)

```python
expected.index = expected.index.droplevel(0)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
df = frame.T
df['foo', 'four'] = 'foo'
arrays = [np.array(x) for x in zip(*df.columns.values)]
result = df['foo']
result2 = df.loc[:, 'foo']
expected = df.reindex(columns=df.columns[arrays[0] == 'foo'])
expected.columns = expected.columns.droplevel(0)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)
df = df.T
result = df.xs('foo')
result2 = df.loc['foo']
expected = df.reindex(df.index[arrays[0] == 'foo'])
expected.index = expected.index.droplevel(0)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)
```

## Next Steps


---

*Source: test_sorted.py:115 | Complexity: Advanced | Last updated: 2026-06-02*