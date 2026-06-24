# How To: View I8

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test view i8

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.arrays`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('ab') * 50)
```

### Step 2: Assign msg = 'When changing to a larger dtype, its size must be a divisor'

```python
msg = 'When changing to a larger dtype, its size must be a divisor'
```

### Step 3: Assign ci = value

```python
ci = ci[:-4]
```

### Step 4: Assign res = ci.view(...)

```python
res = ci.view('i8')
```

### Step 5: Assign expected = ci._data.codes.view(...)

```python
expected = ci._data.codes.view('i8')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 7: Assign cat = value

```python
cat = ci._data
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(cat.view('i8'), expected)
```

### Step 9: Call ci.view()

```python
ci.view('i8')
```

### Step 10: Call ci._data.view()

```python
ci._data.view('i8')
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(list('ab') * 50)
msg = 'When changing to a larger dtype, its size must be a divisor'
with pytest.raises(ValueError, match=msg):
    ci.view('i8')
with pytest.raises(ValueError, match=msg):
    ci._data.view('i8')
ci = ci[:-4]
res = ci.view('i8')
expected = ci._data.codes.view('i8')
tm.assert_numpy_array_equal(res, expected)
cat = ci._data
tm.assert_numpy_array_equal(cat.view('i8'), expected)
```

## Next Steps


---

*Source: test_category.py:262 | Complexity: Advanced | Last updated: 2026-06-02*