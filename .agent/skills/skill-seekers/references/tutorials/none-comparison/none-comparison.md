# How To: None Comparison

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test none comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`

**Setup Required:**
```python
# Fixtures: request, series_with_simple_index
```

## Step-by-Step Guide

### Step 1: Assign series = series_with_simple_index

```python
series = series_with_simple_index
```

**Verification:**
```python
assert not result.iat[0]
```

### Step 2: Assign unknown = value

```python
series.iloc[0] = np.nan
```

**Verification:**
```python
assert not result.iat[1]
```

### Step 3: Assign result = value

```python
result = series == None
```

**Verification:**
```python
assert result.iat[0]
```

### Step 4: Assign result = value

```python
result = series != None
```

**Verification:**
```python
assert result.iat[1]
```

### Step 5: Assign result = value

```python
result = None == series
```

**Verification:**
```python
assert not result.iat[0]
```

### Step 6: Assign result = value

```python
result = None != series
```

**Verification:**
```python
assert not result.iat[1]
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason="Test doesn't make sense on empty data"))
```

**Verification:**
```python
assert result.iat[0]
```

### Step 8: Assign msg = 'Invalid comparison'

```python
msg = 'Invalid comparison'
```

**Verification:**
```python
assert result.iat[1]
```

### Step 9: Assign result = value

```python
result = None > series
```

**Verification:**
```python
assert not result.iat[0]
```

### Step 10: Assign result = value

```python
result = series < None
```

**Verification:**
```python
assert not result.iat[1]
```

### Step 11: None > series

```python
None > series
```

**Verification:**
```python
assert not result.iat[0]
```

### Step 12: series > None

```python
series > None
```

**Verification:**
```python
assert not result.iat[1]
```


## Complete Example

```python
# Setup
# Fixtures: request, series_with_simple_index

# Workflow
series = series_with_simple_index
if len(series) < 1:
    request.applymarker(pytest.mark.xfail(reason="Test doesn't make sense on empty data"))
series.iloc[0] = np.nan
result = series == None
assert not result.iat[0]
assert not result.iat[1]
result = series != None
assert result.iat[0]
assert result.iat[1]
result = None == series
assert not result.iat[0]
assert not result.iat[1]
result = None != series
assert result.iat[0]
assert result.iat[1]
if lib.is_np_dtype(series.dtype, 'M') or isinstance(series.dtype, DatetimeTZDtype):
    msg = 'Invalid comparison'
    with pytest.raises(TypeError, match=msg):
        None > series
    with pytest.raises(TypeError, match=msg):
        series > None
else:
    result = None > series
    assert not result.iat[0]
    assert not result.iat[1]
    result = series < None
    assert not result.iat[0]
    assert not result.iat[1]
```

## Next Steps


---

*Source: test_arithmetic.py:895 | Complexity: Advanced | Last updated: 2026-06-02*