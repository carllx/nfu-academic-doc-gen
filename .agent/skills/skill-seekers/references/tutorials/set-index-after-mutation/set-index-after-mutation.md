# How To: Set Index After Mutation

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index after mutation

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'val': [0, 1, 2], 'key': ['a', 'b', 'c']})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'val': [1, 2]}, Index(['b', 'c'], name='key'))
```

### Step 3: Assign df2 = value

```python
df2 = df.loc[df.index.map(lambda indx: indx >= 1)]
```

### Step 4: Assign result = df2.set_index(...)

```python
result = df2.set_index('key')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'val': [0, 1, 2], 'key': ['a', 'b', 'c']})
expected = DataFrame({'val': [1, 2]}, Index(['b', 'c'], name='key'))
df2 = df.loc[df.index.map(lambda indx: indx >= 1)]
result = df2.set_index('key')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_set_index.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*