# How To: Boxplot Legacy3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test boxplot legacy3

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: subplots, warn, axes_num, layout
```

## Step-by-Step Guide

### Step 1: Assign tuples = zip(...)

```python
tuples = zip(string.ascii_letters[:10], range(10))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=MultiIndex.from_tuples(tuples))
```

### Step 3: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 4: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=axes_num, layout=layout)
```

### Step 5: Assign grouped = df.unstack.groupby(...)

```python
grouped = df.unstack(level=1).groupby(level=0, axis=1)
```

### Step 6: Assign axes = _check_plot_works(...)

```python
axes = _check_plot_works(grouped.boxplot, subplots=subplots, return_type='axes')
```


## Complete Example

```python
# Setup
# Fixtures: subplots, warn, axes_num, layout

# Workflow
tuples = zip(string.ascii_letters[:10], range(10))
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=MultiIndex.from_tuples(tuples))
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = df.unstack(level=1).groupby(level=0, axis=1)
with tm.assert_produces_warning(warn, check_stacklevel=False):
    axes = _check_plot_works(grouped.boxplot, subplots=subplots, return_type='axes')
_check_axes_shape(axes, axes_num=axes_num, layout=layout)
```

## Next Steps


---

*Source: test_boxplot_method.py:458 | Complexity: Intermediate | Last updated: 2026-06-02*