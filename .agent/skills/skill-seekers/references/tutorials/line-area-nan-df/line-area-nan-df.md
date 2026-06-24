# How To: Line Area Nan Df

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line area nan df

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
# Fixtures: idx
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

### Step 4: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(df.plot)
```

### Step 5: Assign masked1 = unknown.get_ydata(...)

```python
masked1 = ax.lines[0].get_ydata()
```

### Step 6: Assign masked2 = unknown.get_ydata(...)

```python
masked2 = ax.lines[1].get_ydata()
```

### Step 7: Assign exp = np.array(...)

```python
exp = np.array([1, 2, 3], dtype=np.float64)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.delete(masked1.data, 2), exp)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([3, 2, 1], dtype=np.float64)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.delete(masked2.data, 1), exp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(masked1.mask, np.array([False, False, True, False]))
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(masked2.mask, np.array([False, True, False, False]))
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
values1 = [1, 2, np.nan, 3]
values2 = [3, np.nan, 2, 1]
df = DataFrame({'a': values1, 'b': values2}, index=idx)
ax = _check_plot_works(df.plot)
masked1 = ax.lines[0].get_ydata()
masked2 = ax.lines[1].get_ydata()
exp = np.array([1, 2, 3], dtype=np.float64)
tm.assert_numpy_array_equal(np.delete(masked1.data, 2), exp)
exp = np.array([3, 2, 1], dtype=np.float64)
tm.assert_numpy_array_equal(np.delete(masked2.data, 1), exp)
tm.assert_numpy_array_equal(masked1.mask, np.array([False, False, True, False]))
tm.assert_numpy_array_equal(masked2.mask, np.array([False, True, False, False]))
```

## Next Steps


---

*Source: test_frame.py:567 | Complexity: Advanced | Last updated: 2026-06-02*