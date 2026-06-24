# How To: Agg Nested Dicts

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg nested dicts

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(5), 'B': range(0, 10, 2)})
```

### Step 2: Assign r = df.rolling(...)

```python
r = df.rolling(window=3)
```

### Step 3: Assign msg = 'nested renamer is not supported'

```python
msg = 'nested renamer is not supported'
```

### Step 4: Assign expected = concat(...)

```python
expected = concat([r['A'].mean(), r['A'].std(), r['B'].mean(), r['B'].std()], axis=1)
```

### Step 5: Assign expected.columns = MultiIndex.from_tuples(...)

```python
expected.columns = MultiIndex.from_tuples([('ra', 'mean'), ('ra', 'std'), ('rb', 'mean'), ('rb', 'std')])
```

### Step 6: Call r.aggregate()

```python
r.aggregate({'r1': {'A': ['mean', 'sum']}, 'r2': {'B': ['mean', 'sum']}})
```

### Step 7: Call unknown.agg()

```python
r[['A', 'B']].agg({'A': {'ra': ['mean', 'std']}, 'B': {'rb': ['mean', 'std']}})
```

### Step 8: Call r.agg()

```python
r.agg({'A': {'ra': ['mean', 'std']}, 'B': {'rb': ['mean', 'std']}})
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': range(5), 'B': range(0, 10, 2)})
r = df.rolling(window=3)
msg = 'nested renamer is not supported'
with pytest.raises(SpecificationError, match=msg):
    r.aggregate({'r1': {'A': ['mean', 'sum']}, 'r2': {'B': ['mean', 'sum']}})
expected = concat([r['A'].mean(), r['A'].std(), r['B'].mean(), r['B'].std()], axis=1)
expected.columns = MultiIndex.from_tuples([('ra', 'mean'), ('ra', 'std'), ('rb', 'mean'), ('rb', 'std')])
with pytest.raises(SpecificationError, match=msg):
    r[['A', 'B']].agg({'A': {'ra': ['mean', 'std']}, 'B': {'rb': ['mean', 'std']}})
with pytest.raises(SpecificationError, match=msg):
    r.agg({'A': {'ra': ['mean', 'std']}, 'B': {'rb': ['mean', 'std']}})
```

## Next Steps


---

*Source: test_api.py:177 | Complexity: Advanced | Last updated: 2026-06-02*