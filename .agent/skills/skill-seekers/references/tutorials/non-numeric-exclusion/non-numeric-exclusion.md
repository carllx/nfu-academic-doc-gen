# How To: Non Numeric Exclusion

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non numeric exclusion

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
df = DataFrame({'col1': ['A', 'A', 'B', 'B'], 'col2': [1, 2, 3, 4]})
```

### Step 3: Assign rs = df.quantile(...)

```python
rs = df.quantile(0.5, numeric_only=True, interpolation=interpolation, method=method)
```

### Step 4: Assign xp = df.median.rename(...)

```python
xp = df.median(numeric_only=True).rename(0.5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, xp)
```

### Step 6: Assign xp = unknown.astype(...)

```python
xp = (xp + 0.5).astype(np.int64)
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
df = DataFrame({'col1': ['A', 'A', 'B', 'B'], 'col2': [1, 2, 3, 4]})
rs = df.quantile(0.5, numeric_only=True, interpolation=interpolation, method=method)
xp = df.median(numeric_only=True).rename(0.5)
if interpolation == 'nearest':
    xp = (xp + 0.5).astype(np.int64)
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_series_equal(rs, xp)
```

## Next Steps


---

*Source: test_quantile.py:102 | Complexity: Intermediate | Last updated: 2026-06-02*