# How To: Ts Area Lim Xcompat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ts area lim xcompat

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
# Fixtures: ts
```

## Step-by-Step Guide

### Step 1: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

**Verification:**
```python
assert xmin <= line[0]
```

### Step 2: Assign ax = ts.plot.area(...)

```python
ax = ts.plot.area(stacked=False, x_compat=True, ax=ax)
```

**Verification:**
```python
assert xmax >= line[-1]
```

### Step 3: Assign unknown = ax.get_xlim(...)

```python
xmin, xmax = ax.get_xlim()
```

### Step 4: Assign line = value

```python
line = ax.get_lines()[0].get_data(orig=False)[0]
```

**Verification:**
```python
assert xmin <= line[0]
```

### Step 5: Call _check_ticks_props()

```python
_check_ticks_props(ax, xrot=30)
```


## Complete Example

```python
# Setup
# Fixtures: ts

# Workflow
_, ax = mpl.pyplot.subplots()
ax = ts.plot.area(stacked=False, x_compat=True, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
_check_ticks_props(ax, xrot=30)
```

## Next Steps


---

*Source: test_series.py:153 | Complexity: Intermediate | Last updated: 2026-06-02*