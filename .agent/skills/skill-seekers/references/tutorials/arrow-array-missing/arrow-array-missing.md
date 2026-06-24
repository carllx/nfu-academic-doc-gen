# How To: Arrow Array Missing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow array missing

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

### Step 2: Assign arr = IntervalArray.from_breaks(...)

```python
arr = IntervalArray.from_breaks([0.0, 1.0, 2.0, 3.0])
```

**Verification:**
```python
assert result.type.closed == arr.closed
```

### Step 3: Assign unknown = None

```python
arr[1] = None
```

**Verification:**
```python
assert result.type.subtype == pa.float64()
```

### Step 4: Assign result = pa.array(...)

```python
result = pa.array(arr)
```

**Verification:**
```python
assert result.storage.field('left').equals(left)
```

### Step 5: Assign left = pa.array(...)

```python
left = pa.array([0.0, None, 2.0], type='float64')
```

**Verification:**
```python
assert result.storage.field('right').equals(right)
```

### Step 6: Assign right = pa.array(...)

```python
right = pa.array([1.0, None, 3.0], type='float64')
```

**Verification:**
```python
assert result.storage.equals(expected)
```

### Step 7: Assign vals = value

```python
vals = [{'left': 0.0, 'right': 1.0}, {'left': None, 'right': None}, {'left': 2.0, 'right': 3.0}]
```

### Step 8: Assign expected = pa.StructArray.from_pandas(...)

```python
expected = pa.StructArray.from_pandas(vals, mask=np.array([False, True, False]))
```

**Verification:**
```python
assert result.storage.equals(expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
from pandas.core.arrays.arrow.extension_types import ArrowIntervalType
arr = IntervalArray.from_breaks([0.0, 1.0, 2.0, 3.0])
arr[1] = None
result = pa.array(arr)
assert isinstance(result.type, ArrowIntervalType)
assert result.type.closed == arr.closed
assert result.type.subtype == pa.float64()
left = pa.array([0.0, None, 2.0], type='float64')
right = pa.array([1.0, None, 3.0], type='float64')
assert result.storage.field('left').equals(left)
assert result.storage.field('right').equals(right)
vals = [{'left': 0.0, 'right': 1.0}, {'left': None, 'right': None}, {'left': 2.0, 'right': 3.0}]
expected = pa.StructArray.from_pandas(vals, mask=np.array([False, True, False]))
assert result.storage.equals(expected)
```

## Next Steps


---

*Source: test_interval_pyarrow.py:54 | Complexity: Advanced | Last updated: 2026-06-02*