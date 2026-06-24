# How To: Getitem Ndarray 3D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem ndarray 3d

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`

**Setup Required:**
```python
# Fixtures: index, frame_or_series, indexer_sli, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign obj = gen_obj(...)

```python
obj = gen_obj(frame_or_series, index)
```

### Step 2: Assign idxr = indexer_sli(...)

```python
idxr = indexer_sli(obj)
```

### Step 3: Assign nd3 = np.random.default_rng.integers(...)

```python
nd3 = np.random.default_rng(2).integers(5, size=(2, 2, 2))
```

### Step 4: Assign msgs = value

```python
msgs = []
```

### Step 5: Assign msg = unknown.join(...)

```python
msg = '|'.join(msgs)
```

### Step 6: Assign potential_errors = value

```python
potential_errors = (IndexError, ValueError, NotImplementedError)
```

### Step 7: Call msgs.append()

```python
msgs.append('Wrong number of dimensions. values.ndim > ndim \\[3 > 1\\]')
```

### Step 8: Call msgs.append()

```python
msgs.append('Buffer has wrong number of dimensions \\(expected 1, got 3\\)')
```

### Step 9: Call msgs.append()

```python
msgs.append('Cannot index with multidimensional key')
```

### Step 10: Call msgs.append()

```python
msgs.append('Index data must be 1-dimensional')
```

### Step 11: Call msgs.append()

```python
msgs.append('Index data must be 1-dimensional')
```

### Step 12: Call msgs.append()

```python
msgs.append('Data must be 1-dimensional')
```

### Step 13: Call msgs.append()

```python
msgs.append('positional indexers are out-of-bounds')
```

### Step 14: Call msgs.append()

```python
msgs.append('values must be a 1D array')
```

### Step 15: Call msgs.append()

```python
msgs.append('only handle 1-dimensional arrays')
```

### Step 16: idxr[nd3]

```python
idxr[nd3]
```

### Step 17: Call msgs.append()

```python
msgs.append('Passed array should be 1-dimensional')
```

### Step 18: Call msgs.append()

```python
msgs.append('indexer should be 1-dimensional')
```


## Complete Example

```python
# Setup
# Fixtures: index, frame_or_series, indexer_sli, using_array_manager

# Workflow
obj = gen_obj(frame_or_series, index)
idxr = indexer_sli(obj)
nd3 = np.random.default_rng(2).integers(5, size=(2, 2, 2))
msgs = []
if frame_or_series is Series and indexer_sli in [tm.setitem, tm.iloc]:
    msgs.append('Wrong number of dimensions. values.ndim > ndim \\[3 > 1\\]')
    if using_array_manager:
        msgs.append('Passed array should be 1-dimensional')
if frame_or_series is Series or indexer_sli is tm.iloc:
    msgs.append('Buffer has wrong number of dimensions \\(expected 1, got 3\\)')
    if using_array_manager:
        msgs.append('indexer should be 1-dimensional')
if indexer_sli is tm.loc or (frame_or_series is Series and indexer_sli is tm.setitem):
    msgs.append('Cannot index with multidimensional key')
if frame_or_series is DataFrame and indexer_sli is tm.setitem:
    msgs.append('Index data must be 1-dimensional')
if isinstance(index, pd.IntervalIndex) and indexer_sli is tm.iloc:
    msgs.append('Index data must be 1-dimensional')
if isinstance(index, (pd.TimedeltaIndex, pd.DatetimeIndex, pd.PeriodIndex)):
    msgs.append('Data must be 1-dimensional')
if len(index) == 0 or isinstance(index, pd.MultiIndex):
    msgs.append('positional indexers are out-of-bounds')
if type(index) is Index and (not isinstance(index._values, np.ndarray)):
    msgs.append('values must be a 1D array')
    msgs.append('only handle 1-dimensional arrays')
msg = '|'.join(msgs)
potential_errors = (IndexError, ValueError, NotImplementedError)
with pytest.raises(potential_errors, match=msg):
    idxr[nd3]
```

## Next Steps


---

*Source: test_indexing.py:78 | Complexity: Advanced | Last updated: 2026-06-02*