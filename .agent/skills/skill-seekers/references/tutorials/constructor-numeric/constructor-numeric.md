# How To: Constructor Numeric

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor numeric

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: closed, name, freq, periods
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
start, end = (0, 100)
```

### Step 2: Assign breaks = np.arange(...)

```python
breaks = np.arange(101, step=freq)
```

### Step 3: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks(breaks, name=name, closed=closed)
```

### Step 4: Assign result = interval_range(...)

```python
result = interval_range(start=start, end=end, freq=freq, name=name, closed=closed)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = interval_range(...)

```python
result = interval_range(start=start, periods=periods, freq=freq, name=name, closed=closed)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign result = interval_range(...)

```python
result = interval_range(end=end, periods=periods, freq=freq, name=name, closed=closed)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign result = interval_range(...)

```python
result = interval_range(start=start, end=end, periods=periods, name=name, closed=closed)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, name, freq, periods

# Workflow
start, end = (0, 100)
breaks = np.arange(101, step=freq)
expected = IntervalIndex.from_breaks(breaks, name=name, closed=closed)
result = interval_range(start=start, end=end, freq=freq, name=name, closed=closed)
tm.assert_index_equal(result, expected)
result = interval_range(start=start, periods=periods, freq=freq, name=name, closed=closed)
tm.assert_index_equal(result, expected)
result = interval_range(end=end, periods=periods, freq=freq, name=name, closed=closed)
tm.assert_index_equal(result, expected)
result = interval_range(start=start, end=end, periods=periods, name=name, closed=closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_range.py:30 | Complexity: Advanced | Last updated: 2026-06-02*