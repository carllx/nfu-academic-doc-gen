# How To: Take Fill Value Datetime

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take fill value datetime

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = pd.DatetimeIndex(...)

```python
idx = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'], name='xxx')
```

### Step 2: Assign idx = CategoricalIndex(...)

```python
idx = CategoricalIndex(idx)
```

### Step 3: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, 0, -1]))
```

### Step 4: Assign expected = pd.DatetimeIndex(...)

```python
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx')
```

### Step 5: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(expected)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, 0, -1]), fill_value=True)
```

### Step 8: Assign expected = pd.DatetimeIndex(...)

```python
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', 'NaT'], name='xxx')
```

### Step 9: Assign exp_cats = pd.DatetimeIndex(...)

```python
exp_cats = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'])
```

### Step 10: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(expected, categories=exp_cats)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
```

### Step 13: Assign expected = pd.DatetimeIndex(...)

```python
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx')
```

### Step 14: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(expected)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 16: Assign msg = 'When allow_fill=True and fill_value is not None, all indices must be >= -1'

```python
msg = 'When allow_fill=True and fill_value is not None, all indices must be >= -1'
```

### Step 17: Assign msg = 'index -5 is out of bounds for (axis 0 with )?size 3'

```python
msg = 'index -5 is out of bounds for (axis 0 with )?size 3'
```

### Step 18: Call idx.take()

```python
idx.take(np.array([1, 0, -2]), fill_value=True)
```

### Step 19: Call idx.take()

```python
idx.take(np.array([1, 0, -5]), fill_value=True)
```

### Step 20: Call idx.take()

```python
idx.take(np.array([1, -5]))
```


## Complete Example

```python
# Workflow
idx = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'], name='xxx')
idx = CategoricalIndex(idx)
result = idx.take(np.array([1, 0, -1]))
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx')
expected = CategoricalIndex(expected)
tm.assert_index_equal(result, expected)
result = idx.take(np.array([1, 0, -1]), fill_value=True)
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', 'NaT'], name='xxx')
exp_cats = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'])
expected = CategoricalIndex(expected, categories=exp_cats)
tm.assert_index_equal(result, expected)
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = pd.DatetimeIndex(['2011-02-01', '2011-01-01', '2011-03-01'], name='xxx')
expected = CategoricalIndex(expected)
tm.assert_index_equal(result, expected)
msg = 'When allow_fill=True and fill_value is not None, all indices must be >= -1'
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)
msg = 'index -5 is out of bounds for (axis 0 with )?size 3'
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))
```

## Next Steps


---

*Source: test_indexing.py:79 | Complexity: Advanced | Last updated: 2026-06-02*