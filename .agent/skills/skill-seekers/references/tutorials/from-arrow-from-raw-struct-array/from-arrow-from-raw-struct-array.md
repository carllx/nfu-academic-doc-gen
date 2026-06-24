# How To: From Arrow From Raw Struct Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from arrow from raw struct array

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

### Step 2: Assign arr = pa.array(...)

```python
arr = pa.array([{'left': 0, 'right': 1}, {'left': 1, 'right': 2}])
```

### Step 3: Assign dtype = pd.IntervalDtype(...)

```python
dtype = pd.IntervalDtype(np.dtype('int64'), closed='neither')
```

### Step 4: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(arr)
```

### Step 5: Assign expected = IntervalArray.from_breaks(...)

```python
expected = IntervalArray.from_breaks(np.array([0, 1, 2], dtype='int64'), closed='neither')
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 7: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(pa.chunked_array([arr]))
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
arr = pa.array([{'left': 0, 'right': 1}, {'left': 1, 'right': 2}])
dtype = pd.IntervalDtype(np.dtype('int64'), closed='neither')
result = dtype.__from_arrow__(arr)
expected = IntervalArray.from_breaks(np.array([0, 1, 2], dtype='int64'), closed='neither')
tm.assert_extension_array_equal(result, expected)
result = dtype.__from_arrow__(pa.chunked_array([arr]))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_pyarrow.py:144 | Complexity: Advanced | Last updated: 2026-06-02*