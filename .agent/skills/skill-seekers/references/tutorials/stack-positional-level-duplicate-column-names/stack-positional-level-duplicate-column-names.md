# How To: Stack Positional Level Duplicate Column Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stack positional level duplicate column names

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: future_stack
```

## Step-by-Step Guide

### Step 1: Assign columns = MultiIndex.from_product(...)

```python
columns = MultiIndex.from_product([('x', 'y'), ('y', 'z')], names=['a', 'a'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1, 1, 1]], columns=columns)
```

### Step 3: Assign result = df.stack(...)

```python
result = df.stack(0, future_stack=future_stack)
```

### Step 4: Assign new_columns = Index(...)

```python
new_columns = Index(['y', 'z'], name='a')
```

### Step 5: Assign new_index = MultiIndex.from_tuples(...)

```python
new_index = MultiIndex.from_tuples([(0, 'x'), (0, 'y')], names=[None, 'a'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1], [1, 1]], index=new_index, columns=new_columns)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: future_stack

# Workflow
columns = MultiIndex.from_product([('x', 'y'), ('y', 'z')], names=['a', 'a'])
df = DataFrame([[1, 1, 1, 1]], columns=columns)
result = df.stack(0, future_stack=future_stack)
new_columns = Index(['y', 'z'], name='a')
new_index = MultiIndex.from_tuples([(0, 'x'), (0, 'y')], names=[None, 'a'])
expected = DataFrame([[1, 1], [1, 1]], index=new_index, columns=new_columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1492 | Complexity: Intermediate | Last updated: 2026-06-02*