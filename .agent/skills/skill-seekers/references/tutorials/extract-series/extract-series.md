# How To: Extract Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test extract series

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
# Fixtures: name, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['A1', 'B2', 'C3'], name=name, dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.extract(...)

```python
result = s.str.extract('(_)', expand=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([np.nan, np.nan, np.nan], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = s.str.extract(...)

```python
result = s.str.extract('(_)(_)', expand=True)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan, np.nan], [np.nan, np.nan], [np.nan, np.nan]], dtype=any_string_dtype)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = s.str.extract(...)

```python
result = s.str.extract('([AB])[123]', expand=True)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(['A', 'B', np.nan], dtype=any_string_dtype)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = s.str.extract(...)

```python
result = s.str.extract('([AB])([123])', expand=True)
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], dtype=any_string_dtype)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = s.str.extract(...)

```python
result = s.str.extract('(?P<letter>[AB])', expand=True)
```

### Step 15: Assign expected = DataFrame(...)

```python
expected = DataFrame({'letter': ['A', 'B', np.nan]}, dtype=any_string_dtype)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = s.str.extract(...)

```python
result = s.str.extract('(?P<letter>[AB])(?P<number>[123])', expand=True)
```

### Step 18: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=['letter', 'number'], dtype=any_string_dtype)
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 20: Assign result = s.str.extract(...)

```python
result = s.str.extract('([AB])(?P<number>[123])', expand=True)
```

### Step 21: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=[0, 'number'], dtype=any_string_dtype)
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 23: Assign result = s.str.extract(...)

```python
result = s.str.extract('([AB])(?:[123])', expand=True)
```

### Step 24: Assign expected = DataFrame(...)

```python
expected = DataFrame(['A', 'B', np.nan], dtype=any_string_dtype)
```

### Step 25: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: name, any_string_dtype

# Workflow
s = Series(['A1', 'B2', 'C3'], name=name, dtype=any_string_dtype)
result = s.str.extract('(_)', expand=True)
expected = DataFrame([np.nan, np.nan, np.nan], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('(_)(_)', expand=True)
expected = DataFrame([[np.nan, np.nan], [np.nan, np.nan], [np.nan, np.nan]], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('([AB])[123]', expand=True)
expected = DataFrame(['A', 'B', np.nan], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('([AB])([123])', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('(?P<letter>[AB])', expand=True)
expected = DataFrame({'letter': ['A', 'B', np.nan]}, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('(?P<letter>[AB])(?P<number>[123])', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=['letter', 'number'], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('([AB])(?P<number>[123])', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=[0, 'number'], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extract('([AB])(?:[123])', expand=True)
expected = DataFrame(['A', 'B', np.nan], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:274 | Complexity: Advanced | Last updated: 2026-06-02*