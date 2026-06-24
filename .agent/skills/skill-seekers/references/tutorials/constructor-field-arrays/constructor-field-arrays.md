# How To: Constructor Field Arrays

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor field arrays

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

### Step 1: Assign years = value

```python
years = np.arange(1990, 2010).repeat(4)[2:-2]
```

### Step 2: Assign quarters = value

```python
quarters = np.tile(np.arange(1, 5), 20)[2:-2]
```

### Step 3: Assign depr_msg = 'Constructing PeriodIndex from fields is deprecated'

```python
depr_msg = 'Constructing PeriodIndex from fields is deprecated'
```

### Step 4: Assign expected = period_range(...)

```python
expected = period_range('1990Q3', '2009Q2', freq='Q-DEC')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(index.asi8, index2.asi8)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index, expected)
```

### Step 8: Assign years = value

```python
years = [2007, 2007, 2007]
```

### Step 9: Assign months = value

```python
months = [1, 2]
```

### Step 10: Assign msg = 'Mismatched Period array lengths'

```python
msg = 'Mismatched Period array lengths'
```

### Step 11: Assign years = value

```python
years = [2007, 2007, 2007]
```

### Step 12: Assign months = value

```python
months = [1, 2, 3]
```

### Step 13: Assign exp = period_range(...)

```python
exp = period_range('2007-01', periods=3, freq='M')
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 15: Assign index = PeriodIndex(...)

```python
index = PeriodIndex(year=years, quarter=quarters, freq='Q-DEC')
```

### Step 16: Assign index2 = PeriodIndex(...)

```python
index2 = PeriodIndex(year=years, quarter=quarters, freq='2Q-DEC')
```

### Step 17: Assign index = PeriodIndex(...)

```python
index = PeriodIndex(year=years, quarter=quarters)
```

### Step 18: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(year=years, month=months, freq='M')
```

### Step 19: Call PeriodIndex()

```python
PeriodIndex(year=years, month=months, freq='M')
```

### Step 20: Call PeriodIndex()

```python
PeriodIndex(year=years, month=months, freq='2M')
```


## Complete Example

```python
# Workflow
years = np.arange(1990, 2010).repeat(4)[2:-2]
quarters = np.tile(np.arange(1, 5), 20)[2:-2]
depr_msg = 'Constructing PeriodIndex from fields is deprecated'
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    index = PeriodIndex(year=years, quarter=quarters, freq='Q-DEC')
expected = period_range('1990Q3', '2009Q2', freq='Q-DEC')
tm.assert_index_equal(index, expected)
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    index2 = PeriodIndex(year=years, quarter=quarters, freq='2Q-DEC')
tm.assert_numpy_array_equal(index.asi8, index2.asi8)
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    index = PeriodIndex(year=years, quarter=quarters)
tm.assert_index_equal(index, expected)
years = [2007, 2007, 2007]
months = [1, 2]
msg = 'Mismatched Period array lengths'
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=depr_msg):
        PeriodIndex(year=years, month=months, freq='M')
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=depr_msg):
        PeriodIndex(year=years, month=months, freq='2M')
years = [2007, 2007, 2007]
months = [1, 2, 3]
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    idx = PeriodIndex(year=years, month=months, freq='M')
exp = period_range('2007-01', periods=3, freq='M')
tm.assert_index_equal(idx, exp)
```

## Next Steps


---

*Source: test_constructors.py:155 | Complexity: Advanced | Last updated: 2026-06-02*