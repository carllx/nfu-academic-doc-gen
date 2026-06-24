# How To: To Period Quarterly

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to period quarterly

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `dateutil.tz`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: month
```

## Step-by-Step Guide

### Step 1: Assign freq = value

```python
freq = f'Q-{month}'
```

### Step 2: Assign rng = period_range(...)

```python
rng = period_range('1989Q3', '1991Q3', freq=freq)
```

### Step 3: Assign stamps = rng.to_timestamp(...)

```python
stamps = rng.to_timestamp()
```

### Step 4: Assign result = stamps.to_period(...)

```python
result = stamps.to_period(freq)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng, result)
```


## Complete Example

```python
# Setup
# Fixtures: month

# Workflow
freq = f'Q-{month}'
rng = period_range('1989Q3', '1991Q3', freq=freq)
stamps = rng.to_timestamp()
result = stamps.to_period(freq)
tm.assert_index_equal(rng, result)
```

## Next Steps


---

*Source: test_to_period.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*