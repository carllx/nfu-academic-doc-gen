# How To: Delitem

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delitem

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(5))
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(range(1, 5), index=range(1, 5))
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(range(2, 5), index=range(2, 5))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 6: Assign s = Series(...)

```python
s = Series(1)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, Series(dtype='int64', index=Index([], dtype='int64')))
```

### Step 8: Assign unknown = 1

```python
s[0] = 1
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, Series(1))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, Series(dtype='int64', index=Index([], dtype='int64')))
```


## Complete Example

```python
# Workflow
s = Series(range(5))
del s[0]
expected = Series(range(1, 5), index=range(1, 5))
tm.assert_series_equal(s, expected)
del s[1]
expected = Series(range(2, 5), index=range(2, 5))
tm.assert_series_equal(s, expected)
s = Series(1)
del s[0]
tm.assert_series_equal(s, Series(dtype='int64', index=Index([], dtype='int64')))
s[0] = 1
tm.assert_series_equal(s, Series(1))
del s[0]
tm.assert_series_equal(s, Series(dtype='int64', index=Index([], dtype='int64')))
```

## Next Steps


---

*Source: test_delitem.py:12 | Complexity: Advanced | Last updated: 2026-06-02*