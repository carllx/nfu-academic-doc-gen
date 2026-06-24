# How To: Arrow Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`
- `pandas.core.arrays.arrow.extension_types`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

**Verification:**
```python
assert isinstance(result.type, ArrowIntervalType)
```

### Step 2: Assign intervals = value

```python
intervals = pd.interval_range(1, 5, freq=1).array
```

**Verification:**
```python
assert result.type.closed == intervals.closed
```

### Step 3: Assign result = pa.array(...)

```python
result = pa.array(intervals)
```

**Verification:**
```python
assert result.type.subtype == pa.int64()
```

### Step 4: Assign expected = pa.array(...)

```python
expected = pa.array([{'left': i, 'right': i + 1} for i in range(1, 5)])
```

**Verification:**
```python
assert result.storage.field('left').equals(pa.array([1, 2, 3, 4], type='int64'))
```

### Step 5: Assign result = pa.array(...)

```python
result = pa.array(intervals, type=expected.type)
```

**Verification:**
```python
assert result.storage.field('right').equals(pa.array([2, 3, 4, 5], type='int64'))
```

### Step 6: Call pa.array()

```python
pa.array(intervals, type='float64')
```

**Verification:**
```python
assert result.storage.equals(expected)
```

### Step 7: Call pa.array()

```python
pa.array(intervals, type=ArrowIntervalType(pa.float64(), 'left'))
```

**Verification:**
```python
assert result.equals(expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
from pandas.core.arrays.arrow.extension_types import ArrowIntervalType
intervals = pd.interval_range(1, 5, freq=1).array
result = pa.array(intervals)
assert isinstance(result.type, ArrowIntervalType)
assert result.type.closed == intervals.closed
assert result.type.subtype == pa.int64()
assert result.storage.field('left').equals(pa.array([1, 2, 3, 4], type='int64'))
assert result.storage.field('right').equals(pa.array([2, 3, 4, 5], type='int64'))
expected = pa.array([{'left': i, 'right': i + 1} for i in range(1, 5)])
assert result.storage.equals(expected)
result = pa.array(intervals, type=expected.type)
assert result.equals(expected)
with pytest.raises(TypeError, match='Not supported to convert IntervalArray'):
    pa.array(intervals, type='float64')
with pytest.raises(TypeError, match='Not supported to convert IntervalArray'):
    pa.array(intervals, type=ArrowIntervalType(pa.float64(), 'left'))
```

## Next Steps


---

*Source: test_interval_pyarrow.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*