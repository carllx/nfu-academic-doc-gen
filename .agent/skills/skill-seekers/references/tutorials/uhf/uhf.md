# How To: Uhf

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test uhf

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
idx = date_range('2012-6-22 21:59:51.960928', freq='ms', periods=500)
```

**Verification:**
```python
assert xp == rs
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
```

### Step 3: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 4: Call df.plot()

```python
df.plot(ax=ax)
```

### Step 5: Assign axis = ax.get_xaxis(...)

```python
axis = ax.get_xaxis()
```

### Step 6: Assign tlocs = axis.get_ticklocs(...)

```python
tlocs = axis.get_ticklocs()
```

### Step 7: Assign tlabels = axis.get_ticklabels(...)

```python
tlabels = axis.get_ticklabels()
```

### Step 8: Assign xp = conv._from_ordinal.strftime(...)

```python
xp = conv._from_ordinal(loc).strftime('%H:%M:%S.%f')
```

### Step 9: Assign rs = str(...)

```python
rs = str(label.get_text())
```

**Verification:**
```python
assert xp == rs
```


## Complete Example

```python
# Workflow
import pandas.plotting._matplotlib.converter as conv
idx = date_range('2012-6-22 21:59:51.960928', freq='ms', periods=500)
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
_, ax = mpl.pyplot.subplots()
df.plot(ax=ax)
axis = ax.get_xaxis()
tlocs = axis.get_ticklocs()
tlabels = axis.get_ticklabels()
for loc, label in zip(tlocs, tlabels):
    xp = conv._from_ordinal(loc).strftime('%H:%M:%S.%f')
    rs = str(label.get_text())
    if len(rs):
        assert xp == rs
```

## Next Steps


---

*Source: test_datetimelike.py:297 | Complexity: Advanced | Last updated: 2026-06-02*