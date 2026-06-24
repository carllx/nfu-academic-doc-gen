# How To: Series Getitem Not Sorted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series getitem not sorted

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

### Step 2: Assign tuples = zip(...)

```python
tuples = zip(*arrays)
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(8), index=index)
```

### Step 5: Assign arrays = value

```python
arrays = [np.array(x) for x in zip(*index.values)]
```

### Step 6: Assign result = value

```python
result = s['qux']
```

### Step 7: Assign result2 = value

```python
result2 = s.loc['qux']
```

### Step 8: Assign expected = value

```python
expected = s[arrays[0] == 'qux']
```

### Step 9: Assign expected.index = expected.index.droplevel(...)

```python
expected.index = expected.index.droplevel(0)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'bar', 'baz', 'baz', 'qux', 'qux', 'foo', 'foo'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = zip(*arrays)
index = MultiIndex.from_tuples(tuples)
s = Series(np.random.default_rng(2).standard_normal(8), index=index)
arrays = [np.array(x) for x in zip(*index.values)]
result = s['qux']
result2 = s.loc['qux']
expected = s[arrays[0] == 'qux']
expected.index = expected.index.droplevel(0)
tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)
```

## Next Steps


---

*Source: test_sorted.py:137 | Complexity: Advanced | Last updated: 2026-06-02*