# How To: Styler To S3

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test styler to s3

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `time`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.formats.excel`

**Setup Required:**
```python
# Fixtures: s3_public_bucket, s3so
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
mock_bucket_name, target_file = (s3_public_bucket.name, 'test.xlsx')
```

**Verification:**
```python
assert timeout > 0, 'Timed out waiting for file to appear on moto'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 2, 3], 'y': [2, 4, 6]})
```

### Step 3: Assign styler = df.style.set_sticky(...)

```python
styler = df.style.set_sticky(axis='index')
```

### Step 4: Call styler.to_excel()

```python
styler.to_excel(f's3://{mock_bucket_name}/{target_file}', storage_options=s3so)
```

### Step 5: Assign timeout = 5

```python
timeout = 5
```

### Step 6: Call time.sleep()

```python
time.sleep(0.1)
```

**Verification:**
```python
assert timeout > 0, 'Timed out waiting for file to appear on moto'
```

### Step 7: Assign result = read_excel(...)

```python
result = read_excel(f's3://{mock_bucket_name}/{target_file}', index_col=0, storage_options=s3so)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: s3_public_bucket, s3so

# Workflow
mock_bucket_name, target_file = (s3_public_bucket.name, 'test.xlsx')
df = DataFrame({'x': [1, 2, 3], 'y': [2, 4, 6]})
styler = df.style.set_sticky(axis='index')
styler.to_excel(f's3://{mock_bucket_name}/{target_file}', storage_options=s3so)
timeout = 5
while True:
    if target_file in (obj.key for obj in s3_public_bucket.objects.all()):
        break
    time.sleep(0.1)
    timeout -= 0.1
    assert timeout > 0, 'Timed out waiting for file to appear on moto'
    result = read_excel(f's3://{mock_bucket_name}/{target_file}', index_col=0, storage_options=s3so)
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_style.py:281 | Complexity: Advanced | Last updated: 2026-06-02*