# How To: Union Misc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union misc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign index = period_range(...)

```python
index = period_range('1/1/2000', '1/20/2000', freq='D')
```

### Step 2: Assign result = unknown.union(...)

```python
result = index[:-5].union(index[10:], sort=sort)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```

### Step 4: Assign result = _permute.union(...)

```python
result = _permute(index[:-5]).union(_permute(index[10:]), sort=sort)
```

### Step 5: Assign index = period_range(...)

```python
index = period_range('1/1/2000', '1/20/2000', freq='D')
```

### Step 6: Assign index2 = period_range(...)

```python
index2 = period_range('1/1/2000', '1/20/2000', freq='W-WED')
```

### Step 7: Assign result = index.union(...)

```python
result = index.union(index2, sort=sort)
```

### Step 8: Assign expected = index.astype.union(...)

```python
expected = index.astype(object).union(index2.astype(object), sort=sort)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.sort_values(), index)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
index = period_range('1/1/2000', '1/20/2000', freq='D')
result = index[:-5].union(index[10:], sort=sort)
tm.assert_index_equal(result, index)
result = _permute(index[:-5]).union(_permute(index[10:]), sort=sort)
if sort is False:
    tm.assert_index_equal(result.sort_values(), index)
else:
    tm.assert_index_equal(result, index)
index = period_range('1/1/2000', '1/20/2000', freq='D')
index2 = period_range('1/1/2000', '1/20/2000', freq='W-WED')
result = index.union(index2, sort=sort)
expected = index.astype(object).union(index2.astype(object), sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:137 | Complexity: Advanced | Last updated: 2026-06-02*