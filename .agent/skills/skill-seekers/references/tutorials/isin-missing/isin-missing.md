# How To: Isin Missing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign mi1 = MultiIndex.from_tuples(...)

```python
mi1 = MultiIndex.from_tuples([(1, nulls_fixture)])
```

### Step 2: Assign mi2 = MultiIndex.from_tuples(...)

```python
mi2 = MultiIndex.from_tuples([(1, 1), (1, 2)])
```

### Step 3: Assign result = mi2.isin(...)

```python
result = mi2.isin(mi1)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([False, False])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
mi1 = MultiIndex.from_tuples([(1, nulls_fixture)])
mi2 = MultiIndex.from_tuples([(1, 1), (1, 2)])
result = mi2.isin(mi1)
expected = np.array([False, False])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:16 | Complexity: Intermediate | Last updated: 2026-06-02*