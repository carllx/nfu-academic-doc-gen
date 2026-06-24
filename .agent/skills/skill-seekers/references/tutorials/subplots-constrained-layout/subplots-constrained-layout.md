# How To: Subplots Constrained Layout

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subplots constrained layout

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.io.formats.printing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='now', periods=10)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=idx)
```

### Step 3: Assign kwargs = value

```python
kwargs = {}
```

### Step 4: Assign unknown = mpl.pyplot.subplots(...)

```python
_, axes = mpl.pyplot.subplots(2, **kwargs)
```

### Step 5: Assign unknown = True

```python
kwargs['constrained_layout'] = True
```

### Step 6: Call df.plot()

```python
df.plot(ax=axes[0])
```

### Step 7: Call mpl.pyplot.savefig()

```python
mpl.pyplot.savefig(path)
```


## Complete Example

```python
# Workflow
idx = date_range(start='now', periods=10)
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=idx)
kwargs = {}
if hasattr(mpl.pyplot.Figure, 'get_constrained_layout'):
    kwargs['constrained_layout'] = True
_, axes = mpl.pyplot.subplots(2, **kwargs)
with tm.assert_produces_warning(None):
    df.plot(ax=axes[0])
    with tm.ensure_clean(return_filelike=True) as path:
        mpl.pyplot.savefig(path)
```

## Next Steps


---

*Source: test_frame_subplots.py:547 | Complexity: Intermediate | Last updated: 2026-06-02*