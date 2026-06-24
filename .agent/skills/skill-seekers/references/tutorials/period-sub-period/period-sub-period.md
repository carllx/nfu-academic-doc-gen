# How To: Period Sub Period

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period sub period

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign per1 = Period(...)

```python
per1 = Period('2011-01-01', freq='D')
```

**Verification:**
```python
assert per1 - per2 == -14 * off
```

### Step 2: Assign per2 = Period(...)

```python
per2 = Period('2011-01-15', freq='D')
```

**Verification:**
```python
assert per2 - per1 == 14 * off
```

### Step 3: Assign off = value

```python
off = per1.freq
```

**Verification:**
```python
assert per1 - per2 == -14 * off
```

### Step 4: Assign msg = 'Input has different freq=M from Period\\(freq=D\\)'

```python
msg = 'Input has different freq=M from Period\\(freq=D\\)'
```

### Step 5: per1 - Period('2011-02', freq='M')

```python
per1 - Period('2011-02', freq='M')
```


## Complete Example

```python
# Workflow
per1 = Period('2011-01-01', freq='D')
per2 = Period('2011-01-15', freq='D')
off = per1.freq
assert per1 - per2 == -14 * off
assert per2 - per1 == 14 * off
msg = 'Input has different freq=M from Period\\(freq=D\\)'
with pytest.raises(IncompatibleFrequency, match=msg):
    per1 - Period('2011-02', freq='M')
```

## Next Steps


---

*Source: test_arithmetic.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*