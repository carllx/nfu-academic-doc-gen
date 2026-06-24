# How To: Hist With Legend

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test hist with legend

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `matplotlib.pyplot`
- `pylab`
- `matplotlib.patches`
- `pandas.plotting._matplotlib.hist`
- `matplotlib.patches`
- `pandas.plotting._matplotlib.hist`
- `pandas.plotting._matplotlib.hist`
- `pandas.plotting._matplotlib.hist`

**Setup Required:**
```python
# Fixtures: by, column
```

## Step-by-Step Guide

### Step 1: Assign expected_axes_num = value

```python
expected_axes_num = 1 if by is None and column is not None else 2
```

### Step 2: Assign expected_layout = value

```python
expected_layout = (1, expected_axes_num)
```

### Step 3: Assign expected_labels = value

```python
expected_labels = column or ['a', 'b']
```

### Step 4: Assign index = Index(...)

```python
index = Index(15 * ['1'] + 15 * ['2'], name='c')
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((30, 2)), index=index, columns=['a', 'b'])
```

### Step 6: Assign axes = _check_plot_works(...)

```python
axes = _check_plot_works(df.hist, default_axes=True, legend=True, by=by, column=column)
```

### Step 7: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
```

### Step 8: Assign expected_labels = value

```python
expected_labels = [expected_labels] * 2
```

### Step 9: Assign axes = value

```python
axes = axes[0]
```

### Step 10: Call _check_legend_labels()

```python
_check_legend_labels(ax, expected_label)
```


## Complete Example

```python
# Setup
# Fixtures: by, column

# Workflow
expected_axes_num = 1 if by is None and column is not None else 2
expected_layout = (1, expected_axes_num)
expected_labels = column or ['a', 'b']
if by is not None:
    expected_labels = [expected_labels] * 2
index = Index(15 * ['1'] + 15 * ['2'], name='c')
df = DataFrame(np.random.default_rng(2).standard_normal((30, 2)), index=index, columns=['a', 'b'])
axes = _check_plot_works(df.hist, default_axes=True, legend=True, by=by, column=column)
_check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
if by is None and column is None:
    axes = axes[0]
for expected_label, ax in zip(expected_labels, axes):
    _check_legend_labels(ax, expected_label)
```

## Next Steps


---

*Source: test_hist_method.py:513 | Complexity: Advanced | Last updated: 2026-06-02*