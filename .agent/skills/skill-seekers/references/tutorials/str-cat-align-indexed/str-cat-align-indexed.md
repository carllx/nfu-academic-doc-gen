# How To: Str Cat Align Indexed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test str cat align indexed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`

**Setup Required:**
```python
# Fixtures: index_or_series, join
```

## Step-by-Step Guide

### Step 1: Assign box = index_or_series

```python
box = index_or_series
```

### Step 2: Assign s = Series(...)

```python
s = Series(['a', 'b', 'c', 'd'], index=['a', 'b', 'c', 'd'])
```

### Step 3: Assign t = Series(...)

```python
t = Series(['D', 'A', 'E', 'B'], index=['d', 'a', 'e', 'b'])
```

### Step 4: Assign unknown = s.align(...)

```python
sa, ta = s.align(t, join=join)
```

### Step 5: Assign expected = sa.str.cat(...)

```python
expected = sa.str.cat(ta, na_rep='-')
```

### Step 6: Assign result = s.str.cat(...)

```python
result = s.str.cat(t, join=join, na_rep='-')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign s = Index(...)

```python
s = Index(s)
```

### Step 9: Assign sa = Index(...)

```python
sa = Index(sa)
```

### Step 10: Assign expected = Index(...)

```python
expected = Index(expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, join

# Workflow
box = index_or_series
s = Series(['a', 'b', 'c', 'd'], index=['a', 'b', 'c', 'd'])
t = Series(['D', 'A', 'E', 'B'], index=['d', 'a', 'e', 'b'])
sa, ta = s.align(t, join=join)
expected = sa.str.cat(ta, na_rep='-')
if box == Index:
    s = Index(s)
    sa = Index(sa)
    expected = Index(expected)
result = s.str.cat(t, join=join, na_rep='-')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_cat.py:274 | Complexity: Advanced | Last updated: 2026-06-02*