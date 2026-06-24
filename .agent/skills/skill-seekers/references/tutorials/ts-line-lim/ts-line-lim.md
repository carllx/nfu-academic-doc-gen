# How To: Ts Line Lim

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ts line lim

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.plotting._matplotlib.converter`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: ts, kwargs
```

## Step-by-Step Guide

### Step 1: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

**Verification:**
```python
assert xmin <= lines[0].get_data(orig=False)[0][0]
```

### Step 2: Assign ax = ts.plot(...)

```python
ax = ts.plot(ax=ax, **kwargs)
```

**Verification:**
```python
assert xmax >= lines[0].get_data(orig=False)[0][-1]
```

### Step 3: Assign unknown = ax.get_xlim(...)

```python
xmin, xmax = ax.get_xlim()
```

### Step 4: Assign lines = ax.get_lines(...)

```python
lines = ax.get_lines()
```

**Verification:**
```python
assert xmin <= lines[0].get_data(orig=False)[0][0]
```


## Complete Example

```python
# Setup
# Fixtures: ts, kwargs

# Workflow
_, ax = mpl.pyplot.subplots()
ax = ts.plot(ax=ax, **kwargs)
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= lines[0].get_data(orig=False)[0][0]
assert xmax >= lines[0].get_data(orig=False)[0][-1]
```

## Next Steps


---

*Source: test_series.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*