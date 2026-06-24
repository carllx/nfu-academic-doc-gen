# How To: Setitem Bool Int Float Consistency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem bool int float consistency

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `os`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: indexer_sli
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(0, index=range(3), dtype=np.int64)
```

**Verification:**
```python
assert ser.dtype == object
```

### Step 2: Assign unknown = np.float64(...)

```python
indexer_sli(ser)[0] = np.float64(1.0)
```

**Verification:**
```python
assert ser.dtype == object
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(0, index=range(3), dtype=np.float64)
```

**Verification:**
```python
assert ser.dtype == np.int64
```

### Step 4: Assign unknown = np.int64(...)

```python
indexer_sli(ser)[0] = np.int64(1)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(0, index=range(3), dtype=dtype)
```

**Verification:**
```python
assert ser.dtype == object
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(0, index=range(3), dtype=bool)
```

**Verification:**
```python
assert ser.dtype == object
```

### Step 7: Assign unknown = True

```python
indexer_sli(ser)[0] = True
```

### Step 8: Assign unknown = dtype(...)

```python
ser[0] = dtype(1)
```


## Complete Example

```python
# Setup
# Fixtures: indexer_sli

# Workflow
for dtype in [np.float64, np.int64]:
    ser = Series(0, index=range(3), dtype=dtype)
    with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
        indexer_sli(ser)[0] = True
    assert ser.dtype == object
    ser = Series(0, index=range(3), dtype=bool)
    with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
        ser[0] = dtype(1)
    assert ser.dtype == object
ser = Series(0, index=range(3), dtype=np.int64)
indexer_sli(ser)[0] = np.float64(1.0)
assert ser.dtype == np.int64
ser = Series(0, index=range(3), dtype=np.float64)
indexer_sli(ser)[0] = np.int64(1)
```

## Next Steps


---

*Source: test_setitem.py:1697 | Complexity: Advanced | Last updated: 2026-06-02*