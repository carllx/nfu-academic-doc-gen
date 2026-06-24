# How To: Dup Columns Comparisons

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dup columns comparisons

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([[1, 2], [2, np.nan], [3, 4], [4, 4]], columns=['A', 'B'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[0, 1], [2, 4], [2, np.nan], [4, 5]], columns=['A', 'A'])
```

### Step 3: Assign msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'

```python
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
```

### Step 4: Assign df1r = df1.reindex_like(...)

```python
df1r = df1.reindex_like(df2)
```

### Step 5: Assign result = value

```python
result = df1r == df2
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[False, True], [True, False], [False, False], [True, False]], columns=['A', 'A'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: df1 == df2

```python
df1 == df2
```


## Complete Example

```python
# Workflow
df1 = DataFrame([[1, 2], [2, np.nan], [3, 4], [4, 4]], columns=['A', 'B'])
df2 = DataFrame([[0, 1], [2, 4], [2, np.nan], [4, 5]], columns=['A', 'A'])
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
with pytest.raises(ValueError, match=msg):
    df1 == df2
df1r = df1.reindex_like(df2)
result = df1r == df2
expected = DataFrame([[False, True], [True, False], [False, False], [True, False]], columns=['A', 'A'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:193 | Complexity: Advanced | Last updated: 2026-06-02*