# How To: Basic Getitem Dt64Tz Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic getitem dt64tz values

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('2011-01-01', periods=3, tz='US/Eastern'), index=['a', 'b', 'c'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = Timestamp(...)

```python
expected = Timestamp('2011-01-01', tz='US/Eastern')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = value

```python
result = ser.loc['a']
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = value

```python
result = ser.iloc[0]
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = ser['a']
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
ser = Series(date_range('2011-01-01', periods=3, tz='US/Eastern'), index=['a', 'b', 'c'])
expected = Timestamp('2011-01-01', tz='US/Eastern')
result = ser.loc['a']
assert result == expected
result = ser.iloc[0]
assert result == expected
result = ser['a']
assert result == expected
```

## Next Steps


---

*Source: test_indexing.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*