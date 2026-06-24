# How To: Regex Replace List To Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace list to scalar

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
# Fixtures: mix_abc, using_infer_string
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

### Step 2: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_abc['a'], 'b': [np.nan] * 4, 'c': [np.nan, np.nan, np.nan, 'd']})
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign msg = 'Downcasting behavior in `replace`'

```python
msg = 'Downcasting behavior in `replace`'
```

### Step 4: Assign warn = value

```python
warn = None if using_infer_string else FutureWarning
```

### Step 5: Assign res2 = df.copy(...)

```python
res2 = df.copy()
```

### Step 6: Assign res3 = df.copy(...)

```python
res3 = df.copy()
```

**Verification:**
```python
assert return_value is None
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, expec)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res3, expec)
```

### Step 10: Assign unknown = unknown.astype(...)

```python
expec['b'] = expec['b'].astype('str')
```

### Step 11: Assign res = df.replace(...)

```python
res = df.replace(['\\s*\\.\\s*', 'a|b'], np.nan, regex=True)
```

### Step 12: Assign return_value = res2.replace(...)

```python
return_value = res2.replace(['\\s*\\.\\s*', 'a|b'], np.nan, regex=True, inplace=True)
```

### Step 13: Assign return_value = res3.replace(...)

```python
return_value = res3.replace(regex=['\\s*\\.\\s*', 'a|b'], value=np.nan, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: mix_abc, using_infer_string

# Workflow
df = DataFrame(mix_abc)
expec = DataFrame({'a': mix_abc['a'], 'b': [np.nan] * 4, 'c': [np.nan, np.nan, np.nan, 'd']})
if using_infer_string:
    expec['b'] = expec['b'].astype('str')
msg = 'Downcasting behavior in `replace`'
warn = None if using_infer_string else FutureWarning
with tm.assert_produces_warning(warn, match=msg):
    res = df.replace(['\\s*\\.\\s*', 'a|b'], np.nan, regex=True)
res2 = df.copy()
res3 = df.copy()
with tm.assert_produces_warning(warn, match=msg):
    return_value = res2.replace(['\\s*\\.\\s*', 'a|b'], np.nan, regex=True, inplace=True)
assert return_value is None
with tm.assert_produces_warning(warn, match=msg):
    return_value = res3.replace(regex=['\\s*\\.\\s*', 'a|b'], value=np.nan, inplace=True)
assert return_value is None
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
```

## Next Steps


---

*Source: test_replace.py:302 | Complexity: Advanced | Last updated: 2026-06-02*