# How To: Get Indexer Mismatched Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer mismatched dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

### Step 3: Assign pi2 = dti.to_period(...)

```python
pi2 = dti.to_period('W')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([-1, -1, -1], dtype=np.intp)
```

### Step 5: Assign result = pi.get_indexer(...)

```python
result = pi.get_indexer(dti)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = dti.get_indexer(...)

```python
result = dti.get_indexer(pi)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = pi.get_indexer(...)

```python
result = pi.get_indexer(pi2)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = pi.get_indexer_non_unique(dti)[0]
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = dti.get_indexer_non_unique(pi)[0]
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 15: Assign result = value

```python
result = pi.get_indexer_non_unique(pi2)[0]
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
pi = dti.to_period('D')
pi2 = dti.to_period('W')
expected = np.array([-1, -1, -1], dtype=np.intp)
result = pi.get_indexer(dti)
tm.assert_numpy_array_equal(result, expected)
result = dti.get_indexer(pi)
tm.assert_numpy_array_equal(result, expected)
result = pi.get_indexer(pi2)
tm.assert_numpy_array_equal(result, expected)
result = pi.get_indexer_non_unique(dti)[0]
tm.assert_numpy_array_equal(result, expected)
result = dti.get_indexer_non_unique(pi)[0]
tm.assert_numpy_array_equal(result, expected)
result = pi.get_indexer_non_unique(pi2)[0]
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:394 | Complexity: Advanced | Last updated: 2026-06-02*