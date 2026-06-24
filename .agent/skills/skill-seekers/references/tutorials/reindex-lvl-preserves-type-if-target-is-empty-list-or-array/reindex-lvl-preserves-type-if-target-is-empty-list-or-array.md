# How To: Reindex Lvl Preserves Type If Target Is Empty List Or Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex lvl preserves type if target is empty list or array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([[0, 1], ['a', 'b']])
```

**Verification:**
```python
assert idx.reindex([], level=0)[0].levels[0].dtype.type == np.int64
```

### Step 2: Assign exp = value

```python
exp = np.object_ if not using_infer_string else str
```

**Verification:**
```python
assert idx.reindex([], level=1)[0].levels[1].dtype.type == exp
```

### Step 3: Assign cat = pd.Categorical(...)

```python
cat = pd.Categorical(['foo', 'bar'])
```

**Verification:**
```python
assert mi.reindex([], level=0)[0].levels[0].dtype == cat.dtype
```

### Step 4: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=2, tz='US/Pacific')
```

**Verification:**
```python
assert mi.reindex([], level=1)[0].levels[1].dtype == dti.dtype
```

### Step 5: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([cat, dti])
```

**Verification:**
```python
assert mi.reindex([], level=0)[0].levels[0].dtype == cat.dtype
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
idx = MultiIndex.from_product([[0, 1], ['a', 'b']])
assert idx.reindex([], level=0)[0].levels[0].dtype.type == np.int64
exp = np.object_ if not using_infer_string else str
assert idx.reindex([], level=1)[0].levels[1].dtype.type == exp
cat = pd.Categorical(['foo', 'bar'])
dti = pd.date_range('2016-01-01', periods=2, tz='US/Pacific')
mi = MultiIndex.from_product([cat, dti])
assert mi.reindex([], level=0)[0].levels[0].dtype == cat.dtype
assert mi.reindex([], level=1)[0].levels[1].dtype == dti.dtype
```

## Next Steps


---

*Source: test_reindex.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*