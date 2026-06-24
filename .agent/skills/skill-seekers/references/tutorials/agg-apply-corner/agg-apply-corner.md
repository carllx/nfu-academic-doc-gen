# How To: Agg Apply Corner

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg apply corner

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: ts, tsframe
```

## Step-by-Step Guide

### Step 1: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(ts * np.nan, group_keys=False)
```

**Verification:**
```python
assert ts.dtype == np.float64
```

### Step 2: Assign exp = Series(...)

```python
exp = Series([], dtype=np.float64, index=Index([], dtype=np.float64))
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.sum(), exp)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.agg('sum'), exp)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.apply('sum'), exp, check_index_type=False)
```

### Step 6: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby(tsframe['A'] * np.nan, group_keys=False)
```

### Step 7: Assign exp_df = DataFrame(...)

```python
exp_df = DataFrame(columns=tsframe.columns, dtype=float, index=Index([], name='A', dtype=np.float64))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.sum(), exp_df)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.agg('sum'), exp_df)
```

### Step 10: Assign msg = 'The behavior of DataFrame.sum with axis=None is deprecated'

```python
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp_df)
```

### Step 12: Assign res = grouped.apply(...)

```python
res = grouped.apply(np.sum)
```


## Complete Example

```python
# Setup
# Fixtures: ts, tsframe

# Workflow
grouped = ts.groupby(ts * np.nan, group_keys=False)
assert ts.dtype == np.float64
exp = Series([], dtype=np.float64, index=Index([], dtype=np.float64))
tm.assert_series_equal(grouped.sum(), exp)
tm.assert_series_equal(grouped.agg('sum'), exp)
tm.assert_series_equal(grouped.apply('sum'), exp, check_index_type=False)
grouped = tsframe.groupby(tsframe['A'] * np.nan, group_keys=False)
exp_df = DataFrame(columns=tsframe.columns, dtype=float, index=Index([], name='A', dtype=np.float64))
tm.assert_frame_equal(grouped.sum(), exp_df)
tm.assert_frame_equal(grouped.agg('sum'), exp_df)
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg, check_stacklevel=False):
    res = grouped.apply(np.sum)
tm.assert_frame_equal(res, exp_df)
```

## Next Steps


---

*Source: test_aggregate.py:136 | Complexity: Advanced | Last updated: 2026-06-02*