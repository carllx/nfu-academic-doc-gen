# How To: Line Plot Inferred Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line plot inferred freq

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('12/31/1999', freq=freq, periods=100)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).standard_normal(len(idx)), idx)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(ser.values, Index(np.asarray(ser.index)))
```

### Step 4: Call _check_plot_works()

```python
_check_plot_works(ser.plot, ser.index.inferred_freq)
```

### Step 5: Assign ser = value

```python
ser = ser.iloc[[0, 3, 5, 6]]
```

### Step 6: Call _check_plot_works()

```python
_check_plot_works(ser.plot)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
idx = date_range('12/31/1999', freq=freq, periods=100)
ser = Series(np.random.default_rng(2).standard_normal(len(idx)), idx)
ser = Series(ser.values, Index(np.asarray(ser.index)))
_check_plot_works(ser.plot, ser.index.inferred_freq)
ser = ser.iloc[[0, 3, 5, 6]]
_check_plot_works(ser.plot)
```

## Next Steps


---

*Source: test_datetimelike.py:263 | Complexity: Intermediate | Last updated: 2026-06-02*