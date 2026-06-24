# How To: Period Custom

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period custom

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'PeriodIndex.format is deprecated'

```python
msg = 'PeriodIndex.format is deprecated'
```

**Verification:**
```python
assert formatted[0] == '03 12:01:01 (ms=123 us=123000 ns=123000000)'
```

### Step 2: Assign per = pd.period_range(...)

```python
per = pd.period_range('2003-01-01 12:01:01.123', periods=2, freq='ms')
```

**Verification:**
```python
assert formatted[1] == '03 12:01:01 (ms=124 us=124000 ns=124000000)'
```

### Step 3: Assign per = pd.period_range(...)

```python
per = pd.period_range('2003-01-01 12:01:01.123456', periods=2, freq='us')
```

**Verification:**
```python
assert formatted[0] == '03 12:01:01 (ms=123 us=123456 ns=123456000)'
```

### Step 4: Assign per = pd.period_range(...)

```python
per = pd.period_range('2003-01-01 12:01:01.123456789', periods=2, freq='ns')
```

**Verification:**
```python
assert formatted[1] == '03 12:01:01 (ms=123 us=123457 ns=123457000)'
```

### Step 5: Assign formatted = per.format(...)

```python
formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
```

**Verification:**
```python
assert formatted[0] == '03 12:01:01 (ms=123 us=123456 ns=123456789)'
```

### Step 6: Assign formatted = per.format(...)

```python
formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
```

**Verification:**
```python
assert formatted[1] == '03 12:01:01 (ms=123 us=123456 ns=123456790)'
```

### Step 7: Assign formatted = per.format(...)

```python
formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
```


## Complete Example

```python
# Workflow
msg = 'PeriodIndex.format is deprecated'
per = pd.period_range('2003-01-01 12:01:01.123', periods=2, freq='ms')
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
assert formatted[0] == '03 12:01:01 (ms=123 us=123000 ns=123000000)'
assert formatted[1] == '03 12:01:01 (ms=124 us=124000 ns=124000000)'
per = pd.period_range('2003-01-01 12:01:01.123456', periods=2, freq='us')
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
assert formatted[0] == '03 12:01:01 (ms=123 us=123456 ns=123456000)'
assert formatted[1] == '03 12:01:01 (ms=123 us=123457 ns=123457000)'
per = pd.period_range('2003-01-01 12:01:01.123456789', periods=2, freq='ns')
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = per.format(date_format='%y %I:%M:%S (ms=%l us=%u ns=%n)')
assert formatted[0] == '03 12:01:01 (ms=123 us=123456 ns=123456789)'
assert formatted[1] == '03 12:01:01 (ms=123 us=123456 ns=123456790)'
```

## Next Steps


---

*Source: test_formats.py:242 | Complexity: Intermediate | Last updated: 2026-06-02*