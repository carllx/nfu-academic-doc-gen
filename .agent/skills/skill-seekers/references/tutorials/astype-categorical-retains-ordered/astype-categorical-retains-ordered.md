# How To: Astype Categorical Retains Ordered

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype categorical retains ordered

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ordered
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_breaks(...)

```python
index = IntervalIndex.from_breaks(range(5))
```

**Verification:**
```python
assert result.ordered is ordered
```

### Step 2: Assign arr = value

```python
arr = index._data
```

### Step 3: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(None, ordered=ordered)
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(list(arr), ordered=ordered)
```

### Step 5: Assign result = arr.astype(...)

```python
result = arr.astype(dtype)
```

**Verification:**
```python
assert result.ordered is ordered
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 7: Assign result = index.astype(...)

```python
result = index.astype(dtype)
```

### Step 8: Assign expected = Index(...)

```python
expected = Index(expected)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ordered

# Workflow
index = IntervalIndex.from_breaks(range(5))
arr = index._data
dtype = CategoricalDtype(None, ordered=ordered)
expected = Categorical(list(arr), ordered=ordered)
result = arr.astype(dtype)
assert result.ordered is ordered
tm.assert_categorical_equal(result, expected)
result = index.astype(dtype)
expected = Index(expected)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:14 | Complexity: Advanced | Last updated: 2026-06-02*