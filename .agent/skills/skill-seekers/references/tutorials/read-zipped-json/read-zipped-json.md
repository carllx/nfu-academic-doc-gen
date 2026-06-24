# How To: Read Zipped Json

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read zipped json

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign uncompressed_path = datapath(...)

```python
uncompressed_path = datapath('io', 'json', 'data', 'tsframe_v012.json')
```

### Step 2: Assign uncompressed_df = pd.read_json(...)

```python
uncompressed_df = pd.read_json(uncompressed_path)
```

### Step 3: Assign compressed_path = datapath(...)

```python
compressed_path = datapath('io', 'json', 'data', 'tsframe_v012.json.zip')
```

### Step 4: Assign compressed_df = pd.read_json(...)

```python
compressed_df = pd.read_json(compressed_path, compression='zip')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(uncompressed_df, compressed_df)
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
uncompressed_path = datapath('io', 'json', 'data', 'tsframe_v012.json')
uncompressed_df = pd.read_json(uncompressed_path)
compressed_path = datapath('io', 'json', 'data', 'tsframe_v012.json.zip')
compressed_df = pd.read_json(compressed_path, compression='zip')
tm.assert_frame_equal(uncompressed_df, compressed_df)
```

## Next Steps


---

*Source: test_compression.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*