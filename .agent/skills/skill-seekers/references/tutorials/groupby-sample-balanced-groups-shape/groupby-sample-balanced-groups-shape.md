# How To: Groupby Sample Balanced Groups Shape

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby sample balanced groups shape

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: n, frac
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [1] * 10 + [2] * 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': values, 'b': values})
```

### Step 3: Assign result = df.groupby.sample(...)

```python
result = df.groupby('a').sample(n=n, frac=frac)
```

### Step 4: Assign values = value

```python
values = [1] * 2 + [2] * 2
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': values, 'b': values}, index=result.index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = unknown.sample(...)

```python
result = df.groupby('a')['b'].sample(n=n, frac=frac)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(values, name='b', index=result.index)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: n, frac

# Workflow
values = [1] * 10 + [2] * 10
df = DataFrame({'a': values, 'b': values})
result = df.groupby('a').sample(n=n, frac=frac)
values = [1] * 2 + [2] * 2
expected = DataFrame({'a': values, 'b': values}, index=result.index)
tm.assert_frame_equal(result, expected)
result = df.groupby('a')['b'].sample(n=n, frac=frac)
expected = Series(values, name='b', index=result.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:12 | Complexity: Advanced | Last updated: 2026-06-02*