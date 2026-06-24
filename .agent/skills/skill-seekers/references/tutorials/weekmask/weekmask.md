# How To: Weekmask

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weekmask

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign weekmask_saudi = 'Sat Sun Mon Tue Wed'

```python
weekmask_saudi = 'Sat Sun Mon Tue Wed'
```

**Verification:**
```python
assert xp_saudi == dt + bday_saudi
```

### Step 2: Assign weekmask_uae = '1111001'

```python
weekmask_uae = '1111001'
```

**Verification:**
```python
assert xp_uae == dt + bday_uae
```

### Step 3: Assign weekmask_egypt = value

```python
weekmask_egypt = [1, 1, 1, 1, 0, 0, 1]
```

**Verification:**
```python
assert xp_egypt == dt + bday_egypt
```

### Step 4: Assign bday_saudi = CDay(...)

```python
bday_saudi = CDay(weekmask=weekmask_saudi)
```

**Verification:**
```python
assert xp2 == dt + 2 * bday_saudi
```

### Step 5: Assign bday_uae = CDay(...)

```python
bday_uae = CDay(weekmask=weekmask_uae)
```

**Verification:**
```python
assert xp2 == dt + 2 * bday_uae
```

### Step 6: Assign bday_egypt = CDay(...)

```python
bday_egypt = CDay(weekmask=weekmask_egypt)
```

**Verification:**
```python
assert xp2 == dt + 2 * bday_egypt
```

### Step 7: Assign dt = datetime(...)

```python
dt = datetime(2013, 5, 1)
```

### Step 8: Assign xp_saudi = datetime(...)

```python
xp_saudi = datetime(2013, 5, 4)
```

### Step 9: Assign xp_uae = datetime(...)

```python
xp_uae = datetime(2013, 5, 2)
```

### Step 10: Assign xp_egypt = datetime(...)

```python
xp_egypt = datetime(2013, 5, 2)
```

**Verification:**
```python
assert xp_saudi == dt + bday_saudi
```

### Step 11: Assign xp2 = datetime(...)

```python
xp2 = datetime(2013, 5, 5)
```

**Verification:**
```python
assert xp2 == dt + 2 * bday_saudi
```


## Complete Example

```python
# Workflow
weekmask_saudi = 'Sat Sun Mon Tue Wed'
weekmask_uae = '1111001'
weekmask_egypt = [1, 1, 1, 1, 0, 0, 1]
bday_saudi = CDay(weekmask=weekmask_saudi)
bday_uae = CDay(weekmask=weekmask_uae)
bday_egypt = CDay(weekmask=weekmask_egypt)
dt = datetime(2013, 5, 1)
xp_saudi = datetime(2013, 5, 4)
xp_uae = datetime(2013, 5, 2)
xp_egypt = datetime(2013, 5, 2)
assert xp_saudi == dt + bday_saudi
assert xp_uae == dt + bday_uae
assert xp_egypt == dt + bday_egypt
xp2 = datetime(2013, 5, 5)
assert xp2 == dt + 2 * bday_saudi
assert xp2 == dt + 2 * bday_uae
assert xp2 == dt + 2 * bday_egypt
```

## Next Steps


---

*Source: test_custom_business_day.py:51 | Complexity: Advanced | Last updated: 2026-06-02*