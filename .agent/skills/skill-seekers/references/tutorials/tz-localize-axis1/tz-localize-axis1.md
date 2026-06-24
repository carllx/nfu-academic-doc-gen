# How To: Tz Localize Axis1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize axis1

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2011', periods=100, freq='h')
```

**Verification:**
```python
assert result.columns.tz is timezone.utc
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1}, index=rng)
```

### Step 3: Assign df = value

```python
df = df.T
```

### Step 4: Assign result = df.tz_localize(...)

```python
result = df.tz_localize('utc', axis=1)
```

**Verification:**
```python
assert result.columns.tz is timezone.utc
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': 1}, rng.tz_localize('UTC'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.T)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2011', periods=100, freq='h')
df = DataFrame({'a': 1}, index=rng)
df = df.T
result = df.tz_localize('utc', axis=1)
assert result.columns.tz is timezone.utc
expected = DataFrame({'a': 1}, rng.tz_localize('UTC'))
tm.assert_frame_equal(result, expected.T)
```

## Next Steps


---

*Source: test_tz_localize.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*