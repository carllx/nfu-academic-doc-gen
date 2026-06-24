# How To: Construction Quarter

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction quarter

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

### Step 1: Assign i1 = Period(...)

```python
i1 = Period(year=2005, quarter=1, freq='Q')
```

**Verification:**
```python
assert i1 == i2
```

### Step 2: Assign i2 = Period(...)

```python
i2 = Period('1/1/2005', freq='Q')
```

**Verification:**
```python
assert i1 == i2
```

### Step 3: Assign i1 = Period(...)

```python
i1 = Period(year=2005, quarter=3, freq='Q')
```

**Verification:**
```python
assert i1 == i2
```

### Step 4: Assign i2 = Period(...)

```python
i2 = Period('9/1/2005', freq='Q')
```

**Verification:**
```python
assert i1 == i3
```

### Step 5: Assign i1 = Period(...)

```python
i1 = Period('2005Q1')
```

**Verification:**
```python
assert i1 == i2
```

### Step 6: Assign i2 = Period(...)

```python
i2 = Period(year=2005, quarter=1, freq='Q')
```

**Verification:**
```python
assert i1 == lower
```

### Step 7: Assign i3 = Period(...)

```python
i3 = Period('2005q1')
```

**Verification:**
```python
assert i1 == i2
```

### Step 8: Assign i1 = Period(...)

```python
i1 = Period('05Q1')
```

**Verification:**
```python
assert i1 == lower
```

### Step 9: Assign lower = Period(...)

```python
lower = Period('05q1')
```

**Verification:**
```python
assert i1 == i2
```

### Step 10: Assign i1 = Period(...)

```python
i1 = Period('1Q2005')
```

**Verification:**
```python
assert i1 == lower
```

### Step 11: Assign lower = Period(...)

```python
lower = Period('1q2005')
```

**Verification:**
```python
assert i1.year == 1984
```

### Step 12: Assign i1 = Period(...)

```python
i1 = Period('1Q05')
```

**Verification:**
```python
assert i1 == lower
```

### Step 13: Assign lower = Period(...)

```python
lower = Period('1q05')
```

**Verification:**
```python
assert i1 == lower
```

### Step 14: Assign i1 = Period(...)

```python
i1 = Period('4Q1984')
```

**Verification:**
```python
assert i1.year == 1984
```

### Step 15: Assign lower = Period(...)

```python
lower = Period('4q1984')
```

**Verification:**
```python
assert i1 == lower
```


## Complete Example

```python
# Workflow
i1 = Period(year=2005, quarter=1, freq='Q')
i2 = Period('1/1/2005', freq='Q')
assert i1 == i2
i1 = Period(year=2005, quarter=3, freq='Q')
i2 = Period('9/1/2005', freq='Q')
assert i1 == i2
i1 = Period('2005Q1')
i2 = Period(year=2005, quarter=1, freq='Q')
i3 = Period('2005q1')
assert i1 == i2
assert i1 == i3
i1 = Period('05Q1')
assert i1 == i2
lower = Period('05q1')
assert i1 == lower
i1 = Period('1Q2005')
assert i1 == i2
lower = Period('1q2005')
assert i1 == lower
i1 = Period('1Q05')
assert i1 == i2
lower = Period('1q05')
assert i1 == lower
i1 = Period('4Q1984')
assert i1.year == 1984
lower = Period('4q1984')
assert i1 == lower
```

## Next Steps


---

*Source: test_period.py:187 | Complexity: Advanced | Last updated: 2026-06-02*