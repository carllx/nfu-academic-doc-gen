# How To: Get Dummies Just Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get dummies just na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: sparse
```

## Step-by-Step Guide

### Step 1: Assign just_na_list = value

```python
just_na_list = [np.nan]
```

**Verification:**
```python
assert res_list.empty
```

### Step 2: Assign just_na_series = Series(...)

```python
just_na_series = Series(just_na_list)
```

**Verification:**
```python
assert res_series.empty
```

### Step 3: Assign just_na_series_index = Series(...)

```python
just_na_series_index = Series(just_na_list, index=['A'])
```

**Verification:**
```python
assert res_series_index.empty
```

### Step 4: Assign res_list = get_dummies(...)

```python
res_list = get_dummies(just_na_list, sparse=sparse)
```

**Verification:**
```python
assert res_list.index.tolist() == [0]
```

### Step 5: Assign res_series = get_dummies(...)

```python
res_series = get_dummies(just_na_series, sparse=sparse)
```

**Verification:**
```python
assert res_series.index.tolist() == [0]
```

### Step 6: Assign res_series_index = get_dummies(...)

```python
res_series_index = get_dummies(just_na_series_index, sparse=sparse)
```

**Verification:**
```python
assert res_series_index.index.tolist() == ['A']
```


## Complete Example

```python
# Setup
# Fixtures: sparse

# Workflow
just_na_list = [np.nan]
just_na_series = Series(just_na_list)
just_na_series_index = Series(just_na_list, index=['A'])
res_list = get_dummies(just_na_list, sparse=sparse)
res_series = get_dummies(just_na_series, sparse=sparse)
res_series_index = get_dummies(just_na_series_index, sparse=sparse)
assert res_list.empty
assert res_series.empty
assert res_series_index.empty
assert res_list.index.tolist() == [0]
assert res_series.index.tolist() == [0]
assert res_series_index.index.tolist() == ['A']
```

## Next Steps


---

*Source: test_get_dummies.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*