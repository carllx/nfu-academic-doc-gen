# How To: Area Colors Stacked False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test area colors stacked false

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
assert h.get_alpha() == 0.5
```

### Step 2: Assign jet_colors = value

```python
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
```

### Step 3: Assign ax = df.plot.area(...)

```python
ax = df.plot.area(colormap=cm.jet, stacked=False)
```

### Step 4: Call _check_colors()

```python
_check_colors(ax.get_lines(), linecolors=jet_colors)
```

### Step 5: Assign poly = value

```python
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
```

### Step 6: Assign jet_with_alpha = value

```python
jet_with_alpha = [(c[0], c[1], c[2], 0.5) for c in jet_colors]
```

### Step 7: Call _check_colors()

```python
_check_colors(poly, facecolors=jet_with_alpha)
```

### Step 8: Assign unknown = ax.get_legend_handles_labels(...)

```python
handles, _ = ax.get_legend_handles_labels()
```

### Step 9: Assign linecolors = jet_with_alpha

```python
linecolors = jet_with_alpha
```

### Step 10: Call _check_colors()

```python
_check_colors(handles[:len(jet_colors)], linecolors=linecolors)
```

**Verification:**
```python
assert h.get_alpha() == 0.5
```


## Complete Example

```python
# Workflow
from matplotlib import cm
from matplotlib.collections import PolyCollection
df = DataFrame(np.random.default_rng(2).random((5, 5)))
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, len(df))]
ax = df.plot.area(colormap=cm.jet, stacked=False)
_check_colors(ax.get_lines(), linecolors=jet_colors)
poly = [o for o in ax.get_children() if isinstance(o, PolyCollection)]
jet_with_alpha = [(c[0], c[1], c[2], 0.5) for c in jet_colors]
_check_colors(poly, facecolors=jet_with_alpha)
handles, _ = ax.get_legend_handles_labels()
linecolors = jet_with_alpha
_check_colors(handles[:len(jet_colors)], linecolors=linecolors)
for h in handles:
    assert h.get_alpha() == 0.5
```

## Next Steps


---

*Source: test_frame_color.py:399 | Complexity: Advanced | Last updated: 2026-06-02*