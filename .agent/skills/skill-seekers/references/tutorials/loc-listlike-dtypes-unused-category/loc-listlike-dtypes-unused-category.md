# How To: Loc Listlike Dtypes Unused Category

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc listlike dtypes unused category

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = CategoricalIndex(...)

```python
index = CategoricalIndex(['a', 'b', 'a', 'c'], categories=list('abcde'))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)
```

### Step 3: Assign res = value

```python
res = df.loc[['a', 'b']]
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [1, 3, 2], 'B': [5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'b'], categories=list('abcde')))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True)
```

### Step 6: Assign res = value

```python
res = df.loc[['a', 'a', 'b']]
```

### Step 7: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [5, 7, 5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b'], categories=list('abcde')))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True)
```

### Step 9: df.loc[['a', 'x']]

```python
df.loc[['a', 'x']]
```


## Complete Example

```python
# Workflow
index = CategoricalIndex(['a', 'b', 'a', 'c'], categories=list('abcde'))
df = DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)
res = df.loc[['a', 'b']]
exp = DataFrame({'A': [1, 3, 2], 'B': [5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'b'], categories=list('abcde')))
tm.assert_frame_equal(res, exp, check_index_type=True)
res = df.loc[['a', 'a', 'b']]
exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [5, 7, 5, 7, 6]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b'], categories=list('abcde')))
tm.assert_frame_equal(res, exp, check_index_type=True)
with pytest.raises(KeyError, match=re.escape("['x'] not in index")):
    df.loc[['a', 'x']]
```

## Next Steps


---

*Source: test_categorical.py:374 | Complexity: Advanced | Last updated: 2026-06-02*