# How To: From Records Non Tuple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records non tuple

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign recs = value

```python
recs = [Record(1, 2, 3), Record(4, 5, 6), Record(7, 8, 9)]
```

### Step 2: Assign tups = value

```python
tups = [tuple(rec) for rec in recs]
```

### Step 3: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records(recs)
```

### Step 4: Assign expected = DataFrame.from_records(...)

```python
expected = DataFrame.from_records(tups)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign self.args = args

```python
self.args = args
```


## Complete Example

```python
# Workflow
class Record:

    def __init__(self, *args) -> None:
        self.args = args

    def __getitem__(self, i):
        return self.args[i]

    def __iter__(self) -> Iterator:
        return iter(self.args)
recs = [Record(1, 2, 3), Record(4, 5, 6), Record(7, 8, 9)]
tups = [tuple(rec) for rec in recs]
result = DataFrame.from_records(recs)
expected = DataFrame.from_records(tups)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_records.py:233 | Complexity: Intermediate | Last updated: 2026-06-02*