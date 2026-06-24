# How To: Categorical Repr Period Ordered

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical repr period ordered

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 2: Assign c = Categorical(...)

```python
c = Categorical(idx, ordered=True)
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 3: Assign exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'

```python
exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 4: Assign c = Categorical(...)

```python
c = Categorical(idx.append(idx), categories=idx, ordered=True)
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 5: Assign exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00, 2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'

```python
exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00, 2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 6: Assign idx = period_range(...)

```python
idx = period_range('2011-01', freq='M', periods=5)
```

### Step 7: Assign c = Categorical(...)

```python
c = Categorical(idx, ordered=True)
```

### Step 8: Assign exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'

```python
exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'
```

**Verification:**
```python
assert repr(c) == exp
```

### Step 9: Assign c = Categorical(...)

```python
c = Categorical(idx.append(idx), categories=idx, ordered=True)
```

### Step 10: Assign exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05, 2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'

```python
exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05, 2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'
```

**Verification:**
```python
assert repr(c) == exp
```


## Complete Example

```python
# Workflow
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
c = Categorical(idx, ordered=True)
exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'
assert repr(c) == exp
c = Categorical(idx.append(idx), categories=idx, ordered=True)
exp = '[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00, 2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00]\nCategories (5, period[h]): [2011-01-01 09:00 < 2011-01-01 10:00 < 2011-01-01 11:00 < 2011-01-01 12:00 <\n                            2011-01-01 13:00]'
assert repr(c) == exp
idx = period_range('2011-01', freq='M', periods=5)
c = Categorical(idx, ordered=True)
exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'
assert repr(c) == exp
c = Categorical(idx.append(idx), categories=idx, ordered=True)
exp = '[2011-01, 2011-02, 2011-03, 2011-04, 2011-05, 2011-01, 2011-02, 2011-03, 2011-04, 2011-05]\nCategories (5, period[M]): [2011-01 < 2011-02 < 2011-03 < 2011-04 < 2011-05]'
assert repr(c) == exp
```

## Next Steps


---

*Source: test_repr.py:295 | Complexity: Advanced | Last updated: 2026-06-02*