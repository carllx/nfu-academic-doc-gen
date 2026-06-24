# How To: Get Standard Colors No Appending

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test get standard colors no appending

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign color_before = cm.gnuplot(...)

```python
color_before = cm.gnuplot(range(5))
```

**Verification:**
```python
assert len(color_after) == len(color_before)
```

### Step 2: Assign color_after = get_standard_colors(...)

```python
color_after = get_standard_colors(1, color=color_before)
```

**Verification:**
```python
assert p.patches[1].get_facecolor() == p.patches[17].get_facecolor()
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((48, 4)), columns=list('ABCD'))
```

### Step 4: Assign color_list = cm.gnuplot(...)

```python
color_list = cm.gnuplot(np.linspace(0, 1, 16))
```

### Step 5: Assign p = df.A.plot.bar(...)

```python
p = df.A.plot.bar(figsize=(16, 7), color=color_list)
```

**Verification:**
```python
assert p.patches[1].get_facecolor() == p.patches[17].get_facecolor()
```


## Complete Example

```python
# Workflow
from matplotlib import cm
from pandas.plotting._matplotlib.style import get_standard_colors
color_before = cm.gnuplot(range(5))
color_after = get_standard_colors(1, color=color_before)
assert len(color_after) == len(color_before)
df = DataFrame(np.random.default_rng(2).standard_normal((48, 4)), columns=list('ABCD'))
color_list = cm.gnuplot(np.linspace(0, 1, 16))
p = df.A.plot.bar(figsize=(16, 7), color=color_list)
assert p.patches[1].get_facecolor() == p.patches[17].get_facecolor()
```

## Next Steps


---

*Source: test_misc.py:506 | Complexity: Intermediate | Last updated: 2026-06-02*