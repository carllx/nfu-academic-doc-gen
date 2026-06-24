# How To: Constructor Infer Freq

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor infer freq

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

### Step 1: Assign p = Period(...)

```python
p = Period('2007-01-01')
```

**Verification:**
```python
assert p.freq == 'D'
```

### Step 2: Assign p = Period(...)

```python
p = Period('2007-01-01 07')
```

**Verification:**
```python
assert p.freq == 'h'
```

### Step 3: Assign p = Period(...)

```python
p = Period('2007-01-01 07:10')
```

**Verification:**
```python
assert p.freq == 'min'
```

### Step 4: Assign p = Period(...)

```python
p = Period('2007-01-01 07:10:15')
```

**Verification:**
```python
assert p.freq == 's'
```

### Step 5: Assign p = Period(...)

```python
p = Period('2007-01-01 07:10:15.123')
```

**Verification:**
```python
assert p.freq == 'ms'
```

### Step 6: Assign p = Period(...)

```python
p = Period('2007-01-01 07:10:15.123000')
```

**Verification:**
```python
assert p.freq == 'us'
```

### Step 7: Assign p = Period(...)

```python
p = Period('2007-01-01 07:10:15.123400')
```

**Verification:**
```python
assert p.freq == 'us'
```


## Complete Example

```python
# Workflow
p = Period('2007-01-01')
assert p.freq == 'D'
p = Period('2007-01-01 07')
assert p.freq == 'h'
p = Period('2007-01-01 07:10')
assert p.freq == 'min'
p = Period('2007-01-01 07:10:15')
assert p.freq == 's'
p = Period('2007-01-01 07:10:15.123')
assert p.freq == 'ms'
p = Period('2007-01-01 07:10:15.123000')
assert p.freq == 'us'
p = Period('2007-01-01 07:10:15.123400')
assert p.freq == 'us'
```

## Next Steps


---

*Source: test_period.py:368 | Complexity: Intermediate | Last updated: 2026-06-02*