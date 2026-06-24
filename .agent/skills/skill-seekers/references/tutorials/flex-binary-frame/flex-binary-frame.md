# How To: Flex Binary Frame

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test flex binary frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: method, frame
```

## Step-by-Step Guide

### Step 1: Assign series = value

```python
series = frame[1]
```

### Step 2: Assign res = getattr(...)

```python
res = getattr(series.rolling(window=10), method)(frame)
```

### Step 3: Assign res2 = getattr(...)

```python
res2 = getattr(frame.rolling(window=10), method)(series)
```

### Step 4: Assign exp = frame.apply(...)

```python
exp = frame.apply(lambda x: getattr(series.rolling(window=10), method)(x))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, exp)
```

### Step 7: Assign frame2 = frame.copy(...)

```python
frame2 = frame.copy()
```

### Step 8: Assign frame2 = DataFrame(...)

```python
frame2 = DataFrame(np.random.default_rng(2).standard_normal(frame2.shape), index=frame2.index, columns=frame2.columns)
```

### Step 9: Assign res3 = getattr(...)

```python
res3 = getattr(frame.rolling(window=10), method)(frame2)
```

### Step 10: Assign exp = DataFrame(...)

```python
exp = DataFrame({k: getattr(frame[k].rolling(window=10), method)(frame2[k]) for k in frame})
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res3, exp)
```


## Complete Example

```python
# Setup
# Fixtures: method, frame

# Workflow
series = frame[1]
res = getattr(series.rolling(window=10), method)(frame)
res2 = getattr(frame.rolling(window=10), method)(series)
exp = frame.apply(lambda x: getattr(series.rolling(window=10), method)(x))
tm.assert_frame_equal(res, exp)
tm.assert_frame_equal(res2, exp)
frame2 = frame.copy()
frame2 = DataFrame(np.random.default_rng(2).standard_normal(frame2.shape), index=frame2.index, columns=frame2.columns)
res3 = getattr(frame.rolling(window=10), method)(frame2)
exp = DataFrame({k: getattr(frame[k].rolling(window=10), method)(frame2[k]) for k in frame})
tm.assert_frame_equal(res3, exp)
```

## Next Steps


---

*Source: test_pairwise.py:89 | Complexity: Advanced | Last updated: 2026-06-02*