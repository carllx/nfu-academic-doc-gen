# How To: Loc Listlike Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc listlike dtypes

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
index = CategoricalIndex(['a', 'b', 'c'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
```

### Step 3: Assign res = value

```python
res = df.loc[['a', 'b']]
```

### Step 4: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(['a', 'b'], categories=index.categories)
```

### Step 5: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [1, 2], 'B': [4, 5]}, index=exp_index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True)
```

### Step 7: Assign res = value

```python
res = df.loc[['a', 'a', 'b']]
```

### Step 8: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(['a', 'a', 'b'], categories=index.categories)
```

### Step 9: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': [1, 1, 2], 'B': [4, 4, 5]}, index=exp_index)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp, check_index_type=True)
```

### Step 11: df.loc[['a', 'x']]

```python
df.loc[['a', 'x']]
```


## Complete Example

```python
# Workflow
index = CategoricalIndex(['a', 'b', 'c'])
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=index)
res = df.loc[['a', 'b']]
exp_index = CategoricalIndex(['a', 'b'], categories=index.categories)
exp = DataFrame({'A': [1, 2], 'B': [4, 5]}, index=exp_index)
tm.assert_frame_equal(res, exp, check_index_type=True)
res = df.loc[['a', 'a', 'b']]
exp_index = CategoricalIndex(['a', 'a', 'b'], categories=index.categories)
exp = DataFrame({'A': [1, 1, 2], 'B': [4, 4, 5]}, index=exp_index)
tm.assert_frame_equal(res, exp, check_index_type=True)
with pytest.raises(KeyError, match=re.escape("['x'] not in index")):
    df.loc[['a', 'x']]
```

## Next Steps


---

*Source: test_categorical.py:328 | Complexity: Advanced | Last updated: 2026-06-02*