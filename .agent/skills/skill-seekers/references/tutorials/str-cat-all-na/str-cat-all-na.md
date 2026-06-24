# How To: Str Cat All Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str cat all na

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
# Fixtures: index_or_series, index_or_series2
```

## Step-by-Step Guide

### Step 1: Assign box = index_or_series

```python
box = index_or_series
```

### Step 2: Assign other = index_or_series2

```python
other = index_or_series2
```

### Step 3: Assign s = Index(...)

```python
s = Index(['a', 'b', 'c', 'd'])
```

### Step 4: Assign s = value

```python
s = s if box == Index else Series(s, index=s)
```

### Step 5: Assign t = other(...)

```python
t = other([np.nan] * 4, dtype=object)
```

### Step 6: Assign t = value

```python
t = t if other == Index else Series(t, index=s)
```

### Step 7: Assign result = s.str.cat(...)

```python
result = s.str.cat(t, join='left')
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([np.nan] * 4, index=s.index, dtype=s.dtype)
```

### Step 10: Assign expected = Index(...)

```python
expected = Index([np.nan] * 4, dtype=object)
```

### Step 11: Assign expected = Series(...)

```python
expected = Series([np.nan] * 4, dtype=object, index=t.index)
```

### Step 12: Assign result = t.str.cat(...)

```python
result = t.str.cat(s, join='left')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, index_or_series2

# Workflow
box = index_or_series
other = index_or_series2
s = Index(['a', 'b', 'c', 'd'])
s = s if box == Index else Series(s, index=s)
t = other([np.nan] * 4, dtype=object)
t = t if other == Index else Series(t, index=s)
if box == Series:
    expected = Series([np.nan] * 4, index=s.index, dtype=s.dtype)
else:
    expected = Index([np.nan] * 4, dtype=object)
result = s.str.cat(t, join='left')
tm.assert_equal(result, expected)
if other == Series:
    expected = Series([np.nan] * 4, dtype=object, index=t.index)
    result = t.str.cat(s, join='left')
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cat.py:343 | Complexity: Advanced | Last updated: 2026-06-02*