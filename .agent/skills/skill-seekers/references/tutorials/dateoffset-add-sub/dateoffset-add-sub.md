# How To: Dateoffset Add Sub

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dateoffset add sub

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset_kwargs, expected_arg
```

## Step-by-Step Guide

### Step 1: Assign offset = DateOffset(...)

```python
offset = DateOffset(**offset_kwargs)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(0)
```

**Verification:**
```python
assert result == ts
```

### Step 3: Assign result = value

```python
result = ts + offset
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp(expected_arg)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = offset + ts
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: offset_kwargs, expected_arg

# Workflow
offset = DateOffset(**offset_kwargs)
ts = Timestamp(0)
result = ts + offset
expected = Timestamp(expected_arg)
assert result == expected
result -= offset
assert result == ts
result = offset + ts
assert result == expected
```

## Next Steps


---

*Source: test_offsets.py:1002 | Complexity: Intermediate | Last updated: 2026-06-02*