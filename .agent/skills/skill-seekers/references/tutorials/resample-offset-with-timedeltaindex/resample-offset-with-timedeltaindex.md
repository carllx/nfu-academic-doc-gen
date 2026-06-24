# How To: Resample Offset With Timedeltaindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample offset with timedeltaindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.timedeltas`


## Step-by-Step Guide

### Step 1: Assign rng = timedelta_range(...)

```python
rng = timedelta_range(start='0s', periods=25, freq='s')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 3: Assign with_base = ts.resample.mean(...)

```python
with_base = ts.resample('2s', offset='5s').mean()
```

### Step 4: Assign without_base = ts.resample.mean(...)

```python
without_base = ts.resample('2s').mean()
```

### Step 5: Assign exp_without_base = timedelta_range(...)

```python
exp_without_base = timedelta_range(start='0s', end='25s', freq='2s')
```

### Step 6: Assign exp_with_base = timedelta_range(...)

```python
exp_with_base = timedelta_range(start='5s', end='29s', freq='2s')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(without_base.index, exp_without_base)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(with_base.index, exp_with_base)
```


## Complete Example

```python
# Workflow
rng = timedelta_range(start='0s', periods=25, freq='s')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
with_base = ts.resample('2s', offset='5s').mean()
without_base = ts.resample('2s').mean()
exp_without_base = timedelta_range(start='0s', end='25s', freq='2s')
exp_with_base = timedelta_range(start='5s', end='29s', freq='2s')
tm.assert_index_equal(without_base.index, exp_without_base)
tm.assert_index_equal(with_base.index, exp_with_base)
```

## Next Steps


---

*Source: test_timedelta.py:83 | Complexity: Advanced | Last updated: 2026-06-02*