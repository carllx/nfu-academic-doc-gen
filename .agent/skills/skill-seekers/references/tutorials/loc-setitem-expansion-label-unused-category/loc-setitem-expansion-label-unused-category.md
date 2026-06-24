# How To: Loc Setitem Expansion Label Unused Category

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem expansion label unused category

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df2
```

## Step-by-Step Guide

### Step 1: Assign df = df2.copy(...)

```python
df = df2.copy()
```

### Step 2: Assign unknown = 20

```python
df.loc['e'] = 20
```

### Step 3: Assign result = value

```python
result = df.loc[['a', 'b', 'e']]
```

### Step 4: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(list('aaabbe'), categories=list('cabe'), name='B')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0, 1, 5, 2, 3, 20]}, index=exp_index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df2

# Workflow
df = df2.copy()
df.loc['e'] = 20
result = df.loc[['a', 'b', 'e']]
exp_index = CategoricalIndex(list('aaabbe'), categories=list('cabe'), name='B')
expected = DataFrame({'A': [0, 1, 5, 2, 3, 20]}, index=exp_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:319 | Complexity: Intermediate | Last updated: 2026-06-02*