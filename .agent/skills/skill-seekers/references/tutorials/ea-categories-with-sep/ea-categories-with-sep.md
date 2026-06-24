# How To: Ea Categories With Sep

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ea categories with sep

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col1_a': [1, 0, 1], 'col1_b': [0, 1, 0], 'col2_a': [0, 1, 0], 'col2_b': [1, 0, 0], 'col2_c': [0, 0, 1]})
```

### Step 2: Assign df.columns = df.columns.astype(...)

```python
df.columns = df.columns.astype('string[python]')
```

### Step 3: Assign result = from_dummies(...)

```python
result = from_dummies(df, sep='_')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': Series(list('aba'), dtype='string[python]'), 'col2': Series(list('bac'), dtype='string[python]')})
```

### Step 5: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype('string[python]')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'col1_a': [1, 0, 1], 'col1_b': [0, 1, 0], 'col2_a': [0, 1, 0], 'col2_b': [1, 0, 0], 'col2_c': [0, 0, 1]})
df.columns = df.columns.astype('string[python]')
result = from_dummies(df, sep='_')
expected = DataFrame({'col1': Series(list('aba'), dtype='string[python]'), 'col2': Series(list('bac'), dtype='string[python]')})
expected.columns = expected.columns.astype('string[python]')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_dummies.py:419 | Complexity: Intermediate | Last updated: 2026-06-02*