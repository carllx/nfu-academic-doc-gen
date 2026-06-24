# How To: Subclass Pivot

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass pivot

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = tm.SubclassedDataFrame(...)

```python
df = tm.SubclassedDataFrame({'index': ['A', 'B', 'C', 'C', 'B', 'A'], 'columns': ['One', 'One', 'One', 'Two', 'Two', 'Two'], 'values': [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]})
```

### Step 2: Assign pivoted = df.pivot(...)

```python
pivoted = df.pivot(index='index', columns='columns', values='values')
```

### Step 3: Assign expected = tm.SubclassedDataFrame(...)

```python
expected = tm.SubclassedDataFrame({'One': {'A': 1.0, 'B': 2.0, 'C': 3.0}, 'Two': {'A': 1.0, 'B': 2.0, 'C': 3.0}})
```

### Step 4: Assign unknown = value

```python
expected.index.name, expected.columns.name = ('index', 'columns')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(pivoted, expected)
```


## Complete Example

```python
# Workflow
df = tm.SubclassedDataFrame({'index': ['A', 'B', 'C', 'C', 'B', 'A'], 'columns': ['One', 'One', 'One', 'Two', 'Two', 'Two'], 'values': [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]})
pivoted = df.pivot(index='index', columns='columns', values='values')
expected = tm.SubclassedDataFrame({'One': {'A': 1.0, 'B': 2.0, 'C': 3.0}, 'Two': {'A': 1.0, 'B': 2.0, 'C': 3.0}})
expected.index.name, expected.columns.name = ('index', 'columns')
tm.assert_frame_equal(pivoted, expected)
```

## Next Steps


---

*Source: test_subclass.py:462 | Complexity: Intermediate | Last updated: 2026-06-02*