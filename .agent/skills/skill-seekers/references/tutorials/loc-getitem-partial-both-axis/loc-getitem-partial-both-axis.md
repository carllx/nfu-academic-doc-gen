# How To: Loc Getitem Partial Both Axis

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc getitem partial both axis

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign iterables = value

```python
iterables = [['a', 'b'], [2, 1]]
```

### Step 2: Assign columns = MultiIndex.from_product(...)

```python
columns = MultiIndex.from_product(iterables, names=['col1', 'col2'])
```

### Step 3: Assign rows = MultiIndex.from_product(...)

```python
rows = MultiIndex.from_product(iterables, names=['row1', 'row2'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=rows, columns=columns)
```

### Step 5: Assign expected = unknown.droplevel.droplevel(...)

```python
expected = df.iloc[:2, 2:].droplevel('row1').droplevel('col1', axis=1)
```

### Step 6: Assign result = value

```python
result = df.loc['a', 'b']
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
iterables = [['a', 'b'], [2, 1]]
columns = MultiIndex.from_product(iterables, names=['col1', 'col2'])
rows = MultiIndex.from_product(iterables, names=['row1', 'row2'])
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=rows, columns=columns)
expected = df.iloc[:2, 2:].droplevel('row1').droplevel('col1', axis=1)
result = df.loc['a', 'b']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*