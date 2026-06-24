# How To: Replace Categorical Ea Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace categorical ea dtype

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(pd.array(['a', 'b'], dtype='string'))
```

### Step 2: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

### Step 3: Assign expected = Categorical(...)

```python
expected = Categorical(pd.array(['c', pd.NA], dtype='string'))
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = pd.Series(cat).replace(['a', 'b'], ['c', pd.NA])._values
```


## Complete Example

```python
# Workflow
cat = Categorical(pd.array(['a', 'b'], dtype='string'))
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = pd.Series(cat).replace(['a', 'b'], ['c', pd.NA])._values
expected = Categorical(pd.array(['c', pd.NA], dtype='string'))
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*