# How To: Negone Ordinals

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negone ordinals

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.np_datetime`
- `pandas._libs.tslibs.parsing`
- `pandas._libs.tslibs.period`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign freqs = value

```python
freqs = ['Y', 'M', 'Q', 'D', 'h', 'min', 's']
```

**Verification:**
```python
assert period.year == 1969
```

### Step 2: Assign period = Period(...)

```python
period = Period(ordinal=-1, freq='D')
```

### Step 3: Call repr()

```python
repr(period)
```

### Step 4: Assign period = Period(...)

```python
period = Period(ordinal=-1, freq='W')
```

### Step 5: Call repr()

```python
repr(period)
```

### Step 6: Call repr()

```python
repr(period.asfreq(freq))
```

### Step 7: Assign period = Period(...)

```python
period = Period(ordinal=-1, freq=freq)
```

### Step 8: Call repr()

```python
repr(period)
```

**Verification:**
```python
assert period.year == 1969
```

### Step 9: Assign period = Period(...)

```python
period = Period(ordinal=-1, freq='B')
```


## Complete Example

```python
# Workflow
freqs = ['Y', 'M', 'Q', 'D', 'h', 'min', 's']
period = Period(ordinal=-1, freq='D')
for freq in freqs:
    repr(period.asfreq(freq))
for freq in freqs:
    period = Period(ordinal=-1, freq=freq)
    repr(period)
    assert period.year == 1969
with tm.assert_produces_warning(FutureWarning, match=bday_msg):
    period = Period(ordinal=-1, freq='B')
repr(period)
period = Period(ordinal=-1, freq='W')
repr(period)
```

## Next Steps


---

*Source: test_period.py:1142 | Complexity: Advanced | Last updated: 2026-06-02*