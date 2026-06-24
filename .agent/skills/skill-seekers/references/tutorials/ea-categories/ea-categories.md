# How To: Ea Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ea categories

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 0, 0, 1], 'b': [0, 1, 0, 0], 'c': [0, 0, 1, 0]})
```

### Step 2: Assign df.columns = df.columns.astype(...)

```python
df.columns = df.columns.astype('string[python]')
```

### Step 3: Assign result = from_dummies(...)

```python
result = from_dummies(df)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'': Series(list('abca'), dtype='string[python]')})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 0, 0, 1], 'b': [0, 1, 0, 0], 'c': [0, 0, 1, 0]})
df.columns = df.columns.astype('string[python]')
result = from_dummies(df)
expected = DataFrame({'': Series(list('abca'), dtype='string[python]')})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_dummies.py:410 | Complexity: Intermediate | Last updated: 2026-06-02*