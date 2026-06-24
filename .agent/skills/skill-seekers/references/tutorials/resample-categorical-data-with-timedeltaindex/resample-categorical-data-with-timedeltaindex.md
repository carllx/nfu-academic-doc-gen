# How To: Resample Categorical Data With Timedeltaindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample categorical data with timedeltaindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.timedeltas`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'Group_obj': 'A'}, index=pd.to_timedelta(list(range(20)), unit='s'))
```

### Step 2: Assign unknown = unknown.astype(...)

```python
df['Group'] = df['Group_obj'].astype('category')
```

### Step 3: Assign result = df.resample.agg(...)

```python
result = df.resample('10s').agg(lambda x: x.value_counts().index[0])
```

### Step 4: Assign exp_tdi = pd.TimedeltaIndex.as_unit(...)

```python
exp_tdi = pd.TimedeltaIndex(np.array([0, 10], dtype='m8[s]'), freq='10s').as_unit('ns')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Group_obj': ['A', 'A'], 'Group': ['A', 'A']}, index=exp_tdi)
```

### Step 6: Assign expected = expected.reindex(...)

```python
expected = expected.reindex(['Group_obj', 'Group'], axis=1)
```

### Step 7: Assign unknown = unknown.astype(...)

```python
expected['Group'] = expected['Group_obj'].astype('category')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'Group_obj': 'A'}, index=pd.to_timedelta(list(range(20)), unit='s'))
df['Group'] = df['Group_obj'].astype('category')
result = df.resample('10s').agg(lambda x: x.value_counts().index[0])
exp_tdi = pd.TimedeltaIndex(np.array([0, 10], dtype='m8[s]'), freq='10s').as_unit('ns')
expected = DataFrame({'Group_obj': ['A', 'A'], 'Group': ['A', 'A']}, index=exp_tdi)
expected = expected.reindex(['Group_obj', 'Group'], axis=1)
expected['Group'] = expected['Group_obj'].astype('category')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta.py:98 | Complexity: Advanced | Last updated: 2026-06-02*