# How To: Groupby Duplicated Column Errormsg

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby duplicated column errormsg

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['A', 'B', 'A', 'C'], data=[range(4), range(2, 6), range(0, 8, 2)])
```

**Verification:**
```python
assert c.columns.nlevels == 1
```

### Step 2: Assign msg = "Grouper for 'A' not 1-dimensional"

```python
msg = "Grouper for 'A' not 1-dimensional"
```

**Verification:**
```python
assert c.columns.size == 3
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('B')
```

### Step 4: Assign c = grouped.count(...)

```python
c = grouped.count()
```

**Verification:**
```python
assert c.columns.nlevels == 1
```

### Step 5: Call df.groupby()

```python
df.groupby('A')
```

### Step 6: Call df.groupby()

```python
df.groupby(['A', 'B'])
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=['A', 'B', 'A', 'C'], data=[range(4), range(2, 6), range(0, 8, 2)])
msg = "Grouper for 'A' not 1-dimensional"
with pytest.raises(ValueError, match=msg):
    df.groupby('A')
with pytest.raises(ValueError, match=msg):
    df.groupby(['A', 'B'])
grouped = df.groupby('B')
c = grouped.count()
assert c.columns.nlevels == 1
assert c.columns.size == 3
```

## Next Steps


---

*Source: test_grouping.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*