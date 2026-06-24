# How To: Unsorted Index Lims X Y

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unsorted index lims x y

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
df = DataFrame({'y': [0.0, 1.0, 2.0, 3.0], 'z': [91.0, 90.0, 93.0, 92.0]})
```

**Verification:**
```python
assert xmin <= np.nanmin(lines[0].get_data()[0])
```

### Step 2: Assign ax = df.plot(...)

```python
ax = df.plot(x='z', y='y')
```

**Verification:**
```python
assert xmax >= np.nanmax(lines[0].get_data()[0])
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
assert xmin <= np.nanmin(lines[0].get_data()[0])
```


## Complete Example

```python
# Workflow
df = DataFrame({'y': [0.0, 1.0, 2.0, 3.0], 'z': [91.0, 90.0, 93.0, 92.0]})
ax = df.plot(x='z', y='y')
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= np.nanmin(lines[0].get_data()[0])
assert xmax >= np.nanmax(lines[0].get_data()[0])
```

## Next Steps


---

*Source: test_frame.py:484 | Complexity: Intermediate | Last updated: 2026-06-02*