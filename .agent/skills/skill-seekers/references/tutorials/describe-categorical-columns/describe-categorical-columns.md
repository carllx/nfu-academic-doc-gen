# How To: Describe Categorical Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe categorical columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign columns = pd.CategoricalIndex(...)

```python
columns = pd.CategoricalIndex(['int1', 'int2', 'obj'], ordered=True, name='XXX')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'int1': [10, 20, 30, 40, 50], 'int2': [10, 20, 30, 40, 50], 'obj': ['A', 0, None, 'X', 1]}, columns=columns)
```

### Step 3: Assign result = df.describe(...)

```python
result = df.describe()
```

### Step 4: Assign exp_columns = pd.CategoricalIndex(...)

```python
exp_columns = pd.CategoricalIndex(['int1', 'int2'], categories=['int1', 'int2', 'obj'], ordered=True, name='XXX')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'int1': [5, 30, df.int1.std(), 10, 20, 30, 40, 50], 'int2': [5, 30, df.int2.std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], columns=exp_columns)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result.columns.values, expected.columns.values)
```


## Complete Example

```python
# Workflow
columns = pd.CategoricalIndex(['int1', 'int2', 'obj'], ordered=True, name='XXX')
df = DataFrame({'int1': [10, 20, 30, 40, 50], 'int2': [10, 20, 30, 40, 50], 'obj': ['A', 0, None, 'X', 1]}, columns=columns)
result = df.describe()
exp_columns = pd.CategoricalIndex(['int1', 'int2'], categories=['int1', 'int2', 'obj'], ordered=True, name='XXX')
expected = DataFrame({'int1': [5, 30, df.int1.std(), 10, 20, 30, 40, 50], 'int2': [5, 30, df.int2.std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], columns=exp_columns)
tm.assert_frame_equal(result, expected)
tm.assert_categorical_equal(result.columns.values, expected.columns.values)
```

## Next Steps


---

*Source: test_describe.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*