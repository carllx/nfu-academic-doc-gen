# How To: Single Docs Source Creates Top Level Compatibility References

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Docs-only unified skills should expose flat references for easier browsing and scoring.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `skill_seekers.cli.unified_scraper`
- `skill_seekers.cli.unified_scraper`
- `skill_seekers.cli.unified_scraper`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `skill_seekers.cli.unified_skill_builder`
- `re`

**Setup Required:**
```python
'Set up test fixtures.'
self.temp_dir = tempfile.mkdtemp()
self.original_dir = os.getcwd()
os.chdir(self.temp_dir)
```

## Step-by-Step Guide

### Step 1: 'Docs-only unified skills should expose flat references for easier browsing and scoring.'

```python
'Docs-only unified skills should expose flat references for easier browsing and scoring.'
```

### Step 2: Assign refs_dir = os.path.join(...)

```python
refs_dir = os.path.join(self.temp_dir, 'refs')
```

### Step 3: Call os.makedirs()

```python
os.makedirs(refs_dir)
```

### Step 4: Assign config = value

```python
config = {'name': 'docs_only_skill', 'description': 'Test', 'sources': []}
```

### Step 5: Assign scraped_data = value

```python
scraped_data = {'documentation': [{'source_id': 'docs_source', 'base_url': 'https://docs.example.com', 'total_pages': 2, 'refs_dir': refs_dir}], 'github': [], 'pdf': []}
```

### Step 6: Assign builder = UnifiedSkillBuilder(...)

```python
builder = UnifiedSkillBuilder(config, scraped_data)
```

### Step 7: Call builder._generate_docs_references()

```python
builder._generate_docs_references(scraped_data['documentation'])
```

### Step 8: Assign top_level_refs = os.path.join(...)

```python
top_level_refs = os.path.join(builder.skill_dir, 'references')
```

### Step 9: Call self.assertTrue()

```python
self.assertTrue(os.path.exists(os.path.join(top_level_refs, 'api.md')))
```

### Step 10: Call self.assertTrue()

```python
self.assertTrue(os.path.exists(os.path.join(top_level_refs, 'getting_started.md')))
```

### Step 11: Call f.write()

```python
f.write('# API Reference')
```

### Step 12: Call f.write()

```python
f.write('# Getting Started')
```


## Complete Example

```python
# Setup
'Set up test fixtures.'
self.temp_dir = tempfile.mkdtemp()
self.original_dir = os.getcwd()
os.chdir(self.temp_dir)

# Workflow
'Docs-only unified skills should expose flat references for easier browsing and scoring.'
from skill_seekers.cli.unified_skill_builder import UnifiedSkillBuilder
refs_dir = os.path.join(self.temp_dir, 'refs')
os.makedirs(refs_dir)
with open(os.path.join(refs_dir, 'api.md'), 'w') as f:
    f.write('# API Reference')
with open(os.path.join(refs_dir, 'getting_started.md'), 'w') as f:
    f.write('# Getting Started')
config = {'name': 'docs_only_skill', 'description': 'Test', 'sources': []}
scraped_data = {'documentation': [{'source_id': 'docs_source', 'base_url': 'https://docs.example.com', 'total_pages': 2, 'refs_dir': refs_dir}], 'github': [], 'pdf': []}
builder = UnifiedSkillBuilder(config, scraped_data)
builder._generate_docs_references(scraped_data['documentation'])
top_level_refs = os.path.join(builder.skill_dir, 'references')
self.assertTrue(os.path.exists(os.path.join(top_level_refs, 'api.md')))
self.assertTrue(os.path.exists(os.path.join(top_level_refs, 'getting_started.md')))
```

## Next Steps


---

*Source: test_multi_source.py:253 | Complexity: Advanced | Last updated: 2026-06-02*