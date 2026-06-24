# How To: Scatter With C Column Name With Colors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scatter with c column name with colors

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: cmap
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[5.1, 3.5], [4.9, 3.0], [7.0, 3.2], [6.4, 3.2], [5.9, 3.0]], columns=['length', 'width'])
```

**Verification:**
```python
assert ax.collections[0].colorbar is None
```

### Step 2: Assign unknown = value

```python
df['species'] = ['r', 'r', 'g', 'g', 'b']
```

**Verification:**
```python
assert ax.collections[0].colorbar is None
```

### Step 3: Assign ax = df.plot.scatter(...)

```python
ax = df.plot.scatter(x=0, y=1, c='species', cmap=cmap)
```

### Step 4: Assign ax = df.plot.scatter(...)

```python
ax = df.plot.scatter(x=0, y=1, cmap=cmap, c='species')
```


## Complete Example

```python
# Setup
# Fixtures: cmap

# Workflow
df = DataFrame([[5.1, 3.5], [4.9, 3.0], [7.0, 3.2], [6.4, 3.2], [5.9, 3.0]], columns=['length', 'width'])
df['species'] = ['r', 'r', 'g', 'g', 'b']
if cmap is not None:
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        ax = df.plot.scatter(x=0, y=1, cmap=cmap, c='species')
else:
    ax = df.plot.scatter(x=0, y=1, c='species', cmap=cmap)
assert ax.collections[0].colorbar is None
```

## Next Steps


---

*Source: test_frame_color.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*