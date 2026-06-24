# How To: Ts Plot With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ts plot with tz

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
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert (xdata[0].hour, xdata[0].minute) == (0, 0)
```

### Step 2: Assign index = date_range(...)

```python
index = date_range('1/1/2011', periods=2, freq='h', tz=tz)
```

**Verification:**
```python
assert (xdata[-1].hour, xdata[-1].minute) == (1, 0)
```

### Step 3: Assign ts = Series(...)

```python
ts = Series([188.5, 328.25], index=index)
```

### Step 4: Call _check_plot_works()

```python
_check_plot_works(ts.plot)
```

### Step 5: Assign ax = ts.plot(...)

```python
ax = ts.plot()
```

### Step 6: Assign xdata = next.get_xdata(...)

```python
xdata = next(iter(ax.get_lines())).get_xdata()
```

**Verification:**
```python
assert (xdata[0].hour, xdata[0].minute) == (0, 0)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
index = date_range('1/1/2011', periods=2, freq='h', tz=tz)
ts = Series([188.5, 328.25], index=index)
_check_plot_works(ts.plot)
ax = ts.plot()
xdata = next(iter(ax.get_lines())).get_xdata()
assert (xdata[0].hour, xdata[0].minute) == (0, 0)
assert (xdata[-1].hour, xdata[-1].minute) == (1, 0)
```

## Next Steps


---

*Source: test_datetimelike.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*