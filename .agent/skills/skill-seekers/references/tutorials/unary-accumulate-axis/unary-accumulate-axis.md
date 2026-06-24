# How To: Unary Accumulate Axis

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unary accumulate axis

## Prerequisites

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [1, 3, 2, 4]})
```

### Step 2: Assign result = np.maximum.accumulate(...)

```python
result = np.maximum.accumulate(df)
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1, 3, 3, 4]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [1, 3, 2, 4], 'b': [0.1, 4.0, 3.0, 2.0]})
```

### Step 6: Assign result = np.maximum.accumulate(...)

```python
result = np.maximum.accumulate(df)
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1.0, 3.0, 3.0, 4.0], 'b': [0.1, 4.0, 4.0, 4.0]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = np.maximum.accumulate(...)

```python
result = np.maximum.accumulate(df, axis=0)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = np.maximum.accumulate(...)

```python
result = np.maximum.accumulate(df, axis=1)
```

### Step 12: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1.0, 3.0, 2.0, 4.0], 'b': [1.0, 4.0, 3.0, 4.0]})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': [1, 3, 2, 4]})
result = np.maximum.accumulate(df)
expected = pd.DataFrame({'a': [1, 3, 3, 4]})
tm.assert_frame_equal(result, expected)
df = pd.DataFrame({'a': [1, 3, 2, 4], 'b': [0.1, 4.0, 3.0, 2.0]})
result = np.maximum.accumulate(df)
expected = pd.DataFrame({'a': [1.0, 3.0, 3.0, 4.0], 'b': [0.1, 4.0, 4.0, 4.0]})
tm.assert_frame_equal(result, expected)
result = np.maximum.accumulate(df, axis=0)
tm.assert_frame_equal(result, expected)
result = np.maximum.accumulate(df, axis=1)
expected = pd.DataFrame({'a': [1.0, 3.0, 2.0, 4.0], 'b': [1.0, 4.0, 3.0, 4.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:171 | Complexity: Advanced | Last updated: 2026-06-02*