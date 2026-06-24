# How To: Cython Agg Empty Buckets

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython agg empty buckets

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
# Fixtures: op, targop, observed
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([11, 12, 13])
```

### Step 2: Assign grps = range(...)

```python
grps = range(0, 55, 5)
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby(pd.cut(df[0], grps), observed=observed)
```

### Step 4: Assign result = g._cython_agg_general(...)

```python
result = g._cython_agg_general(op, alt=None, numeric_only=True)
```

### Step 5: Assign g = df.groupby(...)

```python
g = df.groupby(pd.cut(df[0], grps), observed=observed)
```

### Step 6: Assign expected = g.agg(...)

```python
expected = g.agg(lambda x: targop(x))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op, targop, observed

# Workflow
df = DataFrame([11, 12, 13])
grps = range(0, 55, 5)
g = df.groupby(pd.cut(df[0], grps), observed=observed)
result = g._cython_agg_general(op, alt=None, numeric_only=True)
g = df.groupby(pd.cut(df[0], grps), observed=observed)
expected = g.agg(lambda x: targop(x))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:216 | Complexity: Intermediate | Last updated: 2026-06-02*