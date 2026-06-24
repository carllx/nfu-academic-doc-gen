# How To: Concat Multiindex 

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex 

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col': ['a', 'b', 'c']}, index=['1', '2', '2'])
```

### Step 2: Assign df = concat(...)

```python
df = concat([df], keys=['X'])
```

### Step 3: Assign iterables = value

```python
iterables = [['X'], ['1', '2', '2']]
```

### Step 4: Assign result_index = value

```python
result_index = df.index
```

### Step 5: Assign expected_index = MultiIndex.from_product(...)

```python
expected_index = MultiIndex.from_product(iterables)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result_index, expected_index)
```

### Step 7: Assign result_df = df

```python
result_df = df
```

### Step 8: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'col': ['a', 'b', 'c']}, index=MultiIndex.from_product(iterables))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_df, expected_df)
```


## Complete Example

```python
# Workflow
df = DataFrame({'col': ['a', 'b', 'c']}, index=['1', '2', '2'])
df = concat([df], keys=['X'])
iterables = [['X'], ['1', '2', '2']]
result_index = df.index
expected_index = MultiIndex.from_product(iterables)
tm.assert_index_equal(result_index, expected_index)
result_df = df
expected_df = DataFrame({'col': ['a', 'b', 'c']}, index=MultiIndex.from_product(iterables))
tm.assert_frame_equal(result_df, expected_df)
```

## Next Steps


---

*Source: test_index.py:326 | Complexity: Advanced | Last updated: 2026-06-02*