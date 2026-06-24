# How To: Extractall No Matches

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test extractall no matches

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`

**Setup Required:**
```python
# Fixtures: data, names, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign n = len(...)

```python
n = len(data)
```

### Step 2: Assign s = Series(...)

```python
s = Series(data, name='series_name', index=index, dtype=any_string_dtype)
```

### Step 3: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([], names=names + ('match',))
```

### Step 4: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(z)')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=[0], index=expected_index, dtype=any_string_dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(z)(z)')
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=[0, 1], index=expected_index, dtype=any_string_dtype)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(?P<first>z)')
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['first'], index=expected_index, dtype=any_string_dtype)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(?P<first>z)(?P<second>z)')
```

### Step 14: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['first', 'second'], index=expected_index, dtype=any_string_dtype)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(z)(?P<second>z)')
```

### Step 17: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=[0, 'second'], index=expected_index, dtype=any_string_dtype)
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 19: Assign index = Index(...)

```python
index = Index(range(n), name=names[0])
```

### Step 20: Assign tuples = value

```python
tuples = (tuple([i] * (n - 1)) for i in range(n))
```

### Step 21: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples, names=names)
```


## Complete Example

```python
# Setup
# Fixtures: data, names, any_string_dtype

# Workflow
n = len(data)
if len(names) == 1:
    index = Index(range(n), name=names[0])
else:
    tuples = (tuple([i] * (n - 1)) for i in range(n))
    index = MultiIndex.from_tuples(tuples, names=names)
s = Series(data, name='series_name', index=index, dtype=any_string_dtype)
expected_index = MultiIndex.from_tuples([], names=names + ('match',))
result = s.str.extractall('(z)')
expected = DataFrame(columns=[0], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extractall('(z)(z)')
expected = DataFrame(columns=[0, 1], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extractall('(?P<first>z)')
expected = DataFrame(columns=['first'], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extractall('(?P<first>z)(?P<second>z)')
expected = DataFrame(columns=['first', 'second'], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extractall('(z)(?P<second>z)')
expected = DataFrame(columns=[0, 'second'], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:554 | Complexity: Advanced | Last updated: 2026-06-02*