# How To: Radviz Colors Handles

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test radviz colors handles

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

### Step 1: Assign colors = value

```python
colors = [[0.0, 0.0, 1.0, 1.0], [0.0, 0.5, 1.0, 1.0], [1.0, 0.0, 0.0, 1.0]]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [2, 1, 3], 'C': [3, 2, 1], 'Name': ['b', 'g', 'r']})
```

### Step 3: Assign ax = radviz(...)

```python
ax = radviz(df, 'Name', color=colors)
```

### Step 4: Assign unknown = ax.get_legend_handles_labels(...)

```python
handles, _ = ax.get_legend_handles_labels()
```

### Step 5: Call _check_colors()

```python
_check_colors(handles, facecolors=colors)
```


## Complete Example

```python
# Workflow
from pandas.plotting import radviz
colors = [[0.0, 0.0, 1.0, 1.0], [0.0, 0.5, 1.0, 1.0], [1.0, 0.0, 0.0, 1.0]]
df = DataFrame({'A': [1, 2, 3], 'B': [2, 1, 3], 'C': [3, 2, 1], 'Name': ['b', 'g', 'r']})
ax = radviz(df, 'Name', color=colors)
handles, _ = ax.get_legend_handles_labels()
_check_colors(handles, facecolors=colors)
```

## Next Steps


---

*Source: test_misc.py:392 | Complexity: Intermediate | Last updated: 2026-06-02*