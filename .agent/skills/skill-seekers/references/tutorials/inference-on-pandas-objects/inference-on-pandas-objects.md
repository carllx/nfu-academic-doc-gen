# How To: Inference On Pandas Objects

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inference on pandas objects

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([pd.Timestamp('2019-12-31')], dtype=object)
```

**Verification:**
```python
assert result.dtype != np.object_
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([pd.Timestamp('2019-12-31')], dtype=object)
```

**Verification:**
```python
assert result.dtype != np.object_
```

### Step 3: Assign result = Index(...)

```python
result = Index(idx)
```

### Step 4: Assign result = Index(...)

```python
result = Index(ser)
```


## Complete Example

```python
# Workflow
idx = Index([pd.Timestamp('2019-12-31')], dtype=object)
with tm.assert_produces_warning(FutureWarning, match='Dtype inference'):
    result = Index(idx)
assert result.dtype != np.object_
ser = Series([pd.Timestamp('2019-12-31')], dtype=object)
with tm.assert_produces_warning(FutureWarning, match='Dtype inference'):
    result = Index(ser)
assert result.dtype != np.object_
```

## Next Steps


---

*Source: test_constructors.py:60 | Complexity: Intermediate | Last updated: 2026-06-02*