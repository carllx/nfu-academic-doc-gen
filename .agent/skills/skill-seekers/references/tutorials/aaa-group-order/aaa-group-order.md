# How To: Aaa Group Order

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aaa group order

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign n = 20

```python
n = 20
```

### Step 2: Assign data = np.random.default_rng.standard_normal(...)

```python
data = np.random.default_rng(2).standard_normal((n, 4))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
```

### Step 4: Assign unknown = value

```python
df['key'] = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4
```

### Step 5: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(Grouper(key='key', freq='D'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 1)), df[::5])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 2)), df[1::5])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 3)), df[2::5])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 4)), df[3::5])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 5)), df[4::5])
```


## Complete Example

```python
# Workflow
n = 20
data = np.random.default_rng(2).standard_normal((n, 4))
df = DataFrame(data, columns=['A', 'B', 'C', 'D'])
df['key'] = [datetime(2013, 1, 1), datetime(2013, 1, 2), datetime(2013, 1, 3), datetime(2013, 1, 4), datetime(2013, 1, 5)] * 4
grouped = df.groupby(Grouper(key='key', freq='D'))
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 1)), df[::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 2)), df[1::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 3)), df[2::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 4)), df[3::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 5)), df[4::5])
```

## Next Steps


---

*Source: test_time_grouper.py:110 | Complexity: Advanced | Last updated: 2026-06-02*