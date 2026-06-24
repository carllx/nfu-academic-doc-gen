# How To: Boxplot Legacy2 Return Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test boxplot legacy2 return type

## Prerequisites

**Required Modules:**
- `__future__`
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.pyplot`


## Step-by-Step Guide

### Step 1: Assign tuples = zip(...)

```python
tuples = zip(string.ascii_letters[:10], range(10))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=MultiIndex.from_tuples(tuples))
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(level=1)
```

### Step 4: Assign axes = _check_plot_works(...)

```python
axes = _check_plot_works(grouped.boxplot, subplots=False, return_type='axes')
```

### Step 5: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=1, layout=(1, 1))
```


## Complete Example

```python
# Workflow
tuples = zip(string.ascii_letters[:10], range(10))
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=MultiIndex.from_tuples(tuples))
grouped = df.groupby(level=1)
axes = _check_plot_works(grouped.boxplot, subplots=False, return_type='axes')
_check_axes_shape(axes, axes_num=1, layout=(1, 1))
```

## Next Steps


---

*Source: test_boxplot_method.py:444 | Complexity: Intermediate | Last updated: 2026-06-02*