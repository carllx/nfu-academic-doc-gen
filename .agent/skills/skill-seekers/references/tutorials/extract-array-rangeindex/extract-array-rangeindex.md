# How To: Extract Array Rangeindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract array rangeindex

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`
- `pandas.core.construction`


## Step-by-Step Guide

### Step 1: Assign ri = Index(...)

```python
ri = Index(range(5))
```

### Step 2: Assign expected = value

```python
expected = ri._values
```

### Step 3: Assign res = extract_array(...)

```python
res = extract_array(ri, extract_numpy=True, extract_range=True)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 5: Assign res = extract_array(...)

```python
res = extract_array(ri, extract_numpy=False, extract_range=True)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 7: Assign res = extract_array(...)

```python
res = extract_array(ri, extract_numpy=True, extract_range=False)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, ri)
```

### Step 9: Assign res = extract_array(...)

```python
res = extract_array(ri, extract_numpy=False, extract_range=False)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, ri)
```


## Complete Example

```python
# Workflow
ri = Index(range(5))
expected = ri._values
res = extract_array(ri, extract_numpy=True, extract_range=True)
tm.assert_numpy_array_equal(res, expected)
res = extract_array(ri, extract_numpy=False, extract_range=True)
tm.assert_numpy_array_equal(res, expected)
res = extract_array(ri, extract_numpy=True, extract_range=False)
tm.assert_index_equal(res, ri)
res = extract_array(ri, extract_numpy=False, extract_range=False)
tm.assert_index_equal(res, ri)
```

## Next Steps


---

*Source: test_extract_array.py:6 | Complexity: Advanced | Last updated: 2026-06-02*