# How To: Special Holidays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test special holidays

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`

**Setup Required:**
```python
# Fixtures: name, kwargs
```

## Step-by-Step Guide

### Step 1: Assign base_date = value

```python
base_date = [datetime(2012, 5, 28)]
```

**Verification:**
```python
assert base_date == holiday.dates(start_date, end_date)
```

### Step 2: Assign holiday = Holiday(...)

```python
holiday = Holiday(name, **kwargs)
```

### Step 3: Assign start_date = datetime(...)

```python
start_date = datetime(2011, 1, 1)
```

### Step 4: Assign end_date = datetime(...)

```python
end_date = datetime(2020, 12, 31)
```

**Verification:**
```python
assert base_date == holiday.dates(start_date, end_date)
```


## Complete Example

```python
# Setup
# Fixtures: name, kwargs

# Workflow
base_date = [datetime(2012, 5, 28)]
holiday = Holiday(name, **kwargs)
start_date = datetime(2011, 1, 1)
end_date = datetime(2020, 12, 31)
assert base_date == holiday.dates(start_date, end_date)
```

## Next Steps


---

*Source: test_holiday.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*