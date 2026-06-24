# How To: Rank

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: window, method, pct, ascending, test_data
```

## Step-by-Step Guide

### Step 1: Assign length = 20

```python
length = 20
```

### Step 2: Assign expected = ser.expanding.apply(...)

```python
expected = ser.expanding(window).apply(lambda x: x.rank(method=method, pct=pct, ascending=ascending).iloc[-1])
```

### Step 3: Assign result = ser.expanding.rank(...)

```python
result = ser.expanding(window).rank(method=method, pct=pct, ascending=ascending)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(data=np.random.default_rng(2).random(length))
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(data=np.random.default_rng(2).choice(3, length))
```

### Step 7: Assign ser = Series(...)

```python
ser = Series(data=np.random.default_rng(2).choice([1.0, 0.25, 0.75, np.nan, np.inf, -np.inf], length))
```


## Complete Example

```python
# Setup
# Fixtures: window, method, pct, ascending, test_data

# Workflow
length = 20
if test_data == 'default':
    ser = Series(data=np.random.default_rng(2).random(length))
elif test_data == 'duplicates':
    ser = Series(data=np.random.default_rng(2).choice(3, length))
elif test_data == 'nans':
    ser = Series(data=np.random.default_rng(2).choice([1.0, 0.25, 0.75, np.nan, np.inf, -np.inf], length))
expected = ser.expanding(window).apply(lambda x: x.rank(method=method, pct=pct, ascending=ascending).iloc[-1])
result = ser.expanding(window).rank(method=method, pct=pct, ascending=ascending)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*