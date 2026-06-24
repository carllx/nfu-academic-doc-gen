# How To: Concat Series Name Npscalar Tuple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat series name npscalar tuple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: s1name, s2name
```

## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series({'a': 1, 'b': 2}, name=s1name)
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series({'c': 5, 'd': 6}, name=s2name)
```

### Step 3: Assign result = concat(...)

```python
result = concat([s1, s2])
```

### Step 4: Assign expected = Series(...)

```python
expected = Series({'a': 1, 'b': 2, 'c': 5, 'd': 6})
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: s1name, s2name

# Workflow
s1 = Series({'a': 1, 'b': 2}, name=s1name)
s2 = Series({'c': 5, 'd': 6}, name=s2name)
result = concat([s1, s2])
expected = Series({'a': 1, 'b': 2, 'c': 5, 'd': 6})
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*