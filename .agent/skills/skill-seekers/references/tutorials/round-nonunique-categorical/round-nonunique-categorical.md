# How To: Round Nonunique Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round nonunique categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = pd.CategoricalIndex(...)

```python
idx = pd.CategoricalIndex(['low'] * 3 + ['hi'] * 3)
```

**Verification:**
```python
assert df_categorical.shape == (6, 3)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((6, 3)), columns=list('abc'))
```

**Verification:**
```python
assert result.shape == (6, 3)
```

### Step 3: Assign expected = df.round(...)

```python
expected = df.round(3)
```

### Step 4: Assign expected.index = idx

```python
expected.index = idx
```

### Step 5: Assign df_categorical = df.copy.set_index(...)

```python
df_categorical = df.copy().set_index(idx)
```

**Verification:**
```python
assert df_categorical.shape == (6, 3)
```

### Step 6: Assign result = df_categorical.round(...)

```python
result = df_categorical.round(3)
```

**Verification:**
```python
assert result.shape == (6, 3)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = pd.CategoricalIndex(['low'] * 3 + ['hi'] * 3)
df = DataFrame(np.random.default_rng(2).random((6, 3)), columns=list('abc'))
expected = df.round(3)
expected.index = idx
df_categorical = df.copy().set_index(idx)
assert df_categorical.shape == (6, 3)
result = df_categorical.round(3)
assert result.shape == (6, 3)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_round.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*