# How To: Unstack Multi Index Categorical Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack multi index categorical values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 2: Assign mi = df.stack.index.rename(...)

```python
mi = df.stack(future_stack=True).index.rename(['major', 'minor'])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(['foo'] * len(mi), index=mi, name='category', dtype='category')
```

### Step 4: Assign result = ser.unstack(...)

```python
result = ser.unstack()
```

### Step 5: Assign dti = value

```python
dti = ser.index.levels[0]
```

### Step 6: Assign c = pd.Categorical(...)

```python
c = pd.Categorical(['foo'] * len(dti))
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': c.copy(), 'B': c.copy(), 'C': c.copy(), 'D': c.copy()}, columns=Index(list('ABCD'), name='minor'), index=dti.rename('major'))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=10, freq='B'))
mi = df.stack(future_stack=True).index.rename(['major', 'minor'])
ser = Series(['foo'] * len(mi), index=mi, name='category', dtype='category')
result = ser.unstack()
dti = ser.index.levels[0]
c = pd.Categorical(['foo'] * len(dti))
expected = DataFrame({'A': c.copy(), 'B': c.copy(), 'C': c.copy(), 'D': c.copy()}, columns=Index(list('ABCD'), name='minor'), index=dti.rename('major'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_unstack.py:137 | Complexity: Advanced | Last updated: 2026-06-02*