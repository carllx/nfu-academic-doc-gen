# How To: Loc Setitem With Expansion Non Category

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc setitem with expansion non category

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign unknown = 20

```python
df.loc['a'] = 20
```

### Step 2: Assign df3 = df.copy(...)

```python
df3 = df.copy()
```

### Step 3: Assign unknown = 10

```python
df3.loc['d', 'A'] = 10
```

### Step 4: Assign bidx3 = Index(...)

```python
bidx3 = Index(list('aabbcad'), name='B')
```

### Step 5: Assign expected3 = DataFrame(...)

```python
expected3 = DataFrame({'A': [20, 20, 2, 3, 4, 20, 10.0]}, index=Index(bidx3))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, expected3)
```

### Step 7: Assign df4 = df.copy(...)

```python
df4 = df.copy()
```

### Step 8: Assign unknown = 10

```python
df4.loc['d', 'C'] = 10
```

### Step 9: Assign expected3 = DataFrame(...)

```python
expected3 = DataFrame({'A': [20, 20, 2, 3, 4, 20, np.nan], 'C': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 10]}, index=Index(bidx3))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df4, expected3)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
df.loc['a'] = 20
df3 = df.copy()
df3.loc['d', 'A'] = 10
bidx3 = Index(list('aabbcad'), name='B')
expected3 = DataFrame({'A': [20, 20, 2, 3, 4, 20, 10.0]}, index=Index(bidx3))
tm.assert_frame_equal(df3, expected3)
df4 = df.copy()
df4.loc['d', 'C'] = 10
expected3 = DataFrame({'A': [20, 20, 2, 3, 4, 20, np.nan], 'C': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 10]}, index=Index(bidx3))
tm.assert_frame_equal(df4, expected3)
```

## Next Steps


---

*Source: test_categorical.py:81 | Complexity: Advanced | Last updated: 2026-06-02*