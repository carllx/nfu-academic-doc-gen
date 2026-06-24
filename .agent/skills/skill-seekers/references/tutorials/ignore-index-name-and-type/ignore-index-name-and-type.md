# How To: Ignore Index Name And Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ignore index name and type

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(['foo', 'bar'], dtype='category', name='baz')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [0, 1], 'y': [2, 3]}, index=index)
```

### Step 3: Assign result = melt(...)

```python
result = melt(df, ignore_index=False)
```

### Step 4: Assign expected_index = Index(...)

```python
expected_index = Index(['foo', 'bar'] * 2, dtype='category', name='baz')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'variable': ['x', 'x', 'y', 'y'], 'value': [0, 1, 2, 3]}, index=expected_index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = Index(['foo', 'bar'], dtype='category', name='baz')
df = DataFrame({'x': [0, 1], 'y': [2, 3]}, index=index)
result = melt(df, ignore_index=False)
expected_index = Index(['foo', 'bar'] * 2, dtype='category', name='baz')
expected = DataFrame({'variable': ['x', 'x', 'y', 'y'], 'value': [0, 1, 2, 3]}, index=expected_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:405 | Complexity: Intermediate | Last updated: 2026-06-02*