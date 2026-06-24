# How To: Area Colors Poly

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test area colors poly

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `matplotlib`
- `matplotlib.collections`
- `cycler`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((5, 5)))
```

**Verification:**
```python
assert h.get_alpha() is None
```

### Step 2: Assign ax = df.plot.area(...)

```python
ax = df.plot.area(colormap='jet')
```

### Step 3: Assign jet_colors = value

```python
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
```

### Step 4: Call _check_colors()

```python
_check_colors(ax.get_lines(), linecolors=jet_colors)
```

### Step 5: Assign poly = value

```python
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
```

### Step 6: Call _check_colors()

```python
_check_colors(poly, facecolors=jet_colors)
```

### Step 7: Assign unknown = ax.get_legend_handles_labels(...)

```python
handles, _ = ax.get_legend_handles_labels()
```

### Step 8: Call _check_colors()

```python
_check_colors(handles, facecolors=jet_colors)
```

**Verification:**
```python
assert h.get_alpha() is None
```


## Complete Example

```python
# Workflow
from matplotlib import cm
from matplotlib.collections import PolyCollection
df = DataFrame(np.random.default_rng(2).random((5, 5)))
ax = df.plot.area(colormap='jet')
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
_check_colors(ax.get_lines(), linecolors=jet_colors)
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
_check_colors(poly, facecolors=jet_colors)
handles, _ = ax.get_legend_handles_labels()
_check_colors(handles, facecolors=jet_colors)
for h in handles:
    assert h.get_alpha() is None
```

## Next Steps


---

*Source: test_frame_color.py:383 | Complexity: Advanced | Last updated: 2026-06-02*