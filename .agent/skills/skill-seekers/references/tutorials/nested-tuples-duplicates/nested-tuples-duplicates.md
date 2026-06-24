# How To: Nested Tuples Duplicates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nested tuples duplicates

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign dti = pd.to_datetime(...)

```python
dti = pd.to_datetime(['20190101', '20190101', '20190102'])
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(['a', 'a', 'c'])
```

### Step 3: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([dti, idx], names=['index1', 'index2'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'c1': [1, 2, 3], 'c2': [np.nan, np.nan, np.nan]}, index=mi)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c1': df['c1'], 'c2': [1.0, 1.0, np.nan]}, index=mi)
```

### Step 6: Assign df2 = df.copy(...)

```python
df2 = df.copy(deep=True)
```

### Step 7: Assign unknown = 1.0

```python
df2.loc[(dti[0], 'a'), 'c2'] = 1.0
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 9: Assign df3 = df.copy(...)

```python
df3 = df.copy(deep=True)
```

### Step 10: Assign unknown = 1.0

```python
df3.loc[[(dti[0], 'a')], 'c2'] = 1.0
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, expected)
```


## Complete Example

```python
# Workflow
dti = pd.to_datetime(['20190101', '20190101', '20190102'])
idx = Index(['a', 'a', 'c'])
mi = MultiIndex.from_arrays([dti, idx], names=['index1', 'index2'])
df = DataFrame({'c1': [1, 2, 3], 'c2': [np.nan, np.nan, np.nan]}, index=mi)
expected = DataFrame({'c1': df['c1'], 'c2': [1.0, 1.0, np.nan]}, index=mi)
df2 = df.copy(deep=True)
df2.loc[(dti[0], 'a'), 'c2'] = 1.0
tm.assert_frame_equal(df2, expected)
df3 = df.copy(deep=True)
df3.loc[[(dti[0], 'a')], 'c2'] = 1.0
tm.assert_frame_equal(df3, expected)
```

## Next Steps


---

*Source: test_multiindex.py:95 | Complexity: Advanced | Last updated: 2026-06-02*