# How To: Sort Index Non Existent Label Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index non existent label multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(0, columns=[], index=MultiIndex.from_product([[], []]))
```

**Verification:**
```python
assert result is True
```

### Step 2: Assign result = value

```python
result = df.sort_index().index.is_monotonic_increasing
```

**Verification:**
```python
assert result is True
```

### Step 3: Assign unknown = 1

```python
df.loc['b', '2'] = 1
```

### Step 4: Assign unknown = 1

```python
df.loc['a', '3'] = 1
```


## Complete Example

```python
# Workflow
df = DataFrame(0, columns=[], index=MultiIndex.from_product([[], []]))
with tm.assert_produces_warning(None):
    df.loc['b', '2'] = 1
    df.loc['a', '3'] = 1
result = df.sort_index().index.is_monotonic_increasing
assert result is True
```

## Next Steps


---

*Source: test_sort_index.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*