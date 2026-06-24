# How To: Partial String Timestamp Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial string timestamp multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign df_swap = df.swaplevel.sort_index(...)

```python
df_swap = df.swaplevel(0, 1).sort_index()
```

### Step 2: Assign SLC = IndexSlice

```python
SLC = IndexSlice
```

### Step 3: Assign result = value

```python
result = df.loc[SLC['2016-01-01':'2016-02-01', :], :]
```

### Step 4: Assign expected = df

```python
expected = df
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = df_swap.loc[SLC[:, '2016-01-01':'2016-01-01'], :]
```

### Step 7: Assign expected = value

```python
expected = df_swap.iloc[[0, 1, 5, 6, 10, 11]]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = df.loc['2016']
```

### Step 10: Assign expected = df

```python
expected = df
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = df.loc['2016-01-01']
```

### Step 13: Assign expected = value

```python
expected = df.iloc[0:6]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign result = value

```python
result = df.loc['2016-01-02 12']
```

### Step 16: Assign expected = unknown.droplevel(...)

```python
expected = df.iloc[9:12].droplevel(0)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = value

```python
result = df_swap.loc[SLC[:, '2016-01-02'], :]
```

### Step 19: Assign expected = value

```python
expected = df_swap.iloc[[2, 3, 7, 8, 12, 13]]
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 21: Assign result = value

```python
result = df.loc[('2016-01-01', 'a'), :]
```

### Step 22: Assign expected = value

```python
expected = df.iloc[[0, 3]]
```

### Step 23: Assign expected = unknown.droplevel(...)

```python
expected = df.iloc[[0, 3]].droplevel(1)
```

### Step 24: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 25: df_swap.loc['2016-01-01']

```python
df_swap.loc['2016-01-01']
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
df_swap = df.swaplevel(0, 1).sort_index()
SLC = IndexSlice
result = df.loc[SLC['2016-01-01':'2016-02-01', :], :]
expected = df
tm.assert_frame_equal(result, expected)
result = df_swap.loc[SLC[:, '2016-01-01':'2016-01-01'], :]
expected = df_swap.iloc[[0, 1, 5, 6, 10, 11]]
tm.assert_frame_equal(result, expected)
result = df.loc['2016']
expected = df
tm.assert_frame_equal(result, expected)
result = df.loc['2016-01-01']
expected = df.iloc[0:6]
tm.assert_frame_equal(result, expected)
result = df.loc['2016-01-02 12']
expected = df.iloc[9:12].droplevel(0)
tm.assert_frame_equal(result, expected)
result = df_swap.loc[SLC[:, '2016-01-02'], :]
expected = df_swap.iloc[[2, 3, 7, 8, 12, 13]]
tm.assert_frame_equal(result, expected)
result = df.loc[('2016-01-01', 'a'), :]
expected = df.iloc[[0, 3]]
expected = df.iloc[[0, 3]].droplevel(1)
tm.assert_frame_equal(result, expected)
with pytest.raises(KeyError, match="'2016-01-01'"):
    df_swap.loc['2016-01-01']
```

## Next Steps


---

*Source: test_partial_indexing.py:85 | Complexity: Advanced | Last updated: 2026-06-02*