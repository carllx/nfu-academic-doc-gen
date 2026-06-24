# How To: Wide To Long String Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wide to long string columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: string_storage
```

## Step-by-Step Guide

### Step 1: Assign string_dtype = pd.StringDtype(...)

```python
string_dtype = pd.StringDtype(string_storage, na_value=np.nan)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'ID': {0: 1}, 'R_test1': {0: 1}, 'R_test2': {0: 1}, 'R_test3': {0: 2}, 'D': {0: 1}})
```

### Step 3: Assign df.columns = df.columns.astype(...)

```python
df.columns = df.columns.astype(string_dtype)
```

### Step 4: Assign result = wide_to_long(...)

```python
result = wide_to_long(df, stubnames='R', i='ID', j='UNPIVOTED', sep='_', suffix='.*')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1], [1, 1], [1, 2]], columns=Index(['D', 'R']), index=pd.MultiIndex.from_arrays([[1, 1, 1], Index(['test1', 'test2', 'test3'], dtype=string_dtype)], names=['ID', 'UNPIVOTED']))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: string_storage

# Workflow
string_dtype = pd.StringDtype(string_storage, na_value=np.nan)
df = DataFrame({'ID': {0: 1}, 'R_test1': {0: 1}, 'R_test2': {0: 1}, 'R_test3': {0: 2}, 'D': {0: 1}})
df.columns = df.columns.astype(string_dtype)
result = wide_to_long(df, stubnames='R', i='ID', j='UNPIVOTED', sep='_', suffix='.*')
expected = DataFrame([[1, 1], [1, 1], [1, 2]], columns=Index(['D', 'R']), index=pd.MultiIndex.from_arrays([[1, 1, 1], Index(['test1', 'test2', 'test3'], dtype=string_dtype)], names=['ID', 'UNPIVOTED']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:1231 | Complexity: Intermediate | Last updated: 2026-06-02*