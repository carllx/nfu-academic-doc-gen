# How To: Xcompat Plot Params

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xcompat plot params

## Prerequisites

**Required Modules:**
- `datetime`
- `gc`
- `itertools`
- `re`
- `string`
- `weakref`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.api`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.patches`
- `matplotlib.patches`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `mpl_toolkits.axes_grid1`
- `mpl_toolkits.axes_grid1.inset_locator`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

**Verification:**
```python
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
```

### Step 2: Assign unknown = True

```python
plotting.plot_params['xaxis.compat'] = True
```

### Step 3: Assign ax = df.plot(...)

```python
ax = df.plot()
```

### Step 4: Assign lines = ax.get_lines(...)

```python
lines = ax.get_lines()
```

**Verification:**
```python
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
```

### Step 5: Call _check_ticks_props()

```python
_check_ticks_props(ax, xrot=30)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
plotting.plot_params['xaxis.compat'] = True
ax = df.plot()
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
_check_ticks_props(ax, xrot=30)
```

## Next Steps


---

*Source: test_frame.py:388 | Complexity: Intermediate | Last updated: 2026-06-02*