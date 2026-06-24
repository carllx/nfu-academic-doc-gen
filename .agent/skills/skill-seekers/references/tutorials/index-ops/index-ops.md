# How To: Index Ops

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index ops

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, func, request
```

## Step-by-Step Guide

### Step 1: Assign unknown = index_view(...)

```python
idx, view_ = index_view()
```

### Step 2: Assign expected = idx.copy(...)

```python
expected = idx.copy(deep=True)
```

### Step 3: Assign idx = func(...)

```python
idx = func(idx)
```

### Step 4: Assign unknown = 100

```python
view_.iloc[0, 0] = 100
```

### Step 5: Assign expected = expected.astype(...)

```python
expected = expected.astype('Int64')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected, check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, func, request

# Workflow
idx, view_ = index_view()
expected = idx.copy(deep=True)
if 'astype' in request.node.callspec.id:
    expected = expected.astype('Int64')
idx = func(idx)
view_.iloc[0, 0] = 100
if using_copy_on_write:
    tm.assert_index_equal(idx, expected, check_names=False)
```

## Next Steps


---

*Source: test_index.py:144 | Complexity: Intermediate | Last updated: 2026-06-02*