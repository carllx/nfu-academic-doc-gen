# How To: Hist Kde Logy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test hist kde logy

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
# Fixtures: ts
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 3: Assign ax = ts.plot.kde(...)

```python
ax = ts.plot.kde(logy=True, ax=ax)
```

### Step 4: Call _check_ax_scales()

```python
_check_ax_scales(ax, yaxis='log')
```

### Step 5: Assign xlabels = ax.get_xticklabels(...)

```python
xlabels = ax.get_xticklabels()
```

### Step 6: Call _check_text_labels()

```python
_check_text_labels(xlabels, [''] * len(xlabels))
```

### Step 7: Assign ylabels = ax.get_yticklabels(...)

```python
ylabels = ax.get_yticklabels()
```

### Step 8: Call _check_text_labels()

```python
_check_text_labels(ylabels, [''] * len(ylabels))
```


## Complete Example

```python
# Setup
# Fixtures: ts

# Workflow
pytest.importorskip('scipy')
_, ax = mpl.pyplot.subplots()
ax = ts.plot.kde(logy=True, ax=ax)
_check_ax_scales(ax, yaxis='log')
xlabels = ax.get_xticklabels()
_check_text_labels(xlabels, [''] * len(xlabels))
ylabels = ax.get_yticklabels()
_check_text_labels(ylabels, [''] * len(ylabels))
```

## Next Steps


---

*Source: test_hist_method.py:228 | Complexity: Advanced | Last updated: 2026-06-02*