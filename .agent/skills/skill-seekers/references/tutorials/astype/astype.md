# How To: Astype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
```

**Verification:**
```python
assert result.equals(ci)
```

### Step 2: Assign result = ci.astype(...)

```python
result = ci.astype(object)
```

**Verification:**
```python
assert isinstance(result, Index)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, Index(np.array(ci), dtype=object))
```

**Verification:**
```python
assert not isinstance(result, CategoricalIndex)
```

### Step 4: Assign ii = IntervalIndex.from_arrays(...)

```python
ii = IntervalIndex.from_arrays(left=[-0.001, 2.0], right=[2, 4], closed='right')
```

### Step 5: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(Categorical.from_codes([0, 1, -1], categories=ii, ordered=True))
```

### Step 6: Assign result = ci.astype(...)

```python
result = ci.astype('interval')
```

### Step 7: Assign expected = ii.take(...)

```python
expected = ii.take([0, 1, -1], allow_fill=True, fill_value=np.nan)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = IntervalIndex(...)

```python
result = IntervalIndex(result.values)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
result = ci.astype(object)
tm.assert_index_equal(result, Index(np.array(ci), dtype=object))
assert result.equals(ci)
assert isinstance(result, Index)
assert not isinstance(result, CategoricalIndex)
ii = IntervalIndex.from_arrays(left=[-0.001, 2.0], right=[2, 4], closed='right')
ci = CategoricalIndex(Categorical.from_codes([0, 1, -1], categories=ii, ordered=True))
result = ci.astype('interval')
expected = ii.take([0, 1, -1], allow_fill=True, fill_value=np.nan)
tm.assert_index_equal(result, expected)
result = IntervalIndex(result.values)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:17 | Complexity: Advanced | Last updated: 2026-06-02*