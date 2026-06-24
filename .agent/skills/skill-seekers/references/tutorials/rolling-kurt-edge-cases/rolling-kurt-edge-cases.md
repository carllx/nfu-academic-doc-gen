# How To: Rolling Kurt Edge Cases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling kurt edge cases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = Series([np.nan] * 4 + [-3.0])[::step]
```

### Step 2: Assign d = Series(...)

```python
d = Series([1] * 5)
```

### Step 3: Assign x = d.rolling.kurt(...)

```python
x = d.rolling(window=5, step=step).kurt()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, x)
```

### Step 5: Assign expected = value

```python
expected = Series([np.nan] * 5)[::step]
```

### Step 6: Assign d = Series(...)

```python
d = Series(np.random.default_rng(2).standard_normal(5))
```

### Step 7: Assign x = d.rolling.kurt(...)

```python
x = d.rolling(window=3, step=step).kurt()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, x)
```

### Step 9: Assign d = Series(...)

```python
d = Series([-1.50837035, -0.1297039, 0.19501095, 1.73508164, 0.41941401])
```

### Step 10: Assign expected = value

```python
expected = Series([np.nan, np.nan, np.nan, 1.224307, 2.671499])[::step]
```

### Step 11: Assign x = d.rolling.kurt(...)

```python
x = d.rolling(window=4, step=step).kurt()
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, x)
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
expected = Series([np.nan] * 4 + [-3.0])[::step]
d = Series([1] * 5)
x = d.rolling(window=5, step=step).kurt()
tm.assert_series_equal(expected, x)
expected = Series([np.nan] * 5)[::step]
d = Series(np.random.default_rng(2).standard_normal(5))
x = d.rolling(window=3, step=step).kurt()
tm.assert_series_equal(expected, x)
d = Series([-1.50837035, -0.1297039, 0.19501095, 1.73508164, 0.41941401])
expected = Series([np.nan, np.nan, np.nan, 1.224307, 2.671499])[::step]
x = d.rolling(window=4, step=step).kurt()
tm.assert_series_equal(expected, x)
```

## Next Steps


---

*Source: test_rolling_skew_kurt.py:193 | Complexity: Advanced | Last updated: 2026-06-02*