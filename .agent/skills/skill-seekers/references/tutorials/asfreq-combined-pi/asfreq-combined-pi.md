# How To: Asfreq Combined Pi

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq combined pi

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='h')
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 2: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='25h')
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 3: Assign result = pi.asfreq(...)

```python
result = pi.asfreq(freq, how=how)
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 5: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq=freq)
```

### Step 6: Assign result = pi.asfreq(...)

```python
result = pi.asfreq('h')
```

### Step 7: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2001-01-02 00:00', '2001-01-03 02:00', 'NaT'], freq='h')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == exp.freq
```

### Step 9: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq=freq)
```

### Step 10: Assign result = pi.asfreq(...)

```python
result = pi.asfreq('h', how='S')
```

### Step 11: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='h')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

**Verification:**
```python
assert result.freq == exp.freq
```


## Complete Example

```python
# Workflow
pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='h')
exp = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='25h')
for freq, how in zip(['1D1h', '1h1D'], ['S', 'E']):
    result = pi.asfreq(freq, how=how)
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq
for freq in ['1D1h', '1h1D']:
    pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq=freq)
    result = pi.asfreq('h')
    exp = PeriodIndex(['2001-01-02 00:00', '2001-01-03 02:00', 'NaT'], freq='h')
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq
    pi = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq=freq)
    result = pi.asfreq('h', how='S')
    exp = PeriodIndex(['2001-01-01 00:00', '2001-01-02 02:00', 'NaT'], freq='h')
    tm.assert_index_equal(result, exp)
    assert result.freq == exp.freq
```

## Next Steps


---

*Source: test_asfreq.py:106 | Complexity: Advanced | Last updated: 2026-06-02*