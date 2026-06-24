# How To: Apply Large N

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply large n

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2012, 10, 23)
```

**Verification:**
```python
assert result == datetime(2013, 7, 31)
```

### Step 2: Assign result = value

```python
result = dt + CBMonthEnd(10)
```

**Verification:**
```python
assert result == dt
```

### Step 3: Assign result = value

```python
result = dt + CDay(100) - CDay(100)
```

**Verification:**
```python
assert rs == xp
```

### Step 4: Assign off = value

```python
off = CBMonthEnd() * 6
```

**Verification:**
```python
assert rs == xp
```

### Step 5: Assign rs = value

```python
rs = datetime(2012, 1, 1) - off
```

### Step 6: Assign xp = datetime(...)

```python
xp = datetime(2011, 7, 29)
```

**Verification:**
```python
assert rs == xp
```

### Step 7: Assign st = datetime(...)

```python
st = datetime(2011, 12, 18)
```

### Step 8: Assign rs = value

```python
rs = st + off
```

### Step 9: Assign xp = datetime(...)

```python
xp = datetime(2012, 5, 31)
```

**Verification:**
```python
assert rs == xp
```


## Complete Example

```python
# Workflow
dt = datetime(2012, 10, 23)
result = dt + CBMonthEnd(10)
assert result == datetime(2013, 7, 31)
result = dt + CDay(100) - CDay(100)
assert result == dt
off = CBMonthEnd() * 6
rs = datetime(2012, 1, 1) - off
xp = datetime(2011, 7, 29)
assert rs == xp
st = datetime(2011, 12, 18)
rs = st + off
xp = datetime(2012, 5, 31)
assert rs == xp
```

## Next Steps


---

*Source: test_custom_business_month.py:361 | Complexity: Advanced | Last updated: 2026-06-02*