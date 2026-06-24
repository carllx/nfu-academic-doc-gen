# How To: Sample Config

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Create a sample config file (unified format).

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
config_data = {'name': 'test-framework', 'description': 'Test framework for testing', 'sources': [{'type': 'documentation', 'base_url': 'https://test-framework.dev/', 'selectors': {'main_content': 'article', 'title': 'h1', 'code_blocks': 'pre'}, 'url_patterns': {'include': ['/docs/'], 'exclude': ['/blog/', '/search/']}, 'categories': {'getting_started': ['introduction', 'getting-started'], 'api': ['api', 'reference']}, 'rate_limit': 0.5, 'max_pages': 100}]}
```


## Complete Example

```python
# Setup
# Fixtures: temp_dirs

# Workflow
config_data = {'name': 'test-framework', 'description': 'Test framework for testing', 'sources': [{'type': 'documentation', 'base_url': 'https://test-framework.dev/', 'selectors': {'main_content': 'article', 'title': 'h1', 'code_blocks': 'pre'}, 'url_patterns': {'include': ['/docs/'], 'exclude': ['/blog/', '/search/']}, 'categories': {'getting_started': ['introduction', 'getting-started'], 'api': ['api', 'reference']}, 'rate_limit': 0.5, 'max_pages': 100}]}
```

## Next Steps


---

*Source: test_mcp_fastmcp.py:66 | Complexity: Beginner | Last updated: 2026-06-02*