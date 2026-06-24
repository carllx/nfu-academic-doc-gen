# How To: Memory Map

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memory map

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

### Step 1: Assign mmap_file = os.path.join(...)

```python
mmap_file = os.path.join(csv_dir_path, 'test_mmap.csv')
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'b': ['one', 'two', 'three'], 'c': ['I', 'II', 'III']})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(mmap_file, memory_map=True)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(mmap_file, memory_map=True)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv_dir_path

# Workflow
mmap_file = os.path.join(csv_dir_path, 'test_mmap.csv')
parser = all_parsers
expected = DataFrame({'a': [1, 2, 3], 'b': ['one', 'two', 'three'], 'c': ['I', 'II', 'III']})
if parser.engine == 'pyarrow':
    msg = "The 'memory_map' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(mmap_file, memory_map=True)
    return
result = parser.read_csv(mmap_file, memory_map=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_file_buffer_url.py:463 | Complexity: Intermediate | Last updated: 2026-06-02*