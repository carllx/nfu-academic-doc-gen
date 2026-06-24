# How To: Dataframe Categorical With Nan

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe categorical with nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: observed
```

## Step-by-Step Guide

### Step 1: Assign s1 = Categorical(...)

```python
s1 = Categorical([np.nan, 'a', np.nan, 'a'], categories=['a', 'b', 'c'])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([1, 2, 3, 4])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'s1': s1, 's2': s2})
```

### Step 4: Assign result = df.groupby.first.reset_index(...)

```python
result = df.groupby('s1', observed=observed).first().reset_index()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'s1': Categorical(['a'], categories=['a', 'b', 'c']), 's2': [2]})
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'s1': Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c']), 's2': [2, np.nan, np.nan]})
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
s1 = Categorical([np.nan, 'a', np.nan, 'a'], categories=['a', 'b', 'c'])
s2 = Series([1, 2, 3, 4])
df = DataFrame({'s1': s1, 's2': s2})
result = df.groupby('s1', observed=observed).first().reset_index()
if observed:
    expected = DataFrame({'s1': Categorical(['a'], categories=['a', 'b', 'c']), 's2': [2]})
else:
    expected = DataFrame({'s1': Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c']), 's2': [2, np.nan, np.nan]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:616 | Complexity: Intermediate | Last updated: 2026-06-02*