# How To: Getitem Iloc Generator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem iloc generator

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 2: Assign indexer = value

```python
indexer = (x for x in [1, 2])
```

### Step 3: Assign result = value

```python
result = df.iloc[indexer]
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [2, 3], 'b': [5, 6]}, index=[1, 2])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
indexer = (x for x in [1, 2])
result = df.iloc[indexer]
expected = DataFrame({'a': [2, 3], 'b': [5, 6]}, index=[1, 2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*