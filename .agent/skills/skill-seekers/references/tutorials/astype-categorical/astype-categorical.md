# How To: Astype Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = period_array(...)

```python
arr = period_array(['2000', '2001', '2001', None], freq='D')
```

### Step 2: Assign result = arr.astype(...)

```python
result = arr.astype('category')
```

### Step 3: Assign categories = pd.PeriodIndex(...)

```python
categories = pd.PeriodIndex(['2000', '2001'], freq='D')
```

### Step 4: Assign expected = pd.Categorical.from_codes(...)

```python
expected = pd.Categorical.from_codes([0, 1, 1, -1], categories=categories)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = period_array(['2000', '2001', '2001', None], freq='D')
result = arr.astype('category')
categories = pd.PeriodIndex(['2000', '2001'], freq='D')
expected = pd.Categorical.from_codes([0, 1, 1, -1], categories=categories)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*