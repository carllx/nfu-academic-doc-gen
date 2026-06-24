# How To: Groupby Level No Obs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby level no obs

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_tuples(...)

```python
midx = MultiIndex.from_tuples([('f1', 's1'), ('f1', 's2'), ('f2', 's1'), ('f2', 's2'), ('f3', 's1'), ('f3', 's2')])
```

**Verification:**
```python
assert (result.columns == ['f2', 'f3']).all()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], columns=midx)
```

### Step 3: Assign df1 = value

```python
df1 = df.loc(axis=1)[df.columns.map(lambda u: u[0] in ['f2', 'f3'])]
```

### Step 4: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 5: Assign result = grouped.sum(...)

```python
result = grouped.sum()
```

**Verification:**
```python
assert (result.columns == ['f2', 'f3']).all()
```

### Step 6: Assign grouped = df1.groupby(...)

```python
grouped = df1.groupby(axis=1, level=0)
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_tuples([('f1', 's1'), ('f1', 's2'), ('f2', 's1'), ('f2', 's2'), ('f3', 's1'), ('f3', 's2')])
df = DataFrame([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], columns=midx)
df1 = df.loc(axis=1)[df.columns.map(lambda u: u[0] in ['f2', 'f3'])]
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = df1.groupby(axis=1, level=0)
result = grouped.sum()
assert (result.columns == ['f2', 'f3']).all()
```

## Next Steps


---

*Source: test_multilevel.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*