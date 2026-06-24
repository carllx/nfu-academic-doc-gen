# How To: Take Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take frame

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign indices = value

```python
indices = [1, 5, -2, 6, 3, -1]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 3: Assign out = df.take(...)

```python
out = df.take(indices)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data=df.values.take(indices, axis=0), index=df.index.take(indices), columns=df.columns)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, expected)
```


## Complete Example

```python
# Workflow
indices = [1, 5, -2, 6, 3, -1]
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
out = df.take(indices)
expected = DataFrame(data=df.values.take(indices, axis=0), index=df.index.take(indices), columns=df.columns)
tm.assert_frame_equal(out, expected)
```

## Next Steps


---

*Source: test_generic.py:446 | Complexity: Intermediate | Last updated: 2026-06-02*