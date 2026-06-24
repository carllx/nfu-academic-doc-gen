# How To: Construction From Timestamp Nanos

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction from timestamp nanos

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

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2022-04-20 09:23:24.123456789')
```

**Verification:**
```python
assert rt == ts
```

### Step 2: Assign per = Period(...)

```python
per = Period(ts, freq='ns')
```

**Verification:**
```python
assert rt2.asm8 == dt64
```

### Step 3: Assign rt = per.to_timestamp(...)

```python
rt = per.to_timestamp()
```

**Verification:**
```python
assert rt == ts
```

### Step 4: Assign dt64 = value

```python
dt64 = ts.asm8
```

### Step 5: Assign per2 = Period(...)

```python
per2 = Period(dt64, freq='ns')
```

### Step 6: Assign rt2 = per2.to_timestamp(...)

```python
rt2 = per2.to_timestamp()
```

**Verification:**
```python
assert rt2.asm8 == dt64
```


## Complete Example

```python
# Workflow
ts = Timestamp('2022-04-20 09:23:24.123456789')
per = Period(ts, freq='ns')
rt = per.to_timestamp()
assert rt == ts
dt64 = ts.asm8
per2 = Period(dt64, freq='ns')
rt2 = per2.to_timestamp()
assert rt2.asm8 == dt64
```

## Next Steps


---

*Source: test_period.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*