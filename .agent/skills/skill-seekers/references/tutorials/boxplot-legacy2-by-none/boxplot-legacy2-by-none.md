# How To: Boxplot Legacy2 By None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boxplot legacy2 by none

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
assert len(ax.get_lines()) == len(lines)
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
_, ax = mpl.pyplot.subplots()
```

### Step 5: Assign d = df.boxplot(...)

```python
d = df.boxplot(ax=ax, return_type='dict')
```

### Step 6: Assign lines = list(...)

```python
lines = list(itertools.chain.from_iterable(d.values()))
```

**Verification:**
```python
assert len(ax.get_lines()) == len(lines)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random((10, 2)), columns=['Col1', 'Col2'])
df['X'] = Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
df['Y'] = Series(['A'] * 10)
_, ax = mpl.pyplot.subplots()
d = df.boxplot(ax=ax, return_type='dict')
lines = list(itertools.chain.from_iterable(d.values()))
assert len(ax.get_lines()) == len(lines)
```

## Next Steps


---

*Source: test_boxplot_method.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*