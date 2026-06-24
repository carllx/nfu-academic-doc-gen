# How To: Regex Replace Dict Nested Non First Character

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace dict nested non first character

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_string_dtype

```python
dtype = any_string_dtype
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'first': ['abc', 'bca', 'cab']}, dtype=dtype)
```

### Step 3: Assign result = df.replace(...)

```python
result = df.replace({'a': '.'}, regex=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'first': ['.bc', 'bc.', 'c.b']}, dtype=dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
dtype = any_string_dtype
df = DataFrame({'first': ['abc', 'bca', 'cab']}, dtype=dtype)
result = df.replace({'a': '.'}, regex=True)
expected = DataFrame({'first': ['.bc', 'bc.', 'c.b']}, dtype=dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:283 | Complexity: Intermediate | Last updated: 2026-06-02*