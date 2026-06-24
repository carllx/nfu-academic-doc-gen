# How To: Ragged Apply

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ragged apply

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: engine_and_raw
```

## Step-by-Step Guide

### Step 1: Assign unknown = engine_and_raw

```python
engine, raw = engine_and_raw
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'B': range(5)})
```

### Step 3: Assign df.index = value

```python
df.index = [Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]
```

### Step 4: Assign f = value

```python
f = lambda x: 1
```

### Step 5: Assign result = df.rolling.apply(...)

```python
result = df.rolling(window='1s', min_periods=1).apply(f, engine=engine, raw=raw)
```

### Step 6: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 7: Assign unknown = 1.0

```python
expected['B'] = 1.0
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.rolling.apply(...)

```python
result = df.rolling(window='2s', min_periods=1).apply(f, engine=engine, raw=raw)
```

### Step 10: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 11: Assign unknown = 1.0

```python
expected['B'] = 1.0
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = df.rolling.apply(...)

```python
result = df.rolling(window='5s', min_periods=1).apply(f, engine=engine, raw=raw)
```

### Step 14: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 15: Assign unknown = 1.0

```python
expected['B'] = 1.0
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine_and_raw

# Workflow
engine, raw = engine_and_raw
df = DataFrame({'B': range(5)})
df.index = [Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]
f = lambda x: 1
result = df.rolling(window='1s', min_periods=1).apply(f, engine=engine, raw=raw)
expected = df.copy()
expected['B'] = 1.0
tm.assert_frame_equal(result, expected)
result = df.rolling(window='2s', min_periods=1).apply(f, engine=engine, raw=raw)
expected = df.copy()
expected['B'] = 1.0
tm.assert_frame_equal(result, expected)
result = df.rolling(window='5s', min_periods=1).apply(f, engine=engine, raw=raw)
expected = df.copy()
expected['B'] = 1.0
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:114 | Complexity: Advanced | Last updated: 2026-06-02*