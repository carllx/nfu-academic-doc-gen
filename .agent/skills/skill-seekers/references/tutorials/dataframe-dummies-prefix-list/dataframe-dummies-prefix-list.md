# How To: Dataframe Dummies Prefix List

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe dummies prefix list

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

### Step 1: Assign prefixes = value

```python
prefixes = ['from_A', 'from_B']
```

### Step 2: Assign result = get_dummies(...)

```python
result = get_dummies(df, prefix=prefixes, sparse=sparse)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'C': [1, 2, 3], 'from_A_a': [True, False, True], 'from_A_b': [False, True, False], 'from_B_b': [True, True, False], 'from_B_c': [False, False, True]})
```

### Step 4: Assign unknown = value

```python
expected[['C']] = df[['C']]
```

### Step 5: Assign cols = value

```python
cols = ['from_A_a', 'from_A_b', 'from_B_b', 'from_B_c']
```

### Step 6: Assign expected = value

```python
expected = expected[['C'] + cols]
```

### Step 7: Assign typ = value

```python
typ = SparseArray if sparse else Series
```

### Step 8: Assign unknown = unknown.apply(...)

```python
expected[cols] = expected[cols].apply(lambda x: typ(x))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: df, sparse

# Workflow
prefixes = ['from_A', 'from_B']
result = get_dummies(df, prefix=prefixes, sparse=sparse)
expected = DataFrame({'C': [1, 2, 3], 'from_A_a': [True, False, True], 'from_A_b': [False, True, False], 'from_B_b': [True, True, False], 'from_B_c': [False, False, True]})
expected[['C']] = df[['C']]
cols = ['from_A_a', 'from_A_b', 'from_B_b', 'from_B_c']
expected = expected[['C'] + cols]
typ = SparseArray if sparse else Series
expected[cols] = expected[cols].apply(lambda x: typ(x))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_dummies.py:258 | Complexity: Advanced | Last updated: 2026-06-02*