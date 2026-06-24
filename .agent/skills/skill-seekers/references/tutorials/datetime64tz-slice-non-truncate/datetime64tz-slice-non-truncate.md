# How To: Datetime64Tz Slice Non Truncate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime64tz slice non truncate

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': date_range('2019', periods=10, tz='UTC')})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = repr(...)

```python
expected = repr(df)
```

### Step 3: Assign df = value

```python
df = df.iloc[:, :5]
```

### Step 4: Assign result = repr(...)

```python
result = repr(df)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': date_range('2019', periods=10, tz='UTC')})
expected = repr(df)
df = df.iloc[:, :5]
result = repr(df)
assert result == expected
```

## Next Steps


---

*Source: test_repr.py:380 | Complexity: Intermediate | Last updated: 2026-06-02*