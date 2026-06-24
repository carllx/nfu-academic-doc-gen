# How To: Radviz Color Cmap

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test radviz color cmap

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting`
- `matplotlib`
- `pandas.plotting`
- `pandas.plotting`
- `pandas.plotting._matplotlib.style`
- `pandas.plotting._matplotlib.style`
- `matplotlib`
- `pandas.plotting._matplotlib.style`
- `matplotlib.text`
- `matplotlib.text`
- `matplotlib.text`

**Setup Required:**
```python
# Fixtures: iris
```

## Step-by-Step Guide

### Step 1: Assign df = iris

```python
df = iris
```

### Step 2: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(radviz, frame=df, class_column='Name', colormap=cm.jet)
```

### Step 3: Assign cmaps = value

```python
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df['Name'].nunique())]
```

### Step 4: Assign patches = value

```python
patches = [p for p in ax.patches[:20] if p.get_label() != '']
```

### Step 5: Call _check_colors()

```python
_check_colors(patches, facecolors=cmaps, mapping=df['Name'][:10])
```


## Complete Example

```python
# Setup
# Fixtures: iris

# Workflow
from matplotlib import cm
from pandas.plotting import radviz
df = iris
ax = _check_plot_works(radviz, frame=df, class_column='Name', colormap=cm.jet)
cmaps = [cm.jet(n) for n in np.linspace(0, 1, df['Name'].nunique())]
patches = [p for p in ax.patches[:20] if p.get_label() != '']
_check_colors(patches, facecolors=cmaps, mapping=df['Name'][:10])
```

## Next Steps


---

*Source: test_misc.py:381 | Complexity: Intermediate | Last updated: 2026-06-02*