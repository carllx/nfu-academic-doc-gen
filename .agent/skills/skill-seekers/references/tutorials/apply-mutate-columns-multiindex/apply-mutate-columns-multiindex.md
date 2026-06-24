# How To: Apply Mutate Columns Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply mutate columns multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({('C', 'julian'): [1, 2, 3], ('B', 'geoffrey'): [1, 2, 3], ('A', 'julian'): [1, 2, 3], ('B', 'julian'): [1, 2, 3], ('A', 'geoffrey'): [1, 2, 3], ('C', 'geoffrey'): [1, 2, 3]}, columns=pd.MultiIndex.from_tuples([('A', 'julian'), ('A', 'geoffrey'), ('B', 'julian'), ('B', 'geoffrey'), ('C', 'julian'), ('C', 'geoffrey')]))
```

### Step 2: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 3: Assign result = gb.apply(...)

```python
result = gb.apply(add_column)
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[1, 1, 1, 3, 1, 1, 1, 3], [2, 2, 2, 6, 2, 2, 2, 6], [3, 3, 3, 9, 3, 3, 3, 9]], columns=pd.MultiIndex.from_tuples([('geoffrey', 'A', 'geoffrey'), ('geoffrey', 'B', 'geoffrey'), ('geoffrey', 'C', 'geoffrey'), ('geoffrey', 'sum', 'geoffrey'), ('julian', 'A', 'julian'), ('julian', 'B', 'julian'), ('julian', 'C', 'julian'), ('julian', 'sum', 'julian')]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign name = value

```python
name = grouped.columns[0][1]
```

### Step 7: Assign unknown = grouped.sum(...)

```python
grouped['sum', name] = grouped.sum(axis=1)
```

### Step 8: Assign gb = df.groupby(...)

```python
gb = df.groupby(level=1, axis=1)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({('C', 'julian'): [1, 2, 3], ('B', 'geoffrey'): [1, 2, 3], ('A', 'julian'): [1, 2, 3], ('B', 'julian'): [1, 2, 3], ('A', 'geoffrey'): [1, 2, 3], ('C', 'geoffrey'): [1, 2, 3]}, columns=pd.MultiIndex.from_tuples([('A', 'julian'), ('A', 'geoffrey'), ('B', 'julian'), ('B', 'geoffrey'), ('C', 'julian'), ('C', 'geoffrey')]))

def add_column(grouped):
    name = grouped.columns[0][1]
    grouped['sum', name] = grouped.sum(axis=1)
    return grouped
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby(level=1, axis=1)
result = gb.apply(add_column)
expected = pd.DataFrame([[1, 1, 1, 3, 1, 1, 1, 3], [2, 2, 2, 6, 2, 2, 2, 6], [3, 3, 3, 9, 3, 3, 3, 9]], columns=pd.MultiIndex.from_tuples([('geoffrey', 'A', 'geoffrey'), ('geoffrey', 'B', 'geoffrey'), ('geoffrey', 'C', 'geoffrey'), ('geoffrey', 'sum', 'geoffrey'), ('julian', 'A', 'julian'), ('julian', 'B', 'julian'), ('julian', 'C', 'julian'), ('julian', 'sum', 'julian')]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_apply_mutate.py:103 | Complexity: Advanced | Last updated: 2026-06-02*