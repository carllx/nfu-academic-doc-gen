# How To: Background Gradient Nullable Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test background gradient nullable dtypes

## Prerequisites

**Required Modules:**
- `gc`
- `numpy`
- `pytest`
- `pandas`
- `matplotlib`
- `pandas.io.formats.style`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([[1], [0], [np.nan]], dtype=float)
```

**Verification:**
```python
assert ctx1 == ctx2
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[1], [0], [None]], dtype='Int64')
```

### Step 3: Assign ctx1 = value

```python
ctx1 = df1.style.background_gradient()._compute().ctx
```

### Step 4: Assign ctx2 = value

```python
ctx2 = df2.style.background_gradient()._compute().ctx
```

**Verification:**
```python
assert ctx1 == ctx2
```


## Complete Example

```python
# Workflow
df1 = DataFrame([[1], [0], [np.nan]], dtype=float)
df2 = DataFrame([[1], [0], [None]], dtype='Int64')
ctx1 = df1.style.background_gradient()._compute().ctx
ctx2 = df2.style.background_gradient()._compute().ctx
assert ctx1 == ctx2
```

## Next Steps


---

*Source: test_matplotlib.py:285 | Complexity: Intermediate | Last updated: 2026-06-02*