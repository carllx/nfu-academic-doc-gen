# How To: Rank Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = concat(...)

```python
df = concat({'a': DataFrame({'col1': [3, 4], 'col2': [1, 2]}), 'b': DataFrame({'col3': [5, 6], 'col4': [7, 8]})}, axis=1)
```

### Step 2: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 3: Assign msg = 'DataFrameGroupBy.rank with axis=1 is deprecated'

```python
msg = 'DataFrameGroupBy.rank with axis=1 is deprecated'
```

### Step 4: Assign expected = concat(...)

```python
expected = concat([df['a'].rank(axis=1), df['b'].rank(axis=1)], axis=1, keys=['a', 'b'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign gb = df.groupby(...)

```python
gb = df.groupby(level=0, axis=1)
```

### Step 7: Assign result = gb.rank(...)

```python
result = gb.rank(axis=1)
```


## Complete Example

```python
# Workflow
df = concat({'a': DataFrame({'col1': [3, 4], 'col2': [1, 2]}), 'b': DataFrame({'col3': [5, 6], 'col4': [7, 8]})}, axis=1)
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby(level=0, axis=1)
msg = 'DataFrameGroupBy.rank with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = gb.rank(axis=1)
expected = concat([df['a'].rank(axis=1), df['b'].rank(axis=1)], axis=1, keys=['a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:612 | Complexity: Intermediate | Last updated: 2026-06-02*