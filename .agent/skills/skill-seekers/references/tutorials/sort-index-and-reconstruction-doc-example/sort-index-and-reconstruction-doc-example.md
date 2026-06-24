# How To: Sort Index And Reconstruction Doc Example

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index and reconstruction doc example

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [1, 2, 3, 4]}, index=MultiIndex(levels=[['a', 'b'], ['bb', 'aa']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
```

**Verification:**
```python
assert df.index._is_lexsorted()
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [2, 1, 4, 3]}, index=MultiIndex(levels=[['a', 'b'], ['aa', 'bb']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
```

**Verification:**
```python
assert not df.index.is_monotonic_increasing
```

### Step 3: Assign result = df.sort_index(...)

```python
result = df.sort_index()
```

**Verification:**
```python
assert result.index.is_monotonic_increasing
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result.index.is_monotonic_increasing
```

### Step 5: Assign result = df.sort_index.copy(...)

```python
result = df.sort_index().copy()
```

### Step 6: Assign result.index = result.index._sort_levels_monotonic(...)

```python
result.index = result.index._sort_levels_monotonic()
```

**Verification:**
```python
assert result.index.is_monotonic_increasing
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'value': [1, 2, 3, 4]}, index=MultiIndex(levels=[['a', 'b'], ['bb', 'aa']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
assert df.index._is_lexsorted()
assert not df.index.is_monotonic_increasing
expected = DataFrame({'value': [2, 1, 4, 3]}, index=MultiIndex(levels=[['a', 'b'], ['aa', 'bb']], codes=[[0, 0, 1, 1], [0, 1, 0, 1]]))
result = df.sort_index()
assert result.index.is_monotonic_increasing
tm.assert_frame_equal(result, expected)
result = df.sort_index().copy()
result.index = result.index._sort_levels_monotonic()
assert result.index.is_monotonic_increasing
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:19 | Complexity: Intermediate | Last updated: 2026-06-02*