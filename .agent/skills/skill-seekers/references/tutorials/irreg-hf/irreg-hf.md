# How To: Irreg Hf

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test irreg hf

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
assert (np.fabs(diffs[1:] - [sec, sec * 2, sec]) < 1e-08).all()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
```

### Step 3: Assign irreg = value

```python
irreg = df.iloc[[0, 1, 3, 4]]
```

### Step 4: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 5: Call irreg.plot()

```python
irreg.plot(ax=ax)
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
assert (np.fabs(diffs[1:] - [sec, sec * 2, sec]) < 1e-08).all()
```


## Complete Example

```python
# Workflow
idx = date_range('2012-6-22 21:59:51', freq='s', periods=10)
df = DataFrame(np.random.default_rng(2).standard_normal((len(idx), 2)), index=idx)
irreg = df.iloc[[0, 1, 3, 4]]
_, ax = mpl.pyplot.subplots()
irreg.plot(ax=ax)
diffs = Series(ax.get_lines()[0].get_xydata()[:, 0]).diff()
sec = 1.0 / 24 / 60 / 60
assert (np.fabs(diffs[1:] - [sec, sec * 2, sec]) < 1e-08).all()
```

## Next Steps


---

*Source: test_datetimelike.py:317 | Complexity: Intermediate | Last updated: 2026-06-02*