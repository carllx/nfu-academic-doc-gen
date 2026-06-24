# How To: Concat Categorical Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categorical datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'x': Series(datetime(2021, 1, 1), index=[0], dtype='category')})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'x': Series(datetime(2021, 1, 2), index=[1], dtype='category')})
```

### Step 3: Assign result = pd.concat(...)

```python
result = pd.concat([df1, df2])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': Series([datetime(2021, 1, 1), datetime(2021, 1, 2)])})
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'x': Series(datetime(2021, 1, 1), index=[0], dtype='category')})
df2 = DataFrame({'x': Series(datetime(2021, 1, 2), index=[1], dtype='category')})
result = pd.concat([df1, df2])
expected = DataFrame({'x': Series([datetime(2021, 1, 1), datetime(2021, 1, 2)])})
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*