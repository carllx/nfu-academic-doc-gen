# How To: Sort Index Inplace

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index inplace

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

**Verification:**
```python
assert result is None
```

### Step 2: Assign rindex = list(...)

```python
rindex = list(datetime_series.index)
```

**Verification:**
```python
assert result is None
```

### Step 3: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(rindex)
```

### Step 4: Assign random_order = datetime_series.reindex(...)

```python
random_order = datetime_series.reindex(rindex)
```

### Step 5: Assign result = random_order.sort_index(...)

```python
result = random_order.sort_index(ascending=False, inplace=True)
```

**Verification:**
```python
assert result is None
```

### Step 6: Assign expected = datetime_series.reindex(...)

```python
expected = datetime_series.reindex(datetime_series.index[::-1])
```

### Step 7: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(random_order, expected)
```

### Step 9: Assign random_order = datetime_series.reindex(...)

```python
random_order = datetime_series.reindex(rindex)
```

### Step 10: Assign result = random_order.sort_index(...)

```python
result = random_order.sort_index(ascending=True, inplace=True)
```

**Verification:**
```python
assert result is None
```

### Step 11: Assign expected = datetime_series.copy(...)

```python
expected = datetime_series.copy()
```

### Step 12: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(random_order, expected)
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
result = random_order.sort_index(ascending=False, inplace=True)
assert result is None
expected = datetime_series.reindex(datetime_series.index[::-1])
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(random_order, expected)
random_order = datetime_series.reindex(rindex)
result = random_order.sort_index(ascending=True, inplace=True)
assert result is None
expected = datetime_series.copy()
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(random_order, expected)
```

## Next Steps


---

*Source: test_sort_index.py:57 | Complexity: Advanced | Last updated: 2026-06-02*