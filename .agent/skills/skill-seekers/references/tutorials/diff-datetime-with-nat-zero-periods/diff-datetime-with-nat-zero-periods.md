# How To: Diff Datetime With Nat Zero Periods

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test diff datetime with nat zero periods

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
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=4, tz=tz)
```

**Verification:**
```python
assert expected[0].isna().all()
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 3: Assign df = ser.to_frame.copy(...)

```python
df = ser.to_frame().copy()
```

### Step 4: Assign unknown = ser.copy(...)

```python
df[1] = ser.copy()
```

### Step 5: Assign unknown = value

```python
df.iloc[:, 0] = pd.NaT
```

### Step 6: Assign expected = value

```python
expected = df - df
```

**Verification:**
```python
assert expected[0].isna().all()
```

### Step 7: Assign result = df.diff(...)

```python
result = df.diff(0, axis=0)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.diff(...)

```python
result = df.diff(0, axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dti = date_range('2016-01-01', periods=4, tz=tz)
ser = Series(dti)
df = ser.to_frame().copy()
df[1] = ser.copy()
df.iloc[:, 0] = pd.NaT
expected = df - df
assert expected[0].isna().all()
result = df.diff(0, axis=0)
tm.assert_frame_equal(result, expected)
result = df.diff(0, axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:88 | Complexity: Advanced | Last updated: 2026-06-02*