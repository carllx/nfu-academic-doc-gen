# How To: Concat Nat Dataframes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat NaT dataframes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([pd.NaT, pd.NaT], tz=tz)
```

### Step 2: Assign first = DataFrame(...)

```python
first = DataFrame({0: dti})
```

### Step 3: Assign second = DataFrame(...)

```python
second = DataFrame([[Timestamp('2015/01/01', tz=tz)], [Timestamp('2016/01/01', tz=tz)]], index=[2, 3])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([pd.NaT, pd.NaT, Timestamp('2015/01/01', tz=tz), Timestamp('2016/01/01', tz=tz)])
```

### Step 5: Assign result = concat(...)

```python
result = concat([first, second], axis=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dti = DatetimeIndex([pd.NaT, pd.NaT], tz=tz)
first = DataFrame({0: dti})
second = DataFrame([[Timestamp('2015/01/01', tz=tz)], [Timestamp('2016/01/01', tz=tz)]], index=[2, 3])
expected = DataFrame([pd.NaT, pd.NaT, Timestamp('2015/01/01', tz=tz), Timestamp('2016/01/01', tz=tz)])
result = concat([first, second], axis=0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*