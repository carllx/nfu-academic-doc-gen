# How To: Parallel Coordinates Line Diff

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parallel coordinates line diff

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

**Verification:**
```python
assert len(ax.get_lines()) == nlines - nxticks
```

### Step 2: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(parallel_coordinates, frame=df, class_column='Name')
```

### Step 3: Assign nlines = len(...)

```python
nlines = len(ax.get_lines())
```

### Step 4: Assign nxticks = len(...)

```python
nxticks = len(ax.xaxis.get_ticklabels())
```

### Step 5: Assign ax = _check_plot_works(...)

```python
ax = _check_plot_works(parallel_coordinates, frame=df, class_column='Name', axvlines=False)
```

**Verification:**
```python
assert len(ax.get_lines()) == nlines - nxticks
```


## Complete Example

```python
# Setup
# Fixtures: iris

# Workflow
from pandas.plotting import parallel_coordinates
df = iris
ax = _check_plot_works(parallel_coordinates, frame=df, class_column='Name')
nlines = len(ax.get_lines())
nxticks = len(ax.xaxis.get_ticklabels())
ax = _check_plot_works(parallel_coordinates, frame=df, class_column='Name', axvlines=False)
assert len(ax.get_lines()) == nlines - nxticks
```

## Next Steps


---

*Source: test_misc.py:308 | Complexity: Intermediate | Last updated: 2026-06-02*