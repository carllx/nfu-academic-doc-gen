# How To: Downloader Redownload

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Test that a second download correctly triggers the 'already up-to-date' message

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `unittest.mock`
- `nltk`
- `nltk.downloader`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: "Test that a second download correctly triggers the 'already up-to-date' message"

```python
"Test that a second download correctly triggers the 'already up-to-date' message"
```

**Verification:**
```python
assert download_status is True
```

### Step 2: Assign first_download = 0

```python
first_download = 0
```

**Verification:**
```python
assert print_mock.call_args_list[1].args == expected_second_call.args
```

### Step 3: Assign second_download = 1

```python
second_download = 1
```

**Verification:**
```python
assert print_mock.call_args_list[1].args == expected_second_call.args
```

### Step 4: Assign download_dir = str(...)

```python
download_dir = str(tmp_path.joinpath('test_repeat_download'))
```

### Step 5: Assign download_status = download(...)

```python
download_status = download('stopwords', download_dir)
```

**Verification:**
```python
assert download_status is True
```

### Step 6: Assign expected_second_call = unittest.mock.call(...)

```python
expected_second_call = unittest.mock.call('[nltk_data]   Unzipping %s.' % os.path.join('corpora', 'stopwords.zip'))
```

**Verification:**
```python
assert print_mock.call_args_list[1].args == expected_second_call.args
```

### Step 7: Assign expected_second_call = unittest.mock.call(...)

```python
expected_second_call = unittest.mock.call('[nltk_data]   Package stopwords is already up-to-date!')
```

**Verification:**
```python
assert print_mock.call_args_list[1].args == expected_second_call.args
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
"Test that a second download correctly triggers the 'already up-to-date' message"
first_download = 0
second_download = 1
download_dir = str(tmp_path.joinpath('test_repeat_download'))
for i in range(first_download, second_download + 1):
    with unittest.mock.patch('builtins.print') as print_mock:
        download_status = download('stopwords', download_dir)
        assert download_status is True
        if i == first_download:
            expected_second_call = unittest.mock.call('[nltk_data]   Unzipping %s.' % os.path.join('corpora', 'stopwords.zip'))
            assert print_mock.call_args_list[1].args == expected_second_call.args
        elif i == second_download:
            expected_second_call = unittest.mock.call('[nltk_data]   Package stopwords is already up-to-date!')
            assert print_mock.call_args_list[1].args == expected_second_call.args
```

## Next Steps


---

*Source: test_downloader.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*