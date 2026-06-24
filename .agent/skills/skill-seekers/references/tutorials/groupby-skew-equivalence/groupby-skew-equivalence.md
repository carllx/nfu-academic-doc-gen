# How To: Groupby Skew Equivalence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby skew equivalence

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign nrows = 1000

```python
nrows = 1000
```

### Step 2: Assign ngroups = 3

```python
ngroups = 3
```

### Step 3: Assign ncols = 2

```python
ncols = 2
```

### Step 4: Assign nan_frac = 0.05

```python
nan_frac = 0.05
```

### Step 5: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((nrows, ncols))
```

### Step 6: Assign unknown = value

```python
arr[np.random.default_rng(2).random(nrows) < nan_frac] = np.nan
```

### Step 7: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(arr)
```

### Step 8: Assign grps = np.random.default_rng.integers(...)

```python
grps = np.random.default_rng(2).integers(0, ngroups, size=nrows)
```

### Step 9: Assign gb = df.groupby(...)

```python
gb = df.groupby(grps)
```

### Step 10: Assign result = gb.skew(...)

```python
result = gb.skew()
```

### Step 11: Assign grpwise = value

```python
grpwise = [grp.skew().to_frame(i).T for i, grp in gb]
```

### Step 12: Assign expected = pd.concat(...)

```python
expected = pd.concat(grpwise, axis=0)
```

### Step 13: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(result.index.dtype)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
nrows = 1000
ngroups = 3
ncols = 2
nan_frac = 0.05
arr = np.random.default_rng(2).standard_normal((nrows, ncols))
arr[np.random.default_rng(2).random(nrows) < nan_frac] = np.nan
df = pd.DataFrame(arr)
grps = np.random.default_rng(2).integers(0, ngroups, size=nrows)
gb = df.groupby(grps)
result = gb.skew()
grpwise = [grp.skew().to_frame(i).T for i, grp in gb]
expected = pd.concat(grpwise, axis=0)
expected.index = expected.index.astype(result.index.dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skew.py:7 | Complexity: Advanced | Last updated: 2026-06-02*