# How To: Mixed Reductions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mixed reductions

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: op, expected
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['a', 'b', 'b'], 'B': [1, None, 3], 'C': array([1, None, 3], dtype='Int64')})
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(df.C, op)()
```

### Step 3: Call tm.assert_equal()

```python
tm.assert_equal(result, expected['C'])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(df, op)()
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(df, op)(numeric_only=True)
```


## Complete Example

```python
# Setup
# Fixtures: op, expected

# Workflow
df = DataFrame({'A': ['a', 'b', 'b'], 'B': [1, None, 3], 'C': array([1, None, 3], dtype='Int64')})
result = getattr(df.C, op)()
tm.assert_equal(result, expected['C'])
if op in ['any', 'all']:
    result = getattr(df, op)()
else:
    result = getattr(df, op)(numeric_only=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reduction.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*