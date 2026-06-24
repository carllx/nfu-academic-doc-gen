# How To: Is Monotonic With Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is monotonic with nat

## Prerequisites

**Required Modules:**
- `pandas`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

**Verification:**
```python
assert obj.is_monotonic_increasing
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

**Verification:**
```python
assert obj.is_monotonic_increasing
```

### Step 3: Assign tdi = Index(...)

```python
tdi = Index(dti.view('timedelta64[ns]'))
```

**Verification:**
```python
assert not obj.is_monotonic_decreasing
```

### Step 4: Assign dti1 = dti.insert(...)

```python
dti1 = dti.insert(0, NaT)
```

**Verification:**
```python
assert obj.is_unique
```

### Step 5: Assign pi1 = dti1.to_period(...)

```python
pi1 = dti1.to_period('D')
```

**Verification:**
```python
assert not obj.is_monotonic_increasing
```

### Step 6: Assign tdi1 = Index(...)

```python
tdi1 = Index(dti1.view('timedelta64[ns]'))
```

**Verification:**
```python
assert not obj.is_monotonic_increasing
```

### Step 7: Assign dti2 = dti.insert(...)

```python
dti2 = dti.insert(3, NaT)
```

**Verification:**
```python
assert not obj.is_monotonic_decreasing
```

### Step 8: Assign pi2 = dti2.to_period(...)

```python
pi2 = dti2.to_period('h')
```

**Verification:**
```python
assert obj.is_unique
```

### Step 9: Assign tdi2 = Index(...)

```python
tdi2 = Index(dti2.view('timedelta64[ns]'))
```

**Verification:**
```python
assert not obj.is_monotonic_increasing
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
pi = dti.to_period('D')
tdi = Index(dti.view('timedelta64[ns]'))
for obj in [pi, pi._engine, dti, dti._engine, tdi, tdi._engine]:
    if isinstance(obj, Index):
        assert obj.is_monotonic_increasing
    assert obj.is_monotonic_increasing
    assert not obj.is_monotonic_decreasing
    assert obj.is_unique
dti1 = dti.insert(0, NaT)
pi1 = dti1.to_period('D')
tdi1 = Index(dti1.view('timedelta64[ns]'))
for obj in [pi1, pi1._engine, dti1, dti1._engine, tdi1, tdi1._engine]:
    if isinstance(obj, Index):
        assert not obj.is_monotonic_increasing
    assert not obj.is_monotonic_increasing
    assert not obj.is_monotonic_decreasing
    assert obj.is_unique
dti2 = dti.insert(3, NaT)
pi2 = dti2.to_period('h')
tdi2 = Index(dti2.view('timedelta64[ns]'))
for obj in [pi2, pi2._engine, dti2, dti2._engine, tdi2, tdi2._engine]:
    if isinstance(obj, Index):
        assert not obj.is_monotonic_increasing
    assert not obj.is_monotonic_increasing
    assert not obj.is_monotonic_decreasing
    assert obj.is_unique
```

## Next Steps


---

*Source: test_is_monotonic.py:8 | Complexity: Advanced | Last updated: 2026-06-02*