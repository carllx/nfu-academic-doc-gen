# How To: All Nans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: date_range_frame
```

## Step-by-Step Guide

### Step 1: Assign N = 150

```python
N = 150
```

### Step 2: Assign rng = value

```python
rng = date_range_frame.index
```

### Step 3: Assign dates = date_range(...)

```python
dates = date_range('1/1/1990', periods=N, freq='25s')
```

### Step 4: Assign result = DataFrame.asof(...)

```python
result = DataFrame(np.nan, index=rng, columns=['A']).asof(dates)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.nan, index=dates, columns=['A'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign dates = date_range(...)

```python
dates = date_range('1/1/1990', periods=N, freq='25s')
```

### Step 8: Assign result = DataFrame.asof(...)

```python
result = DataFrame(np.nan, index=rng, columns=['A', 'B', 'C']).asof(dates)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.nan, index=dates, columns=['A', 'B', 'C'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = DataFrame.asof(...)

```python
result = DataFrame(np.nan, index=[1, 2], columns=['A', 'B']).asof([3])
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.nan, index=[3], columns=['A', 'B'])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = DataFrame.asof(...)

```python
result = DataFrame(np.nan, index=[1, 2], columns=['A', 'B']).asof(3)
```

### Step 15: Assign expected = Series(...)

```python
expected = Series(np.nan, index=['A', 'B'], name=3)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: date_range_frame

# Workflow
N = 150
rng = date_range_frame.index
dates = date_range('1/1/1990', periods=N, freq='25s')
result = DataFrame(np.nan, index=rng, columns=['A']).asof(dates)
expected = DataFrame(np.nan, index=dates, columns=['A'])
tm.assert_frame_equal(result, expected)
dates = date_range('1/1/1990', periods=N, freq='25s')
result = DataFrame(np.nan, index=rng, columns=['A', 'B', 'C']).asof(dates)
expected = DataFrame(np.nan, index=dates, columns=['A', 'B', 'C'])
tm.assert_frame_equal(result, expected)
result = DataFrame(np.nan, index=[1, 2], columns=['A', 'B']).asof([3])
expected = DataFrame(np.nan, index=[3], columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
result = DataFrame(np.nan, index=[1, 2], columns=['A', 'B']).asof(3)
expected = Series(np.nan, index=['A', 'B'], name=3)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_asof.py:111 | Complexity: Advanced | Last updated: 2026-06-02*