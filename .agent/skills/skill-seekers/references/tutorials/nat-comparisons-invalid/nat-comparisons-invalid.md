# How To: Nat Comparisons Invalid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat comparisons invalid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: other_and_type, symbol_and_op
```

## Step-by-Step Guide

### Step 1: Assign unknown = other_and_type

```python
other, other_type = other_and_type
```

**Verification:**
```python
assert not NaT == other
```

### Step 2: Assign unknown = symbol_and_op

```python
symbol, op = symbol_and_op
```

**Verification:**
```python
assert not other == NaT
```

### Step 3: Assign msg = value

```python
msg = f"'{symbol}' not supported between instances of 'NaTType' and '{other_type}'"
```

**Verification:**
```python
assert NaT != other
```

### Step 4: Assign msg = value

```python
msg = f"'{symbol}' not supported between instances of '{other_type}' and 'NaTType'"
```

**Verification:**
```python
assert other != NaT
```

### Step 5: Call op()

```python
op(NaT, other)
```

### Step 6: Call op()

```python
op(other, NaT)
```


## Complete Example

```python
# Setup
# Fixtures: other_and_type, symbol_and_op

# Workflow
other, other_type = other_and_type
symbol, op = symbol_and_op
assert not NaT == other
assert not other == NaT
assert NaT != other
assert other != NaT
msg = f"'{symbol}' not supported between instances of 'NaTType' and '{other_type}'"
with pytest.raises(TypeError, match=msg):
    op(NaT, other)
msg = f"'{symbol}' not supported between instances of '{other_type}' and 'NaTType'"
with pytest.raises(TypeError, match=msg):
    op(other, NaT)
```

## Next Steps


---

*Source: test_nat.py:589 | Complexity: Intermediate | Last updated: 2026-06-02*