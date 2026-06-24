# How To: Round Non Nano

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round non nano

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign td = Timedelta.as_unit(...)

```python
td = Timedelta('1 days 02:34:57').as_unit(unit)
```

**Verification:**
```python
assert res == Timedelta('1 days 02:35:00')
```

### Step 2: Assign res = td.round(...)

```python
res = td.round('min')
```

**Verification:**
```python
assert res._creso == td._creso
```

### Step 3: Assign res = td.floor(...)

```python
res = td.floor('min')
```

**Verification:**
```python
assert res == Timedelta('1 days 02:34:00')
```

### Step 4: Assign res = td.ceil(...)

```python
res = td.ceil('min')
```

**Verification:**
```python
assert res._creso == td._creso
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
td = Timedelta('1 days 02:34:57').as_unit(unit)
res = td.round('min')
assert res == Timedelta('1 days 02:35:00')
assert res._creso == td._creso
res = td.floor('min')
assert res == Timedelta('1 days 02:34:00')
assert res._creso == td._creso
res = td.ceil('min')
assert res == Timedelta('1 days 02:35:00')
assert res._creso == td._creso
```

## Next Steps


---

*Source: test_round.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*