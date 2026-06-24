# How To: Agg Dict Renaming Deprecation

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg dict renaming deprecation

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 1, 1, 2, 2], 'B': range(5), 'C': range(5)})
```

### Step 2: Assign msg = 'nested renamer is not supported'

```python
msg = 'nested renamer is not supported'
```

### Step 3: Assign msg = "Column\\(s\\) \\['ma'\\] do not exist"

```python
msg = "Column\\(s\\) \\['ma'\\] do not exist"
```

### Step 4: Assign msg = 'nested renamer is not supported'

```python
msg = 'nested renamer is not supported'
```

### Step 5: Call df.groupby.agg()

```python
df.groupby('A').agg({'B': {'foo': ['sum', 'max']}, 'C': {'bar': ['count', 'min']}})
```

### Step 6: Call unknown.agg()

```python
df.groupby('A')[['B', 'C']].agg({'ma': 'max'})
```

### Step 7: Call df.groupby.B.agg()

```python
df.groupby('A').B.agg({'foo': 'count'})
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 1, 1, 2, 2], 'B': range(5), 'C': range(5)})
msg = 'nested renamer is not supported'
with pytest.raises(SpecificationError, match=msg):
    df.groupby('A').agg({'B': {'foo': ['sum', 'max']}, 'C': {'bar': ['count', 'min']}})
msg = "Column\\(s\\) \\['ma'\\] do not exist"
with pytest.raises(KeyError, match=msg):
    df.groupby('A')[['B', 'C']].agg({'ma': 'max'})
msg = 'nested renamer is not supported'
with pytest.raises(SpecificationError, match=msg):
    df.groupby('A').B.agg({'foo': 'count'})
```

## Next Steps


---

*Source: test_other.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*