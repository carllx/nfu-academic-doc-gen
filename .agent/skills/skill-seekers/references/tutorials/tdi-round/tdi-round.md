# How To: Tdi Round

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tdi round

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign td = timedelta_range(...)

```python
td = timedelta_range(start='16801 days', periods=5, freq='30Min')
```

**Verification:**
```python
assert elt.round(freq='h') == expected_elt
```

### Step 2: Assign elt = value

```python
elt = td[1]
```

### Step 3: Assign expected_rng = TimedeltaIndex(...)

```python
expected_rng = TimedeltaIndex([Timedelta('16801 days 00:00:00'), Timedelta('16801 days 00:00:00'), Timedelta('16801 days 01:00:00'), Timedelta('16801 days 02:00:00'), Timedelta('16801 days 02:00:00')])
```

### Step 4: Assign expected_elt = value

```python
expected_elt = expected_rng[1]
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(td.round(freq='h'), expected_rng)
```

**Verification:**
```python
assert elt.round(freq='h') == expected_elt
```

### Step 6: Assign msg = INVALID_FREQ_ERR_MSG

```python
msg = INVALID_FREQ_ERR_MSG
```

### Step 7: Assign msg = '<MonthEnd> is a non-fixed frequency'

```python
msg = '<MonthEnd> is a non-fixed frequency'
```

### Step 8: Call td.round()

```python
td.round(freq='foo')
```

### Step 9: Call elt.round()

```python
elt.round(freq='foo')
```

### Step 10: Call td.round()

```python
td.round(freq='ME')
```

### Step 11: Call elt.round()

```python
elt.round(freq='ME')
```


## Complete Example

```python
# Workflow
td = timedelta_range(start='16801 days', periods=5, freq='30Min')
elt = td[1]
expected_rng = TimedeltaIndex([Timedelta('16801 days 00:00:00'), Timedelta('16801 days 00:00:00'), Timedelta('16801 days 01:00:00'), Timedelta('16801 days 02:00:00'), Timedelta('16801 days 02:00:00')])
expected_elt = expected_rng[1]
tm.assert_index_equal(td.round(freq='h'), expected_rng)
assert elt.round(freq='h') == expected_elt
msg = INVALID_FREQ_ERR_MSG
with pytest.raises(ValueError, match=msg):
    td.round(freq='foo')
with pytest.raises(ValueError, match=msg):
    elt.round(freq='foo')
msg = '<MonthEnd> is a non-fixed frequency'
with pytest.raises(ValueError, match=msg):
    td.round(freq='ME')
with pytest.raises(ValueError, match=msg):
    elt.round(freq='ME')
```

## Next Steps


---

*Source: test_scalar_compat.py:51 | Complexity: Advanced | Last updated: 2026-06-02*