# How To: Loc Setitem Multiindex Timestamp

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem multiindex timestamp

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign vals = np.random.default_rng.standard_normal(...)

```python
vals = np.random.default_rng(2).standard_normal((8, 6))
```

### Step 2: Assign idx = date_range(...)

```python
idx = date_range('1/1/2000', periods=8)
```

### Step 3: Assign cols = value

```python
cols = ['A', 'B', 'C', 'D', 'E', 'F']
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame(vals, index=idx, columns=cols)
```

### Step 5: Assign unknown = value

```python
exp.loc[exp.index[1], ('A', 'B')] = np.nan
```

### Step 6: Assign unknown = value

```python
vals[1][0:2] = np.nan
```

### Step 7: Assign res = DataFrame(...)

```python
res = DataFrame(vals, index=idx, columns=cols)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
vals = np.random.default_rng(2).standard_normal((8, 6))
idx = date_range('1/1/2000', periods=8)
cols = ['A', 'B', 'C', 'D', 'E', 'F']
exp = DataFrame(vals, index=idx, columns=cols)
exp.loc[exp.index[1], ('A', 'B')] = np.nan
vals[1][0:2] = np.nan
res = DataFrame(vals, index=idx, columns=cols)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_loc.py:2996 | Complexity: Advanced | Last updated: 2026-06-02*