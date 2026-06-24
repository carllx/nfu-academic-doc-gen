# How To: Quantile Multi

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile multi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: interp_method, request, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign unknown = interp_method

```python
interpolation, method = interp_method
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=['a', 'b', 'c'])
```

### Step 3: Assign result = df.quantile(...)

```python
result = df.quantile([0.25, 0.5], interpolation=interpolation, method=method)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.5, 1.5, 1.5], [2.0, 2.0, 2.0]], index=[0.25, 0.5], columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=['a', 'b', 'c'])
result = df.quantile([0.25, 0.5], interpolation=interpolation, method=method)
expected = DataFrame([[1.5, 1.5, 1.5], [2.0, 2.0, 2.0]], index=[0.25, 0.5], columns=['a', 'b', 'c'])
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:317 | Complexity: Intermediate | Last updated: 2026-06-02*