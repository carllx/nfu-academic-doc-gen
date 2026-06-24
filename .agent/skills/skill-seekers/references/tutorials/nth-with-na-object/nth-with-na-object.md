# How To: Nth With Na Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nth with na object

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
# Fixtures: index, nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, nulls_fixture]})
```

### Step 2: Assign groups = df.groupby(...)

```python
groups = df.groupby('a')
```

### Step 3: Assign result = groups.nth(...)

```python
result = groups.nth(index)
```

### Step 4: Assign expected = value

```python
expected = df.iloc[[0, 2]] if index == 0 else df.iloc[[1, 3]]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index, nulls_fixture

# Workflow
df = DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, nulls_fixture]})
groups = df.groupby('a')
result = groups.nth(index)
expected = df.iloc[[0, 2]] if index == 0 else df.iloc[[1, 3]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nth.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*