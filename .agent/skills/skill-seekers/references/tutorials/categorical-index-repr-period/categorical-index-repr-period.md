# How To: Categorical Index Repr Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical index repr period

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=1)
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 2: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 3: Assign exp = "CategoricalIndex(['2011-01-01 09:00'], categories=[2011-01-01 09:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00'], categories=[2011-01-01 09:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 4: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=2)
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 5: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 6: Assign exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 7: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=3)
```

### Step 8: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

### Step 9: Assign exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 10: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
```

### Step 11: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

### Step 12: Assign exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 13: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx.append(idx)))
```

### Step 14: Assign exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00', '2011-01-01 09:00',\n                  '2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00',\n                  '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00', '2011-01-01 09:00',\n                  '2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00',\n                  '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 15: Assign idx = period_range(...)

```python
idx = period_range('2011-01', freq='M', periods=5)
```

### Step 16: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

### Step 17: Assign exp = "CategoricalIndex(['2011-01', '2011-02', '2011-03', '2011-04', '2011-05'], categories=[2011-01, 2011-02, 2011-03, 2011-04, 2011-05], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01', '2011-02', '2011-03', '2011-04', '2011-05'], categories=[2011-01, 2011-02, 2011-03, 2011-04, 2011-05], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```


## Complete Example

```python
# Workflow
idx = period_range('2011-01-01 09:00', freq='h', periods=1)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00'], categories=[2011-01-01 09:00], ordered=False, dtype='category')"
assert repr(i) == exp
idx = period_range('2011-01-01 09:00', freq='h', periods=2)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00], ordered=False, dtype='category')"
assert repr(i) == exp
idx = period_range('2011-01-01 09:00', freq='h', periods=3)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00], ordered=False, dtype='category')"
assert repr(i) == exp
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"
assert repr(i) == exp
i = CategoricalIndex(Categorical(idx.append(idx)))
exp = "CategoricalIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00',\n                  '2011-01-01 12:00', '2011-01-01 13:00', '2011-01-01 09:00',\n                  '2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00',\n                  '2011-01-01 13:00'],\n                 categories=[2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00, 2011-01-01 13:00], ordered=False, dtype='category')"
assert repr(i) == exp
idx = period_range('2011-01', freq='M', periods=5)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01', '2011-02', '2011-03', '2011-04', '2011-05'], categories=[2011-01, 2011-02, 2011-03, 2011-04, 2011-05], ordered=False, dtype='category')"
assert repr(i) == exp
```

## Next Steps


---

*Source: test_repr.py:456 | Complexity: Advanced | Last updated: 2026-06-02*