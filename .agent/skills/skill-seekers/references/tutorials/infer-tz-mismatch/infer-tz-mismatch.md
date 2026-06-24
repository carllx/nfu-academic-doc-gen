# How To: Infer Tz Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infer tz mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`

**Setup Required:**
```python
# Fixtures: infer_setup, ordered
```

## Step-by-Step Guide

### Step 1: Assign unknown = infer_setup

```python
eastern, _, _, _, start_naive, end_naive = infer_setup
```

### Step 2: Assign msg = 'Inputs must both have the same timezone'

```python
msg = 'Inputs must both have the same timezone'
```

### Step 3: Assign utc = value

```python
utc = pytz.utc
```

### Step 4: Assign start = utc.localize(...)

```python
start = utc.localize(start_naive)
```

### Step 5: Assign end = conversion.localize_pydatetime(...)

```python
end = conversion.localize_pydatetime(end_naive, eastern)
```

### Step 6: Assign args = value

```python
args = (start, end) if ordered else (end, start)
```

### Step 7: Call timezones.infer_tzinfo()

```python
timezones.infer_tzinfo(*args)
```


## Complete Example

```python
# Setup
# Fixtures: infer_setup, ordered

# Workflow
eastern, _, _, _, start_naive, end_naive = infer_setup
msg = 'Inputs must both have the same timezone'
utc = pytz.utc
start = utc.localize(start_naive)
end = conversion.localize_pydatetime(end_naive, eastern)
args = (start, end) if ordered else (end, start)
with pytest.raises(AssertionError, match=msg):
    timezones.infer_tzinfo(*args)
```

## Next Steps


---

*Source: test_timezones.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*