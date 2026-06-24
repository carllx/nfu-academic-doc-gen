# How To: Categorical With Nan Consistency

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical with nan consistency

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.util.hashing`
- `pandas.util`


## Step-by-Step Guide

### Step 1: Assign c = pd.Categorical.from_codes(...)

```python
c = pd.Categorical.from_codes([-1, 0, 1, 2, 3, 4], categories=pd.date_range('2012-01-01', periods=5, name='B'))
```

**Verification:**
```python
assert result[0] in expected
```

### Step 2: Assign expected = hash_array(...)

```python
expected = hash_array(c, categorize=False)
```

**Verification:**
```python
assert result[1] in expected
```

### Step 3: Assign c = pd.Categorical.from_codes(...)

```python
c = pd.Categorical.from_codes([-1, 0], categories=[pd.Timestamp('2012-01-01')])
```

### Step 4: Assign result = hash_array(...)

```python
result = hash_array(c, categorize=False)
```

**Verification:**
```python
assert result[0] in expected
```


## Complete Example

```python
# Workflow
c = pd.Categorical.from_codes([-1, 0, 1, 2, 3, 4], categories=pd.date_range('2012-01-01', periods=5, name='B'))
expected = hash_array(c, categorize=False)
c = pd.Categorical.from_codes([-1, 0], categories=[pd.Timestamp('2012-01-01')])
result = hash_array(c, categorize=False)
assert result[0] in expected
assert result[1] in expected
```

## Next Steps


---

*Source: test_hashing.py:262 | Complexity: Intermediate | Last updated: 2026-06-02*