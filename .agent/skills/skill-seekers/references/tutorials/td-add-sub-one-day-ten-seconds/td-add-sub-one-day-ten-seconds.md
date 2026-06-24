# How To: Td Add Sub One Day Ten Seconds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test td add sub one day ten seconds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: one_day_ten_secs
```

## Step-by-Step Guide

### Step 1: Assign base = Timestamp(...)

```python
base = Timestamp('20130102 09:01:12.123456')
```

**Verification:**
```python
assert result == expected_add
```

### Step 2: Assign expected_add = Timestamp(...)

```python
expected_add = Timestamp('20130103 09:01:22.123456')
```

**Verification:**
```python
assert result == expected_sub
```

### Step 3: Assign expected_sub = Timestamp(...)

```python
expected_sub = Timestamp('20130101 09:01:02.123456')
```

### Step 4: Assign result = value

```python
result = base + one_day_ten_secs
```

**Verification:**
```python
assert result == expected_add
```

### Step 5: Assign result = value

```python
result = base - one_day_ten_secs
```

**Verification:**
```python
assert result == expected_sub
```


## Complete Example

```python
# Setup
# Fixtures: one_day_ten_secs

# Workflow
base = Timestamp('20130102 09:01:12.123456')
expected_add = Timestamp('20130103 09:01:22.123456')
expected_sub = Timestamp('20130101 09:01:02.123456')
result = base + one_day_ten_secs
assert result == expected_add
result = base - one_day_ten_secs
assert result == expected_sub
```

## Next Steps


---

*Source: test_arithmetic.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*