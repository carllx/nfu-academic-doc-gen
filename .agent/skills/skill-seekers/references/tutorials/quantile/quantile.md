# How To: Quantile

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile

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
# Fixtures: datetime_frame, interp_method, using_array_manager, request
```

## Step-by-Step Guide

### Step 1: Assign unknown = interp_method

```python
interpolation, method = interp_method
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign df = datetime_frame

```python
df = datetime_frame
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 3: Assign result = df.quantile(...)

```python
result = df.quantile(0.1, axis=0, numeric_only=True, interpolation=interpolation, method=method)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([np.percentile(df[col], 10) for col in df.columns], index=df.columns, name=0.1)
```

### Step 5: Assign result = df.quantile(...)

```python
result = df.quantile(0.9, axis=1, numeric_only=True, interpolation=interpolation, method=method)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([np.percentile(df.loc[date], 90) for date in df.index], index=df.index, name=0.9)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected.index)
```

### Step 9: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(using_array_manager, reason='Name set incorrectly for arraymanager'))
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected.index)
```

### Step 12: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(using_array_manager, reason='Name set incorrectly for arraymanager'))
```

**Verification:**
```python
assert result.name == expected.name
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame, interp_method, using_array_manager, request

# Workflow
interpolation, method = interp_method
df = datetime_frame
result = df.quantile(0.1, axis=0, numeric_only=True, interpolation=interpolation, method=method)
expected = Series([np.percentile(df[col], 10) for col in df.columns], index=df.columns, name=0.1)
if interpolation == 'linear':
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result.index, expected.index)
    request.applymarker(pytest.mark.xfail(using_array_manager, reason='Name set incorrectly for arraymanager'))
    assert result.name == expected.name
result = df.quantile(0.9, axis=1, numeric_only=True, interpolation=interpolation, method=method)
expected = Series([np.percentile(df.loc[date], 90) for date in df.index], index=df.index, name=0.9)
if interpolation == 'linear':
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result.index, expected.index)
    request.applymarker(pytest.mark.xfail(using_array_manager, reason='Name set incorrectly for arraymanager'))
    assert result.name == expected.name
```

## Next Steps


---

*Source: test_quantile.py:50 | Complexity: Advanced | Last updated: 2026-06-02*