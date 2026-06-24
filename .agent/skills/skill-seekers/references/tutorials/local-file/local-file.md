# How To: Local File

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test local file

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `platform`
- `urllib.error`
- `uuid`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, csv_dir_path
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign kwargs = value

```python
kwargs = {'sep': '\t'}
```

### Step 3: Assign local_path = os.path.join(...)

```python
local_path = os.path.join(csv_dir_path, 'salaries.csv')
```

### Step 4: Assign local_result = parser.read_csv(...)

```python
local_result = parser.read_csv(local_path, **kwargs)
```

### Step 5: Assign url = value

```python
url = 'file://localhost/' + local_path
```

### Step 6: Assign url_result = parser.read_csv(...)

```python
url_result = parser.read_csv(url, **kwargs)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(url_result, local_result)
```

### Step 8: Call pytest.skip()

```python
pytest.skip('Failing on: ' + ' '.join(platform.uname()))
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv_dir_path

# Workflow
parser = all_parsers
kwargs = {'sep': '\t'}
local_path = os.path.join(csv_dir_path, 'salaries.csv')
local_result = parser.read_csv(local_path, **kwargs)
url = 'file://localhost/' + local_path
try:
    url_result = parser.read_csv(url, **kwargs)
    tm.assert_frame_equal(url_result, local_result)
except URLError:
    pytest.skip('Failing on: ' + ' '.join(platform.uname()))
```

## Next Steps


---

*Source: test_file_buffer_url.py:54 | Complexity: Advanced | Last updated: 2026-06-02*