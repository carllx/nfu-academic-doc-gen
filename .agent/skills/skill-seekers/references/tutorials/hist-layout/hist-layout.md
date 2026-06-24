# How To: Hist Layout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test hist layout

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
# Fixtures: layout_test
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 2)))
```

### Step 2: Assign unknown = to_datetime(...)

```python
df[2] = to_datetime(np.random.default_rng(2).integers(812419200000000000, 819331200000000000, size=10, dtype=np.int64))
```

### Step 3: Assign axes = df.hist(...)

```python
axes = df.hist(layout=layout_test['layout'])
```

### Step 4: Assign expected = value

```python
expected = layout_test['expected_size']
```

### Step 5: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=3, layout=expected)
```


## Complete Example

```python
# Setup
# Fixtures: layout_test

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 2)))
df[2] = to_datetime(np.random.default_rng(2).integers(812419200000000000, 819331200000000000, size=10, dtype=np.int64))
axes = df.hist(layout=layout_test['layout'])
expected = layout_test['expected_size']
_check_axes_shape(axes, axes_num=3, layout=expected)
```

## Next Steps


---

*Source: test_hist_method.py:394 | Complexity: Intermediate | Last updated: 2026-06-02*