# How To: Quantile Date Range

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile date range

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

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(ser)
```

### Step 5: Assign result = df.quantile(...)

```python
result = df.quantile(numeric_only=False, interpolation=interpolation, method=method)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['2016-01-02 00:00:00'], name=0.5, dtype='datetime64[ns, US/Pacific]')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
ser = Series(dti)
df = DataFrame(ser)
result = df.quantile(numeric_only=False, interpolation=interpolation, method=method)
expected = Series(['2016-01-02 00:00:00'], name=0.5, dtype='datetime64[ns, US/Pacific]')
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:155 | Complexity: Advanced | Last updated: 2026-06-02*