# How To: Fillna Different Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna different dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 'a', np.nan, 'a'], ['b', 'b', np.nan, 'b'], ['c', 'c', np.nan, 'c']])
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign result = df.fillna(...)

```python
result = df.fillna({2: 'foo'})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([['a', 'a', 'foo', 'a'], ['b', 'b', 'foo', 'b'], ['c', 'c', 'foo', 'c']])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected[2] = expected[2].astype('object')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign return_value = df.fillna(...)

```python
return_value = df.fillna({2: 'foo'}, inplace=True)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert return_value is None
```


## Complete Example

```python
# Workflow
df = DataFrame([['a', 'a', np.nan, 'a'], ['b', 'b', np.nan, 'b'], ['c', 'c', np.nan, 'c']])
result = df.fillna({2: 'foo'})
expected = DataFrame([['a', 'a', 'foo', 'a'], ['b', 'b', 'foo', 'b'], ['c', 'c', 'foo', 'c']])
expected[2] = expected[2].astype('object')
tm.assert_frame_equal(result, expected)
return_value = df.fillna({2: 'foo'}, inplace=True)
tm.assert_frame_equal(df, expected)
assert return_value is None
```

## Next Steps


---

*Source: test_fillna.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*