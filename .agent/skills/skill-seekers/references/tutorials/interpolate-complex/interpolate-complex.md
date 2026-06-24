# How To: Interpolate Complex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate complex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([complex('1+1j'), float('nan'), complex('2+2j')])
```

**Verification:**
```python
assert ser.dtype.kind == 'c'
```

### Step 2: Assign res = ser.interpolate(...)

```python
res = ser.interpolate()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([ser[0], ser[0] * 1.5, ser[2]])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 5: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 6: Assign res = df.interpolate(...)

```python
res = df.interpolate()
```

### Step 7: Assign expected = expected.to_frame(...)

```python
expected = expected.to_frame()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
ser = Series([complex('1+1j'), float('nan'), complex('2+2j')])
assert ser.dtype.kind == 'c'
res = ser.interpolate()
expected = Series([ser[0], ser[0] * 1.5, ser[2]])
tm.assert_series_equal(res, expected)
df = ser.to_frame()
res = df.interpolate()
expected = expected.to_frame()
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_interpolate.py:20 | Complexity: Advanced | Last updated: 2026-06-02*