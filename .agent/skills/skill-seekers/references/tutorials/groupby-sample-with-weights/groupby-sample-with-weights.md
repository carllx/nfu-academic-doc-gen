# How To: Groupby Sample With Weights

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby sample with weights

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, expected_index
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [1] * 2 + [2] * 2
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': values, 'b': values}, index=Index(index))
```

### Step 3: Assign result = df.groupby.sample(...)

```python
result = df.groupby('a').sample(n=2, replace=True, weights=[1, 0, 1, 0])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': values, 'b': values}, index=Index(expected_index))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = unknown.sample(...)

```python
result = df.groupby('a')['b'].sample(n=2, replace=True, weights=[1, 0, 1, 0])
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(values, name='b', index=Index(expected_index))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index, expected_index

# Workflow
values = [1] * 2 + [2] * 2
df = DataFrame({'a': values, 'b': values}, index=Index(index))
result = df.groupby('a').sample(n=2, replace=True, weights=[1, 0, 1, 0])
expected = DataFrame({'a': values, 'b': values}, index=Index(expected_index))
tm.assert_frame_equal(result, expected)
result = df.groupby('a')['b'].sample(n=2, replace=True, weights=[1, 0, 1, 0])
expected = Series(values, name='b', index=Index(expected_index))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:123 | Complexity: Advanced | Last updated: 2026-06-02*