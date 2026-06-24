# How To: Broadcast

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test broadcast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: size, mask, item, box
```

## Step-by-Step Guide

### Step 1: Assign selection = np.resize(...)

```python
selection = np.resize(mask, size)
```

### Step 2: Assign data = np.arange(...)

```python
data = np.arange(size, dtype=float)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([item if use_item else data[i] for i, use_item in enumerate(selection)])
```

### Step 4: Assign s = Series(...)

```python
s = Series(data)
```

### Step 5: Assign unknown = item

```python
s[selection] = item
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 7: Assign s = Series(...)

```python
s = Series(data)
```

### Step 8: Assign result = s.where(...)

```python
result = s.where(~selection, box(item))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign s = Series(...)

```python
s = Series(data)
```

### Step 11: Assign result = s.mask(...)

```python
result = s.mask(selection, box(item))
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: size, mask, item, box

# Workflow
selection = np.resize(mask, size)
data = np.arange(size, dtype=float)
expected = Series([item if use_item else data[i] for i, use_item in enumerate(selection)])
s = Series(data)
s[selection] = item
tm.assert_series_equal(s, expected)
s = Series(data)
result = s.where(~selection, box(item))
tm.assert_series_equal(result, expected)
s = Series(data)
result = s.mask(selection, box(item))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_where.py:302 | Complexity: Advanced | Last updated: 2026-06-02*