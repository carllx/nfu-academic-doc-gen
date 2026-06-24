# How To: Construction Month

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction month

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

### Step 1: Assign expected = Period(...)

```python
expected = Period('2007-01', freq='M')
```

**Verification:**
```python
assert i1 == expected
```

### Step 2: Assign i1 = Period(...)

```python
i1 = Period('200701', freq='M')
```

**Verification:**
```python
assert i1 == expected
```

### Step 3: Assign i1 = Period(...)

```python
i1 = Period('200701', freq='M')
```

**Verification:**
```python
assert i1 == expected
```

### Step 4: Assign i1 = Period(...)

```python
i1 = Period(200701, freq='M')
```

**Verification:**
```python
assert i1.year == 18695
```

### Step 5: Assign i1 = Period(...)

```python
i1 = Period(ordinal=200701, freq='M')
```

**Verification:**
```python
assert i1 == i2
```

### Step 6: Assign i1 = Period(...)

```python
i1 = Period(datetime(2007, 1, 1), freq='M')
```

**Verification:**
```python
assert i1 == i2
```

### Step 7: Assign i2 = Period(...)

```python
i2 = Period('200701', freq='M')
```

**Verification:**
```python
assert i1 == i3
```

### Step 8: Assign i1 = Period(...)

```python
i1 = Period(date(2007, 1, 1), freq='M')
```

**Verification:**
```python
assert i1 == i4
```

### Step 9: Assign i2 = Period(...)

```python
i2 = Period(datetime(2007, 1, 1), freq='M')
```

**Verification:**
```python
assert i1 == i5
```

### Step 10: Assign i3 = Period(...)

```python
i3 = Period(np.datetime64('2007-01-01'), freq='M')
```

### Step 11: Assign i4 = Period(...)

```python
i4 = Period('2007-01-01 00:00:00', freq='M')
```

### Step 12: Assign i5 = Period(...)

```python
i5 = Period('2007-01-01 00:00:00.000', freq='M')
```

**Verification:**
```python
assert i1 == i2
```


## Complete Example

```python
# Workflow
expected = Period('2007-01', freq='M')
i1 = Period('200701', freq='M')
assert i1 == expected
i1 = Period('200701', freq='M')
assert i1 == expected
i1 = Period(200701, freq='M')
assert i1 == expected
i1 = Period(ordinal=200701, freq='M')
assert i1.year == 18695
i1 = Period(datetime(2007, 1, 1), freq='M')
i2 = Period('200701', freq='M')
assert i1 == i2
i1 = Period(date(2007, 1, 1), freq='M')
i2 = Period(datetime(2007, 1, 1), freq='M')
i3 = Period(np.datetime64('2007-01-01'), freq='M')
i4 = Period('2007-01-01 00:00:00', freq='M')
i5 = Period('2007-01-01 00:00:00.000', freq='M')
assert i1 == i2
assert i1 == i3
assert i1 == i4
assert i1 == i5
```

## Next Steps


---

*Source: test_period.py:222 | Complexity: Advanced | Last updated: 2026-06-02*