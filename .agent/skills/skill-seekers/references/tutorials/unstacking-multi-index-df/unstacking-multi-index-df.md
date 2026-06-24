# How To: Unstacking Multi Index Df

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstacking multi index df

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'name': ['Alice', 'Bob'], 'score': [9.5, 8], 'employed': [False, True], 'kids': [0, 0], 'gender': ['female', 'male']})
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index(['name', 'employed', 'kids', 'gender'])
```

### Step 3: Assign df = df.unstack(...)

```python
df = df.unstack(['gender'], fill_value=0)
```

### Step 4: Assign expected = df.unstack.unstack(...)

```python
expected = df.unstack('employed', fill_value=0).unstack('kids', fill_value=0)
```

### Step 5: Assign result = df.unstack(...)

```python
result = df.unstack(['employed', 'kids'], fill_value=0)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[9.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 8.0]], index=Index(['Alice', 'Bob'], name='name'), columns=MultiIndex.from_tuples([('score', 'female', False, 0), ('score', 'female', True, 0), ('score', 'male', False, 0), ('score', 'male', True, 0)], names=[None, 'gender', 'employed', 'kids']))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'name': ['Alice', 'Bob'], 'score': [9.5, 8], 'employed': [False, True], 'kids': [0, 0], 'gender': ['female', 'male']})
df = df.set_index(['name', 'employed', 'kids', 'gender'])
df = df.unstack(['gender'], fill_value=0)
expected = df.unstack('employed', fill_value=0).unstack('kids', fill_value=0)
result = df.unstack(['employed', 'kids'], fill_value=0)
expected = DataFrame([[9.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 8.0]], index=Index(['Alice', 'Bob'], name='name'), columns=MultiIndex.from_tuples([('score', 'female', False, 0), ('score', 'female', True, 0), ('score', 'male', False, 0), ('score', 'male', True, 0)], names=[None, 'gender', 'employed', 'kids']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1460 | Complexity: Intermediate | Last updated: 2026-06-02*