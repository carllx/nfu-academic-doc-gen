# How To: Float64 Index Difference

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float64 index difference

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign float_index = Index(...)

```python
float_index = Index([1.0, 2, 3])
```

### Step 2: Assign string_index = Index(...)

```python
string_index = Index(['1', '2', '3'])
```

### Step 3: Assign result = float_index.difference(...)

```python
result = float_index.difference(string_index)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, float_index)
```

### Step 5: Assign result = string_index.difference(...)

```python
result = string_index.difference(float_index)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, string_index)
```


## Complete Example

```python
# Workflow
float_index = Index([1.0, 2, 3])
string_index = Index(['1', '2', '3'])
result = float_index.difference(string_index)
tm.assert_index_equal(result, float_index)
result = string_index.difference(float_index)
tm.assert_index_equal(result, string_index)
```

## Next Steps


---

*Source: test_setops.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*