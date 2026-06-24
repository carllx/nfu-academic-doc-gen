# How To: Period Add Timestamp Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period add timestamp raises

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2017')
```

### Step 2: Assign per = Period(...)

```python
per = Period('2017', freq='M')
```

### Step 3: Assign msg = "unsupported operand type\\(s\\) for \\+: 'Timestamp' and 'Period'"

```python
msg = "unsupported operand type\\(s\\) for \\+: 'Timestamp' and 'Period'"
```

### Step 4: Assign msg = "unsupported operand type\\(s\\) for \\+: 'Period' and 'Timestamp'"

```python
msg = "unsupported operand type\\(s\\) for \\+: 'Period' and 'Timestamp'"
```

### Step 5: ts + per

```python
ts + per
```

### Step 6: per + ts

```python
per + ts
```


## Complete Example

```python
# Workflow
ts = Timestamp('2017')
per = Period('2017', freq='M')
msg = "unsupported operand type\\(s\\) for \\+: 'Timestamp' and 'Period'"
with pytest.raises(TypeError, match=msg):
    ts + per
msg = "unsupported operand type\\(s\\) for \\+: 'Period' and 'Timestamp'"
with pytest.raises(TypeError, match=msg):
    per + ts
```

## Next Steps


---

*Source: test_arithmetic.py:389 | Complexity: Intermediate | Last updated: 2026-06-02*