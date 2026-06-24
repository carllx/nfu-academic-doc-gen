# How To: Boxplot Axis Limits Two Rows

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boxplot axis limits two rows

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
# Fixtures: hist_df
```

## Step-by-Step Guide

### Step 1: Assign df = hist_df.copy(...)

```python
df = hist_df.copy()
```

**Verification:**
```python
assert weight_ax._sharey == height_ax
```

### Step 2: Assign unknown = np.random.default_rng.integers(...)

```python
df['age'] = np.random.default_rng(2).integers(1, 20, df.shape[0])
```

**Verification:**
```python
assert age_ax._sharey == height_ax
```

### Step 3: Assign p = df.boxplot(...)

```python
p = df.boxplot(['height', 'weight', 'age'], by='category')
```

**Verification:**
```python
assert dummy_ax._sharey is None
```

### Step 4: Assign unknown = value

```python
height_ax, weight_ax, age_ax = (p[0, 0], p[0, 1], p[1, 0])
```

### Step 5: Assign dummy_ax = value

```python
dummy_ax = p[1, 1]
```

### Step 6: Call _check_ax_limits()

```python
_check_ax_limits(df['height'], height_ax)
```

### Step 7: Call _check_ax_limits()

```python
_check_ax_limits(df['weight'], weight_ax)
```

### Step 8: Call _check_ax_limits()

```python
_check_ax_limits(df['age'], age_ax)
```

**Verification:**
```python
assert weight_ax._sharey == height_ax
```


## Complete Example

```python
# Setup
# Fixtures: hist_df

# Workflow
df = hist_df.copy()
df['age'] = np.random.default_rng(2).integers(1, 20, df.shape[0])
p = df.boxplot(['height', 'weight', 'age'], by='category')
height_ax, weight_ax, age_ax = (p[0, 0], p[0, 1], p[1, 0])
dummy_ax = p[1, 1]
_check_ax_limits(df['height'], height_ax)
_check_ax_limits(df['weight'], weight_ax)
_check_ax_limits(df['age'], age_ax)
assert weight_ax._sharey == height_ax
assert age_ax._sharey == height_ax
assert dummy_ax._sharey is None
```

## Next Steps


---

*Source: test_boxplot_method.py:207 | Complexity: Advanced | Last updated: 2026-06-02*