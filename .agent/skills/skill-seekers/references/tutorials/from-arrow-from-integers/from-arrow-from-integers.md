# How To: From Arrow From Integers

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from arrow from integers

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign data = value

```python
data = [0, 123456789, None, 2 ** 63 - 1, iNaT, -123456789]
```

### Step 3: Assign arr = pa.array(...)

```python
arr = pa.array(data)
```

### Step 4: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype(unit='ns', tz='UTC')
```

### Step 5: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(arr)
```

### Step 6: Assign expected = DatetimeArray._from_sequence(...)

```python
expected = DatetimeArray._from_sequence(np.array(data, dtype='datetime64[ns]'))
```

### Step 7: Assign expected = expected.tz_localize(...)

```python
expected = expected.tz_localize('UTC')
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 9: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(pa.chunked_array([arr]))
```

### Step 10: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
data = [0, 123456789, None, 2 ** 63 - 1, iNaT, -123456789]
arr = pa.array(data)
dtype = DatetimeTZDtype(unit='ns', tz='UTC')
result = dtype.__from_arrow__(arr)
expected = DatetimeArray._from_sequence(np.array(data, dtype='datetime64[ns]'))
expected = expected.tz_localize('UTC')
tm.assert_extension_array_equal(result, expected)
result = dtype.__from_arrow__(pa.chunked_array([arr]))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:271 | Complexity: Advanced | Last updated: 2026-06-02*