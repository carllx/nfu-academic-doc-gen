# How To: No Engine Doesnt Raise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no engine doesnt raise

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [3, 2, 3, 2], 'b': range(4), 'c': range(1, 5)})
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('a')
```

### Step 3: Assign expected = gb.agg(...)

```python
expected = gb.agg({'b': 'first'})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 5: Assign res = gb.agg(...)

```python
res = gb.agg({'b': 'first'})
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [3, 2, 3, 2], 'b': range(4), 'c': range(1, 5)})
gb = df.groupby('a')
with option_context('compute.use_numba', True):
    res = gb.agg({'b': 'first'})
expected = gb.agg({'b': 'first'})
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_numba.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*