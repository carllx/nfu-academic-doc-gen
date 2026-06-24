# How To: At Getitem Dt64Tz Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at getitem dt64tz values

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'name': ['John', 'Anderson'], 'date': [Timestamp(2017, 3, 13, 13, 32, 56), Timestamp(2017, 2, 16, 12, 10, 3)]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign unknown = unknown.dt.tz_localize(...)

```python
df['date'] = df['date'].dt.tz_localize('Asia/Shanghai')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2017-03-13 13:32:56+0800', tz='Asia/Shanghai')
```

### Step 4: Assign result = value

```python
result = df.loc[0, 'date']
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = df.at[0, 'date']
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'name': ['John', 'Anderson'], 'date': [Timestamp(2017, 3, 13, 13, 32, 56), Timestamp(2017, 2, 16, 12, 10, 3)]})
df['date'] = df['date'].dt.tz_localize('Asia/Shanghai')
expected = Timestamp('2017-03-13 13:32:56+0800', tz='Asia/Shanghai')
result = df.loc[0, 'date']
assert result == expected
result = df.at[0, 'date']
assert result == expected
```

## Next Steps


---

*Source: test_scalar.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*