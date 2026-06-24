# How To: Mixed Yerr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mixed yerr

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `matplotlib.collections`
- `matplotlib.lines`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([{'x': 1, 'a': 1, 'b': 1}, {'x': 2, 'a': 2, 'b': 3}])
```

**Verification:**
```python
assert isinstance(result_handles[0], LineCollection)
```

### Step 2: Assign ax = df.plot(...)

```python
ax = df.plot('x', 'a', c='orange', yerr=0.1, label='orange')
```

**Verification:**
```python
assert isinstance(result_handles[1], Line2D)
```

### Step 3: Call df.plot()

```python
df.plot('x', 'b', c='blue', yerr=None, ax=ax, label='blue')
```

### Step 4: Assign legend = ax.get_legend(...)

```python
legend = ax.get_legend()
```

**Verification:**
```python
assert isinstance(result_handles[0], LineCollection)
```

### Step 5: Assign result_handles = value

```python
result_handles = legend.legendHandles
```

### Step 6: Assign result_handles = value

```python
result_handles = legend.legend_handles
```


## Complete Example

```python
# Workflow
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
df = DataFrame([{'x': 1, 'a': 1, 'b': 1}, {'x': 2, 'a': 2, 'b': 3}])
ax = df.plot('x', 'a', c='orange', yerr=0.1, label='orange')
df.plot('x', 'b', c='blue', yerr=None, ax=ax, label='blue')
legend = ax.get_legend()
if Version(mpl.__version__) < Version('3.7'):
    result_handles = legend.legendHandles
else:
    result_handles = legend.legend_handles
assert isinstance(result_handles[0], LineCollection)
assert isinstance(result_handles[1], Line2D)
```

## Next Steps


---

*Source: test_frame_legend.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*