# How To: Array Equivalent Index With Tuples

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array equivalent index with tuples

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index(np.array([(pd.NA, 4), (1, 1)], dtype='object'))
```

**Verification:**
```python
assert not array_equivalent(idx1, idx2)
```

### Step 2: Assign idx2 = Index(...)

```python
idx2 = Index(np.array([(1, 1), (pd.NA, 4)], dtype='object'))
```

**Verification:**
```python
assert not idx1.equals(idx2)
```

### Step 3: Assign idx1 = Index(...)

```python
idx1 = Index(np.array([(4, pd.NA), (1, 1)], dtype='object'))
```

**Verification:**
```python
assert not array_equivalent(idx2, idx1)
```

### Step 4: Assign idx2 = Index(...)

```python
idx2 = Index(np.array([(1, 1), (4, pd.NA)], dtype='object'))
```

**Verification:**
```python
assert not idx2.equals(idx1)
```


## Complete Example

```python
# Workflow
idx1 = Index(np.array([(pd.NA, 4), (1, 1)], dtype='object'))
idx2 = Index(np.array([(1, 1), (pd.NA, 4)], dtype='object'))
assert not array_equivalent(idx1, idx2)
assert not idx1.equals(idx2)
assert not array_equivalent(idx2, idx1)
assert not idx2.equals(idx1)
idx1 = Index(np.array([(4, pd.NA), (1, 1)], dtype='object'))
idx2 = Index(np.array([(1, 1), (4, pd.NA)], dtype='object'))
assert not array_equivalent(idx1, idx2)
assert not idx1.equals(idx2)
assert not array_equivalent(idx2, idx1)
assert not idx2.equals(idx1)
```

## Next Steps


---

*Source: test_missing.py:688 | Complexity: Intermediate | Last updated: 2026-06-02*