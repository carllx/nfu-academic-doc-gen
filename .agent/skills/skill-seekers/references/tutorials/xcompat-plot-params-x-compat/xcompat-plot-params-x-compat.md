# How To: Xcompat Plot Params X Compat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xcompat plot params x compat

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

### Step 2: Assign unknown = False

```python
plotting.plot_params['x_compat'] = False
```

**Verification:**
```python
assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)
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

### Step 5: Assign msg = 'PeriodDtype\\[B\\] is deprecated'

```python
msg = 'PeriodDtype\\[B\\] is deprecated'
```

**Verification:**
```python
assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
plotting.plot_params['x_compat'] = False
ax = df.plot()
lines = ax.get_lines()
assert not isinstance(lines[0].get_xdata(), PeriodIndex)
msg = 'PeriodDtype\\[B\\] is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    assert isinstance(PeriodIndex(lines[0].get_xdata()), PeriodIndex)
```

## Next Steps


---

*Source: test_frame.py:400 | Complexity: Intermediate | Last updated: 2026-06-02*