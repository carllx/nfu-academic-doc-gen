# How To: Map Defaultdict Na Key

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test map defaultdict na key

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: na_action
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, np.nan])
```

### Step 2: Assign default_map = defaultdict(...)

```python
default_map = defaultdict(lambda: 'missing', {1: 'a', 2: 'b', np.nan: 'c'})
```

### Step 3: Assign result = s.map(...)

```python
result = s.map(default_map, na_action=na_action)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series({0: 'a', 1: 'b', 2: 'c' if na_action is None else np.nan})
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: na_action

# Workflow
s = Series([1, 2, np.nan])
default_map = defaultdict(lambda: 'missing', {1: 'a', 2: 'b', np.nan: 'c'})
result = s.map(default_map, na_action=na_action)
expected = Series({0: 'a', 1: 'b', 2: 'c' if na_action is None else np.nan})
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_map.py:327 | Complexity: Intermediate | Last updated: 2026-06-02*