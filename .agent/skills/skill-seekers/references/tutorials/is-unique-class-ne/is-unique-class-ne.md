# How To: Is Unique Class Ne

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is unique class ne

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: capsys
```

## Step-by-Step Guide

### Step 1: ser.is_unique

```python
ser.is_unique
```

**Verification:**
```python
assert len(captured.err) == 0
```

### Step 2: Assign captured = capsys.readouterr(...)

```python
captured = capsys.readouterr()
```

**Verification:**
```python
assert len(captured.err) == 0
```

### Step 3: Assign li = value

```python
li = [Foo(i) for i in range(5)]
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(li, index=list(range(5)))
```

### Step 5: Assign self._value = val

```python
self._value = val
```


## Complete Example

```python
# Setup
# Fixtures: capsys

# Workflow
class Foo:

    def __init__(self, val) -> None:
        self._value = val

    def __ne__(self, other):
        raise Exception('NEQ not supported')
with capsys.disabled():
    li = [Foo(i) for i in range(5)]
    ser = Series(li, index=list(range(5)))
ser.is_unique
captured = capsys.readouterr()
assert len(captured.err) == 0
```

## Next Steps


---

*Source: test_is_unique.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*