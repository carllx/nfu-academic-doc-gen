# How To: Groupby Std Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby std datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign tdi = pd.timedelta_range(...)

```python
tdi = pd.timedelta_range('1 Day', periods=10000)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(tdi)
```

### Step 3: Assign df = ser.to_frame.copy(...)

```python
df = ser.to_frame('A').copy()
```

### Step 4: Assign unknown = value

```python
df['B'] = ser + Timestamp(0)
```

### Step 5: Assign unknown = value

```python
df['C'] = ser + Timestamp(0, tz='UTC')
```

### Step 6: Assign unknown = value

```python
df.iloc[-1] = pd.NaT
```

### Step 7: Assign gb = df.groupby(...)

```python
gb = df.groupby(list(range(5)) * 2000)
```

### Step 8: Assign result = gb.std(...)

```python
result = gb.std()
```

### Step 9: Assign td1 = Timedelta(...)

```python
td1 = Timedelta('2887 days 11:21:02.326710176')
```

### Step 10: Assign td4 = Timedelta(...)

```python
td4 = Timedelta('2886 days 00:42:34.664668096')
```

### Step 11: Assign exp_ser = Series(...)

```python
exp_ser = Series([td1 * 2, td1, td1, td1, td4], index=np.arange(5))
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': exp_ser, 'B': exp_ser, 'C': exp_ser})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: warn_copy_on_write

# Workflow
tdi = pd.timedelta_range('1 Day', periods=10000)
ser = Series(tdi)
ser[::5] *= 2
df = ser.to_frame('A').copy()
df['B'] = ser + Timestamp(0)
df['C'] = ser + Timestamp(0, tz='UTC')
df.iloc[-1] = pd.NaT
gb = df.groupby(list(range(5)) * 2000)
result = gb.std()
td1 = Timedelta('2887 days 11:21:02.326710176')
td4 = Timedelta('2886 days 00:42:34.664668096')
exp_ser = Series([td1 * 2, td1, td1, td1, td4], index=np.arange(5))
expected = DataFrame({'A': exp_ser, 'B': exp_ser, 'C': exp_ser})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:44 | Complexity: Advanced | Last updated: 2026-06-02*