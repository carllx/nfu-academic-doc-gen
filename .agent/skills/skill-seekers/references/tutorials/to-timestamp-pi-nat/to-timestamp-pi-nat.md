# How To: To Timestamp Pi Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timestamp pi nat

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = PeriodIndex(...)

```python
index = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='M', name='idx')
```

**Verification:**
```python
assert result.name == 'idx'
```

### Step 2: Assign result = index.to_timestamp(...)

```python
result = index.to_timestamp('D')
```

**Verification:**
```python
assert result2.name == 'idx'
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([NaT, datetime(2011, 1, 1), datetime(2011, 2, 1)], dtype='M8[ns]', name='idx')
```

**Verification:**
```python
assert result3.freqstr == '3M'
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == 'idx'
```

### Step 5: Assign result2 = result.to_period(...)

```python
result2 = result.to_period(freq='M')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2, index)
```

**Verification:**
```python
assert result2.name == 'idx'
```

### Step 7: Assign result3 = result.to_period(...)

```python
result3 = result.to_period(freq='3M')
```

### Step 8: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='3M', name='idx')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result3, exp)
```

**Verification:**
```python
assert result3.freqstr == '3M'
```

### Step 10: Assign msg = 'Frequency must be positive, because it represents span: -2Y'

```python
msg = 'Frequency must be positive, because it represents span: -2Y'
```

### Step 11: Call result.to_period()

```python
result.to_period(freq='-2Y')
```


## Complete Example

```python
# Workflow
index = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='M', name='idx')
result = index.to_timestamp('D')
expected = DatetimeIndex([NaT, datetime(2011, 1, 1), datetime(2011, 2, 1)], dtype='M8[ns]', name='idx')
tm.assert_index_equal(result, expected)
assert result.name == 'idx'
result2 = result.to_period(freq='M')
tm.assert_index_equal(result2, index)
assert result2.name == 'idx'
result3 = result.to_period(freq='3M')
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='3M', name='idx')
tm.assert_index_equal(result3, exp)
assert result3.freqstr == '3M'
msg = 'Frequency must be positive, because it represents span: -2Y'
with pytest.raises(ValueError, match=msg):
    result.to_period(freq='-2Y')
```

## Next Steps


---

*Source: test_to_timestamp.py:55 | Complexity: Advanced | Last updated: 2026-06-02*