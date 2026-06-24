# How To: Reindex Pad2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex pad2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
```

### Step 2: Assign new_index = value

```python
new_index = ['a', 'g', 'c', 'f']
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, 1, 3, 3], index=new_index)
```

### Step 4: Assign result = s.reindex.ffill(...)

```python
result = s.reindex(new_index).ffill()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected.astype('float64'))
```

### Step 6: Assign msg = "The 'downcast' keyword in ffill is deprecated"

```python
msg = "The 'downcast' keyword in ffill is deprecated"
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([1, 5, 3, 5], index=new_index)
```

### Step 9: Assign result = s.reindex(...)

```python
result = s.reindex(new_index, method='ffill')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = s.reindex.ffill(...)

```python
result = s.reindex(new_index).ffill(downcast='infer')
```


## Complete Example

```python
# Workflow
s = Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
new_index = ['a', 'g', 'c', 'f']
expected = Series([1, 1, 3, 3], index=new_index)
result = s.reindex(new_index).ffill()
tm.assert_series_equal(result, expected.astype('float64'))
msg = "The 'downcast' keyword in ffill is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.reindex(new_index).ffill(downcast='infer')
tm.assert_series_equal(result, expected)
expected = Series([1, 5, 3, 5], index=new_index)
result = s.reindex(new_index, method='ffill')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:131 | Complexity: Advanced | Last updated: 2026-06-02*