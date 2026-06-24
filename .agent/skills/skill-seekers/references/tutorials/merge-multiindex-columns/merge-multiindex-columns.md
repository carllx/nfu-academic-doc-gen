# How To: Merge Multiindex Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge multiindex columns

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign letters = value

```python
letters = ['a', 'b', 'c', 'd']
```

### Step 2: Assign numbers = value

```python
numbers = ['1', '2', '3']
```

### Step 3: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product((letters, numbers), names=['outer', 'inner'])
```

### Step 4: Assign frame_x = DataFrame(...)

```python
frame_x = DataFrame(columns=index)
```

### Step 5: Assign unknown = ''

```python
frame_x['id'] = ''
```

### Step 6: Assign frame_y = DataFrame(...)

```python
frame_y = DataFrame(columns=index)
```

### Step 7: Assign unknown = ''

```python
frame_y['id'] = ''
```

### Step 8: Assign l_suf = '_x'

```python
l_suf = '_x'
```

### Step 9: Assign r_suf = '_y'

```python
r_suf = '_y'
```

### Step 10: Assign result = frame_x.merge(...)

```python
result = frame_x.merge(frame_y, on='id', suffixes=(l_suf, r_suf))
```

### Step 11: Assign tuples = value

```python
tuples = [(letter + l_suf, num) for letter in letters for num in numbers]
```

### Step 12: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples(tuples, names=['outer', 'inner'])
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=expected_index)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Workflow
letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3']
index = MultiIndex.from_product((letters, numbers), names=['outer', 'inner'])
frame_x = DataFrame(columns=index)
frame_x['id'] = ''
frame_y = DataFrame(columns=index)
frame_y['id'] = ''
l_suf = '_x'
r_suf = '_y'
result = frame_x.merge(frame_y, on='id', suffixes=(l_suf, r_suf))
tuples = [(letter + l_suf, num) for letter in letters for num in numbers]
tuples += [('id', '')]
tuples += [(letter + r_suf, num) for letter in letters for num in numbers]
expected_index = MultiIndex.from_tuples(tuples, names=['outer', 'inner'])
expected = DataFrame(columns=expected_index)
tm.assert_frame_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_merge.py:2495 | Complexity: Advanced | Last updated: 2026-06-02*