# How To: Concat Nat Dataframes All Nat Axis 0

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat NaT dataframes all NaT axis 0

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
# Fixtures: tz1, tz2, item, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign first = DataFrame.apply(...)

```python
first = DataFrame([[pd.NaT], [pd.NaT]]).apply(lambda x: x.dt.tz_localize(tz1))
```

### Step 2: Assign second = DataFrame.apply(...)

```python
second = DataFrame([item]).apply(lambda x: x.dt.tz_localize(tz2))
```

### Step 3: Assign result = concat(...)

```python
result = concat([first, second], axis=0)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(Series([pd.NaT, pd.NaT, item], index=[0, 1, 0]))
```

### Step 5: Assign expected = expected.apply(...)

```python
expected = expected.apply(lambda x: x.dt.tz_localize(tz2))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = expected.astype(...)

```python
expected = expected.astype(object)
```

### Step 8: Assign unknown = value

```python
expected.iloc[-1, 0] = np.nan
```

### Step 9: Assign unknown = value

```python
expected.iloc[:-1, 0] = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: tz1, tz2, item, using_array_manager

# Workflow
first = DataFrame([[pd.NaT], [pd.NaT]]).apply(lambda x: x.dt.tz_localize(tz1))
second = DataFrame([item]).apply(lambda x: x.dt.tz_localize(tz2))
result = concat([first, second], axis=0)
expected = DataFrame(Series([pd.NaT, pd.NaT, item], index=[0, 1, 0]))
expected = expected.apply(lambda x: x.dt.tz_localize(tz2))
if tz1 != tz2:
    expected = expected.astype(object)
    if item is pd.NaT and (not using_array_manager):
        if tz1 is not None:
            expected.iloc[-1, 0] = np.nan
        else:
            expected.iloc[:-1, 0] = np.nan
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:217 | Complexity: Advanced | Last updated: 2026-06-02*