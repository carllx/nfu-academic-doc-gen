# How To: Where Cast Str

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where cast str

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: simple_index
```

## Step-by-Step Guide

### Step 1: Assign index = simple_index

```python
index = simple_index
```

### Step 2: Assign mask = np.ones(...)

```python
mask = np.ones(len(index), dtype=bool)
```

### Step 3: Assign unknown = False

```python
mask[-1] = False
```

### Step 4: Assign result = index.where(...)

```python
result = index.where(mask, str(index[0]))
```

### Step 5: Assign expected = index.where(...)

```python
expected = index.where(mask, index[0])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = index.where(...)

```python
result = index.where(mask, [str(index[0])])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign expected = index.astype.where(...)

```python
expected = index.astype(object).where(mask, 'foo')
```

### Step 10: Assign result = index.where(...)

```python
result = index.where(mask, 'foo')
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign result = index.where(...)

```python
result = index.where(mask, ['foo'])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: simple_index

# Workflow
index = simple_index
mask = np.ones(len(index), dtype=bool)
mask[-1] = False
result = index.where(mask, str(index[0]))
expected = index.where(mask, index[0])
tm.assert_index_equal(result, expected)
result = index.where(mask, [str(index[0])])
tm.assert_index_equal(result, expected)
expected = index.astype(object).where(mask, 'foo')
result = index.where(mask, 'foo')
tm.assert_index_equal(result, expected)
result = index.where(mask, ['foo'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimelike.py:145 | Complexity: Advanced | Last updated: 2026-06-02*