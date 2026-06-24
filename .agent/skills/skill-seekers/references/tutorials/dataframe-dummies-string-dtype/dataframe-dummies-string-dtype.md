# How To: Dataframe Dummies String Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe dummies string dtype

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
# Fixtures: df, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = value

```python
df = df[['A', 'B']]
```

### Step 2: Assign df = df.astype(...)

```python
df = df.astype({'A': 'str', 'B': any_string_dtype})
```

### Step 3: Assign result = get_dummies(...)

```python
result = get_dummies(df)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A_a': [1, 0, 1], 'A_b': [0, 1, 0], 'B_b': [1, 1, 0], 'B_c': [0, 0, 1]}, dtype=bool)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign unknown = unknown.astype(...)

```python
expected[['B_b', 'B_c']] = expected[['B_b', 'B_c']].astype('boolean')
```


## Complete Example

```python
# Setup
# Fixtures: df, any_string_dtype

# Workflow
df = df[['A', 'B']]
df = df.astype({'A': 'str', 'B': any_string_dtype})
result = get_dummies(df)
expected = DataFrame({'A_a': [1, 0, 1], 'A_b': [0, 1, 0], 'B_b': [1, 1, 0], 'B_c': [0, 0, 1]}, dtype=bool)
if any_string_dtype == 'string' and any_string_dtype.na_value is pd.NA:
    expected[['B_b', 'B_c']] = expected[['B_b', 'B_c']].astype('boolean')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_dummies.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*