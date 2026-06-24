# How To: Min Max Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min max categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`


## Step-by-Step Guide

### Step 1: Assign ci = pd.CategoricalIndex(...)

```python
ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
```

**Verification:**
```python
assert ci.min() == 'c'
```

### Step 2: Assign msg = 'Categorical is not ordered for operation min\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'

```python
msg = 'Categorical is not ordered for operation min\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'
```

**Verification:**
```python
assert ci.max() == 'b'
```

### Step 3: Assign msg = 'Categorical is not ordered for operation max\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'

```python
msg = 'Categorical is not ordered for operation max\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'
```

### Step 4: Assign ci = pd.CategoricalIndex(...)

```python
ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=True)
```

**Verification:**
```python
assert ci.min() == 'c'
```

### Step 5: Call ci.min()

```python
ci.min()
```

### Step 6: Call ci.max()

```python
ci.max()
```


## Complete Example

```python
# Workflow
ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
msg = 'Categorical is not ordered for operation min\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'
with pytest.raises(TypeError, match=msg):
    ci.min()
msg = 'Categorical is not ordered for operation max\\nyou can use .as_ordered\\(\\) to change the Categorical to an ordered one\\n'
with pytest.raises(TypeError, match=msg):
    ci.max()
ci = pd.CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=True)
assert ci.min() == 'c'
assert ci.max() == 'b'
```

## Next Steps


---

*Source: test_reductions.py:560 | Complexity: Intermediate | Last updated: 2026-06-02*