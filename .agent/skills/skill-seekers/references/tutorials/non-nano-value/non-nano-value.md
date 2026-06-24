# How To: Non Nano Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non nano value

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `zoneinfo`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat`
- `pandas.errors`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign result = value

```python
result = Timestamp('1800-01-01', unit='s').value
```

**Verification:**
```python
assert result == -5364662400000000000
```

### Step 2: Assign msg = "Cannot convert Timestamp to nanoseconds without overflow. Use `.asm8.view\\('i8'\\)` to cast represent Timestamp in its own unit \\(here, s\\).$"

```python
msg = "Cannot convert Timestamp to nanoseconds without overflow. Use `.asm8.view\\('i8'\\)` to cast represent Timestamp in its own unit \\(here, s\\).$"
```

**Verification:**
```python
assert result == -52700112000
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp('0300-01-01')
```

### Step 4: Assign result = ts.asm8.view(...)

```python
result = ts.asm8.view('i8')
```

**Verification:**
```python
assert result == -52700112000
```

### Step 5: ts.value

```python
ts.value
```


## Complete Example

```python
# Workflow
result = Timestamp('1800-01-01', unit='s').value
assert result == -5364662400000000000
msg = "Cannot convert Timestamp to nanoseconds without overflow. Use `.asm8.view\\('i8'\\)` to cast represent Timestamp in its own unit \\(here, s\\).$"
ts = Timestamp('0300-01-01')
with pytest.raises(OverflowError, match=msg):
    ts.value
result = ts.asm8.view('i8')
assert result == -52700112000
```

## Next Steps


---

*Source: test_constructors.py:1052 | Complexity: Intermediate | Last updated: 2026-06-02*