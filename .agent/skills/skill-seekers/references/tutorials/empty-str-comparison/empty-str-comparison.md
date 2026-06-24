# How To: Empty Str Comparison

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test empty str comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: power, string_size
```

## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array(range(10 ** power))
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame(a, dtype=np.int64)
```

### Step 3: Assign left = value

```python
left = ' ' * string_size
```

### Step 4: Assign result = value

```python
result = right == left
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(np.zeros(right.shape, dtype=bool))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: power, string_size

# Workflow
a = np.array(range(10 ** power))
right = pd.DataFrame(a, dtype=np.int64)
left = ' ' * string_size
result = right == left
expected = pd.DataFrame(np.zeros(right.shape, dtype=bool))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:1545 | Complexity: Intermediate | Last updated: 2026-06-02*