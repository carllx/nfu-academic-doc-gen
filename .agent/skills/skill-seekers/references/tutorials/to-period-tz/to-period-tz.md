# How To: To Period Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to period tz

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
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign ts = date_range(...)

```python
ts = date_range('1/1/2000', '2/1/2000', tz=tz)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = date_range.to_period(...)

```python
expected = date_range('1/1/2000', '2/1/2000').to_period()
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign result = value

```python
result = ts.to_period()[0]
```

### Step 5: Assign expected = unknown.to_period(...)

```python
expected = ts[0].to_period(ts.freq)
```

### Step 6: Assign result = ts.to_period(...)

```python
result = ts.to_period(ts.freq)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
ts = date_range('1/1/2000', '2/1/2000', tz=tz)
with tm.assert_produces_warning(UserWarning):
    result = ts.to_period()[0]
    expected = ts[0].to_period(ts.freq)
assert result == expected
expected = date_range('1/1/2000', '2/1/2000').to_period()
with tm.assert_produces_warning(UserWarning):
    result = ts.to_period(ts.freq)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_to_period.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*