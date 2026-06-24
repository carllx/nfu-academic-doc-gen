# How To: Diff Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff timedelta

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'time': [Timestamp('20130101 9:01'), Timestamp('20130101 9:02')], 'value': [1.0, 2.0]})
```

### Step 2: Assign unknown = unknown.dt.as_unit(...)

```python
df['time'] = df['time'].dt.as_unit(unit)
```

### Step 3: Assign res = df.diff(...)

```python
res = df.diff()
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame([[pd.NaT, np.nan], [pd.Timedelta('00:01:00'), 1]], columns=['time', 'value'])
```

### Step 5: Assign unknown = unknown.dt.as_unit(...)

```python
exp['time'] = exp['time'].dt.as_unit(unit)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
df = DataFrame({'time': [Timestamp('20130101 9:01'), Timestamp('20130101 9:02')], 'value': [1.0, 2.0]})
df['time'] = df['time'].dt.as_unit(unit)
res = df.diff()
exp = DataFrame([[pd.NaT, np.nan], [pd.Timedelta('00:01:00'), 1]], columns=['time', 'value'])
exp['time'] = exp['time'].dt.as_unit(unit)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_diff.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*