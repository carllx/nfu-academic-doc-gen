# How To: Ufunc Coercions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ufunc coercions

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['2h', '4h', '6h', '8h', '10h'], freq='2h', name='x')
```

**Verification:**
```python
assert isinstance(result, TimedeltaIndex)
```

### Step 2: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['-2h', '-1h', '0h', '1h', '2h'], freq='h', name='x')
```

**Verification:**
```python
assert result.freq == '4h'
```

### Step 3: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['4h', '8h', '12h', '16h', '20h'], freq='4h', name='x')
```

**Verification:**
```python
assert isinstance(result, TimedeltaIndex)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == 'h'
```

### Step 5: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['1h', '2h', '3h', '4h', '5h'], freq='h', name='x')
```

**Verification:**
```python
assert isinstance(result, TimedeltaIndex)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == '-2h'
```

### Step 7: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['-2h', '-4h', '-6h', '-8h', '-10h'], freq='-2h', name='x')
```

**Verification:**
```python
assert isinstance(result, TimedeltaIndex)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq is None
```

### Step 9: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['2h', '1h', '0h', '1h', '2h'], freq=None, name='x')
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq is None
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['2h', '4h', '6h', '8h', '10h'], freq='2h', name='x')
for result in [idx * 2, np.multiply(idx, 2)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(['4h', '8h', '12h', '16h', '20h'], freq='4h', name='x')
    tm.assert_index_equal(result, exp)
    assert result.freq == '4h'
for result in [idx / 2, np.divide(idx, 2)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(['1h', '2h', '3h', '4h', '5h'], freq='h', name='x')
    tm.assert_index_equal(result, exp)
    assert result.freq == 'h'
for result in [-idx, np.negative(idx)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(['-2h', '-4h', '-6h', '-8h', '-10h'], freq='-2h', name='x')
    tm.assert_index_equal(result, exp)
    assert result.freq == '-2h'
idx = TimedeltaIndex(['-2h', '-1h', '0h', '1h', '2h'], freq='h', name='x')
for result in [abs(idx), np.absolute(idx)]:
    assert isinstance(result, TimedeltaIndex)
    exp = TimedeltaIndex(['2h', '1h', '0h', '1h', '2h'], freq=None, name='x')
    tm.assert_index_equal(result, exp)
    assert result.freq is None
```

## Next Steps


---

*Source: test_timedelta64.py:277 | Complexity: Advanced | Last updated: 2026-06-02*