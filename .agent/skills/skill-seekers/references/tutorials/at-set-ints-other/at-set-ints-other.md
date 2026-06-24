# How To: At Set Ints Other

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test at set ints other

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: kind, col, request
```

## Step-by-Step Guide

### Step 1: Assign f = request.getfixturevalue(...)

```python
f = request.getfixturevalue(f'{kind}_{col}')
```

### Step 2: Assign indices = generate_indices(...)

```python
indices = generate_indices(f, False)
```

### Step 3: Assign unknown = 1

```python
f.at[i] = 1
```

### Step 4: Assign expected = value

```python
expected = f.loc[i]
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(expected, 1)
```


## Complete Example

```python
# Setup
# Fixtures: kind, col, request

# Workflow
f = request.getfixturevalue(f'{kind}_{col}')
indices = generate_indices(f, False)
for i in indices:
    f.at[i] = 1
    expected = f.loc[i]
    tm.assert_almost_equal(expected, 1)
```

## Next Steps


---

*Source: test_scalar.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*