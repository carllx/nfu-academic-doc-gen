# How To: Object Casting Indexing Wraps Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test object casting indexing wraps datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2], 'B': date_range('2000', periods=2), 'C': pd.timedelta_range('1 Day', periods=2)})
```

**Verification:**
```python
assert isinstance(ser.values[1], Timestamp)
```

### Step 2: Assign ser = value

```python
ser = df.loc[0]
```

**Verification:**
```python
assert isinstance(ser.values[2], pd.Timedelta)
```

### Step 3: Assign ser = value

```python
ser = df.iloc[0]
```

**Verification:**
```python
assert isinstance(ser.values[1], Timestamp)
```

### Step 4: Assign ser = df.xs(...)

```python
ser = df.xs(0, axis=0)
```

**Verification:**
```python
assert isinstance(ser.values[2], pd.Timedelta)
```

### Step 5: Assign mgr = value

```python
mgr = df._mgr
```

**Verification:**
```python
assert isinstance(ser.values[1], Timestamp)
```

### Step 6: Call mgr._rebuild_blknos_and_blklocs()

```python
mgr._rebuild_blknos_and_blklocs()
```

**Verification:**
```python
assert isinstance(ser.values[2], pd.Timedelta)
```

### Step 7: Assign arr = value

```python
arr = mgr.fast_xs(0).array
```

**Verification:**
```python
assert isinstance(arr[1], Timestamp)
```

### Step 8: Assign blk = value

```python
blk = mgr.blocks[mgr.blknos[1]]
```

**Verification:**
```python
assert isinstance(arr[2], pd.Timedelta)
```

### Step 9: Assign val = blk.iget(...)

```python
val = blk.iget((0, 0))
```

**Verification:**
```python
assert blk.dtype == 'M8[ns]'
```

### Step 10: Assign blk = value

```python
blk = mgr.blocks[mgr.blknos[2]]
```

**Verification:**
```python
assert isinstance(val, Timestamp)
```

### Step 11: Assign val = blk.iget(...)

```python
val = blk.iget((0, 0))
```

**Verification:**
```python
assert blk.dtype == 'm8[ns]'
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
df = DataFrame({'A': [1, 2], 'B': date_range('2000', periods=2), 'C': pd.timedelta_range('1 Day', periods=2)})
ser = df.loc[0]
assert isinstance(ser.values[1], Timestamp)
assert isinstance(ser.values[2], pd.Timedelta)
ser = df.iloc[0]
assert isinstance(ser.values[1], Timestamp)
assert isinstance(ser.values[2], pd.Timedelta)
ser = df.xs(0, axis=0)
assert isinstance(ser.values[1], Timestamp)
assert isinstance(ser.values[2], pd.Timedelta)
if using_array_manager:
    return
mgr = df._mgr
mgr._rebuild_blknos_and_blklocs()
arr = mgr.fast_xs(0).array
assert isinstance(arr[1], Timestamp)
assert isinstance(arr[2], pd.Timedelta)
blk = mgr.blocks[mgr.blknos[1]]
assert blk.dtype == 'M8[ns]'
val = blk.iget((0, 0))
assert isinstance(val, Timestamp)
blk = mgr.blocks[mgr.blknos[2]]
assert blk.dtype == 'm8[ns]'
val = blk.iget((0, 0))
assert isinstance(val, pd.Timedelta)
```

## Next Steps


---

*Source: test_indexing.py:1633 | Complexity: Advanced | Last updated: 2026-06-02*