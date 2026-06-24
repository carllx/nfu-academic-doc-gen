# How To: Infer Tz Utc Localize

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer tz utc localize

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
# Fixtures: infer_setup
```

## Step-by-Step Guide

### Step 1: Assign unknown = infer_setup

```python
_, _, start, end, start_naive, end_naive = infer_setup
```

**Verification:**
```python
assert timezones.infer_tzinfo(start, end) is utc
```

### Step 2: Assign utc = value

```python
utc = pytz.utc
```

### Step 3: Assign start = utc.localize(...)

```python
start = utc.localize(start_naive)
```

### Step 4: Assign end = utc.localize(...)

```python
end = utc.localize(end_naive)
```

**Verification:**
```python
assert timezones.infer_tzinfo(start, end) is utc
```


## Complete Example

```python
# Setup
# Fixtures: infer_setup

# Workflow
_, _, start, end, start_naive, end_naive = infer_setup
utc = pytz.utc
start = utc.localize(start_naive)
end = utc.localize(end_naive)
assert timezones.infer_tzinfo(start, end) is utc
```

## Next Steps


---

*Source: test_timezones.py:112 | Complexity: Intermediate | Last updated: 2026-06-02*