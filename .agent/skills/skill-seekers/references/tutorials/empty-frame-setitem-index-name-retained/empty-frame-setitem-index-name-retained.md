# How To: Empty Frame Setitem Index Name Retained

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty frame setitem index name retained

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
df = DataFrame({}, index=pd.RangeIndex(0, name='df_index'))
```

### Step 2: Assign series = Series(...)

```python
series = Series(1.23, index=pd.RangeIndex(4, name='series_index'))
```

### Step 3: Assign unknown = series

```python
df['series'] = series
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'series': [1.23] * 4}, index=pd.RangeIndex(4, name='df_index'), columns=Index(['series']))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({}, index=pd.RangeIndex(0, name='df_index'))
series = Series(1.23, index=pd.RangeIndex(4, name='series_index'))
df['series'] = series
expected = DataFrame({'series': [1.23] * 4}, index=pd.RangeIndex(4, name='df_index'), columns=Index(['series']))
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_partial.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*