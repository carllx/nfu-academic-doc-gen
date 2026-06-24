# How To: Fill Consistency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fill consistency

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
df = DataFrame(index=pd.MultiIndex.from_product([['value1', 'value2'], date_range('2014-01-01', '2014-01-06')]), columns=Index(['1', '2'], name='id'))
```

### Step 2: Assign unknown = value

```python
df['1'] = [np.nan, 1, np.nan, np.nan, 11, np.nan, np.nan, 2, np.nan, np.nan, 22, np.nan]
```

### Step 3: Assign unknown = value

```python
df['2'] = [np.nan, 3, np.nan, np.nan, 33, np.nan, np.nan, 4, np.nan, np.nan, 44, np.nan]
```

### Step 4: Assign msg = "The 'axis' keyword in DataFrame.groupby is deprecated"

```python
msg = "The 'axis' keyword in DataFrame.groupby is deprecated"
```

### Step 5: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = df.groupby.fillna(...)

```python
expected = df.groupby(level=0, axis=0).fillna(method='ffill')
```

### Step 8: Assign result = value

```python
result = df.T.groupby(level=0, axis=1).fillna(method='ffill').T
```


## Complete Example

```python
# Workflow
df = DataFrame(index=pd.MultiIndex.from_product([['value1', 'value2'], date_range('2014-01-01', '2014-01-06')]), columns=Index(['1', '2'], name='id'))
df['1'] = [np.nan, 1, np.nan, np.nan, 11, np.nan, np.nan, 2, np.nan, np.nan, 22, np.nan]
df['2'] = [np.nan, 3, np.nan, np.nan, 33, np.nan, np.nan, 4, np.nan, np.nan, 44, np.nan]
msg = "The 'axis' keyword in DataFrame.groupby is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.groupby(level=0, axis=0).fillna(method='ffill')
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.T.groupby(level=0, axis=1).fillna(method='ffill').T
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:62 | Complexity: Advanced | Last updated: 2026-06-02*