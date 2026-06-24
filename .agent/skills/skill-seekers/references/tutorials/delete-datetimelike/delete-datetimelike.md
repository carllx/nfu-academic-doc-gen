# How To: Delete Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete datetimelike

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.internals`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.internals`
- `pandas.core.internals.blocks`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape.view(...)

```python
arr = np.arange(20, dtype='i8').reshape(5, 4).view('m8[ns]')
```

**Verification:**
```python
assert isinstance(blk.values, TimedeltaArray)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

**Verification:**
```python
assert len(nb) == 2
```

### Step 3: Assign blk = value

```python
blk = df._mgr.blocks[0]
```

**Verification:**
```python
assert isinstance(nb[0].values, TimedeltaArray)
```

### Step 4: Assign nb = blk.delete(...)

```python
nb = blk.delete(1)
```

**Verification:**
```python
assert isinstance(nb[1].values, TimedeltaArray)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(arr.view('M8[ns]'))
```

**Verification:**
```python
assert isinstance(blk.values, DatetimeArray)
```

### Step 6: Assign blk = value

```python
blk = df._mgr.blocks[0]
```

**Verification:**
```python
assert len(nb) == 2
```

### Step 7: Assign nb = blk.delete(...)

```python
nb = blk.delete([1, 3])
```

**Verification:**
```python
assert isinstance(nb[0].values, DatetimeArray)
```


## Complete Example

```python
# Workflow
arr = np.arange(20, dtype='i8').reshape(5, 4).view('m8[ns]')
df = DataFrame(arr)
blk = df._mgr.blocks[0]
assert isinstance(blk.values, TimedeltaArray)
nb = blk.delete(1)
assert len(nb) == 2
assert isinstance(nb[0].values, TimedeltaArray)
assert isinstance(nb[1].values, TimedeltaArray)
df = DataFrame(arr.view('M8[ns]'))
blk = df._mgr.blocks[0]
assert isinstance(blk.values, DatetimeArray)
nb = blk.delete([1, 3])
assert len(nb) == 2
assert isinstance(nb[0].values, DatetimeArray)
assert isinstance(nb[1].values, DatetimeArray)
```

## Next Steps


---

*Source: test_internals.py:330 | Complexity: Intermediate | Last updated: 2026-06-02*