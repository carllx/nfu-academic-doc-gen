# How To: Dti To Period

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti to period

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

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(start='1/1/2005', end='12/1/2005', freq='ME')
```

**Verification:**
```python
assert pi1[0] == Period('Jan 2005', freq='M')
```

### Step 2: Assign pi1 = dti.to_period(...)

```python
pi1 = dti.to_period()
```

**Verification:**
```python
assert pi2[0] == Period('1/31/2005', freq='D')
```

### Step 3: Assign pi2 = dti.to_period(...)

```python
pi2 = dti.to_period(freq='D')
```

**Verification:**
```python
assert pi3[0] == Period('1/31/2005', freq='3D')
```

### Step 4: Assign pi3 = dti.to_period(...)

```python
pi3 = dti.to_period(freq='3D')
```

**Verification:**
```python
assert pi1[-1] == Period('Nov 2005', freq='M')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi1, period_range('1/1/2005', '11/1/2005', freq='M'))
```

**Verification:**
```python
assert pi2[-1] == Period('11/30/2005', freq='D')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi2, period_range('1/1/2005', '11/1/2005', freq='M').asfreq('D'))
```

**Verification:**
```python
assert pi3[-1], Period('11/30/2005', freq='3D')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi3, period_range('1/1/2005', '11/1/2005', freq='M').asfreq('3D'))
```


## Complete Example

```python
# Workflow
dti = date_range(start='1/1/2005', end='12/1/2005', freq='ME')
pi1 = dti.to_period()
pi2 = dti.to_period(freq='D')
pi3 = dti.to_period(freq='3D')
assert pi1[0] == Period('Jan 2005', freq='M')
assert pi2[0] == Period('1/31/2005', freq='D')
assert pi3[0] == Period('1/31/2005', freq='3D')
assert pi1[-1] == Period('Nov 2005', freq='M')
assert pi2[-1] == Period('11/30/2005', freq='D')
assert pi3[-1], Period('11/30/2005', freq='3D')
tm.assert_index_equal(pi1, period_range('1/1/2005', '11/1/2005', freq='M'))
tm.assert_index_equal(pi2, period_range('1/1/2005', '11/1/2005', freq='M').asfreq('D'))
tm.assert_index_equal(pi3, period_range('1/1/2005', '11/1/2005', freq='M').asfreq('3D'))
```

## Next Steps


---

*Source: test_to_period.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*