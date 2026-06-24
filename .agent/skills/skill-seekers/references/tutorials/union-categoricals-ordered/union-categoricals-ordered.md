# How To: Union Categoricals Ordered

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categoricals ordered

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 3], ordered=True)
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical([1, 2, 3], ordered=False)
```

### Step 3: Assign msg = 'Categorical.ordered must be the same'

```python
msg = 'Categorical.ordered must be the same'
```

### Step 4: Assign res = union_categoricals(...)

```python
res = union_categoricals([c1, c1])
```

### Step 5: Assign exp = Categorical(...)

```python
exp = Categorical([1, 2, 3, 1, 2, 3], ordered=True)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 7: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 3, np.nan], ordered=True)
```

### Step 8: Assign c2 = Categorical(...)

```python
c2 = Categorical([3, 2], categories=[1, 2, 3], ordered=True)
```

### Step 9: Assign res = union_categoricals(...)

```python
res = union_categoricals([c1, c2])
```

### Step 10: Assign exp = Categorical(...)

```python
exp = Categorical([1, 2, 3, np.nan, 3, 2], ordered=True)
```

### Step 11: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 12: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 3], ordered=True)
```

### Step 13: Assign c2 = Categorical(...)

```python
c2 = Categorical([1, 2, 3], categories=[3, 2, 1], ordered=True)
```

### Step 14: Assign msg = 'to union ordered Categoricals, all categories must be the same'

```python
msg = 'to union ordered Categoricals, all categories must be the same'
```

### Step 15: Call union_categoricals()

```python
union_categoricals([c1, c2])
```

### Step 16: Call union_categoricals()

```python
union_categoricals([c1, c2])
```


## Complete Example

```python
# Workflow
c1 = Categorical([1, 2, 3], ordered=True)
c2 = Categorical([1, 2, 3], ordered=False)
msg = 'Categorical.ordered must be the same'
with pytest.raises(TypeError, match=msg):
    union_categoricals([c1, c2])
res = union_categoricals([c1, c1])
exp = Categorical([1, 2, 3, 1, 2, 3], ordered=True)
tm.assert_categorical_equal(res, exp)
c1 = Categorical([1, 2, 3, np.nan], ordered=True)
c2 = Categorical([3, 2], categories=[1, 2, 3], ordered=True)
res = union_categoricals([c1, c2])
exp = Categorical([1, 2, 3, np.nan, 3, 2], ordered=True)
tm.assert_categorical_equal(res, exp)
c1 = Categorical([1, 2, 3], ordered=True)
c2 = Categorical([1, 2, 3], categories=[3, 2, 1], ordered=True)
msg = 'to union ordered Categoricals, all categories must be the same'
with pytest.raises(TypeError, match=msg):
    union_categoricals([c1, c2])
```

## Next Steps


---

*Source: test_union_categoricals.py:163 | Complexity: Advanced | Last updated: 2026-06-02*