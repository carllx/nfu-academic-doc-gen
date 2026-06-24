# How To: Cython With Timestamp And Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython with timestamp and nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: op, data
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [0, 1], 'b': [data, NaT]})
```

### Step 2: Assign index = Index(...)

```python
index = Index([0, 1], name='a')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [data, NaT]}, index=index)
```

### Step 4: Assign result = df.groupby.aggregate(...)

```python
result = df.groupby('a').aggregate(op)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: op, data

# Workflow
df = DataFrame({'a': [0, 1], 'b': [data, NaT]})
index = Index([0, 1], name='a')
expected = DataFrame({'b': [data, NaT]}, index=index)
result = df.groupby('a').aggregate(op)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_cython.py:267 | Complexity: Intermediate | Last updated: 2026-06-02*