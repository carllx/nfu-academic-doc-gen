# How To: Constructor Int Float With Ym Unit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor int float with YM unit

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: typ
```

## Step-by-Step Guide

### Step 1: Assign val = typ(...)

```python
val = typ(150)
```

**Verification:**
```python
assert ts == expected
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(val, unit='Y')
```

**Verification:**
```python
assert ts == expected
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2120-01-01')
```

**Verification:**
```python
assert ts == expected
```

### Step 4: Assign ts = Timestamp(...)

```python
ts = Timestamp(val, unit='M')
```

### Step 5: Assign expected = Timestamp(...)

```python
expected = Timestamp('1982-07-01')
```

**Verification:**
```python
assert ts == expected
```


## Complete Example

```python
# Setup
# Fixtures: typ

# Workflow
val = typ(150)
ts = Timestamp(val, unit='Y')
expected = Timestamp('2120-01-01')
assert ts == expected
ts = Timestamp(val, unit='M')
expected = Timestamp('1982-07-01')
assert ts == expected
```

## Next Steps


---

*Source: test_constructors.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*