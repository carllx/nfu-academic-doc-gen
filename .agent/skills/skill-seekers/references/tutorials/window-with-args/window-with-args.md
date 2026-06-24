# How To: Window With Args

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test window with args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign r = Series.rolling(...)

```python
r = Series(np.random.default_rng(2).standard_normal(100)).rolling(window=10, min_periods=1, win_type='gaussian', step=step)
```

### Step 3: Assign expected = concat(...)

```python
expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
```

### Step 4: Assign expected.columns = value

```python
expected.columns = ['<lambda>', '<lambda>']
```

### Step 5: Assign result = r.aggregate(...)

```python
result = r.aggregate([lambda x: x.mean(std=10), lambda x: x.mean(std=0.01)])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = concat(...)

```python
expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
```

### Step 8: Assign expected.columns = value

```python
expected.columns = ['a', 'b']
```

### Step 9: Assign result = r.aggregate(...)

```python
result = r.aggregate([a, b])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
pytest.importorskip('scipy')
r = Series(np.random.default_rng(2).standard_normal(100)).rolling(window=10, min_periods=1, win_type='gaussian', step=step)
expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
expected.columns = ['<lambda>', '<lambda>']
result = r.aggregate([lambda x: x.mean(std=10), lambda x: x.mean(std=0.01)])
tm.assert_frame_equal(result, expected)

def a(x):
    return x.mean(std=10)

def b(x):
    return x.mean(std=0.01)
expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
expected.columns = ['a', 'b']
result = r.aggregate([a, b])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_win_type.py:109 | Complexity: Advanced | Last updated: 2026-06-02*