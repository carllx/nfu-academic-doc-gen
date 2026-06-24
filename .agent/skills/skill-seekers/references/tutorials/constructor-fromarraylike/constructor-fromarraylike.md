# How To: Constructor Fromarraylike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor fromarraylike

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2007-01', periods=20, freq='M')
```

**Verification:**
```python
assert result.freq == 'ME'
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(PeriodIndex(idx.values), idx)
```

**Verification:**
```python
assert result.freq == '2ME'
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(PeriodIndex(list(idx.values)), idx)
```

**Verification:**
```python
assert result.freq == '2ME'
```

### Step 4: Assign msg = 'freq not specified and cannot be inferred'

```python
msg = 'freq not specified and cannot be inferred'
```

### Step 5: Assign msg = "'Period' object is not iterable"

```python
msg = "'Period' object is not iterable"
```

### Step 6: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(iter(idx))
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 8: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 10: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx, freq='M')
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 12: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx, freq=offsets.MonthEnd())
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

**Verification:**
```python
assert result.freq == 'ME'
```

### Step 14: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx, freq='2M')
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx.asfreq('2M'))
```

**Verification:**
```python
assert result.freq == '2ME'
```

### Step 16: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx, freq=offsets.MonthEnd(2))
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx.asfreq('2M'))
```

**Verification:**
```python
assert result.freq == '2ME'
```

### Step 18: Assign result = PeriodIndex(...)

```python
result = PeriodIndex(idx, freq='D')
```

### Step 19: Assign exp = idx.asfreq(...)

```python
exp = idx.asfreq('D', 'e')
```

### Step 20: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 21: Call PeriodIndex()

```python
PeriodIndex(idx.asi8)
```

### Step 22: Call PeriodIndex()

```python
PeriodIndex(list(idx.asi8))
```

### Step 23: Call PeriodIndex()

```python
PeriodIndex(data=Period('2007', freq='Y'))
```


## Complete Example

```python
# Workflow
idx = period_range('2007-01', periods=20, freq='M')
tm.assert_index_equal(PeriodIndex(idx.values), idx)
tm.assert_index_equal(PeriodIndex(list(idx.values)), idx)
msg = 'freq not specified and cannot be inferred'
with pytest.raises(ValueError, match=msg):
    PeriodIndex(idx.asi8)
with pytest.raises(ValueError, match=msg):
    PeriodIndex(list(idx.asi8))
msg = "'Period' object is not iterable"
with pytest.raises(TypeError, match=msg):
    PeriodIndex(data=Period('2007', freq='Y'))
result = PeriodIndex(iter(idx))
tm.assert_index_equal(result, idx)
result = PeriodIndex(idx)
tm.assert_index_equal(result, idx)
result = PeriodIndex(idx, freq='M')
tm.assert_index_equal(result, idx)
result = PeriodIndex(idx, freq=offsets.MonthEnd())
tm.assert_index_equal(result, idx)
assert result.freq == 'ME'
result = PeriodIndex(idx, freq='2M')
tm.assert_index_equal(result, idx.asfreq('2M'))
assert result.freq == '2ME'
result = PeriodIndex(idx, freq=offsets.MonthEnd(2))
tm.assert_index_equal(result, idx.asfreq('2M'))
assert result.freq == '2ME'
result = PeriodIndex(idx, freq='D')
exp = idx.asfreq('D', 'e')
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_constructors.py:247 | Complexity: Advanced | Last updated: 2026-06-02*