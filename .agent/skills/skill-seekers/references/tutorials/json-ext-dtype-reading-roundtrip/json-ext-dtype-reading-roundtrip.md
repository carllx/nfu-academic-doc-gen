# How To: Json Ext Dtype Reading Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test json ext dtype reading roundtrip

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `io`
- `json`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`
- `pandas.core.arrays.string_`
- `pandas.core.series`
- `pandas.tests.extension.date`
- `pandas.tests.extension.decimal.array`
- `pandas.io.json._table_schema`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([2, NA], dtype='Int64'), 'b': Series([1.5, NA], dtype='Float64'), 'c': Series([True, NA], dtype='boolean')}, index=Index([1, NA], dtype='Int64'))
```

### Step 2: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 3: Assign data_json = df.to_json(...)

```python
data_json = df.to_json(orient='table', indent=4)
```

### Step 4: Assign result = read_json(...)

```python
result = read_json(StringIO(data_json), orient='table')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': Series([2, NA], dtype='Int64'), 'b': Series([1.5, NA], dtype='Float64'), 'c': Series([True, NA], dtype='boolean')}, index=Index([1, NA], dtype='Int64'))
expected = df.copy()
data_json = df.to_json(orient='table', indent=4)
result = read_json(StringIO(data_json), orient='table')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_json_table_schema_ext_dtype.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*