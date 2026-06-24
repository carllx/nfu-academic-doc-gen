# How To: Nanosecond Getitem Setitem With Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanosecond getitem setitem with tz

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['2016-06-28 08:30:00.123456789']
```

### Step 2: Assign index = pd.DatetimeIndex(...)

```python
index = pd.DatetimeIndex(data, dtype='datetime64[ns, America/Chicago]')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [10]}, index=index)
```

### Step 4: Assign result = value

```python
result = df.loc[df.index[0]]
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(10, index=['a'], name=df.index[0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = df.copy(...)

```python
result = df.copy()
```

### Step 8: Assign unknown = value

```python
result.loc[df.index[0], 'a'] = -1
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(-1, index=index, columns=['a'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = ['2016-06-28 08:30:00.123456789']
index = pd.DatetimeIndex(data, dtype='datetime64[ns, America/Chicago]')
df = DataFrame({'a': [10]}, index=index)
result = df.loc[df.index[0]]
expected = Series(10, index=['a'], name=df.index[0])
tm.assert_series_equal(result, expected)
result = df.copy()
result.loc[df.index[0], 'a'] = -1
expected = DataFrame(-1, index=index, columns=['a'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:138 | Complexity: Advanced | Last updated: 2026-06-02*