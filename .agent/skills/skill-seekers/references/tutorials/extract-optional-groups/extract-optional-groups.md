# How To: Extract Optional Groups

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract optional groups

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
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['A11', 'B22', 'C33'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.extract(...)

```python
result = s.str.extract('([AB])([123])(?:[123])', expand=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign s = Series(...)

```python
s = Series(['A1', 'B2', '3'], dtype=any_string_dtype)
```

### Step 6: Assign result = s.str.extract(...)

```python
result = s.str.extract('(?P<letter>[AB])?(?P<number>[123])', expand=True)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, '3']], columns=['letter', 'number'], dtype=any_string_dtype)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign s = Series(...)

```python
s = Series(['A1', 'B2', 'C'], dtype=any_string_dtype)
```

### Step 10: Assign result = s.str.extract(...)

```python
result = s.str.extract('(?P<letter>[ABC])(?P<number>[123])?', expand=True)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'], dtype=any_string_dtype)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['A11', 'B22', 'C33'], dtype=any_string_dtype)
result = s.str.extract('([AB])([123])(?:[123])', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
s = Series(['A1', 'B2', '3'], dtype=any_string_dtype)
result = s.str.extract('(?P<letter>[AB])?(?P<number>[123])', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], [np.nan, '3']], columns=['letter', 'number'], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
s = Series(['A1', 'B2', 'C'], dtype=any_string_dtype)
result = s.str.extract('(?P<letter>[ABC])(?P<number>[123])?', expand=True)
expected = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'], dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:331 | Complexity: Advanced | Last updated: 2026-06-02*