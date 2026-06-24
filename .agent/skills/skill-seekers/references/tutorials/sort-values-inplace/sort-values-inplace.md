# How To: Sort Values Inplace

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values inplace

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=[1, 2, 3, 4], columns=['A', 'B', 'C', 'D'])
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign sorted_df = frame.copy(...)

```python
sorted_df = frame.copy()
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign return_value = sorted_df.sort_values(...)

```python
return_value = sorted_df.sort_values(by='A', inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 4: Assign expected = frame.sort_values(...)

```python
expected = frame.sort_values(by='A')
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 6: Assign sorted_df = frame.copy(...)

```python
sorted_df = frame.copy()
```

### Step 7: Assign return_value = sorted_df.sort_values(...)

```python
return_value = sorted_df.sort_values(by=1, axis=1, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 8: Assign expected = frame.sort_values(...)

```python
expected = frame.sort_values(by=1, axis=1)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 10: Assign sorted_df = frame.copy(...)

```python
sorted_df = frame.copy()
```

### Step 11: Assign return_value = sorted_df.sort_values(...)

```python
return_value = sorted_df.sort_values(by='A', ascending=False, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 12: Assign expected = frame.sort_values(...)

```python
expected = frame.sort_values(by='A', ascending=False)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 14: Assign sorted_df = frame.copy(...)

```python
sorted_df = frame.copy()
```

### Step 15: Assign return_value = sorted_df.sort_values(...)

```python
return_value = sorted_df.sort_values(by=['A', 'B'], ascending=False, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 16: Assign expected = frame.sort_values(...)

```python
expected = frame.sort_values(by=['A', 'B'], ascending=False)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```


## Complete Example

```python
# Workflow
frame = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=[1, 2, 3, 4], columns=['A', 'B', 'C', 'D'])
sorted_df = frame.copy()
return_value = sorted_df.sort_values(by='A', inplace=True)
assert return_value is None
expected = frame.sort_values(by='A')
tm.assert_frame_equal(sorted_df, expected)
sorted_df = frame.copy()
return_value = sorted_df.sort_values(by=1, axis=1, inplace=True)
assert return_value is None
expected = frame.sort_values(by=1, axis=1)
tm.assert_frame_equal(sorted_df, expected)
sorted_df = frame.copy()
return_value = sorted_df.sort_values(by='A', ascending=False, inplace=True)
assert return_value is None
expected = frame.sort_values(by='A', ascending=False)
tm.assert_frame_equal(sorted_df, expected)
sorted_df = frame.copy()
return_value = sorted_df.sort_values(by=['A', 'B'], ascending=False, inplace=True)
assert return_value is None
expected = frame.sort_values(by=['A', 'B'], ascending=False)
tm.assert_frame_equal(sorted_df, expected)
```

## Next Steps


---

*Source: test_sort_values.py:96 | Complexity: Advanced | Last updated: 2026-06-02*