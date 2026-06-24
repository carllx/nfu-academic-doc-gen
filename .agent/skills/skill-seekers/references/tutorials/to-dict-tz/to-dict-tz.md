# How To: To Dict Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to dict tz

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [(datetime(2017, 11, 18, 21, 53, 0, 219225, tzinfo=pytz.utc),), (datetime(2017, 11, 18, 22, 6, 30, 61810, tzinfo=pytz.utc),)]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(list(data), columns=['d'])
```

### Step 3: Assign result = df.to_dict(...)

```python
result = df.to_dict(orient='records')
```

### Step 4: Assign expected = value

```python
expected = [{'d': Timestamp('2017-11-18 21:53:00.219225+0000', tz=pytz.utc)}, {'d': Timestamp('2017-11-18 22:06:30.061810+0000', tz=pytz.utc)}]
```

### Step 5: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result[0], expected[0])
```

### Step 6: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result[1], expected[1])
```


## Complete Example

```python
# Workflow
data = [(datetime(2017, 11, 18, 21, 53, 0, 219225, tzinfo=pytz.utc),), (datetime(2017, 11, 18, 22, 6, 30, 61810, tzinfo=pytz.utc),)]
df = DataFrame(list(data), columns=['d'])
result = df.to_dict(orient='records')
expected = [{'d': Timestamp('2017-11-18 21:53:00.219225+0000', tz=pytz.utc)}, {'d': Timestamp('2017-11-18 22:06:30.061810+0000', tz=pytz.utc)}]
tm.assert_dict_equal(result[0], expected[0])
tm.assert_dict_equal(result[1], expected[1])
```

## Next Steps


---

*Source: test_to_dict.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*