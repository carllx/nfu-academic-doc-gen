# How To: Sub Day

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub day

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign delta_1d = Timedelta(...)

```python
delta_1d = Timedelta(1, unit='D')
```

**Verification:**
```python
assert drepr(delta_1d) == '1 days'
```

### Step 2: Assign delta_0d = Timedelta(...)

```python
delta_0d = Timedelta(0, unit='D')
```

**Verification:**
```python
assert drepr(-delta_1d) == '-1 days'
```

### Step 3: Assign delta_1s = Timedelta(...)

```python
delta_1s = Timedelta(1, unit='s')
```

**Verification:**
```python
assert drepr(delta_0d) == '00:00:00'
```

### Step 4: Assign delta_500ms = Timedelta(...)

```python
delta_500ms = Timedelta(500, unit='ms')
```

**Verification:**
```python
assert drepr(delta_1s) == '00:00:01'
```

### Step 5: Assign drepr = value

```python
drepr = lambda x: x._repr_base(format='sub_day')
```

**Verification:**
```python
assert drepr(delta_500ms) == '00:00:00.500000'
```


## Complete Example

```python
# Workflow
delta_1d = Timedelta(1, unit='D')
delta_0d = Timedelta(0, unit='D')
delta_1s = Timedelta(1, unit='s')
delta_500ms = Timedelta(500, unit='ms')
drepr = lambda x: x._repr_base(format='sub_day')
assert drepr(delta_1d) == '1 days'
assert drepr(-delta_1d) == '-1 days'
assert drepr(delta_0d) == '00:00:00'
assert drepr(delta_1s) == '00:00:01'
assert drepr(delta_500ms) == '00:00:00.500000'
assert drepr(delta_1d + delta_1s) == '1 days 00:00:01'
assert drepr(-delta_1d + delta_1s) == '-1 days +00:00:01'
assert drepr(delta_1d + delta_500ms) == '1 days 00:00:00.500000'
assert drepr(-delta_1d + delta_500ms) == '-1 days +00:00:00.500000'
```

## Next Steps


---

*Source: test_formats.py:65 | Complexity: Intermediate | Last updated: 2026-06-02*