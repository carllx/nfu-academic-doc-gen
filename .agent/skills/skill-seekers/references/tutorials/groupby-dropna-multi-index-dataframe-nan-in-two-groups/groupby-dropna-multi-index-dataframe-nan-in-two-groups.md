# How To: Groupby Dropna Multi Index Dataframe Nan In Two Groups

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby dropna multi index dataframe nan in two groups

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
# Fixtures: dropna, tuples, outputs, nulls_fixture, nulls_fixture2
```

## Step-by-Step Guide

### Step 1: Assign df_list = value

```python
df_list = [['A', 'B', 12, 12, 12], ['A', nulls_fixture, 12.3, 233.0, 12], ['B', 'A', 123.23, 123, 1], [nulls_fixture2, 'B', 1, 1, 1.0], ['A', nulls_fixture2, 1, 1, 1.0]]
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd', 'e'])
```

### Step 3: Assign grouped = df.groupby.sum(...)

```python
grouped = df.groupby(['a', 'b'], dropna=dropna).sum()
```

### Step 4: Assign mi = pd.MultiIndex.from_tuples(...)

```python
mi = pd.MultiIndex.from_tuples(tuples, names=list('ab'))
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(outputs, index=mi)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped, expected)
```

### Step 7: Assign mi = mi.set_levels(...)

```python
mi = mi.set_levels([['A', 'B', np.nan], ['A', 'B', np.nan]])
```


## Complete Example

```python
# Setup
# Fixtures: dropna, tuples, outputs, nulls_fixture, nulls_fixture2

# Workflow
df_list = [['A', 'B', 12, 12, 12], ['A', nulls_fixture, 12.3, 233.0, 12], ['B', 'A', 123.23, 123, 1], [nulls_fixture2, 'B', 1, 1, 1.0], ['A', nulls_fixture2, 1, 1, 1.0]]
df = pd.DataFrame(df_list, columns=['a', 'b', 'c', 'd', 'e'])
grouped = df.groupby(['a', 'b'], dropna=dropna).sum()
mi = pd.MultiIndex.from_tuples(tuples, names=list('ab'))
if not dropna:
    mi = mi.set_levels([['A', 'B', np.nan], ['A', 'B', np.nan]])
expected = pd.DataFrame(outputs, index=mi)
tm.assert_frame_equal(grouped, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*