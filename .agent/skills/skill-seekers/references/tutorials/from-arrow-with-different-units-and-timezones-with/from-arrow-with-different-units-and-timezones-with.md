# How To: From Arrow With Different Units And Timezones With

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from arrow with different units and timezones with

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: pa_unit, pd_unit, pa_tz, pd_tz, data
```

## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign pa_type = pa.timestamp(...)

```python
pa_type = pa.timestamp(pa_unit, tz=pa_tz)
```

### Step 3: Assign arr = pa.array(...)

```python
arr = pa.array(data, type=pa_type)
```

### Step 4: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype(unit=pd_unit, tz=pd_tz)
```

### Step 5: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(arr)
```

### Step 6: Assign expected = DatetimeArray._from_sequence.astype(...)

```python
expected = DatetimeArray._from_sequence(data, dtype=f'M8[{pa_unit}, UTC]').astype(dtype, copy=False)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 8: Assign result = dtype.__from_arrow__(...)

```python
result = dtype.__from_arrow__(pa.chunked_array([arr]))
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: pa_unit, pd_unit, pa_tz, pd_tz, data

# Workflow
pa = pytest.importorskip('pyarrow')
pa_type = pa.timestamp(pa_unit, tz=pa_tz)
arr = pa.array(data, type=pa_type)
dtype = DatetimeTZDtype(unit=pd_unit, tz=pd_tz)
result = dtype.__from_arrow__(arr)
expected = DatetimeArray._from_sequence(data, dtype=f'M8[{pa_unit}, UTC]').astype(dtype, copy=False)
tm.assert_extension_array_equal(result, expected)
result = dtype.__from_arrow__(pa.chunked_array([arr]))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:226 | Complexity: Advanced | Last updated: 2026-06-02*