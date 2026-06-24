# How To: Groupby Dropna Normal Index Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby dropna normal index dataframe

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: dropna, idx, outputs
```

## Step-by-Step Guide

### Step 1: Assign df_list = value

```python
df_list = [['B', 12, 12, 12], [None, 12.3, 233.0, 12], ['A', 123.23, 123, 1], ['B', 1, 1, 1.0]]
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd'])
```

### Step 3: Assign grouped = df.groupby.sum(...)

```python
grouped = df.groupby('a', dropna=dropna).sum()
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(outputs, index=pd.Index(idx, name='a'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dropna, idx, outputs

# Workflow
df_list = [['B', 12, 12, 12], [None, 12.3, 233.0, 12], ['A', 123.23, 123, 1], ['B', 1, 1, 1.0]]
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd'])
grouped = df.groupby('a', dropna=dropna).sum()
expected = pd.DataFrame(outputs, index=pd.Index(idx, name='a'))
tm.assert_frame_equal(grouped, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*