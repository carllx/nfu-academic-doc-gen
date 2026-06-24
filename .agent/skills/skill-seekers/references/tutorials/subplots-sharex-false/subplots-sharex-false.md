# How To: Subplots Sharex False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subplots sharex false

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.io.formats.printing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 2)))
```

### Step 2: Assign unknown = value

```python
df.iloc[5:, 1] = np.nan
```

### Step 3: Assign unknown = value

```python
df.iloc[:5, 0] = np.nan
```

### Step 4: Assign unknown = mpl.pyplot.subplots(...)

```python
_, axs = mpl.pyplot.subplots(2, 1)
```

### Step 5: Call df.plot.line()

```python
df.plot.line(ax=axs, subplots=True, sharex=False)
```

### Step 6: Assign expected_ax1 = np.arange(...)

```python
expected_ax1 = np.arange(4.5, 10, 0.5)
```

### Step 7: Assign expected_ax2 = np.arange(...)

```python
expected_ax2 = np.arange(-0.5, 5, 0.5)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(axs[0].get_xticks(), expected_ax1)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(axs[1].get_xticks(), expected_ax2)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random((10, 2)))
df.iloc[5:, 1] = np.nan
df.iloc[:5, 0] = np.nan
_, axs = mpl.pyplot.subplots(2, 1)
df.plot.line(ax=axs, subplots=True, sharex=False)
expected_ax1 = np.arange(4.5, 10, 0.5)
expected_ax2 = np.arange(-0.5, 5, 0.5)
tm.assert_numpy_array_equal(axs[0].get_xticks(), expected_ax1)
tm.assert_numpy_array_equal(axs[1].get_xticks(), expected_ax2)
```

## Next Steps


---

*Source: test_frame_subplots.py:531 | Complexity: Advanced | Last updated: 2026-06-02*