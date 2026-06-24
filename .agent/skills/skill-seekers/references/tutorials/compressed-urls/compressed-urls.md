# How To: Compressed Urls

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compressed urls

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `logging`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.feather_format`
- `pandas.io.parsers`
- `botocore`
- `botocore`

**Setup Required:**
```python
# Fixtures: httpserver, datapath, salaries_table, mode, engine, compression_only, compression_to_extension
```

## Step-by-Step Guide

### Step 1: Assign extension = value

```python
extension = compression_to_extension[compression_only]
```

### Step 2: Assign url = value

```python
url = httpserver.url + '/salaries.csv' + extension
```

### Step 3: Assign url_table = read_csv(...)

```python
url_table = read_csv(url, sep='\t', compression=compression_only, engine=engine)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(url_table, salaries_table)
```

### Step 5: Call pytest.skip()

```python
pytest.skip('TODO: Add tar salaraies.csv to pandas/io/parsers/data')
```

### Step 6: Call httpserver.serve_content()

```python
httpserver.serve_content(content=f.read())
```

### Step 7: Assign compression_only = mode

```python
compression_only = mode
```


## Complete Example

```python
# Setup
# Fixtures: httpserver, datapath, salaries_table, mode, engine, compression_only, compression_to_extension

# Workflow
if compression_only == 'tar':
    pytest.skip('TODO: Add tar salaraies.csv to pandas/io/parsers/data')
extension = compression_to_extension[compression_only]
with open(datapath('io', 'parser', 'data', 'salaries.csv' + extension), 'rb') as f:
    httpserver.serve_content(content=f.read())
url = httpserver.url + '/salaries.csv' + extension
if mode != 'explicit':
    compression_only = mode
url_table = read_csv(url, sep='\t', compression=compression_only, engine=engine)
tm.assert_frame_equal(url_table, salaries_table)
```

## Next Steps


---

*Source: test_network.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*