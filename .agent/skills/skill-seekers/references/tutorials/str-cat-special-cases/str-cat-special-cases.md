# How To: Str Cat Special Cases

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str cat special cases

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', 'b', 'c', 'd'])
```

### Step 2: Assign t = Series(...)

```python
t = Series(['d', 'a', 'e', 'b'], index=[3, 0, 4, 1])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['aaa', 'bbb', 'c-c', 'ddd', '-e-'])
```

### Step 4: Assign result = s.str.cat(...)

```python
result = s.str.cat(iter([t, s.values]), join='outer', na_rep='-')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['aa-', 'd-d'], index=[0, 3])
```

### Step 7: Assign result = s.str.cat(...)

```python
result = s.str.cat([t.loc[[0]], t.loc[[3]]], join='right', na_rep='-')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(['a', 'b', 'c', 'd'])
t = Series(['d', 'a', 'e', 'b'], index=[3, 0, 4, 1])
expected = Series(['aaa', 'bbb', 'c-c', 'ddd', '-e-'])
result = s.str.cat(iter([t, s.values]), join='outer', na_rep='-')
tm.assert_series_equal(result, expected)
expected = Series(['aa-', 'd-d'], index=[0, 3])
result = s.str.cat([t.loc[[0]], t.loc[[3]]], join='right', na_rep='-')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cat.py:371 | Complexity: Advanced | Last updated: 2026-06-02*