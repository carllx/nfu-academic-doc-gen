# How To: Concat Named Keys

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat named keys

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
df = DataFrame({'foo': [1, 2], 'bar': [0.1, 0.2]})
```

### Step 2: Assign index = Index(...)

```python
index = Index(['a', 'b'], name='baz')
```

### Step 3: Assign concatted_named_from_keys = concat(...)

```python
concatted_named_from_keys = concat([df, df], keys=index)
```

### Step 4: Assign expected_named = DataFrame(...)

```python
expected_named = DataFrame({'foo': [1, 2, 1, 2], 'bar': [0.1, 0.2, 0.1, 0.2]}, index=pd.MultiIndex.from_product((['a', 'b'], [0, 1]), names=['baz', None]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_named_from_keys, expected_named)
```

### Step 6: Assign index_no_name = Index(...)

```python
index_no_name = Index(['a', 'b'], name=None)
```

### Step 7: Assign concatted_named_from_names = concat(...)

```python
concatted_named_from_names = concat([df, df], keys=index_no_name, names=['baz'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_named_from_names, expected_named)
```

### Step 9: Assign concatted_unnamed = concat(...)

```python
concatted_unnamed = concat([df, df], keys=index_no_name)
```

### Step 10: Assign expected_unnamed = DataFrame(...)

```python
expected_unnamed = DataFrame({'foo': [1, 2, 1, 2], 'bar': [0.1, 0.2, 0.1, 0.2]}, index=pd.MultiIndex.from_product((['a', 'b'], [0, 1]), names=[None, None]))
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_unnamed, expected_unnamed)
```


## Complete Example

```python
# Workflow
df = DataFrame({'foo': [1, 2], 'bar': [0.1, 0.2]})
index = Index(['a', 'b'], name='baz')
concatted_named_from_keys = concat([df, df], keys=index)
expected_named = DataFrame({'foo': [1, 2, 1, 2], 'bar': [0.1, 0.2, 0.1, 0.2]}, index=pd.MultiIndex.from_product((['a', 'b'], [0, 1]), names=['baz', None]))
tm.assert_frame_equal(concatted_named_from_keys, expected_named)
index_no_name = Index(['a', 'b'], name=None)
concatted_named_from_names = concat([df, df], keys=index_no_name, names=['baz'])
tm.assert_frame_equal(concatted_named_from_names, expected_named)
concatted_unnamed = concat([df, df], keys=index_no_name)
expected_unnamed = DataFrame({'foo': [1, 2, 1, 2], 'bar': [0.1, 0.2, 0.1, 0.2]}, index=pd.MultiIndex.from_product((['a', 'b'], [0, 1]), names=[None, None]))
tm.assert_frame_equal(concatted_unnamed, expected_unnamed)
```

## Next Steps


---

*Source: test_dataframe.py:51 | Complexity: Advanced | Last updated: 2026-06-02*