# How To: Savefig

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test savefig

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
# Fixtures: kind, data, index
```

## Step-by-Step Guide

### Step 1: Assign unknown = plt.subplots(...)

```python
fig, ax = plt.subplots()
```

### Step 2: Assign data.index = index

```python
data.index = index
```

### Step 3: Assign kwargs = value

```python
kwargs = {}
```

### Step 4: Call data.plot()

```python
data.plot(kind=kind, ax=ax, **kwargs)
```

### Step 5: Call fig.savefig()

```python
fig.savefig(os.devnull)
```

### Step 6: Assign kwargs = value

```python
kwargs = {'x': 0, 'y': 1}
```

### Step 7: Call pytest.skip()

```python
pytest.skip(f'{kind} not supported with Series')
```


## Complete Example

```python
# Setup
# Fixtures: kind, data, index

# Workflow
fig, ax = plt.subplots()
data.index = index
kwargs = {}
if kind in ['hexbin', 'scatter', 'pie']:
    if isinstance(data, Series):
        pytest.skip(f'{kind} not supported with Series')
    kwargs = {'x': 0, 'y': 1}
data.plot(kind=kind, ax=ax, **kwargs)
fig.savefig(os.devnull)
```

## Next Steps


---

*Source: test_misc.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*