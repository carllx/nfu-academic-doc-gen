# How To: Dateoffset Add Sub Timestamp With Nano

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dateoffset add sub timestamp with nano

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign offset = DateOffset(...)

```python
offset = DateOffset(minutes=2, nanoseconds=9)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(4)
```

**Verification:**
```python
assert result == ts
```

### Step 3: Assign result = value

```python
result = ts + offset
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp('1970-01-01 00:02:00.000000013')
```

**Verification:**
```python
assert offset2._use_relativedelta
```

### Step 5: Assign result = value

```python
result = offset + ts
```

**Verification:**
```python
assert result2 == expected2
```

### Step 6: Assign offset2 = DateOffset(...)

```python
offset2 = DateOffset(minutes=2, nanoseconds=9, hour=1)
```

**Verification:**
```python
assert offset2._use_relativedelta
```

### Step 7: Assign expected2 = Timestamp(...)

```python
expected2 = Timestamp('1970-01-01 01:02:00.000000013')
```

**Verification:**
```python
assert result2 == expected2
```

### Step 8: Assign result2 = value

```python
result2 = ts + offset2
```


## Complete Example

```python
# Workflow
offset = DateOffset(minutes=2, nanoseconds=9)
ts = Timestamp(4)
result = ts + offset
expected = Timestamp('1970-01-01 00:02:00.000000013')
assert result == expected
result -= offset
assert result == ts
result = offset + ts
assert result == expected
offset2 = DateOffset(minutes=2, nanoseconds=9, hour=1)
assert offset2._use_relativedelta
with tm.assert_produces_warning(None):
    result2 = ts + offset2
expected2 = Timestamp('1970-01-01 01:02:00.000000013')
assert result2 == expected2
```

## Next Steps


---

*Source: test_offsets.py:1014 | Complexity: Advanced | Last updated: 2026-06-02*