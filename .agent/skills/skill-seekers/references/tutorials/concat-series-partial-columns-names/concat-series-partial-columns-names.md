# How To: Concat Series Partial Columns Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series partial columns names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign named_series = Series(...)

```python
named_series = Series([1, 2], name='foo')
```

### Step 2: Assign unnamed_series1 = Series(...)

```python
unnamed_series1 = Series([1, 2])
```

### Step 3: Assign unnamed_series2 = Series(...)

```python
unnamed_series2 = Series([4, 5])
```

### Step 4: Assign result = concat(...)

```python
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'foo': [1, 2], 0: [1, 2], 1: [4, 5]}, columns=['foo', 0, 1])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = concat(...)

```python
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1, keys=['red', 'blue', 'yellow'])
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'red': [1, 2], 'blue': [1, 2], 'yellow': [4, 5]}, columns=['red', 'blue', 'yellow'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = concat(...)

```python
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1, ignore_index=True)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [1, 2], 1: [1, 2], 2: [4, 5]})
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
named_series = Series([1, 2], name='foo')
unnamed_series1 = Series([1, 2])
unnamed_series2 = Series([4, 5])
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1)
expected = DataFrame({'foo': [1, 2], 0: [1, 2], 1: [4, 5]}, columns=['foo', 0, 1])
tm.assert_frame_equal(result, expected)
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1, keys=['red', 'blue', 'yellow'])
expected = DataFrame({'red': [1, 2], 'blue': [1, 2], 'yellow': [4, 5]}, columns=['red', 'blue', 'yellow'])
tm.assert_frame_equal(result, expected)
result = concat([named_series, unnamed_series1, unnamed_series2], axis=1, ignore_index=True)
expected = DataFrame({0: [1, 2], 1: [1, 2], 2: [4, 5]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:142 | Complexity: Advanced | Last updated: 2026-06-02*