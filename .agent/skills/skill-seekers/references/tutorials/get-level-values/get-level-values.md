# How To: Get Level Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get level values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign result = idx.get_level_values(...)

```python
result = idx.get_level_values(0)
```

**Verification:**
```python
assert result.name == 'first'
```

### Step 2: Assign expected = Index(...)

```python
expected = Index(['foo', 'foo', 'bar', 'baz', 'qux', 'qux'], name='first')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == 'first'
```

### Step 4: Assign result = idx.get_level_values(...)

```python
result = idx.get_level_values('first')
```

### Step 5: Assign expected = idx.get_level_values(...)

```python
expected = idx.get_level_values(0)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[CategoricalIndex(['A', 'B']), CategoricalIndex([1, 2, 3])], codes=[np.array([0, 0, 0, 1, 1, 1]), np.array([0, 1, 2, 0, 1, 2])])
```

### Step 8: Assign exp = CategoricalIndex(...)

```python
exp = CategoricalIndex(['A', 'A', 'A', 'B', 'B', 'B'])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.get_level_values(0), exp)
```

### Step 10: Assign exp = CategoricalIndex(...)

```python
exp = CategoricalIndex([1, 2, 3, 1, 2, 3])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index.get_level_values(1), exp)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
result = idx.get_level_values(0)
expected = Index(['foo', 'foo', 'bar', 'baz', 'qux', 'qux'], name='first')
tm.assert_index_equal(result, expected)
assert result.name == 'first'
result = idx.get_level_values('first')
expected = idx.get_level_values(0)
tm.assert_index_equal(result, expected)
index = MultiIndex(levels=[CategoricalIndex(['A', 'B']), CategoricalIndex([1, 2, 3])], codes=[np.array([0, 0, 0, 1, 1, 1]), np.array([0, 1, 2, 0, 1, 2])])
exp = CategoricalIndex(['A', 'A', 'A', 'B', 'B', 'B'])
tm.assert_index_equal(index.get_level_values(0), exp)
exp = CategoricalIndex([1, 2, 3, 1, 2, 3])
tm.assert_index_equal(index.get_level_values(1), exp)
```

## Next Steps


---

*Source: test_get_level_values.py:25 | Complexity: Advanced | Last updated: 2026-06-02*