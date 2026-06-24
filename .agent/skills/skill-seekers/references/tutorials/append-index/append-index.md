# How To: Append Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append index

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index([1.1, 1.2, 1.3])
```

### Step 2: Assign idx2 = pd.date_range(...)

```python
idx2 = pd.date_range('2011-01-01', freq='D', periods=3, tz='Asia/Tokyo')
```

### Step 3: Assign idx3 = Index(...)

```python
idx3 = Index(['A', 'B', 'C'])
```

### Step 4: Assign midx_lv2 = MultiIndex.from_arrays(...)

```python
midx_lv2 = MultiIndex.from_arrays([idx1, idx2])
```

### Step 5: Assign midx_lv3 = MultiIndex.from_arrays(...)

```python
midx_lv3 = MultiIndex.from_arrays([idx1, idx2, idx3])
```

### Step 6: Assign result = idx1.append(...)

```python
result = idx1.append(midx_lv2)
```

### Step 7: Assign tz = pytz.timezone(...)

```python
tz = pytz.timezone('Asia/Tokyo')
```

### Step 8: Assign expected_tuples = value

```python
expected_tuples = [(1.1, tz.localize(datetime(2011, 1, 1))), (1.2, tz.localize(datetime(2011, 1, 2))), (1.3, tz.localize(datetime(2011, 1, 3)))]
```

### Step 9: Assign expected = Index(...)

```python
expected = Index([1.1, 1.2, 1.3] + expected_tuples)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 11: Assign result = midx_lv2.append(...)

```python
result = midx_lv2.append(idx1)
```

### Step 12: Assign expected = Index(...)

```python
expected = Index(expected_tuples + [1.1, 1.2, 1.3])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 14: Assign result = midx_lv2.append(...)

```python
result = midx_lv2.append(midx_lv2)
```

### Step 15: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([idx1.append(idx1), idx2.append(idx2)])
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 17: Assign result = midx_lv2.append(...)

```python
result = midx_lv2.append(midx_lv3)
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 19: Assign result = midx_lv3.append(...)

```python
result = midx_lv3.append(midx_lv2)
```

### Step 20: Assign expected = Index._simple_new(...)

```python
expected = Index._simple_new(np.array([(1.1, tz.localize(datetime(2011, 1, 1)), 'A'), (1.2, tz.localize(datetime(2011, 1, 2)), 'B'), (1.3, tz.localize(datetime(2011, 1, 3)), 'C')] + expected_tuples, dtype=object), None)
```

### Step 21: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx1 = Index([1.1, 1.2, 1.3])
idx2 = pd.date_range('2011-01-01', freq='D', periods=3, tz='Asia/Tokyo')
idx3 = Index(['A', 'B', 'C'])
midx_lv2 = MultiIndex.from_arrays([idx1, idx2])
midx_lv3 = MultiIndex.from_arrays([idx1, idx2, idx3])
result = idx1.append(midx_lv2)
tz = pytz.timezone('Asia/Tokyo')
expected_tuples = [(1.1, tz.localize(datetime(2011, 1, 1))), (1.2, tz.localize(datetime(2011, 1, 2))), (1.3, tz.localize(datetime(2011, 1, 3)))]
expected = Index([1.1, 1.2, 1.3] + expected_tuples)
tm.assert_index_equal(result, expected)
result = midx_lv2.append(idx1)
expected = Index(expected_tuples + [1.1, 1.2, 1.3])
tm.assert_index_equal(result, expected)
result = midx_lv2.append(midx_lv2)
expected = MultiIndex.from_arrays([idx1.append(idx1), idx2.append(idx2)])
tm.assert_index_equal(result, expected)
result = midx_lv2.append(midx_lv3)
tm.assert_index_equal(result, expected)
result = midx_lv3.append(midx_lv2)
expected = Index._simple_new(np.array([(1.1, tz.localize(datetime(2011, 1, 1)), 'A'), (1.2, tz.localize(datetime(2011, 1, 2)), 'B'), (1.3, tz.localize(datetime(2011, 1, 3)), 'C')] + expected_tuples, dtype=object), None)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_reshape.py:106 | Complexity: Advanced | Last updated: 2026-06-02*