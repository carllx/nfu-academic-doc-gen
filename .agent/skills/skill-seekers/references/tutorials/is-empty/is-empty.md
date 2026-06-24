# How To: Is Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: left, right, closed
```

## Step-by-Step Guide

### Step 1: Assign iv = Interval(...)

```python
iv = Interval(left, right, closed)
```

**Verification:**
```python
assert iv.is_empty is False
```

### Step 2: Assign iv = Interval(...)

```python
iv = Interval(left, left, closed)
```

**Verification:**
```python
assert result is expected
```

### Step 3: Assign result = value

```python
result = iv.is_empty
```

### Step 4: Assign expected = value

```python
expected = closed != 'both'
```

**Verification:**
```python
assert result is expected
```


## Complete Example

```python
# Setup
# Fixtures: left, right, closed

# Workflow
iv = Interval(left, right, closed)
assert iv.is_empty is False
iv = Interval(left, left, closed)
result = iv.is_empty
expected = closed != 'both'
assert result is expected
```

## Next Steps


---

*Source: test_interval.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*