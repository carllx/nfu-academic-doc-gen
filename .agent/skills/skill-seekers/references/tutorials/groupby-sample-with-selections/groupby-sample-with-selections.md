# How To: Groupby Sample With Selections

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby sample with selections

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [1] * 10 + [2] * 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': values, 'b': values, 'c': values})
```

### Step 3: Assign result = unknown.sample(...)

```python
result = df.groupby('a')[['b', 'c']].sample(n=None, frac=None)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [1, 2], 'c': [1, 2]}, index=result.index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
values = [1] * 10 + [2] * 10
df = DataFrame({'a': values, 'b': values, 'c': values})
result = df.groupby('a')[['b', 'c']].sample(n=None, frac=None)
expected = DataFrame({'b': [1, 2], 'c': [1, 2]}, index=result.index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*