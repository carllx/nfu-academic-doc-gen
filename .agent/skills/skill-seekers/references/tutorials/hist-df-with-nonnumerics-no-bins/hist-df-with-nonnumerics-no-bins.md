# How To: Hist Df With Nonnumerics No Bins

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test hist df with nonnumerics no bins

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'B', 'C', 'D'])
```

**Verification:**
```python
assert len(ax.patches) == 40
```

### Step 2: Assign unknown = value

```python
df['E'] = ['x', 'y'] * 5
```

### Step 3: Assign unknown = mpl.pyplot.subplots(...)

```python
_, ax = mpl.pyplot.subplots()
```

### Step 4: Assign ax = df.plot.hist(...)

```python
ax = df.plot.hist(ax=ax)
```

**Verification:**
```python
assert len(ax.patches) == 40
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=['A', 'B', 'C', 'D'])
df['E'] = ['x', 'y'] * 5
_, ax = mpl.pyplot.subplots()
ax = df.plot.hist(ax=ax)
assert len(ax.patches) == 40
```

## Next Steps


---

*Source: test_hist_method.py:574 | Complexity: Intermediate | Last updated: 2026-06-02*