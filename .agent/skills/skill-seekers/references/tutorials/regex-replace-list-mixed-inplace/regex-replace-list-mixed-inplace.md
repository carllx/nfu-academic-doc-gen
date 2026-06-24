# How To: Regex Replace List Mixed Inplace

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace list mixed inplace

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
# Fixtures: mix_ab
```

## Step-by-Step Guide

### Step 1: Assign dfmix = DataFrame(...)

```python
dfmix = DataFrame(mix_ab)
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign to_replace_res = value

```python
to_replace_res = ['\\s*\\.\\s*', 'a']
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign values = value

```python
values = [np.nan, 'crap']
```

**Verification:**
```python
assert return_value is None
```

### Step 4: Assign res = dfmix.copy(...)

```python
res = dfmix.copy()
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Assign return_value = res.replace(...)

```python
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 6: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b', np.nan, np.nan]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 8: Assign to_replace_res = value

```python
to_replace_res = ['\\s*(\\.)\\s*', '(a|b)']
```

### Step 9: Assign values = value

```python
values = ['\\1\\1', '\\1_crap']
```

### Step 10: Assign res = dfmix.copy(...)

```python
res = dfmix.copy()
```

### Step 11: Assign return_value = res.replace(...)

```python
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 12: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['a_crap', 'b_crap', '..', '..']})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 14: Assign to_replace_res = value

```python
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
```

### Step 15: Assign values = value

```python
values = ['\\1\\1', 'crap', '\\1_crap']
```

### Step 16: Assign res = dfmix.copy(...)

```python
res = dfmix.copy()
```

### Step 17: Assign return_value = res.replace(...)

```python
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 18: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 20: Assign to_replace_res = value

```python
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
```

### Step 21: Assign values = value

```python
values = ['\\1\\1', 'crap', '\\1_crap']
```

### Step 22: Assign res = dfmix.copy(...)

```python
res = dfmix.copy()
```

### Step 23: Assign return_value = res.replace(...)

```python
return_value = res.replace(regex=to_replace_res, value=values, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 24: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
```

### Step 25: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```


## Complete Example

```python
# Setup
# Fixtures: mix_ab

# Workflow
dfmix = DataFrame(mix_ab)
to_replace_res = ['\\s*\\.\\s*', 'a']
values = [np.nan, 'crap']
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b', np.nan, np.nan]})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', '(a|b)']
values = ['\\1\\1', '\\1_crap']
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({'a': mix_ab['a'], 'b': ['a_crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
values = ['\\1\\1', 'crap', '\\1_crap']
res = dfmix.copy()
return_value = res.replace(to_replace_res, values, inplace=True, regex=True)
assert return_value is None
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
values = ['\\1\\1', 'crap', '\\1_crap']
res = dfmix.copy()
return_value = res.replace(regex=to_replace_res, value=values, inplace=True)
assert return_value is None
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
```

## Next Steps


---

*Source: test_replace.py:153 | Complexity: Advanced | Last updated: 2026-06-02*