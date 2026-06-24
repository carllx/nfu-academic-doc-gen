# How To: Bool Aggs Dup Column Labels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bool aggs dup column labels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: bool_agg_func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[True, True]], columns=['a', 'a'])
```

### Step 2: Assign grp_by = df.groupby(...)

```python
grp_by = df.groupby([0])
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(grp_by, bool_agg_func)()
```

### Step 4: Assign expected = df.set_axis(...)

```python
expected = df.set_axis(np.array([0]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: bool_agg_func

# Workflow
df = DataFrame([[True, True]], columns=['a', 'a'])
grp_by = df.groupby([0])
result = getattr(grp_by, bool_agg_func)()
expected = df.set_axis(np.array([0]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*