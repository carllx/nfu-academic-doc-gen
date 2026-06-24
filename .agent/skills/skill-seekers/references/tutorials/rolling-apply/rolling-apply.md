# How To: Rolling Apply

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling apply

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
# Fixtures: engine_and_raw, step
```

## Step-by-Step Guide

### Step 1: Assign unknown = engine_and_raw

```python
engine, raw = engine_and_raw
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([], dtype='float64')
```

### Step 3: Assign result = expected.rolling.apply(...)

```python
result = expected.rolling(10, step=step).apply(lambda x: x.mean(), engine=engine, raw=raw)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign s = Series(...)

```python
s = Series([None, None, None])
```

### Step 6: Assign result = s.rolling.apply(...)

```python
result = s.rolling(2, min_periods=0, step=step).apply(lambda x: len(x), engine=engine, raw=raw)
```

### Step 7: Assign expected = value

```python
expected = Series([1.0, 2.0, 2.0])[::step]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = s.rolling.apply(...)

```python
result = s.rolling(2, min_periods=0, step=step).apply(len, engine=engine, raw=raw)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine_and_raw, step

# Workflow
engine, raw = engine_and_raw
expected = Series([], dtype='float64')
result = expected.rolling(10, step=step).apply(lambda x: x.mean(), engine=engine, raw=raw)
tm.assert_series_equal(result, expected)
s = Series([None, None, None])
result = s.rolling(2, min_periods=0, step=step).apply(lambda x: len(x), engine=engine, raw=raw)
expected = Series([1.0, 2.0, 2.0])[::step]
tm.assert_series_equal(result, expected)
result = s.rolling(2, min_periods=0, step=step).apply(len, engine=engine, raw=raw)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:76 | Complexity: Advanced | Last updated: 2026-06-02*