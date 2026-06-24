# How To: Background Gradient Int64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test background gradient int64

## Prerequisites

**Required Modules:**
- `gc`
- `numpy`
- `pytest`
- `pandas`
- `matplotlib`
- `pandas.io.formats.style`


## Step-by-Step Guide

### Step 1: Assign df1 = Series.to_frame(...)

```python
df1 = Series(range(3)).to_frame()
```

**Verification:**
```python
assert ctx2[0, 0] == ctx1[0, 0]
```

### Step 2: Assign df2 = Series.to_frame(...)

```python
df2 = Series(range(3), dtype='Int64').to_frame()
```

**Verification:**
```python
assert ctx2[1, 0] == ctx1[1, 0]
```

### Step 3: Assign ctx1 = value

```python
ctx1 = df1.style.background_gradient()._compute().ctx
```

**Verification:**
```python
assert ctx2[2, 0] == ctx1[2, 0]
```

### Step 4: Assign ctx2 = value

```python
ctx2 = df2.style.background_gradient()._compute().ctx
```

**Verification:**
```python
assert ctx2[0, 0] == ctx1[0, 0]
```


## Complete Example

```python
# Workflow
df1 = Series(range(3)).to_frame()
df2 = Series(range(3), dtype='Int64').to_frame()
ctx1 = df1.style.background_gradient()._compute().ctx
ctx2 = df2.style.background_gradient()._compute().ctx
assert ctx2[0, 0] == ctx1[0, 0]
assert ctx2[1, 0] == ctx1[1, 0]
assert ctx2[2, 0] == ctx1[2, 0]
```

## Next Steps


---

*Source: test_matplotlib.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*