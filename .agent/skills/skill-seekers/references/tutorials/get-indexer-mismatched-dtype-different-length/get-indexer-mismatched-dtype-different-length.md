# How To: Get Indexer Mismatched Dtype Different Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer mismatched dtype different length

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: non_comparable_idx
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('D')
```

### Step 3: Assign other = non_comparable_idx

```python
other = non_comparable_idx
```

### Step 4: Assign res = unknown.get_indexer(...)

```python
res = pi[:-1].get_indexer(other)
```

### Step 5: Assign expected = value

```python
expected = -np.ones(other.shape, dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: non_comparable_idx

# Workflow
dti = date_range('2016-01-01', periods=3)
pi = dti.to_period('D')
other = non_comparable_idx
res = pi[:-1].get_indexer(other)
expected = -np.ones(other.shape, dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_indexing.py:423 | Complexity: Intermediate | Last updated: 2026-06-02*