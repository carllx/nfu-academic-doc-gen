# How To: Iat Getitem Series With Period Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iat getitem series with period index

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = period_range(...)

```python
index = period_range('1/1/2001', periods=10)
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).standard_normal(10), index=index)
```

### Step 3: Assign expected = value

```python
expected = ser[index[0]]
```

### Step 4: Assign result = value

```python
result = ser.iat[0]
```

**Verification:**
```python
assert expected == result
```


## Complete Example

```python
# Workflow
index = period_range('1/1/2001', periods=10)
ser = Series(np.random.default_rng(2).standard_normal(10), index=index)
expected = ser[index[0]]
result = ser.iat[0]
assert expected == result
```

## Next Steps


---

*Source: test_iat.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*