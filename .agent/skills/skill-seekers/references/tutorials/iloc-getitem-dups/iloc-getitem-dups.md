# How To: Iloc Getitem Dups

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem dups

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([{'A': None, 'B': 1}, {'A': 2, 'B': 2}])
```

**Verification:**
```python
assert isna(result)
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([{'A': 3, 'B': 3}, {'A': 4, 'B': 4}])
```

### Step 3: Assign df = concat(...)

```python
df = concat([df1, df2], axis=1)
```

### Step 4: Assign result = value

```python
result = df.iloc[0, 0]
```

**Verification:**
```python
assert isna(result)
```

### Step 5: Assign result = value

```python
result = df.iloc[0, :]
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([np.nan, 1, 3, 3], index=['A', 'B', 'A', 'B'], name=0)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame([{'A': None, 'B': 1}, {'A': 2, 'B': 2}])
df2 = DataFrame([{'A': 3, 'B': 3}, {'A': 4, 'B': 4}])
df = concat([df1, df2], axis=1)
result = df.iloc[0, 0]
assert isna(result)
result = df.iloc[0, :]
expected = Series([np.nan, 1, 3, 3], index=['A', 'B', 'A', 'B'], name=0)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:324 | Complexity: Intermediate | Last updated: 2026-06-02*