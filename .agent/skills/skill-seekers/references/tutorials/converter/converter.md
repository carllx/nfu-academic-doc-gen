# How To: Converter

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: Create a converter with tmp output directory.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `logging`
- `os`
- `pytest`
- `skill_seekers.cli.doc_scraper`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign config = value

```python
config = {'name': 'test-site', 'base_url': 'https://example.com', 'selectors': {'title': 'title', 'code_blocks': 'pre code'}, 'url_patterns': {'include': [], 'exclude': []}, 'rate_limit': 0, 'max_pages': 100}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
config = {'name': 'test-site', 'base_url': 'https://example.com', 'selectors': {'title': 'title', 'code_blocks': 'pre code'}, 'url_patterns': {'include': [], 'exclude': []}, 'rate_limit': 0, 'max_pages': 100}
```

## Next Steps


---

*Source: test_scrape_count.py:14 | Complexity: Beginner | Last updated: 2026-06-02*