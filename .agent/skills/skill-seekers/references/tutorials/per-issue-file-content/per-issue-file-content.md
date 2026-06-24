# How To: Per Issue File Content

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Per-issue file contains full body and YAML frontmatter.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `datetime`
- `pathlib`
- `unittest.mock`
- `github`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`

**Setup Required:**
```python
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()
```

## Step-by-Step Guide

### Step 1: 'Per-issue file contains full body and YAML frontmatter.'

```python
'Per-issue file contains full body and YAML frontmatter.'
```

### Step 2: Assign issues = value

```python
issues = [{'number': 99, 'title': 'Feature request', 'state': 'open', 'labels': ['enhancement'], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/repo/issues/99', 'body': 'Please add dark mode support', 'comments': []}]
```

### Step 3: Assign converter = self._setup_converter(...)

```python
converter = self._setup_converter(issues)
```

### Step 4: Call converter._generate_issues_reference()

```python
converter._generate_issues_reference()
```

### Step 5: Assign filepath = os.path.join(...)

```python
filepath = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-99.md')
```

### Step 6: Assign content = Path.read_text(...)

```python
content = Path(filepath).read_text()
```

### Step 7: Call self.assertTrue()

```python
self.assertTrue(content.startswith('---'))
```

### Step 8: Call self.assertIn()

```python
self.assertIn('type: github_issue', content)
```

### Step 9: Call self.assertIn()

```python
self.assertIn('issue_number: 99', content)
```

### Step 10: Call self.assertIn()

```python
self.assertIn('state: open', content)
```

### Step 11: Call self.assertIn()

```python
self.assertIn('Please add dark mode support', content)
```


## Complete Example

```python
# Setup
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()

# Workflow
'Per-issue file contains full body and YAML frontmatter.'
issues = [{'number': 99, 'title': 'Feature request', 'state': 'open', 'labels': ['enhancement'], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/repo/issues/99', 'body': 'Please add dark mode support', 'comments': []}]
converter = self._setup_converter(issues)
converter._generate_issues_reference()
filepath = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-99.md')
content = Path(filepath).read_text()
self.assertTrue(content.startswith('---'))
self.assertIn('type: github_issue', content)
self.assertIn('issue_number: 99', content)
self.assertIn('state: open', content)
self.assertIn('Please add dark mode support', content)
```

## Next Steps


---

*Source: test_github_scraper.py:1440 | Complexity: Advanced | Last updated: 2026-06-02*