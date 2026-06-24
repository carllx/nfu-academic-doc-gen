# How To: Boxplot Legacy2 With Multi Col

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boxplot legacy2 with multi col

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 2)), columns=['Col1', 'Col2'])
```

**Verification:**
```python
assert axes['Col1'].get_figure() is fig
```

### Step 2: Assign unknown = Series(...)

```python
df['X'] = Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
```

### Step 3: Assign unknown = Series(...)

```python
df['Y'] = Series(['A'] * 10)
```

### Step 4: Assign unknown = mpl.pyplot.subplots(...)

```python
fig, ax = mpl.pyplot.subplots()
```

**Verification:**
```python
assert axes['Col1'].get_figure() is fig
```

### Step 5: Assign axes = df.boxplot(...)

```python
axes = df.boxplot(column=['Col1', 'Col2'], by='X', ax=ax, return_type='axes')
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random((10, 2)), columns=['Col1', 'Col2'])
df['X'] = Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
df['Y'] = Series(['A'] * 10)
fig, ax = mpl.pyplot.subplots()
with tm.assert_produces_warning(UserWarning):
    axes = df.boxplot(column=['Col1', 'Col2'], by='X', ax=ax, return_type='axes')
assert axes['Col1'].get_figure() is fig
```

## Next Steps


---

*Source: test_boxplot_method.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*