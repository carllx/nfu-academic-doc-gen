# How To: Components

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test components

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = timedelta_range(...)

```python
rng = timedelta_range('1 days, 10:11:12', periods=2, freq='s')
```

**Verification:**
```python
assert not result.iloc[0].isna().all()
```

### Step 2: rng.components

```python
rng.components
```

**Verification:**
```python
assert result.iloc[1].isna().all()
```

### Step 3: Assign s = Series(...)

```python
s = Series(rng)
```

### Step 4: Assign unknown = value

```python
s[1] = np.nan
```

### Step 5: Assign result = value

```python
result = s.dt.components
```

**Verification:**
```python
assert not result.iloc[0].isna().all()
```


## Complete Example

```python
# Workflow
rng = timedelta_range('1 days, 10:11:12', periods=2, freq='s')
rng.components
s = Series(rng)
s[1] = np.nan
result = s.dt.components
assert not result.iloc[0].isna().all()
assert result.iloc[1].isna().all()
```

## Next Steps


---

*Source: test_scalar_compat.py:132 | Complexity: Intermediate | Last updated: 2026-06-02*