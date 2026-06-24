# How To: Dataframe Dummies Subset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe dummies subset

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: df, sparse
```

## Step-by-Step Guide

### Step 1: Assign result = get_dummies(...)

```python
result = get_dummies(df, prefix=['from_A'], columns=['A'], sparse=sparse)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': ['b', 'b', 'c'], 'C': [1, 2, 3], 'from_A_a': [1, 0, 1], 'from_A_b': [0, 1, 0]})
```

### Step 3: Assign cols = value

```python
cols = expected.columns
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected[cols[1:]] = expected[cols[1:]].astype(bool)
```

### Step 5: Assign unknown = value

```python
expected[['C']] = df[['C']]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign cols = value

```python
cols = ['from_A_a', 'from_A_b']
```

### Step 8: Assign unknown = unknown.astype(...)

```python
expected[cols] = expected[cols].astype(SparseDtype('bool', False))
```


## Complete Example

```python
# Setup
# Fixtures: df, sparse

# Workflow
result = get_dummies(df, prefix=['from_A'], columns=['A'], sparse=sparse)
expected = DataFrame({'B': ['b', 'b', 'c'], 'C': [1, 2, 3], 'from_A_a': [1, 0, 1], 'from_A_b': [0, 1, 0]})
cols = expected.columns
expected[cols[1:]] = expected[cols[1:]].astype(bool)
expected[['C']] = df[['C']]
if sparse:
    cols = ['from_A_a', 'from_A_b']
    expected[cols] = expected[cols].astype(SparseDtype('bool', False))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_dummies.py:307 | Complexity: Advanced | Last updated: 2026-06-02*