# How To: Simple Normalize With Separator

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple normalize with separator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`

**Setup Required:**
```python
# Fixtures: deep_nested
```

## Step-by-Step Guide

### Step 1: Assign result = json_normalize(...)

```python
result = json_normalize({'A': {'A': 1, 'B': 2}})
```

**Verification:**
```python
assert result.columns.sort_values().equals(expected)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2]], columns=['A.A', 'A.B'])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.reindex_like(expected), expected)
```

### Step 4: Assign result = json_normalize(...)

```python
result = json_normalize({'A': {'A': 1, 'B': 2}}, sep='_')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2]], columns=['A_A', 'A_B'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.reindex_like(expected), expected)
```

### Step 7: Assign result = json_normalize(...)

```python
result = json_normalize({'A': {'A': 1, 'B': 2}}, sep='σ')
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2]], columns=['AσA', 'AσB'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.reindex_like(expected), expected)
```

### Step 10: Assign result = json_normalize(...)

```python
result = json_normalize(deep_nested, ['states', 'cities'], meta=['country', ['states', 'name']], sep='_')
```

### Step 11: Assign expected = Index.sort_values(...)

```python
expected = Index(['name', 'pop', 'country', 'states_name']).sort_values()
```

**Verification:**
```python
assert result.columns.sort_values().equals(expected)
```


## Complete Example

```python
# Setup
# Fixtures: deep_nested

# Workflow
result = json_normalize({'A': {'A': 1, 'B': 2}})
expected = DataFrame([[1, 2]], columns=['A.A', 'A.B'])
tm.assert_frame_equal(result.reindex_like(expected), expected)
result = json_normalize({'A': {'A': 1, 'B': 2}}, sep='_')
expected = DataFrame([[1, 2]], columns=['A_A', 'A_B'])
tm.assert_frame_equal(result.reindex_like(expected), expected)
result = json_normalize({'A': {'A': 1, 'B': 2}}, sep='σ')
expected = DataFrame([[1, 2]], columns=['AσA', 'AσB'])
tm.assert_frame_equal(result.reindex_like(expected), expected)
result = json_normalize(deep_nested, ['states', 'cities'], meta=['country', ['states', 'name']], sep='_')
expected = Index(['name', 'pop', 'country', 'states_name']).sort_values()
assert result.columns.sort_values().equals(expected)
```

## Next Steps


---

*Source: test_normalize.py:210 | Complexity: Advanced | Last updated: 2026-06-02*