# How To: At Time Errors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test at time errors

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: hour
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2018', periods=3, freq='h')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(len(dti))), index=dti)
```

### Step 3: Assign result = df.at_time(...)

```python
result = df.at_time(hour)
```

### Step 4: Assign expected = value

```python
expected = df.iloc[1:2]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call df.at_time()

```python
df.at_time(hour)
```


## Complete Example

```python
# Setup
# Fixtures: hour

# Workflow
dti = date_range('2018', periods=3, freq='h')
df = DataFrame(list(range(len(dti))), index=dti)
if getattr(hour, 'tzinfo', None) is None:
    result = df.at_time(hour)
    expected = df.iloc[1:2]
    tm.assert_frame_equal(result, expected)
else:
    with pytest.raises(ValueError, match='Index must be timezone'):
        df.at_time(hour)
```

## Next Steps


---

*Source: test_at_time.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*