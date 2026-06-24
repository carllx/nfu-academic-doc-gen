# How To: If Scatterplot Colorbars Are Next To Parent Axes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test if scatterplot colorbars are next to parent axes

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

### Step 1: Assign random_array = np.random.default_rng.random(...)

```python
random_array = np.random.default_rng(2).random((10, 3))
```

**Verification:**
```python
assert np.isclose(parent_distance, colorbar_distance, atol=1e-07).all()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(random_array, columns=['A label', 'B label', 'C label'])
```

### Step 3: Assign unknown = plt.subplots(...)

```python
fig, axes = plt.subplots(1, 2)
```

### Step 4: Call df.plot.scatter()

```python
df.plot.scatter('A label', 'B label', c='C label', ax=axes[0])
```

### Step 5: Call df.plot.scatter()

```python
df.plot.scatter('A label', 'B label', c='C label', ax=axes[1])
```

### Step 6: Call plt.tight_layout()

```python
plt.tight_layout()
```

### Step 7: Assign points = np.array(...)

```python
points = np.array([ax.get_position().get_points() for ax in fig.axes])
```

### Step 8: Assign axes_x_coords = value

```python
axes_x_coords = points[:, :, 0]
```

### Step 9: Assign parent_distance = value

```python
parent_distance = axes_x_coords[1, :] - axes_x_coords[0, :]
```

### Step 10: Assign colorbar_distance = value

```python
colorbar_distance = axes_x_coords[3, :] - axes_x_coords[2, :]
```

**Verification:**
```python
assert np.isclose(parent_distance, colorbar_distance, atol=1e-07).all()
```


## Complete Example

```python
# Workflow
random_array = np.random.default_rng(2).random((10, 3))
df = DataFrame(random_array, columns=['A label', 'B label', 'C label'])
fig, axes = plt.subplots(1, 2)
df.plot.scatter('A label', 'B label', c='C label', ax=axes[0])
df.plot.scatter('A label', 'B label', c='C label', ax=axes[1])
plt.tight_layout()
points = np.array([ax.get_position().get_points() for ax in fig.axes])
axes_x_coords = points[:, :, 0]
parent_distance = axes_x_coords[1, :] - axes_x_coords[0, :]
colorbar_distance = axes_x_coords[3, :] - axes_x_coords[2, :]
assert np.isclose(parent_distance, colorbar_distance, atol=1e-07).all()
```

## Next Steps


---

*Source: test_frame_color.py:179 | Complexity: Advanced | Last updated: 2026-06-02*