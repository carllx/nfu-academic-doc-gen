# How To: Groupby Dropna Multi Index Dataframe Agg

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby dropna multi index dataframe agg

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
# Fixtures: dropna, tuples, outputs
```

## Step-by-Step Guide

### Step 1: Assign df_list = value

```python
df_list = [['A', 'B', 12, 12, 12], ['A', None, 12.3, 233.0, 12], ['B', 'A', 123.23, 123, 1], ['A', 'B', 1, 1, 1.0]]
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd', 'e'])
```

### Step 3: Assign agg_dict = value

```python
agg_dict = {'c': 'sum', 'd': 'max', 'e': 'min'}
```

### Step 4: Assign grouped = df.groupby.agg(...)

```python
grouped = df.groupby(['a', 'b'], dropna=dropna).agg(agg_dict)
```

### Step 5: Assign mi = pd.MultiIndex.from_tuples(...)

```python
mi = pd.MultiIndex.from_tuples(tuples, names=list('ab'))
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(outputs, index=mi)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped, expected)
```

### Step 8: Assign mi = mi.set_levels(...)

```python
mi = mi.set_levels(['A', 'B', np.nan], level='b')
```


## Complete Example

```python
# Setup
# Fixtures: dropna, tuples, outputs

# Workflow
df_list = [['A', 'B', 12, 12, 12], ['A', None, 12.3, 233.0, 12], ['B', 'A', 123.23, 123, 1], ['A', 'B', 1, 1, 1.0]]
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd', 'e'])
agg_dict = {'c': 'sum', 'd': 'max', 'e': 'min'}
grouped = df.groupby(['a', 'b'], dropna=dropna).agg(agg_dict)
mi = pd.MultiIndex.from_tuples(tuples, names=list('ab'))
if not dropna:
    mi = mi.set_levels(['A', 'B', np.nan], level='b')
expected = pd.DataFrame(outputs, index=mi)
tm.assert_frame_equal(grouped, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:225 | Complexity: Advanced | Last updated: 2026-06-02*