# How To: Mask With Boolean Na Treated As False

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mask with boolean na treated as false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(3))
```

### Step 2: Assign idx = Categorical(...)

```python
idx = Categorical([True, False, None])
```

### Step 3: Assign result = value

```python
result = ser[idx]
```

### Step 4: Assign expected = value

```python
expected = ser[idx.fillna(False)]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign idx = CategoricalIndex(...)

```python
idx = CategoricalIndex(idx)
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
ser = Series(range(3))
idx = Categorical([True, False, None])
if index:
    idx = CategoricalIndex(idx)
result = ser[idx]
expected = ser[idx.fillna(False)]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*