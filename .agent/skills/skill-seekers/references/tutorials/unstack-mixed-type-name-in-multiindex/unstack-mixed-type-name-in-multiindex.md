# How To: Unstack Mixed Type Name In Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unstack mixed type name in multiindex

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
# Fixtures: unstack_idx, expected_values, expected_index, expected_columns
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([['a', 'b'], [1, 2], [3, 4]], names=[('A', 'a'), 'B', 'C'])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(1, index=idx)
```

### Step 3: Assign result = ser.unstack(...)

```python
result = ser.unstack(unstack_idx)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_values, columns=expected_columns, index=expected_index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unstack_idx, expected_values, expected_index, expected_columns

# Workflow
idx = MultiIndex.from_product([['a', 'b'], [1, 2], [3, 4]], names=[('A', 'a'), 'B', 'C'])
ser = Series(1, index=idx)
result = ser.unstack(unstack_idx)
expected = DataFrame(expected_values, columns=expected_columns, index=expected_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_unstack.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*