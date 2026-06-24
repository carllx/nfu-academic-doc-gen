# How To: Boxplot Colors Default Color

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boxplot colors default color

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

### Step 1: Assign default_colors = _unpack_cycler(...)

```python
default_colors = _unpack_cycler(mpl.pyplot.rcParams)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
```

### Step 3: Assign dict_colors = value

```python
dict_colors = {'whiskers': 'c', 'medians': 'm'}
```

### Step 4: Assign bp = df.plot.box(...)

```python
bp = df.plot.box(color=dict_colors, return_type='dict')
```

### Step 5: Call _check_colors_box()

```python
_check_colors_box(bp, default_colors[0], 'c', 'm', default_colors[0])
```


## Complete Example

```python
# Workflow
default_colors = _unpack_cycler(mpl.pyplot.rcParams)
df = DataFrame(np.random.default_rng(2).standard_normal((5, 5)))
dict_colors = {'whiskers': 'c', 'medians': 'm'}
bp = df.plot.box(color=dict_colors, return_type='dict')
_check_colors_box(bp, default_colors[0], 'c', 'm', default_colors[0])
```

## Next Steps


---

*Source: test_frame_color.py:556 | Complexity: Intermediate | Last updated: 2026-06-02*