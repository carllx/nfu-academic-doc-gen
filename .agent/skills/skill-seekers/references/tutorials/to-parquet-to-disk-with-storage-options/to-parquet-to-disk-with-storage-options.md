# How To: To Parquet To Disk With Storage Options

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: test to parquet to disk with storage options

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `gzip`
- `io`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `fsspec`

**Setup Required:**
```python
# Fixtures: engine
```

## Step-by-Step Guide

### Step 1: Assign headers = value

```python
headers = {'User-Agent': 'custom', 'Auth': 'other_custom'}
```


## Complete Example

```python
# Setup
# Fixtures: engine

# Workflow
headers = {'User-Agent': 'custom', 'Auth': 'other_custom'}
```

## Next Steps


---

*Source: test_http_headers.py:162 | Complexity: Beginner | Last updated: 2026-06-02*