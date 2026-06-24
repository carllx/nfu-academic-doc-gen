# How To: Indexing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2001-1-1', periods=20, freq='ME')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).random(len(idx)), index=idx)
```

### Step 3: Assign result = value

```python
result = ts['2001']
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ts.iloc[:12])
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ts.copy()})
```

### Step 6: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).random(len(idx)), index=idx)
```

### Step 7: Assign expected = ts.copy(...)

```python
expected = ts.copy()
```

### Step 8: Assign unknown = 1

```python
expected.iloc[:12] = 1
```

### Step 9: Assign unknown = 1

```python
ts['2001'] = 1
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts, expected)
```

### Step 11: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 12: Assign unknown = 1

```python
expected.iloc[:12, 0] = 1
```

### Step 13: Assign unknown = 1

```python
df.loc['2001', 'A'] = 1
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 15: df['2001']

```python
df['2001']
```


## Complete Example

```python
# Workflow
idx = date_range('2001-1-1', periods=20, freq='ME')
ts = Series(np.random.default_rng(2).random(len(idx)), index=idx)
result = ts['2001']
tm.assert_series_equal(result, ts.iloc[:12])
df = DataFrame({'A': ts.copy()})
with pytest.raises(KeyError, match='2001'):
    df['2001']
ts = Series(np.random.default_rng(2).random(len(idx)), index=idx)
expected = ts.copy()
expected.iloc[:12] = 1
ts['2001'] = 1
tm.assert_series_equal(ts, expected)
expected = df.copy()
expected.iloc[:12, 0] = 1
df.loc['2001', 'A'] = 1
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_datetime.py:423 | Complexity: Advanced | Last updated: 2026-06-02*