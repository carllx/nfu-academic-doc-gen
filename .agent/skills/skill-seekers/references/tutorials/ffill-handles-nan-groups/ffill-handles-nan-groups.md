# How To: Ffill Handles Nan Groups

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ffill handles nan groups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dropna, method, has_nan_group
```

## Step-by-Step Guide

### Step 1: Assign df_without_nan_rows = DataFrame(...)

```python
df_without_nan_rows = DataFrame([(1, 0.1), (2, 0.2)])
```

### Step 2: Assign ridx = value

```python
ridx = [-1, 0, -1, -1, 1, -1]
```

### Step 3: Assign df = df_without_nan_rows.reindex.reset_index(...)

```python
df = df_without_nan_rows.reindex(ridx).reset_index(drop=True)
```

### Step 4: Assign group_b = value

```python
group_b = np.nan if has_nan_group else 'b'
```

### Step 5: Assign unknown = pd.Series(...)

```python
df['group_col'] = pd.Series(['a'] * 3 + [group_b] * 3)
```

### Step 6: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(by='group_col', dropna=dropna)
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(grouped, method)(limit=None)
```

### Step 8: Assign expected_rows = value

```python
expected_rows = {('ffill', True, True): [-1, 0, 0, -1, -1, -1], ('ffill', True, False): [-1, 0, 0, -1, 1, 1], ('ffill', False, True): [-1, 0, 0, -1, 1, 1], ('ffill', False, False): [-1, 0, 0, -1, 1, 1], ('bfill', True, True): [0, 0, -1, -1, -1, -1], ('bfill', True, False): [0, 0, -1, 1, 1, -1], ('bfill', False, True): [0, 0, -1, 1, 1, -1], ('bfill', False, False): [0, 0, -1, 1, 1, -1]}
```

### Step 9: Assign ridx = expected_rows.get(...)

```python
ridx = expected_rows.get((method, dropna, has_nan_group))
```

### Step 10: Assign expected = df_without_nan_rows.reindex.reset_index(...)

```python
expected = df_without_nan_rows.reindex(ridx).reset_index(drop=True)
```

### Step 11: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(object)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dropna, method, has_nan_group

# Workflow
df_without_nan_rows = DataFrame([(1, 0.1), (2, 0.2)])
ridx = [-1, 0, -1, -1, 1, -1]
df = df_without_nan_rows.reindex(ridx).reset_index(drop=True)
group_b = np.nan if has_nan_group else 'b'
df['group_col'] = pd.Series(['a'] * 3 + [group_b] * 3)
grouped = df.groupby(by='group_col', dropna=dropna)
result = getattr(grouped, method)(limit=None)
expected_rows = {('ffill', True, True): [-1, 0, 0, -1, -1, -1], ('ffill', True, False): [-1, 0, 0, -1, 1, 1], ('ffill', False, True): [-1, 0, 0, -1, 1, 1], ('ffill', False, False): [-1, 0, 0, -1, 1, 1], ('bfill', True, True): [0, 0, -1, -1, -1, -1], ('bfill', True, False): [0, 0, -1, 1, 1, -1], ('bfill', False, True): [0, 0, -1, 1, 1, -1], ('bfill', False, False): [0, 0, -1, 1, 1, -1]}
ridx = expected_rows.get((method, dropna, has_nan_group))
expected = df_without_nan_rows.reindex(ridx).reset_index(drop=True)
expected.columns = expected.columns.astype(object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:114 | Complexity: Advanced | Last updated: 2026-06-02*