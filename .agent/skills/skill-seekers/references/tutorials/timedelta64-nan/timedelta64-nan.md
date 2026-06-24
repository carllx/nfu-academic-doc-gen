# How To: Timedelta64 Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta64 nan

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign td = Series(...)

```python
td = Series([timedelta(days=i) for i in range(10)])
```

**Verification:**
```python
assert isna(td1[0])
```

### Step 2: Assign td1 = td.copy(...)

```python
td1 = td.copy()
```

**Verification:**
```python
assert td1[0]._value == iNaT
```

### Step 3: Assign unknown = value

```python
td1[0] = np.nan
```

**Verification:**
```python
assert not isna(td1[0])
```

### Step 4: Assign unknown = value

```python
td1[0] = td[0]
```

**Verification:**
```python
assert not isna(td1[1])
```

### Step 5: Assign unknown = value

```python
td1[1] = td[1]
```

**Verification:**
```python
assert td1.dtype == np.object_
```

### Step 6: Assign unknown = NaT

```python
td1[2] = NaT
```

**Verification:**
```python
assert td1[1] == iNaT
```

### Step 7: Assign unknown = value

```python
td1[2] = td[2]
```

**Verification:**
```python
assert not isna(td1[1])
```

### Step 8: Assign td3 = np.timedelta64(...)

```python
td3 = np.timedelta64(timedelta(days=3))
```

**Verification:**
```python
assert isna(td1[2])
```

### Step 9: Assign td7 = np.timedelta64(...)

```python
td7 = np.timedelta64(timedelta(days=7))
```

**Verification:**
```python
assert td1[2]._value == iNaT
```

### Step 10: Assign unknown = value

```python
td[(td > td3) & (td < td7)] = np.nan
```

**Verification:**
```python
assert not isna(td1[2])
```

### Step 11: Assign unknown = iNaT

```python
td1[1] = iNaT
```

**Verification:**
```python
assert isna(td).sum() == 3
```


## Complete Example

```python
# Workflow
td = Series([timedelta(days=i) for i in range(10)])
td1 = td.copy()
td1[0] = np.nan
assert isna(td1[0])
assert td1[0]._value == iNaT
td1[0] = td[0]
assert not isna(td1[0])
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    td1[1] = iNaT
assert not isna(td1[1])
assert td1.dtype == np.object_
assert td1[1] == iNaT
td1[1] = td[1]
assert not isna(td1[1])
td1[2] = NaT
assert isna(td1[2])
assert td1[2]._value == iNaT
td1[2] = td[2]
assert not isna(td1[2])
td3 = np.timedelta64(timedelta(days=3))
td7 = np.timedelta64(timedelta(days=7))
td[(td > td3) & (td < td7)] = np.nan
assert isna(td).sum() == 3
```

## Next Steps


---

*Source: test_missing.py:40 | Complexity: Advanced | Last updated: 2026-06-02*