# How To: Asfreq Normalize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq normalize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 09:30', periods=20)
```

### Step 2: Assign norm = date_range(...)

```python
norm = date_range('1/1/2000', periods=20)
```

### Step 3: Assign vals = np.random.default_rng.standard_normal(...)

```python
vals = np.random.default_rng(2).standard_normal((20, 3))
```

### Step 4: Assign obj = DataFrame(...)

```python
obj = DataFrame(vals, index=rng)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(vals, index=norm)
```

### Step 6: Assign result = obj.asfreq(...)

```python
result = obj.asfreq('D', normalize=True)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign obj = value

```python
obj = obj[0]
```

### Step 9: Assign expected = value

```python
expected = expected[0]
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000 09:30', periods=20)
norm = date_range('1/1/2000', periods=20)
vals = np.random.default_rng(2).standard_normal((20, 3))
obj = DataFrame(vals, index=rng)
expected = DataFrame(vals, index=norm)
if frame_or_series is Series:
    obj = obj[0]
    expected = expected[0]
result = obj.asfreq('D', normalize=True)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_asfreq.py:82 | Complexity: Advanced | Last updated: 2026-06-02*