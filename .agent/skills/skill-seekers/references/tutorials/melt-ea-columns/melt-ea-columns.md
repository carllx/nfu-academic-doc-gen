# How To: Melt Ea Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test melt ea columns

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'}, 'B': {0: 1, 1: 3, 2: 5}, 'C': {0: 2, 1: 4, 2: 6}})
```

### Step 2: Assign df.columns = df.columns.astype(...)

```python
df.columns = df.columns.astype('string[python]')
```

### Step 3: Assign result = df.melt(...)

```python
result = df.melt(id_vars=['A'], value_vars=['B'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': list('abc'), 'variable': pd.Series(['B'] * 3, dtype='string[python]'), 'value': [1, 3, 5]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'}, 'B': {0: 1, 1: 3, 2: 5}, 'C': {0: 2, 1: 4, 2: 6}})
df.columns = df.columns.astype('string[python]')
result = df.melt(id_vars=['A'], value_vars=['B'])
expected = DataFrame({'A': list('abc'), 'variable': pd.Series(['B'] * 3, dtype='string[python]'), 'value': [1, 3, 5]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:446 | Complexity: Intermediate | Last updated: 2026-06-02*