# How To: Loc Listlike Dtypes Duplicated Categories And Codes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc listlike dtypes duplicated categories and codes

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
index = CategoricalIndex(['a', 'b', 'a'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
```

### Step 3: Assign res = value

```python
res = df.loc[['a', 'b']]
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [1, 3, 2], 'B': [4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'b']))
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
exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [4, 6, 4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b']))
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
index = CategoricalIndex(['a', 'b', 'a'])
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
res = df.loc[['a', 'b']]
exp = DataFrame({'A': [1, 3, 2], 'B': [4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'b']))
tm.assert_frame_equal(res, exp, check_index_type=True)
res = df.loc[['a', 'a', 'b']]
exp = DataFrame({'A': [1, 3, 1, 3, 2], 'B': [4, 6, 4, 6, 5]}, index=CategoricalIndex(['a', 'a', 'a', 'a', 'b']))
tm.assert_frame_equal(res, exp, check_index_type=True)
with pytest.raises(KeyError, match=re.escape("['x'] not in index")):
    df.loc[['a', 'x']]
```

## Next Steps


---

*Source: test_categorical.py:351 | Complexity: Advanced | Last updated: 2026-06-02*