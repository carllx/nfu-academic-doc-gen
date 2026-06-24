# How To: Reindex With None In Nested Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex with none in nested multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([(('a', None), 1), (('b', None), 2)])
```

### Step 2: Assign index2 = MultiIndex.from_tuples(...)

```python
index2 = MultiIndex.from_tuples([(('b', None), 2), (('a', None), 1)])
```

### Step 3: Assign df1_dtype = pd.DataFrame(...)

```python
df1_dtype = pd.DataFrame([1, 2], index=index)
```

### Step 4: Assign df2_dtype = pd.DataFrame(...)

```python
df2_dtype = pd.DataFrame([2, 1], index=index2)
```

### Step 5: Assign result = df1_dtype.reindex_like(...)

```python
result = df1_dtype.reindex_like(df2_dtype)
```

### Step 6: Assign expected = df2_dtype

```python
expected = df2_dtype
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = MultiIndex.from_tuples([(('a', None), 1), (('b', None), 2)])
index2 = MultiIndex.from_tuples([(('b', None), 2), (('a', None), 1)])
df1_dtype = pd.DataFrame([1, 2], index=index)
df2_dtype = pd.DataFrame([2, 1], index=index2)
result = df1_dtype.reindex_like(df2_dtype)
expected = df2_dtype
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*