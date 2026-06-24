# How To: Compare Nullable Int64 Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare nullable int64 dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df1_val, df2_val, diff_self, diff_other
```

## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'a': pd.Series([df1_val, pd.NA], dtype='Int64'), 'b': [1.0, 2]})
```

### Step 2: Assign df2 = df1.copy(...)

```python
df2 = df1.copy()
```

### Step 3: Assign unknown = df2_val

```python
df2.loc[0, 'a'] = df2_val
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({('a', 'self'): pd.Series([diff_self, pd.NA], dtype='Int64'), ('a', 'other'): pd.Series([diff_other, pd.NA], dtype='Int64'), ('b', 'self'): np.nan, ('b', 'other'): np.nan})
```

### Step 5: Assign result = df1.compare(...)

```python
result = df1.compare(df2, keep_shape=True)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df1_val, df2_val, diff_self, diff_other

# Workflow
df1 = pd.DataFrame({'a': pd.Series([df1_val, pd.NA], dtype='Int64'), 'b': [1.0, 2]})
df2 = df1.copy()
df2.loc[0, 'a'] = df2_val
expected = pd.DataFrame({('a', 'self'): pd.Series([diff_self, pd.NA], dtype='Int64'), ('a', 'other'): pd.Series([diff_other, pd.NA], dtype='Int64'), ('b', 'self'): np.nan, ('b', 'other'): np.nan})
result = df1.compare(df2, keep_shape=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:290 | Complexity: Intermediate | Last updated: 2026-06-02*