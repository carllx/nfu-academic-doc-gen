# How To: Llms Txt Url Forwarded To Doc Config

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: llms_txt_url from source is forwarded to the doc config.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.unified_scraper`
- `argparse`
- `argparse`
- `contextlib`
- `skill_seekers.cli.unified_scraper`
- `skill_seekers.cli.workflow_runner`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'llms_txt_url from source is forwarded to the doc config.'

```python
'llms_txt_url from source is forwarded to the doc config.'
```

**Verification:**
```python
assert any(('llms_txt_url' in s for s in sources))
```

### Step 2: Assign scraper = _make_scraper(...)

```python
scraper = _make_scraper(tmp_path=tmp_path)
```

### Step 3: Assign source = value

```python
source = {'base_url': 'https://docs.example.com/', 'type': 'documentation', 'llms_txt_url': 'https://docs.example.com/llms.txt'}
```

### Step 4: Assign captured_config = value

```python
captured_config = {}
```

### Step 5: Assign sources = captured_config.get(...)

```python
sources = captured_config.get('sources', [])
```

**Verification:**
```python
assert any(('llms_txt_url' in s for s in sources))
```

### Step 6: Call captured_config.update()

```python
captured_config.update(config)
```

### Step 7: Call scraper._scrape_documentation()

```python
scraper._scrape_documentation(source)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'llms_txt_url from source is forwarded to the doc config.'
scraper = _make_scraper(tmp_path=tmp_path)
source = {'base_url': 'https://docs.example.com/', 'type': 'documentation', 'llms_txt_url': 'https://docs.example.com/llms.txt'}
captured_config = {}

def fake_scrape(config, ctx=None):
    captured_config.update(config)
    return 1
with patch('skill_seekers.cli.doc_scraper.scrape_documentation', side_effect=fake_scrape):
    scraper._scrape_documentation(source)
sources = captured_config.get('sources', [])
assert any(('llms_txt_url' in s for s in sources))
```

## Next Steps


---

*Source: test_unified_scraper_orchestration.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*