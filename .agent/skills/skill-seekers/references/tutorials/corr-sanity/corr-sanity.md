# How To: Corr Sanity

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corr sanity

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.array([[0.87024726, 0.18505595], [0.64355431, 0.3091617], [0.92372966, 0.50552513], [0.00203756, 0.04520709], [0.84780328, 0.33394331], [0.78369152, 0.63919667]]))
```

**Verification:**
```python
assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
```

### Step 2: Assign res = unknown.rolling.corr(...)

```python
res = df[0].rolling(5, center=True).corr(df[1])
```

**Verification:**
```python
assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((30, 2)))
```

### Step 4: Assign res = unknown.rolling.corr(...)

```python
res = df[0].rolling(5, center=True).corr(df[1])
```

**Verification:**
```python
assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
```


## Complete Example

```python
# Workflow
df = DataFrame(np.array([[0.87024726, 0.18505595], [0.64355431, 0.3091617], [0.92372966, 0.50552513], [0.00203756, 0.04520709], [0.84780328, 0.33394331], [0.78369152, 0.63919667]]))
res = df[0].rolling(5, center=True).corr(df[1])
assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
df = DataFrame(np.random.default_rng(2).random((30, 2)))
res = df[0].rolling(5, center=True).corr(df[1])
assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
```

## Next Steps


---

*Source: test_pairwise.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*