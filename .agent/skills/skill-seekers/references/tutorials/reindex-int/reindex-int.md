# How To: Reindex Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = datetime_series[::2]
```

**Verification:**
```python
assert reindexed_int.dtype == np.float64
```

### Step 2: Assign int_ts = Series(...)

```python
int_ts = Series(np.zeros(len(ts), dtype=int), index=ts.index)
```

**Verification:**
```python
assert reindexed_int.dtype == np.dtype(int)
```

### Step 3: Assign reindexed_int = int_ts.reindex(...)

```python
reindexed_int = int_ts.reindex(datetime_series.index)
```

**Verification:**
```python
assert reindexed_int.dtype == np.float64
```

### Step 4: Assign reindexed_int = int_ts.reindex(...)

```python
reindexed_int = int_ts.reindex(int_ts.index[::2])
```

**Verification:**
```python
assert reindexed_int.dtype == np.dtype(int)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
ts = datetime_series[::2]
int_ts = Series(np.zeros(len(ts), dtype=int), index=ts.index)
reindexed_int = int_ts.reindex(datetime_series.index)
assert reindexed_int.dtype == np.float64
reindexed_int = int_ts.reindex(int_ts.index[::2])
assert reindexed_int.dtype == np.dtype(int)
```

## Next Steps


---

*Source: test_reindex.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*