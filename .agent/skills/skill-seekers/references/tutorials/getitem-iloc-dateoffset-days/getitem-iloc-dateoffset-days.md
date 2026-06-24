# How To: Getitem Iloc Dateoffset Days

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem iloc dateoffset days

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(days=1)))
```

### Step 2: Assign result = value

```python
result = df.loc['2022-01-01':'2022-01-03']
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([0, 1, 2], index=DatetimeIndex(['2022-01-01', '2022-01-02', '2022-01-03'], dtype='datetime64[ns]', freq=DateOffset(days=1)))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(days=1, hours=2)))
```

### Step 6: Assign result = value

```python
result = df.loc['2022-01-01':'2022-01-03']
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([0, 1, 2], index=DatetimeIndex(['2022-01-01 00:00:00', '2022-01-02 02:00:00', '2022-01-03 04:00:00'], dtype='datetime64[ns]', freq=DateOffset(days=1, hours=2)))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(minutes=3)))
```

### Step 10: Assign result = value

```python
result = df.loc['2022-01-01':'2022-01-03']
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Workflow
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(days=1)))
result = df.loc['2022-01-01':'2022-01-03']
expected = DataFrame([0, 1, 2], index=DatetimeIndex(['2022-01-01', '2022-01-02', '2022-01-03'], dtype='datetime64[ns]', freq=DateOffset(days=1)))
tm.assert_frame_equal(result, expected)
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(days=1, hours=2)))
result = df.loc['2022-01-01':'2022-01-03']
expected = DataFrame([0, 1, 2], index=DatetimeIndex(['2022-01-01 00:00:00', '2022-01-02 02:00:00', '2022-01-03 04:00:00'], dtype='datetime64[ns]', freq=DateOffset(days=1, hours=2)))
tm.assert_frame_equal(result, expected)
df = DataFrame(list(range(10)), index=date_range('01-01-2022', periods=10, freq=DateOffset(minutes=3)))
result = df.loc['2022-01-01':'2022-01-03']
tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_getitem.py:175 | Complexity: Advanced | Last updated: 2026-06-02*