# How To: Groupby Column Index In References

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby column index in references

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['a', 'b', 'c', 'd'], 'B': [1, 2, 3, 4], 'C': ['a', 'a', 'b', 'b']})
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index('A')
```

### Step 3: Assign key = value

```python
key = df['C']
```

### Step 4: Assign result = df.groupby.sum(...)

```python
result = df.groupby(key, observed=True).sum()
```

### Step 5: Assign expected = df.groupby.sum(...)

```python
expected = df.groupby('C', observed=True).sum()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['a', 'b', 'c', 'd'], 'B': [1, 2, 3, 4], 'C': ['a', 'a', 'b', 'b']})
df = df.set_index('A')
key = df['C']
result = df.groupby(key, observed=True).sum()
expected = df.groupby('C', observed=True).sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_methods.py:288 | Complexity: Intermediate | Last updated: 2026-06-02*