# How To: Value Counts Inferred

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts inferred

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: index_or_series, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

**Verification:**
```python
assert s.nunique() == 4
```

### Step 2: Assign s_values = value

```python
s_values = ['a', 'b', 'b', 'b', 'b', 'c', 'd', 'd', 'a', 'a']
```

### Step 3: Assign s = klass(...)

```python
s = klass(s_values)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([4, 3, 2, 1], index=['b', 'a', 'd', 'c'], name='count')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.value_counts(), expected)
```

**Verification:**
```python
assert s.nunique() == 4
```

### Step 6: Assign hist = s.value_counts.sort_values(...)

```python
hist = s.value_counts(sort=False).sort_values()
```

### Step 7: Assign expected = Series.sort_values(...)

```python
expected = Series([3, 1, 4, 2], index=list('acbd'), name='count').sort_values()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(hist, expected)
```

### Step 9: Assign hist = s.value_counts(...)

```python
hist = s.value_counts(ascending=True)
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([1, 2, 3, 4], index=list('cdab'), name='count')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(hist, expected)
```

### Step 12: Assign hist = s.value_counts(...)

```python
hist = s.value_counts(normalize=True)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([0.4, 0.3, 0.2, 0.1], index=['b', 'a', 'd', 'c'], name='proportion')
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(hist, expected)
```

### Step 15: Assign exp = Index(...)

```python
exp = Index(np.unique(np.array(s_values, dtype=np.object_)))
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(s.unique(), exp)
```

### Step 17: Assign exp = np.unique(...)

```python
exp = np.unique(np.array(s_values, dtype=np.object_))
```

### Step 18: Call tm.assert_equal()

```python
tm.assert_equal(s.unique(), exp)
```

### Step 19: Assign exp = array(...)

```python
exp = array(exp, dtype='str')
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, using_infer_string

# Workflow
klass = index_or_series
s_values = ['a', 'b', 'b', 'b', 'b', 'c', 'd', 'd', 'a', 'a']
s = klass(s_values)
expected = Series([4, 3, 2, 1], index=['b', 'a', 'd', 'c'], name='count')
tm.assert_series_equal(s.value_counts(), expected)
if isinstance(s, Index):
    exp = Index(np.unique(np.array(s_values, dtype=np.object_)))
    tm.assert_index_equal(s.unique(), exp)
else:
    exp = np.unique(np.array(s_values, dtype=np.object_))
    if using_infer_string:
        exp = array(exp, dtype='str')
    tm.assert_equal(s.unique(), exp)
assert s.nunique() == 4
hist = s.value_counts(sort=False).sort_values()
expected = Series([3, 1, 4, 2], index=list('acbd'), name='count').sort_values()
tm.assert_series_equal(hist, expected)
hist = s.value_counts(ascending=True)
expected = Series([1, 2, 3, 4], index=list('cdab'), name='count')
tm.assert_series_equal(hist, expected)
hist = s.value_counts(normalize=True)
expected = Series([0.4, 0.3, 0.2, 0.1], index=['b', 'a', 'd', 'c'], name='proportion')
tm.assert_series_equal(hist, expected)
```

## Next Steps


---

*Source: test_value_counts.py:117 | Complexity: Advanced | Last updated: 2026-06-02*