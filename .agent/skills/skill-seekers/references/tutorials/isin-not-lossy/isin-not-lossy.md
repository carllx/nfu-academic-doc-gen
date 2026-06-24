# How To: Isin Not Lossy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin not lossy

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign val = 1666880195890293744

```python
val = 1666880195890293744
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [val], 'b': [1.0]})
```

### Step 3: Assign result = df.isin(...)

```python
result = df.isin([val])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [True], 'b': [False]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
val = 1666880195890293744
df = DataFrame({'a': [val], 'b': [1.0]})
result = df.isin([val])
expected = DataFrame({'a': [True], 'b': [False]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*