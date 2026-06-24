# How To: Concatlike Datetimetz Short

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concatlike datetimetz short

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

### Step 1: Assign ix1 = pd.date_range(...)

```python
ix1 = pd.date_range(start='2014-07-15', end='2014-07-17', freq='D', tz=tz)
```

### Step 2: Assign ix2 = pd.DatetimeIndex(...)

```python
ix2 = pd.DatetimeIndex(['2014-07-11', '2014-07-21'], tz=tz)
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(0, index=ix1, columns=['A', 'B'])
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(0, index=ix2, columns=['A', 'B'])
```

### Step 5: Assign exp_idx = pd.DatetimeIndex.as_unit(...)

```python
exp_idx = pd.DatetimeIndex(['2014-07-15', '2014-07-16', '2014-07-17', '2014-07-11', '2014-07-21'], tz=tz).as_unit('ns')
```

### Step 6: Assign exp = DataFrame(...)

```python
exp = DataFrame(0, index=exp_idx, columns=['A', 'B'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1._append(df2), exp)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(pd.concat([df1, df2]), exp)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
ix1 = pd.date_range(start='2014-07-15', end='2014-07-17', freq='D', tz=tz)
ix2 = pd.DatetimeIndex(['2014-07-11', '2014-07-21'], tz=tz)
df1 = DataFrame(0, index=ix1, columns=['A', 'B'])
df2 = DataFrame(0, index=ix2, columns=['A', 'B'])
exp_idx = pd.DatetimeIndex(['2014-07-15', '2014-07-16', '2014-07-17', '2014-07-11', '2014-07-21'], tz=tz).as_unit('ns')
exp = DataFrame(0, index=exp_idx, columns=['A', 'B'])
tm.assert_frame_equal(df1._append(df2), exp)
tm.assert_frame_equal(pd.concat([df1, df2]), exp)
```

## Next Steps


---

*Source: test_append_common.py:310 | Complexity: Advanced | Last updated: 2026-06-02*