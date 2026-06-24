# How To:  Gen Two Subplots With Ax

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test  gen two subplots with ax

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas.tests.plotting.common`


## Step-by-Step Guide

### Step 1: Assign fig = plt.gcf(...)

```python
fig = plt.gcf()
```

**Verification:**
```python
assert fig.get_axes() == []
```

### Step 2: Assign gen = _gen_two_subplots(...)

```python
gen = _gen_two_subplots(f=lambda **kwargs: None, fig=fig, ax='test')
```

**Verification:**
```python
assert len(axes) == 1
```

### Step 3: Call next()

```python
next(gen)
```

**Verification:**
```python
assert subplot_geometry == [2, 1, 2]
```

### Step 4: Call next()

```python
next(gen)
```

### Step 5: Assign axes = fig.get_axes(...)

```python
axes = fig.get_axes()
```

**Verification:**
```python
assert len(axes) == 1
```

### Step 6: Assign subplot_geometry = list(...)

```python
subplot_geometry = list(axes[0].get_subplotspec().get_geometry()[:-1])
```

**Verification:**
```python
assert subplot_geometry == [2, 1, 2]
```


## Complete Example

```python
# Workflow
fig = plt.gcf()
gen = _gen_two_subplots(f=lambda **kwargs: None, fig=fig, ax='test')
next(gen)
assert fig.get_axes() == []
next(gen)
axes = fig.get_axes()
assert len(axes) == 1
subplot_geometry = list(axes[0].get_subplotspec().get_geometry()[:-1])
subplot_geometry[-1] += 1
assert subplot_geometry == [2, 1, 2]
```

## Next Steps


---

*Source: test_common.py:29 | Complexity: Advanced | Last updated: 2026-06-02*