# How To: Groupby Hist Frame With Legend

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby hist frame with legend

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.plotting.common`

**Setup Required:**
```python
# Fixtures: column, expected_axes_num
```

## Step-by-Step Guide

### Step 1: Assign expected_layout = value

```python
expected_layout = (1, expected_axes_num)
```

### Step 2: Assign expected_labels = value

```python
expected_labels = column or [['a'], ['b']]
```

### Step 3: Assign index = Index(...)

```python
index = Index(15 * ['1'] + 15 * ['2'], name='c')
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((30, 2)), index=index, columns=['a', 'b'])
```

### Step 5: Assign g = df.groupby(...)

```python
g = df.groupby('c')
```

### Step 6: Call _check_axes_shape()

```python
_check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
```

### Step 7: Call _check_legend_labels()

```python
_check_legend_labels(ax, expected_label)
```


## Complete Example

```python
# Setup
# Fixtures: column, expected_axes_num

# Workflow
expected_layout = (1, expected_axes_num)
expected_labels = column or [['a'], ['b']]
index = Index(15 * ['1'] + 15 * ['2'], name='c')
df = DataFrame(np.random.default_rng(2).standard_normal((30, 2)), index=index, columns=['a', 'b'])
g = df.groupby('c')
for axes in g.hist(legend=True, column=column):
    _check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
    for ax, expected_label in zip(axes[0], expected_labels):
        _check_legend_labels(ax, expected_label)
```

## Next Steps


---

*Source: test_groupby.py:98 | Complexity: Intermediate | Last updated: 2026-06-02*