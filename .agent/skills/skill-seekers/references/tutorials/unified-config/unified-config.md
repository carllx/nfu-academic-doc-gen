# How To: Unified Config

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Create a sample unified config file.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `unittest.mock`
- `pytest`
- `mcp.server`
- `mcp.types`
- `skill_seekers.mcp`

**Setup Required:**
```python
# Fixtures: temp_dirs
```

## Step-by-Step Guide

### Step 1: Assign config_data = value

```python
config_data = {'name': 'test-unified', 'description': 'Test unified scraping', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/docs/', 'extract_api': True, 'max_pages': 10}, {'type': 'github', 'repo': 'test/repo', 'extract_readme': True}]}
```


## Complete Example

```python
# Setup
# Fixtures: temp_dirs

# Workflow
config_data = {'name': 'test-unified', 'description': 'Test unified scraping', 'merge_mode': 'rule-based', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/docs/', 'extract_api': True, 'max_pages': 10}, {'type': 'github', 'repo': 'test/repo', 'extract_readme': True}]}
```

## Next Steps


---

*Source: test_mcp_fastmcp.py:93 | Complexity: Beginner | Last updated: 2026-06-02*