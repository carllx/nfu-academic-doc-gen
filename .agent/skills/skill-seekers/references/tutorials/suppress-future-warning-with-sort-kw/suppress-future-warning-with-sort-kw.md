# How To: Suppress Future Warning With Sort Kw

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test suppress future warning with sort kw

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: sort_kw
```

## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame({'col1': [1, 2]}, index=['c', 'a'])
```

### Step 2: Assign b = DataFrame(...)

```python
b = DataFrame({'col2': [4, 5]}, index=['b', 'a'])
```

### Step 3: Assign c = DataFrame(...)

```python
c = DataFrame({'col3': [7, 8]}, index=['a', 'b'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': {'a': 2.0, 'b': float('nan'), 'c': 1.0}, 'col2': {'a': 5.0, 'b': 4.0, 'c': float('nan')}, 'col3': {'a': 7.0, 'b': 8.0, 'c': float('nan')}})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = expected.reindex(...)

```python
expected = expected.reindex(index=['c', 'a', 'b'])
```

### Step 7: Assign result = a.join(...)

```python
result = a.join([b, c], how='outer', sort=sort_kw)
```


## Complete Example

```python
# Setup
# Fixtures: sort_kw

# Workflow
a = DataFrame({'col1': [1, 2]}, index=['c', 'a'])
b = DataFrame({'col2': [4, 5]}, index=['b', 'a'])
c = DataFrame({'col3': [7, 8]}, index=['a', 'b'])
expected = DataFrame({'col1': {'a': 2.0, 'b': float('nan'), 'c': 1.0}, 'col2': {'a': 5.0, 'b': 4.0, 'c': float('nan')}, 'col3': {'a': 7.0, 'b': 8.0, 'c': float('nan')}})
if sort_kw is False:
    expected = expected.reindex(index=['c', 'a', 'b'])
with tm.assert_produces_warning(None):
    result = a.join([b, c], how='outer', sort=sort_kw)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:395 | Complexity: Intermediate | Last updated: 2026-06-02*