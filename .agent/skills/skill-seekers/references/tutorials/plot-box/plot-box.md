# How To: Plot Box

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test plot box

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.pyplot`

**Setup Required:**
```python
# Fixtures: vert
```

## Step-by-Step Guide

### Step 1: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(2)
```

**Verification:**
```python
assert ax.get_xlabel() == xlabel
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
```

**Verification:**
```python
assert ax.get_ylabel() == ylabel
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
```

### Step 4: Assign unknown = value

```python
xlabel, ylabel = ('x', 'y')
```

### Step 5: Assign unknown = plt.subplots(...)

```python
_, axs = plt.subplots(ncols=2, figsize=(10, 7), sharey=True)
```

### Step 6: Call df1.plot.box()

```python
df1.plot.box(ax=axs[0], xlabel=xlabel, ylabel=ylabel, **vert)
```

### Step 7: Call df2.plot.box()

```python
df2.plot.box(ax=axs[1], xlabel=xlabel, ylabel=ylabel, **vert)
```

### Step 8: Call mpl.pyplot.close()

```python
mpl.pyplot.close()
```

**Verification:**
```python
assert ax.get_xlabel() == xlabel
```


## Complete Example

```python
# Setup
# Fixtures: vert

# Workflow
rng = np.random.default_rng(2)
df1 = DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
df2 = DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
xlabel, ylabel = ('x', 'y')
_, axs = plt.subplots(ncols=2, figsize=(10, 7), sharey=True)
df1.plot.box(ax=axs[0], xlabel=xlabel, ylabel=ylabel, **vert)
df2.plot.box(ax=axs[1], xlabel=xlabel, ylabel=ylabel, **vert)
for ax in axs:
    assert ax.get_xlabel() == xlabel
    assert ax.get_ylabel() == ylabel
mpl.pyplot.close()
```

## Next Steps


---

*Source: test_boxplot_method.py:347 | Complexity: Advanced | Last updated: 2026-06-02*