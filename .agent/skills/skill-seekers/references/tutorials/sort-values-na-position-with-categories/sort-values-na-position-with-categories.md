# How To: Sort Values Na Position With Categories

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values na position with categories

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = ['A', 'B', 'C']
```

### Step 2: Assign category_indices = value

```python
category_indices = [0, 2, 4]
```

### Step 3: Assign list_of_nans = value

```python
list_of_nans = [np.nan, np.nan]
```

### Step 4: Assign na_indices = value

```python
na_indices = [1, 3]
```

### Step 5: Assign na_position_first = 'first'

```python
na_position_first = 'first'
```

### Step 6: Assign na_position_last = 'last'

```python
na_position_last = 'last'
```

### Step 7: Assign column_name = 'c'

```python
column_name = 'c'
```

### Step 8: Assign reversed_categories = sorted(...)

```python
reversed_categories = sorted(categories, reverse=True)
```

### Step 9: Assign reversed_category_indices = sorted(...)

```python
reversed_category_indices = sorted(category_indices, reverse=True)
```

### Step 10: Assign reversed_na_indices = sorted(...)

```python
reversed_na_indices = sorted(na_indices)
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame({column_name: Categorical(['A', np.nan, 'B', np.nan, 'C'], categories=categories, ordered=True)})
```

### Step 12: Assign result = df.sort_values(...)

```python
result = df.sort_values(by=column_name, ascending=True, na_position=na_position_first)
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({column_name: Categorical(list_of_nans + categories, categories=categories, ordered=True)}, index=na_indices + category_indices)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign result = df.sort_values(...)

```python
result = df.sort_values(by=column_name, ascending=True, na_position=na_position_last)
```

### Step 16: Assign expected = DataFrame(...)

```python
expected = DataFrame({column_name: Categorical(categories + list_of_nans, categories=categories, ordered=True)}, index=category_indices + na_indices)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = df.sort_values(...)

```python
result = df.sort_values(by=column_name, ascending=False, na_position=na_position_first)
```

### Step 19: Assign expected = DataFrame(...)

```python
expected = DataFrame({column_name: Categorical(list_of_nans + reversed_categories, categories=categories, ordered=True)}, index=reversed_na_indices + reversed_category_indices)
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 21: Assign result = df.sort_values(...)

```python
result = df.sort_values(by=column_name, ascending=False, na_position=na_position_last)
```

### Step 22: Assign expected = DataFrame(...)

```python
expected = DataFrame({column_name: Categorical(reversed_categories + list_of_nans, categories=categories, ordered=True)}, index=reversed_category_indices + reversed_na_indices)
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
categories = ['A', 'B', 'C']
category_indices = [0, 2, 4]
list_of_nans = [np.nan, np.nan]
na_indices = [1, 3]
na_position_first = 'first'
na_position_last = 'last'
column_name = 'c'
reversed_categories = sorted(categories, reverse=True)
reversed_category_indices = sorted(category_indices, reverse=True)
reversed_na_indices = sorted(na_indices)
df = DataFrame({column_name: Categorical(['A', np.nan, 'B', np.nan, 'C'], categories=categories, ordered=True)})
result = df.sort_values(by=column_name, ascending=True, na_position=na_position_first)
expected = DataFrame({column_name: Categorical(list_of_nans + categories, categories=categories, ordered=True)}, index=na_indices + category_indices)
tm.assert_frame_equal(result, expected)
result = df.sort_values(by=column_name, ascending=True, na_position=na_position_last)
expected = DataFrame({column_name: Categorical(categories + list_of_nans, categories=categories, ordered=True)}, index=category_indices + na_indices)
tm.assert_frame_equal(result, expected)
result = df.sort_values(by=column_name, ascending=False, na_position=na_position_first)
expected = DataFrame({column_name: Categorical(list_of_nans + reversed_categories, categories=categories, ordered=True)}, index=reversed_na_indices + reversed_category_indices)
tm.assert_frame_equal(result, expected)
result = df.sort_values(by=column_name, ascending=False, na_position=na_position_last)
expected = DataFrame({column_name: Categorical(reversed_categories + list_of_nans, categories=categories, ordered=True)}, index=reversed_category_indices + reversed_na_indices)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_values.py:426 | Complexity: Advanced | Last updated: 2026-06-02*