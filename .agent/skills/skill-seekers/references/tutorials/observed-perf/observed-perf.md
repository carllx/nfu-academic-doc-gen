# How To: Observed Perf

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test observed perf

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'cat': np.random.default_rng(2).integers(0, 255, size=30000), 'int_id': np.random.default_rng(2).integers(0, 255, size=30000), 'other_id': np.random.default_rng(2).integers(0, 10000, size=30000), 'foo': 0})
```

**Verification:**
```python
assert result.index.levels[0].nunique() == df.cat.nunique()
```

### Step 2: Assign unknown = df.cat.astype.astype(...)

```python
df['cat'] = df.cat.astype(str).astype('category')
```

**Verification:**
```python
assert result.index.levels[1].nunique() == df.int_id.nunique()
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(['cat', 'int_id', 'other_id'], observed=True)
```

**Verification:**
```python
assert result.index.levels[2].nunique() == df.other_id.nunique()
```

### Step 4: Assign result = grouped.count(...)

```python
result = grouped.count()
```

**Verification:**
```python
assert result.index.levels[0].nunique() == df.cat.nunique()
```


## Complete Example

```python
# Workflow
df = DataFrame({'cat': np.random.default_rng(2).integers(0, 255, size=30000), 'int_id': np.random.default_rng(2).integers(0, 255, size=30000), 'other_id': np.random.default_rng(2).integers(0, 10000, size=30000), 'foo': 0})
df['cat'] = df.cat.astype(str).astype('category')
grouped = df.groupby(['cat', 'int_id', 'other_id'], observed=True)
result = grouped.count()
assert result.index.levels[0].nunique() == df.cat.nunique()
assert result.index.levels[1].nunique() == df.int_id.nunique()
assert result.index.levels[2].nunique() == df.other_id.nunique()
```

## Next Steps


---

*Source: test_categorical.py:488 | Complexity: Intermediate | Last updated: 2026-06-02*