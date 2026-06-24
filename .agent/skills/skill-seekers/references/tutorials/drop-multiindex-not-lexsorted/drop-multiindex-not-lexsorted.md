# How To: Drop Multiindex Not Lexsorted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop multiindex not lexsorted

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign lexsorted_mi = MultiIndex.from_tuples(...)

```python
lexsorted_mi = MultiIndex.from_tuples([('a', ''), ('b1', 'c1'), ('b2', 'c2')], names=['b', 'c'])
```

**Verification:**
```python
assert lexsorted_df.columns._is_lexsorted()
```

### Step 2: Assign lexsorted_df = DataFrame(...)

```python
lexsorted_df = DataFrame([[1, 3, 4]], columns=lexsorted_mi)
```

**Verification:**
```python
assert not not_lexsorted_df.columns._is_lexsorted()
```

### Step 3: Assign not_lexsorted_df = DataFrame(...)

```python
not_lexsorted_df = DataFrame(columns=['a', 'b', 'c', 'd'], data=[[1, 'b1', 'c1', 3], [1, 'b2', 'c2', 4]])
```

### Step 4: Assign not_lexsorted_df = not_lexsorted_df.pivot_table(...)

```python
not_lexsorted_df = not_lexsorted_df.pivot_table(index='a', columns=['b', 'c'], values='d')
```

### Step 5: Assign not_lexsorted_df = not_lexsorted_df.reset_index(...)

```python
not_lexsorted_df = not_lexsorted_df.reset_index()
```

**Verification:**
```python
assert not not_lexsorted_df.columns._is_lexsorted()
```

### Step 6: Assign expected = lexsorted_df.drop.astype(...)

```python
expected = lexsorted_df.drop('a', axis=1).astype(float)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = not_lexsorted_df.drop(...)

```python
result = not_lexsorted_df.drop('a', axis=1)
```


## Complete Example

```python
# Workflow
lexsorted_mi = MultiIndex.from_tuples([('a', ''), ('b1', 'c1'), ('b2', 'c2')], names=['b', 'c'])
lexsorted_df = DataFrame([[1, 3, 4]], columns=lexsorted_mi)
assert lexsorted_df.columns._is_lexsorted()
not_lexsorted_df = DataFrame(columns=['a', 'b', 'c', 'd'], data=[[1, 'b1', 'c1', 3], [1, 'b2', 'c2', 4]])
not_lexsorted_df = not_lexsorted_df.pivot_table(index='a', columns=['b', 'c'], values='d')
not_lexsorted_df = not_lexsorted_df.reset_index()
assert not not_lexsorted_df.columns._is_lexsorted()
expected = lexsorted_df.drop('a', axis=1).astype(float)
with tm.assert_produces_warning(PerformanceWarning):
    result = not_lexsorted_df.drop('a', axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:170 | Complexity: Advanced | Last updated: 2026-06-02*