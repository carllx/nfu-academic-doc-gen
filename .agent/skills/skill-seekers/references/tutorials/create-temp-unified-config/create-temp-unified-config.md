# How To: Create Temp Unified Config

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Configuration example: Test creating a unified config from scratch

## Prerequisites

**Required Modules:**
- `json`
- `os`
- `sys`
- `tempfile`
- `pathlib`
- `config_validator`
- `traceback`


## Step-by-Step Guide

### Step 1: Assign config = value

```python
config = {'name': 'test_unified', 'description': 'Test unified config', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/docs', 'extract_api': True, 'max_pages': 50}, {'type': 'github', 'repo': 'test/repo', 'include_code': True, 'code_analysis_depth': 'surface'}]}
```


## Complete Example

```python
# Workflow
config = {'name': 'test_unified', 'description': 'Test unified config', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/docs', 'extract_api': True, 'max_pages': 50}, {'type': 'github', 'repo': 'test/repo', 'include_code': True, 'code_analysis_depth': 'surface'}]}
```

## Next Steps


---

*Source: test_unified_simple.py:59 | Complexity: Beginner | Last updated: 2026-06-02*