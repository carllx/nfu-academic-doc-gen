# How To: Concat Mismatched Categoricals With Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat mismatched categoricals with empty

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser1 = Series(...)

```python
ser1 = Series(['a', 'b', 'c'], dtype='category')
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series([], dtype='category')
```

### Step 3: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 5: Assign result = _concat.concat_compat(...)

```python
result = _concat.concat_compat([ser1._values, ser2._values])
```

### Step 6: Assign expected = value

```python
expected = pd.concat([ser1, ser2])._values
```


## Complete Example

```python
# Workflow
ser1 = Series(['a', 'b', 'c'], dtype='category')
ser2 = Series([], dtype='category')
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = _concat.concat_compat([ser1._values, ser2._values])
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = pd.concat([ser1, ser2])._values
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:10 | Complexity: Intermediate | Last updated: 2026-06-02*