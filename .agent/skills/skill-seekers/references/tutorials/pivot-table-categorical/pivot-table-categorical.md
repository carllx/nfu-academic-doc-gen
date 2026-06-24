# How To: Pivot Table Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`


## Step-by-Step Guide

### Step 1: Assign cat1 = Categorical(...)

```python
cat1 = Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b', 'z'], ordered=True)
```

### Step 2: Assign cat2 = Categorical(...)

```python
cat2 = Categorical(['c', 'd', 'c', 'd'], categories=['c', 'd', 'y'], ordered=True)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': cat1, 'B': cat2, 'values': [1, 2, 3, 4]})
```

### Step 4: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 5: Assign exp_index = MultiIndex.from_arrays(...)

```python
exp_index = MultiIndex.from_arrays([cat1, cat2], names=['A', 'B'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'values': [1.0, 2.0, 3.0, 4.0]}, index=exp_index)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = pivot_table(...)

```python
result = pivot_table(df, values='values', index=['A', 'B'], dropna=True)
```


## Complete Example

```python
# Workflow
cat1 = Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b', 'z'], ordered=True)
cat2 = Categorical(['c', 'd', 'c', 'd'], categories=['c', 'd', 'y'], ordered=True)
df = DataFrame({'A': cat1, 'B': cat2, 'values': [1, 2, 3, 4]})
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = pivot_table(df, values='values', index=['A', 'B'], dropna=True)
exp_index = MultiIndex.from_arrays([cat1, cat2], names=['A', 'B'])
expected = DataFrame({'values': [1.0, 2.0, 3.0, 4.0]}, index=exp_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:198 | Complexity: Advanced | Last updated: 2026-06-02*