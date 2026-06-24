# How To: Nan Stays Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nan stays float

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx0 = MultiIndex(...)

```python
idx0 = MultiIndex(levels=[['A', 'B'], []], codes=[[1, 0], [-1, -1]], names=[0, 1])
```

**Verification:**
```python
assert pd.isna(idx0.get_level_values(1)).all()
```

### Step 2: Assign idx1 = MultiIndex(...)

```python
idx1 = MultiIndex(levels=[['C'], ['D']], codes=[[0], [0]], names=[0, 1])
```

**Verification:**
```python
assert pd.isna(idxm.get_level_values(1)[:-1]).all()
```

### Step 3: Assign idxm = idx0.join(...)

```python
idxm = idx0.join(idx1, how='outer')
```

**Verification:**
```python
assert pd.isna(df0.index.get_level_values(1)).all()
```

### Step 4: Assign df0 = pd.DataFrame(...)

```python
df0 = pd.DataFrame([[1, 2]], index=idx0)
```

**Verification:**
```python
assert pd.isna(dfm.index.get_level_values(1)[:-1]).all()
```

### Step 5: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame([[3, 4]], index=idx1)
```

### Step 6: Assign dfm = value

```python
dfm = df0 - df1
```

**Verification:**
```python
assert pd.isna(df0.index.get_level_values(1)).all()
```


## Complete Example

```python
# Workflow
idx0 = MultiIndex(levels=[['A', 'B'], []], codes=[[1, 0], [-1, -1]], names=[0, 1])
idx1 = MultiIndex(levels=[['C'], ['D']], codes=[[0], [0]], names=[0, 1])
idxm = idx0.join(idx1, how='outer')
assert pd.isna(idx0.get_level_values(1)).all()
assert pd.isna(idxm.get_level_values(1)[:-1]).all()
df0 = pd.DataFrame([[1, 2]], index=idx0)
df1 = pd.DataFrame([[3, 4]], index=idx1)
dfm = df0 - df1
assert pd.isna(df0.index.get_level_values(1)).all()
assert pd.isna(dfm.index.get_level_values(1)[:-1]).all()
```

## Next Steps


---

*Source: test_missing.py:87 | Complexity: Intermediate | Last updated: 2026-06-02*