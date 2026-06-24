# How To: Regex Replace List Obj

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test regex replace list obj

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
# Fixtures: to_replace, values, expected, inplace, use_value_regex_args
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('ab..'), 'b': list('efgh'), 'c': list('helo')})
```

**Verification:**
```python
assert result is None
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign result = df.replace(...)

```python
result = df.replace(value=values, regex=to_replace, inplace=inplace)
```

### Step 5: Assign result = df.replace(...)

```python
result = df.replace(to_replace, values, regex=True, inplace=inplace)
```

**Verification:**
```python
assert result is None
```

### Step 6: Assign result = df

```python
result = df
```


## Complete Example

```python
# Setup
# Fixtures: to_replace, values, expected, inplace, use_value_regex_args

# Workflow
df = DataFrame({'a': list('ab..'), 'b': list('efgh'), 'c': list('helo')})
if use_value_regex_args:
    result = df.replace(value=values, regex=to_replace, inplace=inplace)
else:
    result = df.replace(to_replace, values, regex=True, inplace=inplace)
if inplace:
    assert result is None
    result = df
expected = DataFrame(expected)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*