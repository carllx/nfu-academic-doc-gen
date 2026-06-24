# How To: Frame Inferred

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame inferred

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.indexes.timedeltas`
- `pandas.tests.plotting.common`
- `pandas.tseries.offsets`
- `matplotlib.pyplot`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.converter`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('1/1/1987', freq='MS', periods=100)
```

### Step 2: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(idx.values, freq=None)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx)
```

### Step 4: Call _check_plot_works()

```python
_check_plot_works(df.plot)
```

### Step 5: Assign idx = unknown.union(...)

```python
idx = idx[0:40].union(idx[45:99])
```

### Step 6: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx)
```

### Step 7: Call _check_plot_works()

```python
_check_plot_works(df2.plot)
```


## Complete Example

```python
# Workflow
idx = date_range('1/1/1987', freq='MS', periods=100)
idx = DatetimeIndex(idx.values, freq=None)
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx)
_check_plot_works(df.plot)
idx = idx[0:40].union(idx[45:99])
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 3)), index=idx)
_check_plot_works(df2.plot)
```

## Next Steps


---

*Source: test_datetimelike.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*