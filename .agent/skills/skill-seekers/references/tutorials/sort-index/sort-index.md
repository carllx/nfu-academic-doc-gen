# How To: Sort Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign datetime_series.index = datetime_series.index._with_freq(...)

```python
datetime_series.index = datetime_series.index._with_freq(None)
```

### Step 2: Assign rindex = list(...)

```python
rindex = list(datetime_series.index)
```

### Step 3: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(rindex)
```

### Step 4: Assign random_order = datetime_series.reindex(...)

```python
random_order = datetime_series.reindex(rindex)
```

### Step 5: Assign sorted_series = random_order.sort_index(...)

```python
sorted_series = random_order.sort_index()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sorted_series, datetime_series)
```

### Step 7: Assign sorted_series = random_order.sort_index(...)

```python
sorted_series = random_order.sort_index(ascending=False)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sorted_series, datetime_series.reindex(datetime_series.index[::-1]))
```

### Step 9: Assign sorted_series = random_order.sort_index(...)

```python
sorted_series = random_order.sort_index(level=0)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sorted_series, datetime_series)
```

### Step 11: Assign sorted_series = random_order.sort_index(...)

```python
sorted_series = random_order.sort_index(axis=0)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sorted_series, datetime_series)
```

### Step 13: Assign msg = 'No axis named 1 for object type Series'

```python
msg = 'No axis named 1 for object type Series'
```

### Step 14: Assign sorted_series = random_order.sort_index(...)

```python
sorted_series = random_order.sort_index(level=0, axis=0)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sorted_series, datetime_series)
```

### Step 16: Call random_order.sort_values()

```python
random_order.sort_values(axis=1)
```

### Step 17: Call random_order.sort_index()

```python
random_order.sort_index(level=0, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
datetime_series.index = datetime_series.index._with_freq(None)
rindex = list(datetime_series.index)
np.random.default_rng(2).shuffle(rindex)
random_order = datetime_series.reindex(rindex)
sorted_series = random_order.sort_index()
tm.assert_series_equal(sorted_series, datetime_series)
sorted_series = random_order.sort_index(ascending=False)
tm.assert_series_equal(sorted_series, datetime_series.reindex(datetime_series.index[::-1]))
sorted_series = random_order.sort_index(level=0)
tm.assert_series_equal(sorted_series, datetime_series)
sorted_series = random_order.sort_index(axis=0)
tm.assert_series_equal(sorted_series, datetime_series)
msg = 'No axis named 1 for object type Series'
with pytest.raises(ValueError, match=msg):
    random_order.sort_values(axis=1)
sorted_series = random_order.sort_index(level=0, axis=0)
tm.assert_series_equal(sorted_series, datetime_series)
with pytest.raises(ValueError, match=msg):
    random_order.sort_index(level=0, axis=1)
```

## Next Steps


---

*Source: test_sort_index.py:23 | Complexity: Advanced | Last updated: 2026-06-02*