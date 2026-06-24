# How To: Categorical Non Unique Monotonic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical non unique monotonic

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: n_categories
```

## Step-by-Step Guide

### Step 1: Assign left_index = CategoricalIndex(...)

```python
left_index = CategoricalIndex([0] + list(range(n_categories)))
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(range(n_categories + 1), columns=['value'], index=left_index)
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[6]], columns=['value'], index=CategoricalIndex([0], categories=list(range(n_categories))))
```

### Step 4: Assign result = merge(...)

```python
result = merge(df1, df2, how='left', left_index=True, right_index=True)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[i, 6.0] if i < 2 else [i, np.nan] for i in range(n_categories + 1)], columns=['value_x', 'value_y'], index=left_index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: n_categories

# Workflow
left_index = CategoricalIndex([0] + list(range(n_categories)))
df1 = DataFrame(range(n_categories + 1), columns=['value'], index=left_index)
df2 = DataFrame([[6]], columns=['value'], index=CategoricalIndex([0], categories=list(range(n_categories))))
result = merge(df1, df2, how='left', left_index=True, right_index=True)
expected = DataFrame([[i, 6.0] if i < 2 else [i, np.nan] for i in range(n_categories + 1)], columns=['value_x', 'value_y'], index=left_index)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_merge.py:2543 | Complexity: Intermediate | Last updated: 2026-06-02*