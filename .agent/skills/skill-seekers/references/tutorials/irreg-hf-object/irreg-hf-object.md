# How To: Irreg Hf Object

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test irreg hf object

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
idx = date_range('2012-6-22 21:59:51', freq='s', periods=10)
```

**Verification:**
```python
assert (np.fabs(diffs[1:] - sec) < 1e-08).all()
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
```

### Step 3: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 4: Assign df2.index = df2.index.astype(...)

```python
df2.index = df2.index.astype(object)
```

### Step 5: Call df2.plot()

```python
df2.plot(ax=ax)
```

### Step 6: Assign diffs = Series.diff(...)

```python
diffs = Series(ax.get_lines()[0].get_xydata()[:, 0]).diff()
```

### Step 7: Assign sec = value

```python
sec = 1.0 / 24 / 60 / 60
```

**Verification:**
```python
assert (np.fabs(diffs[1:] - sec) < 1e-08).all()
```


## Complete Example

```python
# Workflow
idx = date_range('2012-6-22 21:59:51', freq='s', periods=10)
df2 = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
_, ax = mpl.pyplot.subplots()
df2.index = df2.index.astype(object)
df2.plot(ax=ax)
diffs = Series(ax.get_lines()[0].get_xydata()[:, 0]).diff()
sec = 1.0 / 24 / 60 / 60
assert (np.fabs(diffs[1:] - sec) < 1e-08).all()
```

## Next Steps


---

*Source: test_datetimelike.py:331 | Complexity: Intermediate | Last updated: 2026-06-02*