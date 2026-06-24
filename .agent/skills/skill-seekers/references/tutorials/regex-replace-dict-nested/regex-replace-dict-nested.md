# How To: Regex Replace Dict Nested

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test regex replace dict nested

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

### Step 1: Assign dfmix = DataFrame(...)

```python
dfmix = DataFrame(mix_abc)
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign res = dfmix.replace(...)

```python
res = dfmix.replace({'b': {'\\s*\\.\\s*': np.nan}}, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign res2 = dfmix.copy(...)

```python
res2 = dfmix.copy()
```

### Step 4: Assign res4 = dfmix.copy(...)

```python
res4 = dfmix.copy()
```

### Step 5: Assign return_value = res2.replace(...)

```python
return_value = res2.replace({'b': {'\\s*\\.\\s*': np.nan}}, inplace=True, regex=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 6: Assign res3 = dfmix.replace(...)

```python
res3 = dfmix.replace(regex={'b': {'\\s*\\.\\s*': np.nan}})
```

### Step 7: Assign return_value = res4.replace(...)

```python
return_value = res4.replace(regex={'b': {'\\s*\\.\\s*': np.nan}}, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 8: Assign expec = DataFrame(...)

```python
expec = DataFrame({'a': mix_abc['a'], 'b': ['a', 'b', np.nan, np.nan], 'c': mix_abc['c']})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expec)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, expec)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res3, expec)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res4, expec)
```


## Complete Example

```python
# Setup
# Fixtures: mix_abc

# Workflow
dfmix = DataFrame(mix_abc)
res = dfmix.replace({'b': {'\\s*\\.\\s*': np.nan}}, regex=True)
res2 = dfmix.copy()
res4 = dfmix.copy()
return_value = res2.replace({'b': {'\\s*\\.\\s*': np.nan}}, inplace=True, regex=True)
assert return_value is None
res3 = dfmix.replace(regex={'b': {'\\s*\\.\\s*': np.nan}})
return_value = res4.replace(regex={'b': {'\\s*\\.\\s*': np.nan}}, inplace=True)
assert return_value is None
expec = DataFrame({'a': mix_abc['a'], 'b': ['a', 'b', np.nan, np.nan], 'c': mix_abc['c']})
tm.assert_frame_equal(res, expec)
tm.assert_frame_equal(res2, expec)
tm.assert_frame_equal(res3, expec)
tm.assert_frame_equal(res4, expec)
```

## Next Steps


---

*Source: test_replace.py:262 | Complexity: Advanced | Last updated: 2026-06-02*