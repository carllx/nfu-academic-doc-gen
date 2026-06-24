# How To: First Last With Na Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test first last with na object

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign groups = DataFrame.groupby(...)

```python
groups = DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, nulls_fixture]}).groupby('a')
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(groups, method)()
```

### Step 3: Assign values = np.array(...)

```python
values = np.array(values, dtype=result['b'].dtype)
```

### Step 4: Assign idx = Index(...)

```python
idx = Index([1, 2], name='a')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': values}, index=idx)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign values = value

```python
values = [1, 3]
```

### Step 8: Assign values = value

```python
values = [2, 3]
```


## Complete Example

```python
# Setup
# Fixtures: method, nulls_fixture

# Workflow
groups = DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 3, nulls_fixture]}).groupby('a')
result = getattr(groups, method)()
if method == 'first':
    values = [1, 3]
else:
    values = [2, 3]
values = np.array(values, dtype=result['b'].dtype)
idx = Index([1, 2], name='a')
expected = DataFrame({'b': values}, index=idx)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nth.py:67 | Complexity: Advanced | Last updated: 2026-06-02*