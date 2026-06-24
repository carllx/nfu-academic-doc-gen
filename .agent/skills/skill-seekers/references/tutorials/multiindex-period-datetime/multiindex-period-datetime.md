# How To: Multiindex Period Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex period datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index(['a', 'a', 'a', 'b', 'b'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign idx2 = period_range(...)

```python
idx2 = period_range('2012-01', periods=len(idx1), freq='M')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(len(idx1)), [idx1, idx2])
```

### Step 4: Assign expected = value

```python
expected = s.iloc[0]
```

### Step 5: Assign result = value

```python
result = s.loc['a', Period('2012-01')]
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign result = value

```python
result = s.loc['a', datetime(2012, 1, 1)]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
idx1 = Index(['a', 'a', 'a', 'b', 'b'])
idx2 = period_range('2012-01', periods=len(idx1), freq='M')
s = Series(np.random.default_rng(2).standard_normal(len(idx1)), [idx1, idx2])
expected = s.iloc[0]
result = s.loc['a', Period('2012-01')]
assert result == expected
result = s.loc['a', datetime(2012, 1, 1)]
assert result == expected
```

## Next Steps


---

*Source: test_datetime.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*