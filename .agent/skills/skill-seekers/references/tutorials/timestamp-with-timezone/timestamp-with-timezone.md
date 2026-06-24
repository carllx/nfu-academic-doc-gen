# How To: Timestamp With Timezone

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp with timezone

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign left = DatetimeIndex(...)

```python
left = DatetimeIndex(['2020-01-01'], dtype=f'M8[{unit}, UTC]')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign right = DatetimeIndex(...)

```python
right = DatetimeIndex(['2020-01-02'], dtype=f'M8[{unit}, UTC]')
```

### Step 3: Assign index = IntervalIndex.from_arrays(...)

```python
index = IntervalIndex.from_arrays(left, right)
```

### Step 4: Assign result = repr(...)

```python
result = repr(index)
```

### Step 5: Assign expected = value

```python
expected = f"IntervalIndex([(2020-01-01 00:00:00+00:00, 2020-01-02 00:00:00+00:00]], dtype='interval[datetime64[{unit}, UTC], right]')"
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
left = DatetimeIndex(['2020-01-01'], dtype=f'M8[{unit}, UTC]')
right = DatetimeIndex(['2020-01-02'], dtype=f'M8[{unit}, UTC]')
index = IntervalIndex.from_arrays(left, right)
result = repr(index)
expected = f"IntervalIndex([(2020-01-01 00:00:00+00:00, 2020-01-02 00:00:00+00:00]], dtype='interval[datetime64[{unit}, UTC], right]')"
assert result == expected
```

## Next Steps


---

*Source: test_formats.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*