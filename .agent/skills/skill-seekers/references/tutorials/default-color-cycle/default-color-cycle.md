# How To: Default Color Cycle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default color cycle

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

### Step 1: Assign colors = list(...)

```python
colors = list('rgbk')
```

### Step 2: Assign unknown = cycler.cycler(...)

```python
plt.rcParams['axes.prop_cycle'] = cycler.cycler('color', colors)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
```

### Step 4: Assign ax = df.plot(...)

```python
ax = df.plot()
```

### Step 5: Assign expected = value

```python
expected = _unpack_cycler(plt.rcParams)[:3]
```

### Step 6: Call _check_colors()

```python
_check_colors(ax.get_lines(), linecolors=expected)
```


## Complete Example

```python
# Workflow
import cycler
colors = list('rgbk')
plt.rcParams['axes.prop_cycle'] = cycler.cycler('color', colors)
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)))
ax = df.plot()
expected = _unpack_cycler(plt.rcParams)[:3]
_check_colors(ax.get_lines(), linecolors=expected)
```

## Next Steps


---

*Source: test_frame_color.py:595 | Complexity: Intermediate | Last updated: 2026-06-02*