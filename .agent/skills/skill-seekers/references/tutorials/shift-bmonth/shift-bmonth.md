# How To: Shift Bmonth

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift bmonth

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(START, END, freq=pd.offsets.BMonthEnd(), unit=unit)
```

**Verification:**
```python
assert shifted[0] == rng[0] + pd.offsets.BDay()
```

### Step 2: Assign shifted = rng.shift(...)

```python
shifted = rng.shift(1, freq=pd.offsets.BDay())
```

**Verification:**
```python
assert shifted[0] == rng[0] + pd.offsets.CDay()
```

### Step 3: Assign rng = date_range(...)

```python
rng = date_range(START, END, freq=pd.offsets.BMonthEnd(), unit=unit)
```

### Step 4: Assign shifted = rng.shift(...)

```python
shifted = rng.shift(1, freq=pd.offsets.CDay())
```

**Verification:**
```python
assert shifted[0] == rng[0] + pd.offsets.CDay()
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
rng = date_range(START, END, freq=pd.offsets.BMonthEnd(), unit=unit)
shifted = rng.shift(1, freq=pd.offsets.BDay())
assert shifted[0] == rng[0] + pd.offsets.BDay()
rng = date_range(START, END, freq=pd.offsets.BMonthEnd(), unit=unit)
with tm.assert_produces_warning(pd.errors.PerformanceWarning):
    shifted = rng.shift(1, freq=pd.offsets.CDay())
    assert shifted[0] == rng[0] + pd.offsets.CDay()
```

## Next Steps


---

*Source: test_shift.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*