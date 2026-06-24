# How To: Extract Expand Kwarg

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract expand kwarg

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
s = Series(['fooBAD__barBAD', np.nan, 'foo'], dtype=any_string_dtype)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(['BAD__', np.nan, np.nan], dtype=any_string_dtype)
```

### Step 3: Assign result = s.str.extract(...)

```python
result = s.str.extract('.*(BAD[_]+).*')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = s.str.extract(...)

```python
result = s.str.extract('.*(BAD[_]+).*', expand=True)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([['BAD__', 'BAD'], [np.nan, np.nan], [np.nan, np.nan]], dtype=any_string_dtype)
```

### Step 8: Assign result = s.str.extract(...)

```python
result = s.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['fooBAD__barBAD', np.nan, 'foo'], dtype=any_string_dtype)
expected = DataFrame(['BAD__', np.nan, np.nan], dtype=any_string_dtype)
result = s.str.extract('.*(BAD[_]+).*')
tm.assert_frame_equal(result, expected)
result = s.str.extract('.*(BAD[_]+).*', expand=True)
tm.assert_frame_equal(result, expected)
expected = DataFrame([['BAD__', 'BAD'], [np.nan, np.nan], [np.nan, np.nan]], dtype=any_string_dtype)
result = s.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:25 | Complexity: Advanced | Last updated: 2026-06-02*