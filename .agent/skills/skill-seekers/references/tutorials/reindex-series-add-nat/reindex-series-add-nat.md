# How To: Reindex Series Add Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex series add nat

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 00:00:00', periods=10, freq='10s')
```

**Verification:**
```python
assert np.issubdtype(result.dtype, np.dtype('M8[ns]'))
```

### Step 2: Assign series = Series(...)

```python
series = Series(rng)
```

**Verification:**
```python
assert mask[-5:].all()
```

### Step 3: Assign result = series.reindex(...)

```python
result = series.reindex(range(15))
```

**Verification:**
```python
assert not mask[:-5].any()
```

### Step 4: Assign mask = result.isna(...)

```python
mask = result.isna()
```

**Verification:**
```python
assert mask[-5:].all()
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000 00:00:00', periods=10, freq='10s')
series = Series(rng)
result = series.reindex(range(15))
assert np.issubdtype(result.dtype, np.dtype('M8[ns]'))
mask = result.isna()
assert mask[-5:].all()
assert not mask[:-5].any()
```

## Next Steps


---

*Source: test_reindex.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*