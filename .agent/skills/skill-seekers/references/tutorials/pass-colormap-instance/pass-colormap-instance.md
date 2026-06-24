# How To: Pass Colormap Instance

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pass colormap instance

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `gc`
- `numpy`
- `pytest`
- `pandas`
- `matplotlib`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: df, plot_method
```

## Step-by-Step Guide

### Step 1: Assign cmap = mpl.colors.ListedColormap(...)

```python
cmap = mpl.colors.ListedColormap([[1, 1, 1], [0, 0, 0]])
```

### Step 2: Assign unknown = value

```python
df['c'] = df.A + df.B
```

### Step 3: Assign kwargs = value

```python
kwargs = {'x': 'A', 'y': 'B', 'c': 'c', 'colormap': cmap}
```

### Step 4: Call getattr()

```python
getattr(df.plot, plot_method)(**kwargs)
```

### Step 5: Assign unknown = kwargs.pop(...)

```python
kwargs['C'] = kwargs.pop('c')
```


## Complete Example

```python
# Setup
# Fixtures: df, plot_method

# Workflow
cmap = mpl.colors.ListedColormap([[1, 1, 1], [0, 0, 0]])
df['c'] = df.A + df.B
kwargs = {'x': 'A', 'y': 'B', 'c': 'c', 'colormap': cmap}
if plot_method == 'hexbin':
    kwargs['C'] = kwargs.pop('c')
getattr(df.plot, plot_method)(**kwargs)
```

## Next Steps


---

*Source: test_matplotlib.py:328 | Complexity: Intermediate | Last updated: 2026-06-02*