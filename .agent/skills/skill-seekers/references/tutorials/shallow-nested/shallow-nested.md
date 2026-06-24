# How To: Shallow Nested

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shallow nested

## Prerequisites

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [{'state': 'Florida', 'shortname': 'FL', 'info': {'governor': 'Rick Scott'}, 'counties': [{'name': 'Dade', 'population': 12345}, {'name': 'Broward', 'population': 40000}, {'name': 'Palm Beach', 'population': 60000}]}, {'state': 'Ohio', 'shortname': 'OH', 'info': {'governor': 'John Kasich'}, 'counties': [{'name': 'Summit', 'population': 1234}, {'name': 'Cuyahoga', 'population': 1337}]}]
```

### Step 2: Assign result = json_normalize(...)

```python
result = json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
```

### Step 3: Assign ex_data = value

```python
ex_data = {'name': ['Dade', 'Broward', 'Palm Beach', 'Summit', 'Cuyahoga'], 'state': ['Florida'] * 3 + ['Ohio'] * 2, 'shortname': ['FL', 'FL', 'FL', 'OH', 'OH'], 'info.governor': ['Rick Scott'] * 3 + ['John Kasich'] * 2, 'population': [12345, 40000, 60000, 1234, 1337]}
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(ex_data, columns=result.columns)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [{'state': 'Florida', 'shortname': 'FL', 'info': {'governor': 'Rick Scott'}, 'counties': [{'name': 'Dade', 'population': 12345}, {'name': 'Broward', 'population': 40000}, {'name': 'Palm Beach', 'population': 60000}]}, {'state': 'Ohio', 'shortname': 'OH', 'info': {'governor': 'John Kasich'}, 'counties': [{'name': 'Summit', 'population': 1234}, {'name': 'Cuyahoga', 'population': 1337}]}]
result = json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
ex_data = {'name': ['Dade', 'Broward', 'Palm Beach', 'Summit', 'Cuyahoga'], 'state': ['Florida'] * 3 + ['Ohio'] * 2, 'shortname': ['FL', 'FL', 'FL', 'OH', 'OH'], 'info.governor': ['Rick Scott'] * 3 + ['John Kasich'] * 2, 'population': [12345, 40000, 60000, 1234, 1337]}
expected = DataFrame(ex_data, columns=result.columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:296 | Complexity: Intermediate | Last updated: 2026-06-02*