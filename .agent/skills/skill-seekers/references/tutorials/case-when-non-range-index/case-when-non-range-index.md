# How To: Case When Non Range Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test output if index is not RangeIndex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: '\n    Test output if index is not RangeIndex\n    '

```python
'\n    Test output if index is not RangeIndex\n    '
```

### Step 2: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(seed=123)
```

### Step 3: Assign dates = date_range(...)

```python
dates = date_range('1/1/2000', periods=8)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(rng.standard_normal(size=(8, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
```

### Step 5: Assign result = Series.case_when(...)

```python
result = Series(5, index=df.index, name='A').case_when([(df.A.gt(0), df.B)])
```

### Step 6: Assign expected = df.A.mask.where(...)

```python
expected = df.A.mask(df.A.gt(0), df.B).where(df.A.gt(0), 5)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
'\n    Test output if index is not RangeIndex\n    '
rng = np.random.default_rng(seed=123)
dates = date_range('1/1/2000', periods=8)
df = DataFrame(rng.standard_normal(size=(8, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
result = Series(5, index=df.index, name='A').case_when([(df.A.gt(0), df.B)])
expected = df.A.mask(df.A.gt(0), df.B).where(df.A.gt(0), 5)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_when.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*