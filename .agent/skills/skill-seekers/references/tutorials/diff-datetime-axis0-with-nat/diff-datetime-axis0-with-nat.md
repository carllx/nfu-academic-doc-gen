# How To: Diff Datetime Axis0 With Nat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test diff datetime axis0 with nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = pd.DatetimeIndex.as_unit(...)

```python
dti = pd.DatetimeIndex(['NaT', '2019-01-01', '2019-01-02'], tz=tz).as_unit(unit)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 3: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 4: Assign result = df.diff(...)

```python
result = df.diff()
```

### Step 5: Assign ex_index = pd.TimedeltaIndex.as_unit(...)

```python
ex_index = pd.TimedeltaIndex([pd.NaT, pd.NaT, pd.Timedelta(days=1)]).as_unit(unit)
```

### Step 6: Assign expected = Series.to_frame(...)

```python
expected = Series(ex_index).to_frame()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz, unit

# Workflow
dti = pd.DatetimeIndex(['NaT', '2019-01-01', '2019-01-02'], tz=tz).as_unit(unit)
ser = Series(dti)
df = ser.to_frame()
result = df.diff()
ex_index = pd.TimedeltaIndex([pd.NaT, pd.NaT, pd.Timedelta(days=1)]).as_unit(unit)
expected = Series(ex_index).to_frame()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*