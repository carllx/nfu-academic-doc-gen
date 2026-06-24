# How To: Where Period Invalid Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where period invalid na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: frame_or_series, as_cat, request
```

## Step-by-Step Guide

### Step 1: Assign idx = pd.period_range(...)

```python
idx = pd.period_range('2016-01-01', periods=3, freq='D')
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(idx)
```

### Step 3: Assign tdnat = pd.NaT.to_numpy(...)

```python
tdnat = pd.NaT.to_numpy('m8[ns]')
```

### Step 4: Assign mask = value

```python
mask = np.array([True, True, False], ndmin=obj.ndim).T
```

### Step 5: Assign idx = idx.astype(...)

```python
idx = idx.astype('category')
```

### Step 6: Assign msg = 'Cannot setitem on a Categorical with a new category \\(NaT\\), set the categories first'

```python
msg = 'Cannot setitem on a Categorical with a new category \\(NaT\\), set the categories first'
```

### Step 7: Assign msg = "value should be a 'Period'"

```python
msg = "value should be a 'Period'"
```

### Step 8: Assign expected = obj.astype.where(...)

```python
expected = obj.astype(object).where(mask, tdnat)
```

### Step 9: Assign result = obj.where(...)

```python
result = obj.where(mask, tdnat)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 11: Assign expected = obj.astype.mask(...)

```python
expected = obj.astype(object).mask(mask, tdnat)
```

### Step 12: Assign result = obj.mask(...)

```python
result = obj.mask(mask, tdnat)
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 14: Call tm.assert_equal()

```python
tm.assert_equal(obj, expected)
```

### Step 15: Call obj.where()

```python
obj.where(mask, tdnat)
```

### Step 16: Call obj.mask()

```python
obj.mask(mask, tdnat)
```

### Step 17: Call obj.mask()

```python
obj.mask(mask, tdnat, inplace=True)
```

### Step 18: Call obj.mask()

```python
obj.mask(mask, tdnat, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, as_cat, request

# Workflow
idx = pd.period_range('2016-01-01', periods=3, freq='D')
if as_cat:
    idx = idx.astype('category')
obj = frame_or_series(idx)
tdnat = pd.NaT.to_numpy('m8[ns]')
mask = np.array([True, True, False], ndmin=obj.ndim).T
if as_cat:
    msg = 'Cannot setitem on a Categorical with a new category \\(NaT\\), set the categories first'
else:
    msg = "value should be a 'Period'"
if as_cat:
    with pytest.raises(TypeError, match=msg):
        obj.where(mask, tdnat)
    with pytest.raises(TypeError, match=msg):
        obj.mask(mask, tdnat)
    with pytest.raises(TypeError, match=msg):
        obj.mask(mask, tdnat, inplace=True)
else:
    expected = obj.astype(object).where(mask, tdnat)
    result = obj.where(mask, tdnat)
    tm.assert_equal(result, expected)
    expected = obj.astype(object).mask(mask, tdnat)
    result = obj.mask(mask, tdnat)
    tm.assert_equal(result, expected)
    with tm.assert_produces_warning(FutureWarning, match='Setting an item of incompatible dtype'):
        obj.mask(mask, tdnat, inplace=True)
    tm.assert_equal(obj, expected)
```

## Next Steps


---

*Source: test_where.py:924 | Complexity: Advanced | Last updated: 2026-06-02*