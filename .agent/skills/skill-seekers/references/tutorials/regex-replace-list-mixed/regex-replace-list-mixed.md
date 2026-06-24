# How To: Regex Replace List Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace list mixed

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

### Step 2: Assign to_replace_res = value

```python
to_replace_res = ['\\s*\\.\\s*', 'a']
```

### Step 3: Assign values = value

```python
values = [np.nan, 'crap']
```

### Step 4: Assign mix2 = value

```python
mix2 = {'a': list(range(4)), 'b': list('ab..'), 'c': list('halo')}
```

### Step 5: Assign dfmix2 = DataFrame(...)

```python
dfmix2 = DataFrame(mix2)
```

### Step 6: Assign res = dfmix2.replace(...)

```python
res = dfmix2.replace(to_replace_res, values, regex=True)
```

### Step 7: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix2['a'], 'b': ['crap', 'b', np.nan, np.nan], 'c': ['h', 'crap', 'l', 'o']})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 9: Assign to_replace_res = value

```python
to_replace_res = ['\\s*(\\.)\\s*', '(a|b)']
```

### Step 10: Assign values = value

```python
values = ['\\1\\1', '\\1_crap']
```

### Step 11: Assign res = dfmix.replace(...)

```python
res = dfmix.replace(to_replace_res, values, regex=True)
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

### Step 16: Assign res = dfmix.replace(...)

```python
res = dfmix.replace(to_replace_res, values, regex=True)
```

### Step 17: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 19: Assign to_replace_res = value

```python
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
```

### Step 20: Assign values = value

```python
values = ['\\1\\1', 'crap', '\\1_crap']
```

### Step 21: Assign res = dfmix.replace(...)

```python
res = dfmix.replace(regex=to_replace_res, value=values)
```

### Step 22: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
```

### Step 23: Call tm.assert_frame_equal()

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
mix2 = {'a': list(range(4)), 'b': list('ab..'), 'c': list('halo')}
dfmix2 = DataFrame(mix2)
res = dfmix2.replace(to_replace_res, values, regex=True)
expec = DataFrame({'a': mix2['a'], 'b': ['crap', 'b', np.nan, np.nan], 'c': ['h', 'crap', 'l', 'o']})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', '(a|b)']
values = ['\\1\\1', '\\1_crap']
res = dfmix.replace(to_replace_res, values, regex=True)
expec = DataFrame({'a': mix_ab['a'], 'b': ['a_crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
values = ['\\1\\1', 'crap', '\\1_crap']
res = dfmix.replace(to_replace_res, values, regex=True)
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
to_replace_res = ['\\s*(\\.)\\s*', 'a', '(b)']
values = ['\\1\\1', 'crap', '\\1_crap']
res = dfmix.replace(regex=to_replace_res, value=values)
expec = DataFrame({'a': mix_ab['a'], 'b': ['crap', 'b_crap', '..', '..']})
tm.assert_frame_equal(res, expec)
```

## Next Steps


---

*Source: test_replace.py:112 | Complexity: Advanced | Last updated: 2026-06-02*