# How To: To Period Monthish

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period monthish

## Prerequisites

**Required Modules:**
- `dateutil.tz`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign offsets = value

```python
offsets = ['MS', 'BME']
```

**Verification:**
```python
assert prng.freqstr == 'M'
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range('01-Jan-2012', periods=8, freq='ME')
```

**Verification:**
```python
assert prng.freqstr == 'M'
```

### Step 3: Assign prng = rng.to_period(...)

```python
prng = rng.to_period()
```

**Verification:**
```python
assert prng.freqstr == 'M'
```

### Step 4: Assign rng = date_range(...)

```python
rng = date_range('01-Jan-2012', periods=8, freq=off)
```

### Step 5: Assign prng = rng.to_period(...)

```python
prng = rng.to_period()
```

**Verification:**
```python
assert prng.freqstr == 'M'
```

### Step 6: Call date_range()

```python
date_range('01-Jan-2012', periods=8, freq='EOM')
```


## Complete Example

```python
# Workflow
offsets = ['MS', 'BME']
for off in offsets:
    rng = date_range('01-Jan-2012', periods=8, freq=off)
    prng = rng.to_period()
    assert prng.freqstr == 'M'
rng = date_range('01-Jan-2012', periods=8, freq='ME')
prng = rng.to_period()
assert prng.freqstr == 'M'
with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    date_range('01-Jan-2012', periods=8, freq='EOM')
```

## Next Steps


---

*Source: test_to_period.py:65 | Complexity: Intermediate | Last updated: 2026-06-02*