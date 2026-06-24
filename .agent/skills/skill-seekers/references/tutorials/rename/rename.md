# How To: Rename

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign ts = datetime_series

```python
ts = datetime_series
```

**Verification:**
```python
assert renamed.index[0] == renamer(ts.index[0])
```

### Step 2: Assign renamer = value

```python
renamer = lambda x: x.strftime('%Y%m%d')
```

### Step 3: Assign renamed = ts.rename(...)

```python
renamed = ts.rename(renamer)
```

**Verification:**
```python
assert renamed.index[0] == renamer(ts.index[0])
```

### Step 4: Assign rename_dict = dict(...)

```python
rename_dict = dict(zip(ts.index, renamed.index))
```

### Step 5: Assign renamed2 = ts.rename(...)

```python
renamed2 = ts.rename(rename_dict)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(renamed, renamed2)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
ts = datetime_series
renamer = lambda x: x.strftime('%Y%m%d')
renamed = ts.rename(renamer)
assert renamed.index[0] == renamer(ts.index[0])
rename_dict = dict(zip(ts.index, renamed.index))
renamed2 = ts.rename(rename_dict)
tm.assert_series_equal(renamed, renamed2)
```

## Next Steps


---

*Source: test_rename.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*