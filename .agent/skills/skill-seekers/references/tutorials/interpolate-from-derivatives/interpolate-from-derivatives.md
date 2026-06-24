# How To: Interpolate From Derivatives

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate from derivatives

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([10, 11, 12, 13])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0], index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]))
```

### Step 4: Assign new_index = ser.index.union.astype(...)

```python
new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(float)
```

### Step 5: Assign interp_s = ser.reindex.interpolate(...)

```python
interp_s = ser.reindex(new_index).interpolate(method='from_derivatives')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(interp_s.loc[1:3], expected)
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
ser = Series([10, 11, 12, 13])
expected = Series([11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0], index=Index([1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]))
new_index = ser.index.union(Index([1.25, 1.5, 1.75, 2.25, 2.5, 2.75])).astype(float)
interp_s = ser.reindex(new_index).interpolate(method='from_derivatives')
tm.assert_series_equal(interp_s.loc[1:3], expected)
```

## Next Steps


---

*Source: test_interpolate.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*