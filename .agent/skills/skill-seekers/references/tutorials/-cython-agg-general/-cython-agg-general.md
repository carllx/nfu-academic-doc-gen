# How To:  Cython Agg General

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test  cython agg general

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
# Fixtures: op, targop
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal(1000))
```

### Step 2: Assign labels = np.random.default_rng.integers.astype(...)

```python
labels = np.random.default_rng(2).integers(0, 50, size=1000).astype(float)
```

### Step 3: Assign result = df.groupby._cython_agg_general(...)

```python
result = df.groupby(labels)._cython_agg_general(op, alt=None, numeric_only=True)
```

### Step 4: Assign warn = value

```python
warn = FutureWarning if targop in com._cython_table else None
```

### Step 5: Assign msg = value

```python
msg = f'using DataFrameGroupBy.{op}'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = df.groupby.agg(...)

```python
expected = df.groupby(labels).agg(targop)
```


## Complete Example

```python
# Setup
# Fixtures: op, targop

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal(1000))
labels = np.random.default_rng(2).integers(0, 50, size=1000).astype(float)
result = df.groupby(labels)._cython_agg_general(op, alt=None, numeric_only=True)
warn = FutureWarning if targop in com._cython_table else None
msg = f'using DataFrameGroupBy.{op}'
with tm.assert_produces_warning(warn, match=msg):
    expected = df.groupby(labels).agg(targop)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*