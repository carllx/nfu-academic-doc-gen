# How To: Select Dtypes Datetime With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes datetime with tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': Timestamp('20130102', tz='US/Eastern'), 'B': Timestamp('20130603', tz='CET')}, index=range(5))
```

### Step 2: Assign df3 = pd.concat(...)

```python
df3 = pd.concat([df2.A.to_frame(), df2.B.to_frame()], axis=1)
```

### Step 3: Assign result = df3.select_dtypes(...)

```python
result = df3.select_dtypes(include=['datetime64[ns]'])
```

### Step 4: Assign expected = df3.reindex(...)

```python
expected = df3.reindex(columns=[])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df2 = DataFrame({'A': Timestamp('20130102', tz='US/Eastern'), 'B': Timestamp('20130603', tz='CET')}, index=range(5))
df3 = pd.concat([df2.A.to_frame(), df2.B.to_frame()], axis=1)
result = df3.select_dtypes(include=['datetime64[ns]'])
expected = df3.reindex(columns=[])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_select_dtypes.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*