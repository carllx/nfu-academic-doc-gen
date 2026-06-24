# How To: Union Coverage

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union coverage

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['3d', '1d', '2d'])
```

**Verification:**
```python
assert result.freq == ordered.freq
```

### Step 2: Assign ordered = TimedeltaIndex(...)

```python
ordered = TimedeltaIndex(idx.sort_values(), freq='infer')
```

### Step 3: Assign result = ordered.union(...)

```python
result = ordered.union(idx)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ordered)
```

### Step 5: Assign result = unknown.union(...)

```python
result = ordered[:0].union(ordered)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ordered)
```

**Verification:**
```python
assert result.freq == ordered.freq
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['3d', '1d', '2d'])
ordered = TimedeltaIndex(idx.sort_values(), freq='infer')
result = ordered.union(idx)
tm.assert_index_equal(result, ordered)
result = ordered[:0].union(ordered)
tm.assert_index_equal(result, ordered)
assert result.freq == ordered.freq
```

## Next Steps


---

*Source: test_setops.py:44 | Complexity: Intermediate | Last updated: 2026-06-02*