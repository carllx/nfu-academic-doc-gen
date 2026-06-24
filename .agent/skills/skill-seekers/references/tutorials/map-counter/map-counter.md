# How To: Map Counter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map counter

## Prerequisites

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', 'b', 'c'], index=[1, 2, 3])
```

### Step 2: Assign counter = Counter(...)

```python
counter = Counter()
```

### Step 3: Assign unknown = 5

```python
counter['b'] = 5
```

### Step 4: Assign result = s.map(...)

```python
result = s.map(counter)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0, 5, 1], index=[1, 2, 3])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(['a', 'b', 'c'], index=[1, 2, 3])
counter = Counter()
counter['b'] = 5
counter['c'] += 1
result = s.map(counter)
expected = Series([0, 5, 1], index=[1, 2, 3])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_map.py:298 | Complexity: Intermediate | Last updated: 2026-06-02*