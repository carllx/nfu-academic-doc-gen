# How To: Groupby Apply With Dropna For Multi Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby apply with dropna for multi index

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
# Fixtures: dropna, data, selected_data, levels
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data)
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('groups', dropna=dropna)
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 4: Assign mi_tuples = tuple(...)

```python
mi_tuples = tuple(zip(data['groups'], selected_data['values']))
```

### Step 5: Assign mi = pd.MultiIndex.from_tuples(...)

```python
mi = pd.MultiIndex.from_tuples(mi_tuples, names=['groups', None])
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(selected_data, index=mi)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = gb.apply(...)

```python
result = gb.apply(lambda grp: pd.DataFrame({'values': range(len(grp))}))
```

### Step 9: Assign mi = mi.set_levels(...)

```python
mi = mi.set_levels(levels, level='groups')
```


## Complete Example

```python
# Setup
# Fixtures: dropna, data, selected_data, levels

# Workflow
df = pd.DataFrame(data)
gb = df.groupby('groups', dropna=dropna)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = gb.apply(lambda grp: pd.DataFrame({'values': range(len(grp))}))
mi_tuples = tuple(zip(data['groups'], selected_data['values']))
mi = pd.MultiIndex.from_tuples(mi_tuples, names=['groups', None])
if not dropna and levels:
    mi = mi.set_levels(levels, level='groups')
expected = pd.DataFrame(selected_data, index=mi)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_dropna.py:322 | Complexity: Advanced | Last updated: 2026-06-02*