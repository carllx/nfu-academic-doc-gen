# How To: Categorical Index Repr Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical index repr datetime

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2011-01-01 09:00', freq='h', periods=5)
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

### Step 3: Assign exp = "CategoricalIndex(['2011-01-01 09:00:00', '2011-01-01 10:00:00',\n                  '2011-01-01 11:00:00', '2011-01-01 12:00:00',\n                  '2011-01-01 13:00:00'],\n                 categories=[2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00, 2011-01-01 12:00:00, 2011-01-01 13:00:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00:00', '2011-01-01 10:00:00',\n                  '2011-01-01 11:00:00', '2011-01-01 12:00:00',\n                  '2011-01-01 13:00:00'],\n                 categories=[2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00, 2011-01-01 12:00:00, 2011-01-01 13:00:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```

### Step 4: Assign idx = date_range(...)

```python
idx = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
```

### Step 5: Assign i = CategoricalIndex(...)

```python
i = CategoricalIndex(Categorical(idx))
```

### Step 6: Assign exp = "CategoricalIndex(['2011-01-01 09:00:00-05:00', '2011-01-01 10:00:00-05:00',\n                  '2011-01-01 11:00:00-05:00', '2011-01-01 12:00:00-05:00',\n                  '2011-01-01 13:00:00-05:00'],\n                 categories=[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00, 2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00, 2011-01-01 13:00:00-05:00], ordered=False, dtype='category')"

```python
exp = "CategoricalIndex(['2011-01-01 09:00:00-05:00', '2011-01-01 10:00:00-05:00',\n                  '2011-01-01 11:00:00-05:00', '2011-01-01 12:00:00-05:00',\n                  '2011-01-01 13:00:00-05:00'],\n                 categories=[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00, 2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00, 2011-01-01 13:00:00-05:00], ordered=False, dtype='category')"
```

**Verification:**
```python
assert repr(i) == exp
```


## Complete Example

```python
# Workflow
idx = date_range('2011-01-01 09:00', freq='h', periods=5)
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00:00', '2011-01-01 10:00:00',\n                  '2011-01-01 11:00:00', '2011-01-01 12:00:00',\n                  '2011-01-01 13:00:00'],\n                 categories=[2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00, 2011-01-01 12:00:00, 2011-01-01 13:00:00], ordered=False, dtype='category')"
assert repr(i) == exp
idx = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
i = CategoricalIndex(Categorical(idx))
exp = "CategoricalIndex(['2011-01-01 09:00:00-05:00', '2011-01-01 10:00:00-05:00',\n                  '2011-01-01 11:00:00-05:00', '2011-01-01 12:00:00-05:00',\n                  '2011-01-01 13:00:00-05:00'],\n                 categories=[2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00, 2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00, 2011-01-01 13:00:00-05:00], ordered=False, dtype='category')"
assert repr(i) == exp
```

## Next Steps


---

*Source: test_repr.py:408 | Complexity: Intermediate | Last updated: 2026-06-02*