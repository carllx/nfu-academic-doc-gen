# How To: Join Multi With Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join multi with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(data={'col1': [1.1, 1.2]}, index=MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2']))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data={'col2': [2.1, 2.2]}, index=MultiIndex.from_product([['A'], [np.nan, 2.0]], names=['id1', 'id2']))
```

### Step 3: Assign result = df1.join(...)

```python
result = df1.join(df2)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data={'col1': [1.1, 1.2], 'col2': [np.nan, 2.2]}, index=MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2']))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(data={'col1': [1.1, 1.2]}, index=MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2']))
df2 = DataFrame(data={'col2': [2.1, 2.2]}, index=MultiIndex.from_product([['A'], [np.nan, 2.0]], names=['id1', 'id2']))
result = df1.join(df2)
expected = DataFrame(data={'col1': [1.1, 1.2], 'col2': [np.nan, 2.2]}, index=MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*