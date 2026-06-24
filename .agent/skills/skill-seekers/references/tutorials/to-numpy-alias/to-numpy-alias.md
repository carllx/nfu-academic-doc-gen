# How To: To Numpy Alias

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numpy alias

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign expected = NaT.to_datetime64(...)

```python
expected = NaT.to_datetime64()
```

**Verification:**
```python
assert isna(expected) and isna(result)
```

### Step 2: Assign result = NaT.to_numpy(...)

```python
result = NaT.to_numpy()
```

**Verification:**
```python
assert isinstance(result, np.datetime64)
```

### Step 3: Assign result = NaT.to_numpy(...)

```python
result = NaT.to_numpy('M8[s]')
```

**Verification:**
```python
assert result.dtype == 'M8[s]'
```

### Step 4: Assign result = NaT.to_numpy(...)

```python
result = NaT.to_numpy('m8[ns]')
```

**Verification:**
```python
assert isinstance(result, np.timedelta64)
```

### Step 5: Assign result = NaT.to_numpy(...)

```python
result = NaT.to_numpy('m8[s]')
```

**Verification:**
```python
assert result.dtype == 'm8[ns]'
```

### Step 6: Call NaT.to_numpy()

```python
NaT.to_numpy(np.int64)
```

**Verification:**
```python
assert isinstance(result, np.timedelta64)
```


## Complete Example

```python
# Workflow
expected = NaT.to_datetime64()
result = NaT.to_numpy()
assert isna(expected) and isna(result)
result = NaT.to_numpy('M8[s]')
assert isinstance(result, np.datetime64)
assert result.dtype == 'M8[s]'
result = NaT.to_numpy('m8[ns]')
assert isinstance(result, np.timedelta64)
assert result.dtype == 'm8[ns]'
result = NaT.to_numpy('m8[s]')
assert isinstance(result, np.timedelta64)
assert result.dtype == 'm8[s]'
with pytest.raises(ValueError, match='NaT.to_numpy dtype must be a '):
    NaT.to_numpy(np.int64)
```

## Next Steps


---

*Source: test_nat.py:510 | Complexity: Intermediate | Last updated: 2026-06-02*