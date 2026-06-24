# How To: Append Preserve Index Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append preserve index name

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(columns=['A', 'B', 'C'])
```

**Verification:**
```python
assert result.index.name == 'A'
```

### Step 2: Assign df1 = df1.set_index(...)

```python
df1 = df1.set_index(['A'])
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data=[[1, 4, 7], [2, 5, 8], [3, 6, 9]], columns=['A', 'B', 'C'])
```

### Step 4: Assign df2 = df2.set_index(...)

```python
df2 = df2.set_index(['A'])
```

### Step 5: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

**Verification:**
```python
assert result.index.name == 'A'
```

### Step 6: Assign result = df1._append(...)

```python
result = df1._append(df2)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(columns=['A', 'B', 'C'])
df1 = df1.set_index(['A'])
df2 = DataFrame(data=[[1, 4, 7], [2, 5, 8], [3, 6, 9]], columns=['A', 'B', 'C'])
df2 = df2.set_index(['A'])
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df1._append(df2)
assert result.index.name == 'A'
```

## Next Steps


---

*Source: test_append.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*