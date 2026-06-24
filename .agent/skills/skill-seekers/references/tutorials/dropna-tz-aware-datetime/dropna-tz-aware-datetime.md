# How To: Dropna Tz Aware Datetime

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropna tz aware datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame()
```

### Step 2: Assign dt1 = datetime.datetime(...)

```python
dt1 = datetime.datetime(2015, 1, 1, tzinfo=dateutil.tz.tzutc())
```

### Step 3: Assign dt2 = datetime.datetime(...)

```python
dt2 = datetime.datetime(2015, 2, 2, tzinfo=dateutil.tz.tzutc())
```

### Step 4: Assign unknown = value

```python
df['Time'] = [dt1]
```

### Step 5: Assign result = df.dropna(...)

```python
result = df.dropna(axis=0)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Time': [dt1]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'Time': [dt1, None, np.nan, dt2]})
```

### Step 9: Assign result = df.dropna(...)

```python
result = df.dropna(axis=0)
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame([dt1, dt2], columns=['Time'], index=[0, 3])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame()
dt1 = datetime.datetime(2015, 1, 1, tzinfo=dateutil.tz.tzutc())
dt2 = datetime.datetime(2015, 2, 2, tzinfo=dateutil.tz.tzutc())
df['Time'] = [dt1]
result = df.dropna(axis=0)
expected = DataFrame({'Time': [dt1]})
tm.assert_frame_equal(result, expected)
df = DataFrame({'Time': [dt1, None, np.nan, dt2]})
result = df.dropna(axis=0)
expected = DataFrame([dt1, dt2], columns=['Time'], index=[0, 3])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dropna.py:185 | Complexity: Advanced | Last updated: 2026-06-02*