# How To: Replace Dst Fold

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace dst fold

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.util._test_decorators`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: fold, tz, unit
```

## Step-by-Step Guide

### Step 1: Assign d = datetime(...)

```python
d = datetime(2019, 10, 27, 2, 30)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp(d, tz=tz).as_unit(unit)
```

**Verification:**
```python
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

### Step 3: Assign result = ts.replace(...)

```python
result = ts.replace(hour=1, fold=fold)
```

### Step 4: Assign expected = Timestamp.tz_localize(...)

```python
expected = Timestamp(datetime(2019, 10, 27, 1, 30)).tz_localize(tz, ambiguous=not fold)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: fold, tz, unit

# Workflow
d = datetime(2019, 10, 27, 2, 30)
ts = Timestamp(d, tz=tz).as_unit(unit)
result = ts.replace(hour=1, fold=fold)
expected = Timestamp(datetime(2019, 10, 27, 1, 30)).tz_localize(tz, ambiguous=not fold)
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

## Next Steps


---

*Source: test_replace.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*