# How To: Ts Tz Area Lim Xcompat Secondary Y

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ts tz area lim xcompat secondary y

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

### Step 1: Assign tz_ts = ts.copy(...)

```python
tz_ts = ts.copy()
```

**Verification:**
```python
assert xmin <= line[0]
```

### Step 2: Assign tz_ts.index = tz_ts.tz_localize.tz_convert(...)

```python
tz_ts.index = tz_ts.tz_localize('GMT').tz_convert('CET')
```

**Verification:**
```python
assert xmax >= line[-1]
```

### Step 3: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 4: Assign ax = tz_ts.plot.area(...)

```python
ax = tz_ts.plot.area(stacked=False, secondary_y=True, ax=ax)
```

### Step 5: Assign unknown = ax.get_xlim(...)

```python
xmin, xmax = ax.get_xlim()
```

### Step 6: Assign line = value

```python
line = ax.get_lines()[0].get_data(orig=False)[0]
```

**Verification:**
```python
assert xmin <= line[0]
```

### Step 7: Call _check_ticks_props()

```python
_check_ticks_props(ax, xrot=0)
```


## Complete Example

```python
# Setup
# Fixtures: ts

# Workflow
tz_ts = ts.copy()
tz_ts.index = tz_ts.tz_localize('GMT').tz_convert('CET')
_, ax = mpl.pyplot.subplots()
ax = tz_ts.plot.area(stacked=False, secondary_y=True, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
_check_ticks_props(ax, xrot=0)
```

## Next Steps


---

*Source: test_series.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*