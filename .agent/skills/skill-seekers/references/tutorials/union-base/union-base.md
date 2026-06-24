# How To: Union Base

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union base

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: idx, sort, klass
```

## Step-by-Step Guide

### Step 1: Assign first = value

```python
first = idx[::-1]
```

### Step 2: Assign second = value

```python
second = idx[:5]
```

### Step 3: Assign union = first.union(...)

```python
union = first.union(second, sort=sort)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(union, expected)
```

### Step 5: Assign msg = 'other must be a MultiIndex or a list of tuples'

```python
msg = 'other must be a MultiIndex or a list of tuples'
```

### Step 6: Assign second = klass(...)

```python
second = klass(second.values)
```

### Step 7: Assign expected = first.sort_values(...)

```python
expected = first.sort_values()
```

### Step 8: Assign expected = first

```python
expected = first
```

### Step 9: Call first.union()

```python
first.union([1, 2, 3], sort=sort)
```


## Complete Example

```python
# Setup
# Fixtures: idx, sort, klass

# Workflow
first = idx[::-1]
second = idx[:5]
if klass is not MultiIndex:
    second = klass(second.values)
union = first.union(second, sort=sort)
if sort is None:
    expected = first.sort_values()
else:
    expected = first
tm.assert_index_equal(union, expected)
msg = 'other must be a MultiIndex or a list of tuples'
with pytest.raises(TypeError, match=msg):
    first.union([1, 2, 3], sort=sort)
```

## Next Steps


---

*Source: test_setops.py:53 | Complexity: Advanced | Last updated: 2026-06-02*