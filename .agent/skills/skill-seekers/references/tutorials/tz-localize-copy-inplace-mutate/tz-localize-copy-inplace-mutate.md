# How To: Tz Localize Copy Inplace Mutate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz localize copy inplace mutate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: copy, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1h', tz=None))
```

**Verification:**
```python
assert result.index is not obj.index
```

### Step 2: Assign orig = obj.copy(...)

```python
orig = obj.copy()
```

**Verification:**
```python
assert result is not obj
```

### Step 3: Assign result = obj.tz_localize(...)

```python
result = obj.tz_localize('UTC', copy=copy)
```

### Step 4: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1h', tz='UTC'))
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(obj, orig)
```

**Verification:**
```python
assert result.index is not obj.index
```


## Complete Example

```python
# Setup
# Fixtures: copy, frame_or_series

# Workflow
obj = frame_or_series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1h', tz=None))
orig = obj.copy()
result = obj.tz_localize('UTC', copy=copy)
expected = frame_or_series(np.arange(0, 5), index=date_range('20131027', periods=5, freq='1h', tz='UTC'))
tm.assert_equal(result, expected)
tm.assert_equal(obj, orig)
assert result.index is not obj.index
assert result is not obj
```

## Next Steps


---

*Source: test_tz_localize.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*