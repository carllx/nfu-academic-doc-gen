# How To: Concat Preserves Extension Int64 Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat preserves extension int64 dtype

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`


## Step-by-Step Guide

### Step 1: Assign df_a = DataFrame(...)

```python
df_a = DataFrame({'a': [-1]}, dtype='Int64')
```

### Step 2: Assign df_b = DataFrame(...)

```python
df_b = DataFrame({'b': [1]}, dtype='Int64')
```

### Step 3: Assign result = concat(...)

```python
result = concat([df_a, df_b], ignore_index=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [-1, None], 'b': [None, 1]}, dtype='Int64')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df_a = DataFrame({'a': [-1]}, dtype='Int64')
df_b = DataFrame({'b': [1]}, dtype='Int64')
result = concat([df_a, df_b], ignore_index=True)
expected = DataFrame({'a': [-1, None], 'b': [None, 1]}, dtype='Int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:659 | Complexity: Intermediate | Last updated: 2026-06-02*