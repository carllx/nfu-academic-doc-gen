# How To: Loc Period String Indexing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc period string indexing

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = pd.period_range(...)

```python
a = pd.period_range('2013Q1', '2013Q4', freq='Q')
```

**Verification:**
```python
assert np.isnan(alt)
```

### Step 2: Assign i = value

```python
i = (1111, 2222, 3333)
```

**Verification:**
```python
assert np.isnan(result)
```

### Step 3: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product((a, i), names=('Period', 'CVR'))
```

**Verification:**
```python
assert np.isnan(alt)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(index=idx, columns=('OMS', 'OMK', 'RES', 'DRIFT_IND', 'OEVRIG_IND', 'FIN_IND', 'VARE_UD', 'LOEN_UD', 'FIN_UD'))
```

### Step 5: Assign result = value

```python
result = df.loc[('2013Q1', 1111), 'OMS']
```

### Step 6: Assign alt = value

```python
alt = df.loc[(a[0], 1111), 'OMS']
```

**Verification:**
```python
assert np.isnan(alt)
```

### Step 7: Assign alt = value

```python
alt = df.loc[('2013Q1', 1111), 'OMS']
```

**Verification:**
```python
assert np.isnan(alt)
```


## Complete Example

```python
# Workflow
a = pd.period_range('2013Q1', '2013Q4', freq='Q')
i = (1111, 2222, 3333)
idx = MultiIndex.from_product((a, i), names=('Period', 'CVR'))
df = DataFrame(index=idx, columns=('OMS', 'OMK', 'RES', 'DRIFT_IND', 'OEVRIG_IND', 'FIN_IND', 'VARE_UD', 'LOEN_UD', 'FIN_UD'))
result = df.loc[('2013Q1', 1111), 'OMS']
alt = df.loc[(a[0], 1111), 'OMS']
assert np.isnan(alt)
assert np.isnan(result)
alt = df.loc[('2013Q1', 1111), 'OMS']
assert np.isnan(alt)
```

## Next Steps


---

*Source: test_loc.py:607 | Complexity: Intermediate | Last updated: 2026-06-02*