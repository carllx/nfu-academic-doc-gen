# How To: Int64 Overflow Outer Merge

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int64 overflow outer merge

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((1000, 7)), columns=list('ABCDEF') + ['G1'])
```

**Verification:**
```python
assert len(result) == 2000
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(3).standard_normal((1000, 7)), columns=list('ABCDEF') + ['G2'])
```

### Step 3: Assign result = merge(...)

```python
result = merge(df1, df2, how='outer')
```

**Verification:**
```python
assert len(result) == 2000
```


## Complete Example

```python
# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((1000, 7)), columns=list('ABCDEF') + ['G1'])
df2 = DataFrame(np.random.default_rng(3).standard_normal((1000, 7)), columns=list('ABCDEF') + ['G2'])
result = merge(df1, df2, how='outer')
assert len(result) == 2000
```

## Next Steps


---

*Source: test_sorting.py:196 | Complexity: Beginner | Last updated: 2026-06-02*