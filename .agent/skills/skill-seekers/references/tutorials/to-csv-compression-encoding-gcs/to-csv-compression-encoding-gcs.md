# How To: To Csv Compression Encoding Gcs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Compression and encoding should with GCS.

GH 35677 (to_csv, compression), GH 26124 (to_csv, encoding), and
GH 32392 (read_csv, encoding)

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `pathlib`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.util`
- `fsspec`

**Setup Required:**
```python
# Fixtures: gcs_buffer, compression_only, encoding, compression_to_extension
```

## Step-by-Step Guide

### Step 1: '\n    Compression and encoding should with GCS.\n\n    GH 35677 (to_csv, compression), GH 26124 (to_csv, encoding), and\n    GH 32392 (read_csv, encoding)\n    '

```python
'\n    Compression and encoding should with GCS.\n\n    GH 35677 (to_csv, compression), GH 26124 (to_csv, encoding), and\n    GH 32392 (read_csv, encoding)\n    '
```

**Verification:**
```python
assert_equal_zip_safe(res, expected, compression_only)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
```

**Verification:**
```python
assert_equal_zip_safe(res, expected, compression_only)
```

### Step 3: Assign compression = value

```python
compression = {'method': compression_only}
```

### Step 4: Assign buffer = BytesIO(...)

```python
buffer = BytesIO()
```

### Step 5: Call df.to_csv()

```python
df.to_csv(buffer, compression=compression, encoding=encoding, mode='wb')
```

### Step 6: Assign path_gcs = 'gs://test/test.csv'

```python
path_gcs = 'gs://test/test.csv'
```

### Step 7: Call df.to_csv()

```python
df.to_csv(path_gcs, compression=compression, encoding=encoding)
```

### Step 8: Assign res = gcs_buffer.getvalue(...)

```python
res = gcs_buffer.getvalue()
```

### Step 9: Assign expected = buffer.getvalue(...)

```python
expected = buffer.getvalue()
```

### Step 10: Call assert_equal_zip_safe()

```python
assert_equal_zip_safe(res, expected, compression_only)
```

### Step 11: Assign read_df = read_csv(...)

```python
read_df = read_csv(path_gcs, index_col=0, compression=compression_only, encoding=encoding)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, read_df)
```

### Step 13: Assign file_ext = value

```python
file_ext = compression_to_extension[compression_only]
```

### Step 14: Assign unknown = 'infer'

```python
compression['method'] = 'infer'
```

### Step 15: Call df.to_csv()

```python
df.to_csv(path_gcs, compression=compression, encoding=encoding)
```

### Step 16: Assign res = gcs_buffer.getvalue(...)

```python
res = gcs_buffer.getvalue()
```

### Step 17: Assign expected = buffer.getvalue(...)

```python
expected = buffer.getvalue()
```

### Step 18: Call assert_equal_zip_safe()

```python
assert_equal_zip_safe(res, expected, compression_only)
```

### Step 19: Assign read_df = read_csv(...)

```python
read_df = read_csv(path_gcs, index_col=0, compression='infer', encoding=encoding)
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, read_df)
```

### Step 21: Assign unknown = 1

```python
compression['mtime'] = 1
```


## Complete Example

```python
# Setup
# Fixtures: gcs_buffer, compression_only, encoding, compression_to_extension

# Workflow
'\n    Compression and encoding should with GCS.\n\n    GH 35677 (to_csv, compression), GH 26124 (to_csv, encoding), and\n    GH 32392 (read_csv, encoding)\n    '
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(30)]))
compression = {'method': compression_only}
if compression_only == 'gzip':
    compression['mtime'] = 1
buffer = BytesIO()
df.to_csv(buffer, compression=compression, encoding=encoding, mode='wb')
path_gcs = 'gs://test/test.csv'
df.to_csv(path_gcs, compression=compression, encoding=encoding)
res = gcs_buffer.getvalue()
expected = buffer.getvalue()
assert_equal_zip_safe(res, expected, compression_only)
read_df = read_csv(path_gcs, index_col=0, compression=compression_only, encoding=encoding)
tm.assert_frame_equal(df, read_df)
file_ext = compression_to_extension[compression_only]
compression['method'] = 'infer'
path_gcs += f'.{file_ext}'
df.to_csv(path_gcs, compression=compression, encoding=encoding)
res = gcs_buffer.getvalue()
expected = buffer.getvalue()
assert_equal_zip_safe(res, expected, compression_only)
read_df = read_csv(path_gcs, index_col=0, compression='infer', encoding=encoding)
tm.assert_frame_equal(df, read_df)
```

## Next Steps


---

*Source: test_gcs.py:149 | Complexity: Advanced | Last updated: 2026-06-02*