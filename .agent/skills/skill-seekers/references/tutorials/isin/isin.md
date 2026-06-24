# How To: Isin

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'], 'ids2': ['a', 'n', 'c', 'n']}, index=['foo', 'bar', 'baz', 'qux'])
```

### Step 2: Assign other = value

```python
other = ['a', 'b', 'c']
```

### Step 3: Assign result = df.isin(...)

```python
result = df.isin(other)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([df.loc[s].isin(other) for s in df.index])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'], 'ids2': ['a', 'n', 'c', 'n']}, index=['foo', 'bar', 'baz', 'qux'])
other = ['a', 'b', 'c']
result = df.isin(other)
expected = DataFrame([df.loc[s].isin(other) for s in df.index])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*