# How To: Construction With Categorical Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction with categorical dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
data, cats, ordered = ('a a b b'.split(), 'c b a'.split(), True)
```

### Step 2: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(categories=cats, ordered=ordered)
```

### Step 3: Assign result = CategoricalIndex(...)

```python
result = CategoricalIndex(data, dtype=dtype)
```

### Step 4: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(data, categories=cats, ordered=ordered)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 6: Assign result = Index(...)

```python
result = Index(data, dtype=dtype)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 8: Assign msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'

```python
msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'
```

### Step 9: Call CategoricalIndex()

```python
CategoricalIndex(data, categories=cats, dtype=dtype)
```

### Step 10: Call CategoricalIndex()

```python
CategoricalIndex(data, ordered=ordered, dtype=dtype)
```


## Complete Example

```python
# Workflow
data, cats, ordered = ('a a b b'.split(), 'c b a'.split(), True)
dtype = CategoricalDtype(categories=cats, ordered=ordered)
result = CategoricalIndex(data, dtype=dtype)
expected = CategoricalIndex(data, categories=cats, ordered=ordered)
tm.assert_index_equal(result, expected, exact=True)
result = Index(data, dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)
msg = 'Cannot specify `categories` or `ordered` together with `dtype`.'
with pytest.raises(ValueError, match=msg):
    CategoricalIndex(data, categories=cats, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    CategoricalIndex(data, ordered=ordered, dtype=dtype)
```

## Next Steps


---

*Source: test_constructors.py:122 | Complexity: Advanced | Last updated: 2026-06-02*