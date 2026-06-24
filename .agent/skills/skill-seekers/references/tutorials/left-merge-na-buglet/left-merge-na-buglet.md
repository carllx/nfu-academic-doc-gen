# How To: Left Merge Na Buglet

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test left merge na buglet

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'id': list('abcde'), 'v1': np.random.default_rng(2).standard_normal(5), 'v2': np.random.default_rng(2).standard_normal(5), 'dummy': list('abcde'), 'v3': np.random.default_rng(2).standard_normal(5)}, columns=['id', 'v1', 'v2', 'dummy', 'v3'])
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'id': ['a', 'b', np.nan, np.nan, np.nan], 'sv3': [1.234, 5.678, np.nan, np.nan, np.nan]})
```

### Step 3: Assign result = merge(...)

```python
result = merge(left, right, on='id', how='left')
```

### Step 4: Assign rdf = right.drop(...)

```python
rdf = right.drop(['id'], axis=1)
```

### Step 5: Assign expected = left.join(...)

```python
expected = left.join(rdf)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame({'id': list('abcde'), 'v1': np.random.default_rng(2).standard_normal(5), 'v2': np.random.default_rng(2).standard_normal(5), 'dummy': list('abcde'), 'v3': np.random.default_rng(2).standard_normal(5)}, columns=['id', 'v1', 'v2', 'dummy', 'v3'])
right = DataFrame({'id': ['a', 'b', np.nan, np.nan, np.nan], 'sv3': [1.234, 5.678, np.nan, np.nan, np.nan]})
result = merge(left, right, on='id', how='left')
rdf = right.drop(['id'], axis=1)
expected = left.join(rdf)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:394 | Complexity: Intermediate | Last updated: 2026-06-02*