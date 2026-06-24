# How To: Fake Inferred Business

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fake inferred business

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

### Step 1: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

**Verification:**
```python
assert not hasattr(ax, 'freq')
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range('2001-1-1', '2001-1-10')
```

### Step 3: Assign ts = Series(...)

```python
ts = Series(range(len(rng)), index=rng)
```

### Step 4: Assign ts = concat(...)

```python
ts = concat([ts[:3], ts[5:]])
```

### Step 5: Call ts.plot()

```python
ts.plot(ax=ax)
```

**Verification:**
```python
assert not hasattr(ax, 'freq')
```


## Complete Example

```python
# Workflow
_, ax = mpl.pyplot.subplots()
rng = date_range('2001-1-1', '2001-1-10')
ts = Series(range(len(rng)), index=rng)
ts = concat([ts[:3], ts[5:]])
ts.plot(ax=ax)
assert not hasattr(ax, 'freq')
```

## Next Steps


---

*Source: test_datetimelike.py:272 | Complexity: Intermediate | Last updated: 2026-06-02*