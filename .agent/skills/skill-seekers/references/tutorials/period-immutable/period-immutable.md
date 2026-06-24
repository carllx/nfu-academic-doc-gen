# How To: Period Immutable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period immutable

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

### Step 1: Assign msg = 'not writable'

```python
msg = 'not writable'
```

### Step 2: Assign per = Period(...)

```python
per = Period('2014Q1')
```

### Step 3: Assign freq = value

```python
freq = per.freq
```

### Step 4: Assign per.ordinal = 14

```python
per.ordinal = 14
```

### Step 5: Assign per.freq = value

```python
per.freq = 2 * freq
```


## Complete Example

```python
# Workflow
msg = 'not writable'
per = Period('2014Q1')
with pytest.raises(AttributeError, match=msg):
    per.ordinal = 14
freq = per.freq
with pytest.raises(AttributeError, match=msg):
    per.freq = 2 * freq
```

## Next Steps


---

*Source: test_period.py:1123 | Complexity: Intermediate | Last updated: 2026-06-02*