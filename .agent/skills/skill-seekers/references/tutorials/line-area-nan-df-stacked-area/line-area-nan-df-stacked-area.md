# How To: Line Area Nan Df Stacked Area

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line area nan df stacked area

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: idx, kwargs
```

## Step-by-Step Guide

### Step 1: Assign values1 = value

```python
values1 = [1, 2, np.nan, 3]
```

### Step 2: Assign values2 = value

```python
values2 = [3, np.nan, 2, 1]
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': values1, 'b': values2}, index=idx)
```

### Step 4: Assign expected1 = np.array(...)

```python
expected1 = np.array([1, 2, 0, 3], dtype=np.float64)
```

### Step 5: Assign expected2 = np.array(...)

```python
expected2 = np.array([3, 0, 2, 1], dtype=np.float64)
```

### Step 6: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(df.plot.area, **kwargs)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
```

### Step 8: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(df.plot.area, stacked=False)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected2)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected2)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected1 + expected2)
```


## Complete Example

```python
# Setup
# Fixtures: idx, kwargs

# Workflow
values1 = [1, 2, np.nan, 3]
values2 = [3, np.nan, 2, 1]
df = DataFrame({'a': values1, 'b': values2}, index=idx)
expected1 = np.array([1, 2, 0, 3], dtype=np.float64)
expected2 = np.array([3, 0, 2, 1], dtype=np.float64)
ax = _check_plot_works(df.plot.area, **kwargs)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
if kwargs:
    tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected2)
else:
    tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected1 + expected2)
ax = _check_plot_works(df.plot.area, stacked=False)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected1)
tm.assert_numpy_array_equal(ax.lines[1].get_ydata(), expected2)
```

## Next Steps


---

*Source: test_frame.py:604 | Complexity: Advanced | Last updated: 2026-06-02*