# How To: Regex Replace Regex List To Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace regex list to numeric

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
# Fixtures: mix_abc
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(mix_abc)
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign res = df.replace(...)

```python
res = df.replace(['\\s*\\.\\s*', 'b'], 0, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign res2 = df.copy(...)

```python
res2 = df.copy()
```

### Step 4: Assign return_value = res2.replace(...)

```python
return_value = res2.replace(['\\s*\\.\\s*', 'b'], 0, regex=True, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Assign res3 = df.copy(...)

```python
res3 = df.copy()
```

### Step 6: Assign return_value = res3.replace(...)

```python
return_value = res3.replace(regex=['\\s*\\.\\s*', 'b'], value=0, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 7: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_abc['a'], 'b': ['a', 0, 0, 0], 'c': ['a', 0, np.nan, 'd']})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, expec)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res3, expec)
```


## Complete Example

```python
# Setup
# Fixtures: mix_abc

# Workflow
df = DataFrame(mix_abc)
res = df.replace(['\\s*\\.\\s*', 'b'], 0, regex=True)
res2 = df.copy()
return_value = res2.replace(['\\s*\\.\\s*', 'b'], 0, regex=True, inplace=True)
assert return_value is None
res3 = df.copy()
return_value = res3.replace(regex=['\\s*\\.\\s*', 'b'], value=0, inplace=True)
assert return_value is None
expec = DataFrame({'a': mix_abc['a'], 'b': ['a', 0, 0, 0], 'c': ['a', 0, np.nan, 'd']})
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
```

## Next Steps


---

*Source: test_replace.py:348 | Complexity: Advanced | Last updated: 2026-06-02*