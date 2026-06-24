# How To: From Td64Nat Sequence Raises

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from td64nat sequence raises

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign td = pd.NaT.to_numpy(...)

```python
td = pd.NaT.to_numpy('m8[ns]')
```

### Step 2: Assign dtype = value

```python
dtype = pd.period_range('2005-01-01', periods=3, freq='D').dtype
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([None], dtype=object)
```

### Step 4: Assign unknown = td

```python
arr[0] = td
```

### Step 5: Assign msg = 'Value must be Period, string, integer, or datetime'

```python
msg = 'Value must be Period, string, integer, or datetime'
```

### Step 6: Call PeriodArray._from_sequence()

```python
PeriodArray._from_sequence(arr, dtype=dtype)
```

### Step 7: Call pd.PeriodIndex()

```python
pd.PeriodIndex(arr, dtype=dtype)
```

### Step 8: Call pd.Index()

```python
pd.Index(arr, dtype=dtype)
```

### Step 9: Call pd.array()

```python
pd.array(arr, dtype=dtype)
```

### Step 10: Call pd.Series()

```python
pd.Series(arr, dtype=dtype)
```

### Step 11: Call pd.DataFrame()

```python
pd.DataFrame(arr, dtype=dtype)
```


## Complete Example

```python
# Workflow
td = pd.NaT.to_numpy('m8[ns]')
dtype = pd.period_range('2005-01-01', periods=3, freq='D').dtype
arr = np.array([None], dtype=object)
arr[0] = td
msg = 'Value must be Period, string, integer, or datetime'
with pytest.raises(ValueError, match=msg):
    PeriodArray._from_sequence(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.PeriodIndex(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.Index(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.array(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.Series(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.DataFrame(arr, dtype=dtype)
```

## Next Steps


---

*Source: test_constructors.py:113 | Complexity: Advanced | Last updated: 2026-06-02*