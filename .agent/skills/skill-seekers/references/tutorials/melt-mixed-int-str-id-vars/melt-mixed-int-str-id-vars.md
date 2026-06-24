# How To: Melt Mixed Int Str Id Vars

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test melt mixed int str id vars

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
df = DataFrame({0: ['foo'], 'a': ['bar'], 'b': [1], 'd': [2]})
```

### Step 2: Assign result = melt(...)

```python
result = melt(df, id_vars=[0, 'a'], value_vars=['b', 'd'])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: ['foo'] * 2, 'a': ['bar'] * 2, 'variable': list('bd'), 'value': [1, 2]})
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected['variable'] = expected['variable'].astype(object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({0: ['foo'], 'a': ['bar'], 'b': [1], 'd': [2]})
result = melt(df, id_vars=[0, 'a'], value_vars=['b', 'd'])
expected = DataFrame({0: ['foo'] * 2, 'a': ['bar'] * 2, 'variable': list('bd'), 'value': [1, 2]})
expected['variable'] = expected['variable'].astype(object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:360 | Complexity: Intermediate | Last updated: 2026-06-02*