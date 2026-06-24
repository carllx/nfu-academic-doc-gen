# How To: Cython Vs Numba Times

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython vs numba times

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `numba`
- `numba`

**Setup Required:**
```python
# Fixtures: grouper, nogil, parallel, nopython, ignore_na
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'B': [0, 0, 1, 1, 2, 2]})
```

### Step 2: Assign halflife = '23 days'

```python
halflife = '23 days'
```

### Step 3: Assign times = to_datetime(...)

```python
times = to_datetime(['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-10', '2020-02-23', '2020-01-03'])
```

### Step 4: Assign ewm = grouper.ewm(...)

```python
ewm = grouper(df).ewm(halflife=halflife, adjust=True, ignore_na=ignore_na, times=times)
```

### Step 5: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 6: Assign result = ewm.mean(...)

```python
result = ewm.mean(engine='numba', engine_kwargs=engine_kwargs)
```

### Step 7: Assign expected = ewm.mean(...)

```python
expected = ewm.mean(engine='cython')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign grouper = value

```python
grouper = lambda x: x
```

### Step 10: Assign grouper = value

```python
grouper = lambda x: x.groupby('A')
```

### Step 11: Assign unknown = value

```python
df['A'] = ['a', 'b', 'a', 'b', 'b', 'a']
```


## Complete Example

```python
# Setup
# Fixtures: grouper, nogil, parallel, nopython, ignore_na

# Workflow
df = DataFrame({'B': [0, 0, 1, 1, 2, 2]})
if grouper == 'None':
    grouper = lambda x: x
else:
    grouper = lambda x: x.groupby('A')
    df['A'] = ['a', 'b', 'a', 'b', 'b', 'a']
halflife = '23 days'
times = to_datetime(['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-10', '2020-02-23', '2020-01-03'])
ewm = grouper(df).ewm(halflife=halflife, adjust=True, ignore_na=ignore_na, times=times)
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
result = ewm.mean(engine='numba', engine_kwargs=engine_kwargs)
expected = ewm.mean(engine='cython')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:270 | Complexity: Advanced | Last updated: 2026-06-02*