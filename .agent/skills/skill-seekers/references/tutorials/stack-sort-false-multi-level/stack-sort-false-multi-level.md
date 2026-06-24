# How To: Stack Sort False Multi Level

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stack sort false multi level

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

### Step 1: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([('weight', 'kg'), ('height', 'm')])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1.0, 2.0], [3.0, 4.0]], index=['cat', 'dog'], columns=idx)
```

### Step 3: Assign kwargs = value

```python
kwargs = {} if future_stack else {'sort': False}
```

### Step 4: Assign result = df.stack(...)

```python
result = df.stack([0, 1], future_stack=future_stack, **kwargs)
```

### Step 5: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([('cat', 'weight', 'kg'), ('cat', 'height', 'm'), ('dog', 'weight', 'kg'), ('dog', 'height', 'm')])
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1.0, 2.0, 3.0, 4.0], index=expected_index)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: future_stack

# Workflow
idx = MultiIndex.from_tuples([('weight', 'kg'), ('height', 'm')])
df = DataFrame([[1.0, 2.0], [3.0, 4.0]], index=['cat', 'dog'], columns=idx)
kwargs = {} if future_stack else {'sort': False}
result = df.stack([0, 1], future_stack=future_stack, **kwargs)
expected_index = MultiIndex.from_tuples([('cat', 'weight', 'kg'), ('cat', 'height', 'm'), ('dog', 'weight', 'kg'), ('dog', 'height', 'm')])
expected = Series([1.0, 2.0, 3.0, 4.0], index=expected_index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1567 | Complexity: Intermediate | Last updated: 2026-06-02*