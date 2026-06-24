# How To: Readjson Lines Chunks Fileurl

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test readjson lines chunks fileurl

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json._json`

**Setup Required:**
```python
# Fixtures: request, datapath, engine
```

## Step-by-Step Guide

### Step 1: Assign df_list_expected = value

```python
df_list_expected = [DataFrame([[1, 2]], columns=['a', 'b'], index=[0]), DataFrame([[3, 4]], columns=['a', 'b'], index=[1]), DataFrame([[5, 6]], columns=['a', 'b'], index=[2])]
```

### Step 2: Assign os_path = datapath(...)

```python
os_path = datapath('io', 'json', 'data', 'line_delimited.json')
```

### Step 3: Assign file_url = Path.as_uri(...)

```python
file_url = Path(os_path).as_uri()
```

### Step 4: Assign reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."

```python
reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
```

### Step 5: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chuck, df_list_expected[index])
```


## Complete Example

```python
# Setup
# Fixtures: request, datapath, engine

# Workflow
if engine == 'pyarrow':
    reason = "Pyarrow only supports a file path as an input and line delimited jsonand doesn't support chunksize parameter."
    request.applymarker(pytest.mark.xfail(reason=reason, raises=ValueError))
df_list_expected = [DataFrame([[1, 2]], columns=['a', 'b'], index=[0]), DataFrame([[3, 4]], columns=['a', 'b'], index=[1]), DataFrame([[5, 6]], columns=['a', 'b'], index=[2])]
os_path = datapath('io', 'json', 'data', 'line_delimited.json')
file_url = Path(os_path).as_uri()
with read_json(file_url, lines=True, chunksize=1, engine=engine) as url_reader:
    for index, chuck in enumerate(url_reader):
        tm.assert_frame_equal(chuck, df_list_expected[index])
```

## Next Steps


---

*Source: test_readlines.py:356 | Complexity: Intermediate | Last updated: 2026-06-02*