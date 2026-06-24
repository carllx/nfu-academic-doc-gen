# How To: Invalid Arguments

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invalid arguments

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

### Step 1: Assign msg = 'Must supply freq for datetime value'

```python
msg = 'Must supply freq for datetime value'
```

### Step 2: Assign msg = 'Value must be Period, string, integer, or datetime'

```python
msg = 'Value must be Period, string, integer, or datetime'
```

### Step 3: Assign msg = 'Ordinal must be an integer'

```python
msg = 'Ordinal must be an integer'
```

### Step 4: Assign msg = 'Only value or ordinal but not both should be given but not both'

```python
msg = 'Only value or ordinal but not both should be given but not both'
```

### Step 5: Assign msg = 'If value is None, freq cannot be None'

```python
msg = 'If value is None, freq cannot be None'
```

### Step 6: Assign msg = '^Given date string "-2000" not likely a datetime$'

```python
msg = '^Given date string "-2000" not likely a datetime$'
```

### Step 7: Assign msg = 'Unknown datetime string format, unable to parse'

```python
msg = 'Unknown datetime string format, unable to parse'
```

### Step 8: Call Period()

```python
Period(datetime.now())
```

### Step 9: Call Period()

```python
Period(datetime.now().date())
```

### Step 10: Call Period()

```python
Period(1.6, freq='D')
```

### Step 11: Call Period()

```python
Period(ordinal=1.6, freq='D')
```

### Step 12: Call Period()

```python
Period(ordinal=2, value=1, freq='D')
```

### Step 13: Call Period()

```python
Period(month=1)
```

### Step 14: Call Period()

```python
Period('-2000', 'Y')
```

### Step 15: Assign msg = 'day 0 must be in range 1..31 for month 1 in year 1: 0'

```python
msg = 'day 0 must be in range 1..31 for month 1 in year 1: 0'
```

### Step 16: Assign msg = 'day is out of range for month'

```python
msg = 'day is out of range for month'
```

### Step 17: Call Period()

```python
Period('0', 'Y')
```

### Step 18: Call Period()

```python
Period('1/1/-2000', 'Y')
```


## Complete Example

```python
# Workflow
msg = 'Must supply freq for datetime value'
with pytest.raises(ValueError, match=msg):
    Period(datetime.now())
with pytest.raises(ValueError, match=msg):
    Period(datetime.now().date())
msg = 'Value must be Period, string, integer, or datetime'
with pytest.raises(ValueError, match=msg):
    Period(1.6, freq='D')
msg = 'Ordinal must be an integer'
with pytest.raises(ValueError, match=msg):
    Period(ordinal=1.6, freq='D')
msg = 'Only value or ordinal but not both should be given but not both'
with pytest.raises(ValueError, match=msg):
    Period(ordinal=2, value=1, freq='D')
msg = 'If value is None, freq cannot be None'
with pytest.raises(ValueError, match=msg):
    Period(month=1)
msg = '^Given date string "-2000" not likely a datetime$'
with pytest.raises(ValueError, match=msg):
    Period('-2000', 'Y')
if PY314:
    msg = 'day 0 must be in range 1..31 for month 1 in year 1: 0'
else:
    msg = 'day is out of range for month'
with pytest.raises(DateParseError, match=msg):
    Period('0', 'Y')
msg = 'Unknown datetime string format, unable to parse'
with pytest.raises(DateParseError, match=msg):
    Period('1/1/-2000', 'Y')
```

## Next Steps


---

*Source: test_period.py:322 | Complexity: Advanced | Last updated: 2026-06-02*