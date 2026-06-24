# How To: Line Area Nan Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test line area nan series

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
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [1, 2, np.nan, 3]
```

### Step 2: Assign d = Series(...)

```python
d = Series(values, index=index)
```

### Step 3: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(d.plot)
```

### Step 4: Assign masked = unknown.get_ydata(...)

```python
masked = ax.lines[0].get_ydata()
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([1, 2, 3], dtype=np.float64)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.delete(masked.data, 2), exp)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(masked.mask, np.array([False, False, True, False]))
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([1, 2, 0, 3], dtype=np.float64)
```

### Step 9: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(d.plot, stacked=True)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
```

### Step 11: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(d.plot.area)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
```

### Step 13: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(d.plot.area, stacked=False)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
values = [1, 2, np.nan, 3]
d = Series(values, index=index)
ax = _check_plot_works(d.plot)
masked = ax.lines[0].get_ydata()
exp = np.array([1, 2, 3], dtype=np.float64)
tm.assert_numpy_array_equal(np.delete(masked.data, 2), exp)
tm.assert_numpy_array_equal(masked.mask, np.array([False, False, True, False]))
expected = np.array([1, 2, 0, 3], dtype=np.float64)
ax = _check_plot_works(d.plot, stacked=True)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
ax = _check_plot_works(d.plot.area)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
ax = _check_plot_works(d.plot.area, stacked=False)
tm.assert_numpy_array_equal(ax.lines[0].get_ydata(), expected)
```

## Next Steps


---

*Source: test_series.py:245 | Complexity: Advanced | Last updated: 2026-06-02*