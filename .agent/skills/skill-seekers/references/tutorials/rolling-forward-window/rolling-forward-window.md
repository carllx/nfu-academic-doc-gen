# How To: Rolling Forward Window

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling forward window

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: frame_or_series, func, np_func, expected, np_kwargs, step
```

## Step-by-Step Guide

### Step 1: Assign values = np.arange(...)

```python
values = np.arange(10.0)
```

### Step 2: Assign unknown = 100.0

```python
values[5] = 100.0
```

### Step 3: Assign indexer = FixedForwardWindowIndexer(...)

```python
indexer = FixedForwardWindowIndexer(window_size=3)
```

### Step 4: Assign match = "Forward-looking windows can't have center=True"

```python
match = "Forward-looking windows can't have center=True"
```

### Step 5: Assign match = "Forward-looking windows don't support setting the closed argument"

```python
match = "Forward-looking windows don't support setting the closed argument"
```

### Step 6: Assign rolling = frame_or_series.rolling(...)

```python
rolling = frame_or_series(values).rolling(window=indexer, min_periods=2, step=step)
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(rolling, func)()
```

### Step 8: Assign expected = value

```python
expected = frame_or_series(expected)[::step]
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 10: Assign expected2 = frame_or_series(...)

```python
expected2 = frame_or_series(rolling.apply(lambda x: np_func(x, **np_kwargs)))
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(result, expected2)
```

### Step 12: Assign min_periods = value

```python
min_periods = 0 if func == 'count' else None
```

### Step 13: Assign rolling3 = frame_or_series.rolling(...)

```python
rolling3 = frame_or_series(values).rolling(window=indexer, min_periods=min_periods)
```

### Step 14: Assign result3 = getattr(...)

```python
result3 = getattr(rolling3, func)()
```

### Step 15: Assign expected3 = frame_or_series(...)

```python
expected3 = frame_or_series(rolling3.apply(lambda x: np_func(x, **np_kwargs)))
```

### Step 16: Call tm.assert_equal()

```python
tm.assert_equal(result3, expected3)
```

### Step 17: Assign rolling = frame_or_series.rolling(...)

```python
rolling = frame_or_series(values).rolling(window=indexer, center=True)
```

### Step 18: Call getattr()

```python
getattr(rolling, func)()
```

### Step 19: Assign rolling = frame_or_series.rolling(...)

```python
rolling = frame_or_series(values).rolling(window=indexer, closed='right')
```

### Step 20: Call getattr()

```python
getattr(rolling, func)()
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, func, np_func, expected, np_kwargs, step

# Workflow
values = np.arange(10.0)
values[5] = 100.0
indexer = FixedForwardWindowIndexer(window_size=3)
match = "Forward-looking windows can't have center=True"
with pytest.raises(ValueError, match=match):
    rolling = frame_or_series(values).rolling(window=indexer, center=True)
    getattr(rolling, func)()
match = "Forward-looking windows don't support setting the closed argument"
with pytest.raises(ValueError, match=match):
    rolling = frame_or_series(values).rolling(window=indexer, closed='right')
    getattr(rolling, func)()
rolling = frame_or_series(values).rolling(window=indexer, min_periods=2, step=step)
result = getattr(rolling, func)()
expected = frame_or_series(expected)[::step]
tm.assert_equal(result, expected)
expected2 = frame_or_series(rolling.apply(lambda x: np_func(x, **np_kwargs)))
tm.assert_equal(result, expected2)
min_periods = 0 if func == 'count' else None
rolling3 = frame_or_series(values).rolling(window=indexer, min_periods=min_periods)
result3 = getattr(rolling3, func)()
expected3 = frame_or_series(rolling3.apply(lambda x: np_func(x, **np_kwargs)))
tm.assert_equal(result3, expected3)
```

## Next Steps


---

*Source: test_base_indexer.py:150 | Complexity: Advanced | Last updated: 2026-06-02*