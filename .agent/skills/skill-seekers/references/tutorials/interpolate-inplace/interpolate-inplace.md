# How To: Interpolate Inplace

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate inplace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series, using_array_manager, request
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series([1, np.nan, 2])
```

**Verification:**
```python
assert np.shares_memory(orig, obj.values)
```

### Step 2: Assign orig = value

```python
orig = obj.values
```

**Verification:**
```python
assert orig.squeeze()[1] == 1.5
```

### Step 3: Call obj.interpolate()

```python
obj.interpolate(inplace=True)
```

### Step 4: Assign expected = frame_or_series(...)

```python
expected = frame_or_series([1, 1.5, 2])
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(obj, expected)
```

**Verification:**
```python
assert np.shares_memory(orig, obj.values)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='.values-based in-place check is invalid')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, using_array_manager, request

# Workflow
if using_array_manager and frame_or_series is DataFrame:
    mark = pytest.mark.xfail(reason='.values-based in-place check is invalid')
    request.applymarker(mark)
obj = frame_or_series([1, np.nan, 2])
orig = obj.values
obj.interpolate(inplace=True)
expected = frame_or_series([1, 1.5, 2])
tm.assert_equal(obj, expected)
assert np.shares_memory(orig, obj.values)
assert orig.squeeze()[1] == 1.5
```

## Next Steps


---

*Source: test_interpolate.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*