# How To: Df Series Inf Nan Consistency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test df series inf nan consistency

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
```

### Step 2: Assign col1 = value

```python
col1 = [5, 4, 3, 5, 8, 5, 2, 1, 6, 6]
```

### Step 3: Assign col2 = value

```python
col2 = [5, 4, np.nan, 5, 8, 5, np.inf, np.nan, 6, -np.inf]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(data={'col1': col1, 'col2': col2}, index=index, dtype='f8')
```

### Step 5: Assign df_result = df.rank(...)

```python
df_result = df.rank()
```

### Step 6: Assign series_result = df.copy(...)

```python
series_result = df.copy()
```

### Step 7: Assign unknown = unknown.rank(...)

```python
series_result['col1'] = df['col1'].rank()
```

### Step 8: Assign unknown = unknown.rank(...)

```python
series_result['col2'] = df['col2'].rank()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_result, series_result)
```


## Complete Example

```python
# Workflow
index = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
col1 = [5, 4, 3, 5, 8, 5, 2, 1, 6, 6]
col2 = [5, 4, np.nan, 5, 8, 5, np.inf, np.nan, 6, -np.inf]
df = DataFrame(data={'col1': col1, 'col2': col2}, index=index, dtype='f8')
df_result = df.rank()
series_result = df.copy()
series_result['col1'] = df['col1'].rank()
series_result['col2'] = df['col2'].rank()
tm.assert_frame_equal(df_result, series_result)
```

## Next Steps


---

*Source: test_rank.py:419 | Complexity: Advanced | Last updated: 2026-06-02*