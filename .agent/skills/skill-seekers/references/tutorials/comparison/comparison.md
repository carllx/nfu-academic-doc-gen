# How To: Comparison

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparison

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign stamp = 1337299200000000000

```python
stamp = 1337299200000000000
```

**Verification:**
```python
assert val == val
```

### Step 2: Assign val = Timestamp(...)

```python
val = Timestamp(stamp)
```

**Verification:**
```python
assert not val != val
```

### Step 3: Assign other = datetime(...)

```python
other = datetime(2012, 5, 18)
```

**Verification:**
```python
assert not val < val
```

### Step 4: Assign other = Timestamp(...)

```python
other = Timestamp(stamp + 100)
```

**Verification:**
```python
assert val <= val
```


## Complete Example

```python
# Workflow
stamp = 1337299200000000000
val = Timestamp(stamp)
assert val == val
assert not val != val
assert not val < val
assert val <= val
assert not val > val
assert val >= val
other = datetime(2012, 5, 18)
assert val == other
assert not val != other
assert not val < other
assert val <= other
assert not val > other
assert val >= other
other = Timestamp(stamp + 100)
assert val != other
assert val != other
assert val < other
assert val <= other
assert other > val
assert other >= val
```

## Next Steps


---

*Source: test_comparisons.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*