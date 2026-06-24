# How To: Iloc Setitem Axis Argument

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test iloc setitem axis argument

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: has_ref
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[6, 'c', 10], [7, 'd', 11], [8, 'e', 12]])
```

### Step 2: Assign unknown = unknown.astype(...)

```python
df[1] = df[1].astype(object)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[6, 'c', 10], [7, 'd', 11], [5, 5, 5]])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected[1] = expected[1].astype(object)
```

### Step 5: Assign unknown = 5

```python
df.iloc(axis=0)[2] = 5
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame([[6, 'c', 10], [7, 'd', 11], [8, 'e', 12]])
```

### Step 8: Assign unknown = unknown.astype(...)

```python
df[1] = df[1].astype(object)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame([[6, 'c', 5], [7, 'd', 5], [8, 'e', 5]])
```

### Step 10: Assign unknown = unknown.astype(...)

```python
expected[1] = expected[1].astype(object)
```

### Step 11: Assign unknown = 5

```python
df.iloc(axis=1)[2] = 5
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 13: Assign view = value

```python
view = df[:]
```

### Step 14: Assign view = value

```python
view = df[:]
```


## Complete Example

```python
# Setup
# Fixtures: has_ref

# Workflow
df = DataFrame([[6, 'c', 10], [7, 'd', 11], [8, 'e', 12]])
df[1] = df[1].astype(object)
if has_ref:
    view = df[:]
expected = DataFrame([[6, 'c', 10], [7, 'd', 11], [5, 5, 5]])
expected[1] = expected[1].astype(object)
df.iloc(axis=0)[2] = 5
tm.assert_frame_equal(df, expected)
df = DataFrame([[6, 'c', 10], [7, 'd', 11], [8, 'e', 12]])
df[1] = df[1].astype(object)
if has_ref:
    view = df[:]
expected = DataFrame([[6, 'c', 5], [7, 'd', 5], [8, 'e', 5]])
expected[1] = expected[1].astype(object)
df.iloc(axis=1)[2] = 5
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_iloc.py:464 | Complexity: Advanced | Last updated: 2026-06-02*