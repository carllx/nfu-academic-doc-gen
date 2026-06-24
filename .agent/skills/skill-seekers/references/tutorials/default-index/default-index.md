# How To: Default Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default index

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], name='x')
```

**Verification:**
```python
assert isinstance(res.columns, pd.RangeIndex)
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6], name='y')
```

**Verification:**
```python
assert isinstance(res.columns, pd.RangeIndex)
```

### Step 3: Assign res = concat(...)

```python
res = concat([s1, s2], axis=1, ignore_index=True)
```

**Verification:**
```python
assert isinstance(res.columns, pd.RangeIndex)
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
```

### Step 6: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3])
```

### Step 7: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6])
```

### Step 8: Assign res = concat(...)

```python
res = concat([s1, s2], axis=1, ignore_index=False)
```

**Verification:**
```python
assert isinstance(res.columns, pd.RangeIndex)
```

### Step 9: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
```

### Step 10: Assign exp.columns = pd.RangeIndex(...)

```python
exp.columns = pd.RangeIndex(2)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
```

### Step 12: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1, 2], 'B': [5, 6]})
```

### Step 13: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [3, 4], 'B': [7, 8]})
```

### Step 14: Assign res = concat(...)

```python
res = concat([df1, df2], axis=0, ignore_index=True)
```

### Step 15: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], columns=['A', 'B'])
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
```

### Step 17: Assign res = concat(...)

```python
res = concat([df1, df2], axis=1, ignore_index=True)
```

### Step 18: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 5, 3, 7], [2, 6, 4, 8]])
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, 3], name='x')
s2 = Series([4, 5, 6], name='y')
res = concat([s1, s2], axis=1, ignore_index=True)
assert isinstance(res.columns, pd.RangeIndex)
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
s1 = Series([1, 2, 3])
s2 = Series([4, 5, 6])
res = concat([s1, s2], axis=1, ignore_index=False)
assert isinstance(res.columns, pd.RangeIndex)
exp = DataFrame([[1, 4], [2, 5], [3, 6]])
exp.columns = pd.RangeIndex(2)
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
df1 = DataFrame({'A': [1, 2], 'B': [5, 6]})
df2 = DataFrame({'A': [3, 4], 'B': [7, 8]})
res = concat([df1, df2], axis=0, ignore_index=True)
exp = DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]], columns=['A', 'B'])
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
res = concat([df1, df2], axis=1, ignore_index=True)
exp = DataFrame([[1, 5, 3, 7], [2, 6, 4, 8]])
tm.assert_frame_equal(res, exp, check_index_type=True, check_column_type=True)
```

## Next Steps


---

*Source: test_index.py:126 | Complexity: Advanced | Last updated: 2026-06-02*