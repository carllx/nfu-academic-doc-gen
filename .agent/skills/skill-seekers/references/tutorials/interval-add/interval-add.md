# How To: Interval Add

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval add

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
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: Assign interval = Interval(...)

```python
interval = Interval(0, 1, closed=closed)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = Interval(...)

```python
expected = Interval(1, 2, closed=closed)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = value

```python
result = interval + 1
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = value

```python
result = 1 + interval
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = interval

```python
result = interval
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign msg = 'unsupported operand type\\(s\\) for \\+'

```python
msg = 'unsupported operand type\\(s\\) for \\+'
```

### Step 7: interval + interval

```python
interval + interval
```

### Step 8: interval + 'foo'

```python
interval + 'foo'
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
interval = Interval(0, 1, closed=closed)
expected = Interval(1, 2, closed=closed)
result = interval + 1
assert result == expected
result = 1 + interval
assert result == expected
result = interval
result += 1
assert result == expected
msg = 'unsupported operand type\\(s\\) for \\+'
with pytest.raises(TypeError, match=msg):
    interval + interval
with pytest.raises(TypeError, match=msg):
    interval + 'foo'
```

## Next Steps


---

*Source: test_arithmetic.py:15 | Complexity: Advanced | Last updated: 2026-06-02*