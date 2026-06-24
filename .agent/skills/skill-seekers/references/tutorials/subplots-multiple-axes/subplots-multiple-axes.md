# How To: Subplots Multiple Axes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subplots multiple axes

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

### Step 1: Assign unknown = mpl.pyplot.subplots(...)

```python
fig, axes = mpl.pyplot.subplots(2, 3)
```

**Verification:**
```python
assert returned.shape == (3,)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=list(string.ascii_letters[:10]))
```

**Verification:**
```python
assert returned[0].figure is fig
```

### Step 3: Assign returned = df.plot(...)

```python
returned = df.plot(subplots=True, ax=axes[0], sharex=False, sharey=False)
```

**Verification:**
```python
assert returned.shape == (3,)
```

### Step 4: Call _check_axes_shape()

```python
_check_axes_shape(returned, axes_num=3, layout=(1, 3))
```

**Verification:**
```python
assert returned[0].figure is fig
```

### Step 5: Assign returned = df.plot(...)

```python
returned = df.plot(subplots=True, ax=axes[1], sharex=False, sharey=False)
```

### Step 6: Call _check_axes_shape()

```python
_check_axes_shape(returned, axes_num=3, layout=(1, 3))
```

**Verification:**
```python
assert returned.shape == (3,)
```

### Step 7: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=6, layout=(2, 3))
```


## Complete Example

```python
# Workflow
fig, axes = mpl.pyplot.subplots(2, 3)
df = DataFrame(np.random.default_rng(2).random((10, 3)), index=list(string.ascii_letters[:10]))
returned = df.plot(subplots=True, ax=axes[0], sharex=False, sharey=False)
_check_axes_shape(returned, axes_num=3, layout=(1, 3))
assert returned.shape == (3,)
assert returned[0].figure is fig
returned = df.plot(subplots=True, ax=axes[1], sharex=False, sharey=False)
_check_axes_shape(returned, axes_num=3, layout=(1, 3))
assert returned.shape == (3,)
assert returned[0].figure is fig
_check_axes_shape(axes, axes_num=6, layout=(2, 3))
```

## Next Steps


---

*Source: test_frame_subplots.py:287 | Complexity: Intermediate | Last updated: 2026-06-02*