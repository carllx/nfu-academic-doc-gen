# How To: Symmetric Difference

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test symmetric difference

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
# Fixtures: idx, sort
```

## Step-by-Step Guide

### Step 1: Assign first = value

```python
first = idx[1:]
```

### Step 2: Assign second = value

```python
second = idx[:-1]
```

### Step 3: Assign answer = value

```python
answer = idx[[-1, 0]]
```

### Step 4: Assign result = first.symmetric_difference(...)

```python
result = first.symmetric_difference(second, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, answer)
```

### Step 6: Assign cases = value

```python
cases = [klass(second.values) for klass in [np.array, Series, list]]
```

### Step 7: Assign msg = 'other must be a MultiIndex or a list of tuples'

```python
msg = 'other must be a MultiIndex or a list of tuples'
```

### Step 8: Assign answer = answer.sort_values(...)

```python
answer = answer.sort_values()
```

### Step 9: Assign result = first.symmetric_difference(...)

```python
result = first.symmetric_difference(case, sort=sort)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, answer)
```

### Step 11: Call first.symmetric_difference()

```python
first.symmetric_difference([1, 2, 3], sort=sort)
```


## Complete Example

```python
# Setup
# Fixtures: idx, sort

# Workflow
first = idx[1:]
second = idx[:-1]
answer = idx[[-1, 0]]
result = first.symmetric_difference(second, sort=sort)
if sort is None:
    answer = answer.sort_values()
tm.assert_index_equal(result, answer)
cases = [klass(second.values) for klass in [np.array, Series, list]]
for case in cases:
    result = first.symmetric_difference(case, sort=sort)
    tm.assert_index_equal(result, answer)
msg = 'other must be a MultiIndex or a list of tuples'
with pytest.raises(TypeError, match=msg):
    first.symmetric_difference([1, 2, 3], sort=sort)
```

## Next Steps


---

*Source: test_setops.py:94 | Complexity: Advanced | Last updated: 2026-06-02*