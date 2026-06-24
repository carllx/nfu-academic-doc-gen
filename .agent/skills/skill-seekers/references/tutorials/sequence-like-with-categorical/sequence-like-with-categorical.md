# How To: Sequence Like With Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sequence like with categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'id': [1, 2, 3, 4, 5, 6], 'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e']})
```

### Step 2: Assign unknown = Categorical(...)

```python
df['grade'] = Categorical(df['raw_grade'])
```

### Step 3: Assign result = list(...)

```python
result = list(df.grade.values)
```

### Step 4: Assign expected = np.array.tolist(...)

```python
expected = np.array(df.grade.values).tolist()
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 6: Call str()

```python
str(t)
```

### Step 7: Call str()

```python
str(s)
```

### Step 8: Call str()

```python
str(col)
```


## Complete Example

```python
# Workflow
df = DataFrame({'id': [1, 2, 3, 4, 5, 6], 'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e']})
df['grade'] = Categorical(df['raw_grade'])
result = list(df.grade.values)
expected = np.array(df.grade.values).tolist()
tm.assert_almost_equal(result, expected)
for t in df.itertuples(index=False):
    str(t)
for row, s in df.iterrows():
    str(s)
for c, col in df.items():
    str(col)
```

## Next Steps


---

*Source: test_iteration.py:139 | Complexity: Advanced | Last updated: 2026-06-02*