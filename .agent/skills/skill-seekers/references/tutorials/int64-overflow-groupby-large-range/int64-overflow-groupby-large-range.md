# How To: Int64 Overflow Groupby Large Range

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int64 overflow groupby large range

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`


## Step-by-Step Guide

### Step 1: Assign values = range(...)

```python
values = range(55109)
```

**Verification:**
```python
assert len(grouped) == len(values)
```

### Step 2: Assign data = DataFrame.from_dict(...)

```python
data = DataFrame.from_dict({'a': values, 'b': values, 'c': values, 'd': values})
```

### Step 3: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(['a', 'b', 'c', 'd'])
```

**Verification:**
```python
assert len(grouped) == len(values)
```


## Complete Example

```python
# Workflow
values = range(55109)
data = DataFrame.from_dict({'a': values, 'b': values, 'c': values, 'd': values})
grouped = data.groupby(['a', 'b', 'c', 'd'])
assert len(grouped) == len(values)
```

## Next Steps


---

*Source: test_sorting.py:87 | Complexity: Beginner | Last updated: 2026-06-02*