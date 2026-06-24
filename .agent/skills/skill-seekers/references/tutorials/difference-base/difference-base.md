# How To: Difference Base

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference base

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

### Step 1: Assign second = value

```python
second = idx[4:]
```

**Verification:**
```python
assert result.equals(answer)
```

### Step 2: Assign answer = value

```python
answer = idx[:4]
```

### Step 3: Assign result = idx.difference(...)

```python
result = idx.difference(second, sort=sort)
```

**Verification:**
```python
assert result.equals(answer)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, answer)
```

### Step 5: Assign cases = value

```python
cases = [klass(second.values) for klass in [np.array, Series, list]]
```

### Step 6: Assign msg = 'other must be a MultiIndex or a list of tuples'

```python
msg = 'other must be a MultiIndex or a list of tuples'
```

### Step 7: Assign answer = answer.sort_values(...)

```python
answer = answer.sort_values()
```

### Step 8: Assign result = idx.difference(...)

```python
result = idx.difference(case, sort=sort)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, answer)
```

### Step 10: Call idx.difference()

```python
idx.difference([1, 2, 3], sort=sort)
```


## Complete Example

```python
# Setup
# Fixtures: idx, sort

# Workflow
second = idx[4:]
answer = idx[:4]
result = idx.difference(second, sort=sort)
if sort is None:
    answer = answer.sort_values()
assert result.equals(answer)
tm.assert_index_equal(result, answer)
cases = [klass(second.values) for klass in [np.array, Series, list]]
for case in cases:
    result = idx.difference(case, sort=sort)
    tm.assert_index_equal(result, answer)
msg = 'other must be a MultiIndex or a list of tuples'
with pytest.raises(TypeError, match=msg):
    idx.difference([1, 2, 3], sort=sort)
```

## Next Steps


---

*Source: test_setops.py:72 | Complexity: Advanced | Last updated: 2026-06-02*