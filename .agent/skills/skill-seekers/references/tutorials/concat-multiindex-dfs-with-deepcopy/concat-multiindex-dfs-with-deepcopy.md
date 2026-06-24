# How To: Concat Multiindex Dfs With Deepcopy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex dfs with deepcopy

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

### Step 1: Assign example_multiindex1 = MultiIndex.from_product(...)

```python
example_multiindex1 = MultiIndex.from_product([['a'], ['b']])
```

### Step 2: Assign example_dataframe1 = DataFrame(...)

```python
example_dataframe1 = DataFrame([0], index=example_multiindex1)
```

### Step 3: Assign example_multiindex2 = MultiIndex.from_product(...)

```python
example_multiindex2 = MultiIndex.from_product([['a'], ['c']])
```

### Step 4: Assign example_dataframe2 = DataFrame(...)

```python
example_dataframe2 = DataFrame([1], index=example_multiindex2)
```

### Step 5: Assign example_dict = value

```python
example_dict = {'s1': example_dataframe1, 's2': example_dataframe2}
```

### Step 6: Assign expected_index = MultiIndex(...)

```python
expected_index = MultiIndex(levels=[['s1', 's2'], ['a'], ['b', 'c']], codes=[[0, 1], [0, 0], [0, 1]], names=['testname', None, None])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0], [1]], index=expected_index)
```

### Step 8: Assign result_copy = concat(...)

```python
result_copy = concat(deepcopy(example_dict), names=['testname'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_copy, expected)
```

### Step 10: Assign result_no_copy = concat(...)

```python
result_no_copy = concat(example_dict, names=['testname'])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_no_copy, expected)
```


## Complete Example

```python
# Workflow
example_multiindex1 = MultiIndex.from_product([['a'], ['b']])
example_dataframe1 = DataFrame([0], index=example_multiindex1)
example_multiindex2 = MultiIndex.from_product([['a'], ['c']])
example_dataframe2 = DataFrame([1], index=example_multiindex2)
example_dict = {'s1': example_dataframe1, 's2': example_dataframe2}
expected_index = MultiIndex(levels=[['s1', 's2'], ['a'], ['b', 'c']], codes=[[0, 1], [0, 0], [0, 1]], names=['testname', None, None])
expected = DataFrame([[0], [1]], index=expected_index)
result_copy = concat(deepcopy(example_dict), names=['testname'])
tm.assert_frame_equal(result_copy, expected)
result_no_copy = concat(example_dict, names=['testname'])
tm.assert_frame_equal(result_no_copy, expected)
```

## Next Steps


---

*Source: test_index.py:257 | Complexity: Advanced | Last updated: 2026-06-02*