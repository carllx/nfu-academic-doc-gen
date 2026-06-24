# How To: Transpose Preserves Dtindex Equality With Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test transpose preserves dtindex equality with dst

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('20161101', '20161130', freq='4h', tz=tz)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': range(len(idx)), 'b': range(len(idx))}, index=idx)
```

### Step 3: Assign result = value

```python
result = df.T == df.T
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(True, index=list('ab'), columns=idx)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
idx = date_range('20161101', '20161130', freq='4h', tz=tz)
df = DataFrame({'a': range(len(idx)), 'b': range(len(idx))}, index=idx)
result = df.T == df.T
expected = DataFrame(True, index=list('ab'), columns=idx)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_transpose.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*