# How To: Update Times Mean

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test update times mean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: obj, nogil, parallel, nopython, adjust, ignore_na, halflife_with_times
```

## Step-by-Step Guide

### Step 1: Assign times = Series(...)

```python
times = Series(np.array(['2020-01-01', '2020-01-05', '2020-01-07', '2020-01-17', '2020-01-21'], dtype='datetime64[ns]'))
```

### Step 2: Assign expected = obj.ewm.mean(...)

```python
expected = obj.ewm(0.5, adjust=adjust, ignore_na=ignore_na, times=times, halflife=halflife_with_times).mean()
```

### Step 3: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 4: Assign online_ewm = obj.head.ewm.online(...)

```python
online_ewm = obj.head(2).ewm(0.5, adjust=adjust, ignore_na=ignore_na, times=times.head(2), halflife=halflife_with_times).online(engine_kwargs=engine_kwargs)
```

### Step 5: Assign result = online_ewm.mean(...)

```python
result = online_ewm.mean()
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected.head(2))
```

### Step 7: Assign result = online_ewm.mean(...)

```python
result = online_ewm.mean(update=obj.tail(3), update_times=times.tail(3))
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected.tail(3))
```

### Step 9: Call online_ewm.reset()

```python
online_ewm.reset()
```


## Complete Example

```python
# Setup
# Fixtures: obj, nogil, parallel, nopython, adjust, ignore_na, halflife_with_times

# Workflow
times = Series(np.array(['2020-01-01', '2020-01-05', '2020-01-07', '2020-01-17', '2020-01-21'], dtype='datetime64[ns]'))
expected = obj.ewm(0.5, adjust=adjust, ignore_na=ignore_na, times=times, halflife=halflife_with_times).mean()
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
online_ewm = obj.head(2).ewm(0.5, adjust=adjust, ignore_na=ignore_na, times=times.head(2), halflife=halflife_with_times).online(engine_kwargs=engine_kwargs)
for _ in range(2):
    result = online_ewm.mean()
    tm.assert_equal(result, expected.head(2))
    result = online_ewm.mean(update=obj.tail(3), update_times=times.tail(3))
    tm.assert_equal(result, expected.tail(3))
    online_ewm.reset()
```

## Next Steps


---

*Source: test_online.py:65 | Complexity: Advanced | Last updated: 2026-06-02*