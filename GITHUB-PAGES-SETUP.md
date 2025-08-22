# 🚀 GitHub Pages Setup Guide

This guide will help you set up GitHub Pages for your Murlix documentation website.

## 📋 Prerequisites

- GitHub repository with the documentation files
- Admin access to the repository
- Files pushed to the `main` branch

## ⚙️ Setup Steps

### Step 1: Enable GitHub Pages

1. **Go to your repository on GitHub**
   - Navigate to `https://github.com/manohar3000/murlix`

2. **Open Repository Settings**
   - Click the "Settings" tab (far right in the repository navigation)
   - You need admin access to see this tab

3. **Find Pages Settings**
   - Scroll down in the left sidebar
   - Click on "Pages" under the "Code and automation" section

### Step 2: Configure GitHub Pages

1. **Set Source to GitHub Actions**
   - In the "Source" dropdown, select **"GitHub Actions"**
   - This is crucial - don't select "Deploy from a branch"

2. **Save Configuration**
   - The page will automatically save your selection
   - You should see a message confirming the change

### Step 3: Set Repository Permissions

1. **Go to Actions Settings**
   - In the same Settings page, click "Actions" → "General" in the left sidebar

2. **Set Workflow Permissions**
   - Scroll down to "Workflow permissions"
   - Select **"Read and write permissions"**
   - Check **"Allow GitHub Actions to create and approve pull requests"**
   - Click "Save"

### Step 4: Trigger the Workflow

1. **Push to Main Branch**
   ```bash
   git add .
   git commit -m "Set up documentation with GitHub Pages"
   git push origin main
   ```

2. **Check Actions Tab**
   - Go to the "Actions" tab in your repository
   - You should see the "Deploy Documentation" workflow running

## 🎯 Expected Results

After successful setup:

- ✅ Workflow runs without errors
- ✅ Documentation builds successfully
- ✅ Site deploys to GitHub Pages
- ✅ Available at: `https://manohar3000.github.io/murlix`

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: "Pages not enabled" Error
**Solution:**
- Ensure you selected "GitHub Actions" as the source (not "Deploy from a branch")
- Wait a few minutes after changing settings
- Try pushing a new commit to trigger the workflow

#### Issue 2: "Permission denied" Error
**Solution:**
- Check workflow permissions in Settings → Actions → General
- Ensure "Read and write permissions" is selected
- Make sure you have admin access to the repository

#### Issue 3: "Workflow not found" Error
**Solution:**
- Ensure the workflow file is at `.github/workflows/docs.yml`
- Check that the file is in the `main` branch
- Verify the YAML syntax is correct

#### Issue 4: Build Fails
**Solution:**
- Check the Actions tab for detailed error logs
- Common issues:
  - Missing `requirements-docs.txt` file
  - Incorrect file paths in `mkdocs.yml`
  - Missing documentation files

### Manual Verification

1. **Check Workflow File Location**
   ```
   .github/
   └── workflows/
       └── docs.yml  ← Should be here
   ```

2. **Verify Required Files**
   ```
   ├── mkdocs.yml
   ├── requirements-docs.txt
   └── docs/
       ├── index.md
       └── [other documentation files]
   ```

3. **Test Locally First**
   ```bash
   python setup-docs.py
   # Choose option 1 to serve locally
   # Verify everything works at http://127.0.0.1:8000
   ```

## 🔄 Alternative Setup Methods

### Method 1: Using Repository Template
If you're creating a new repository:

1. Use this repository as a template
2. GitHub Pages settings will be inherited
3. Just push your changes to `main`

### Method 2: Manual Pages Configuration
If automatic enablement doesn't work:

1. Go to Settings → Pages
2. Source: "GitHub Actions"
3. No need to select a folder or branch
4. Save and push to main

### Method 3: Using GitHub CLI
```bash
# Enable Pages with GitHub CLI
gh api repos/:owner/:repo/pages \
  --method POST \
  --field source='{"branch":"main","path":"/"}'
```

## 📝 Workflow Configuration

The workflow is configured to:

- **Trigger on**: Push to `main` branch, changes to docs files, manual dispatch
- **Build with**: Python 3.11, latest MkDocs Material
- **Deploy to**: GitHub Pages automatically
- **Cache**: Dependencies for faster builds

Key workflow features:
```yaml
# Automatic enablement
- name: Setup Pages
  uses: actions/configure-pages@v4
  with:
    enablement: true  # This tries to enable Pages automatically

# Proper permissions
permissions:
  contents: read
  pages: write
  id-token: write
```

## 🎉 Success Indicators

When everything is working correctly:

1. **Actions Tab**: Shows green checkmarks ✅
2. **Pages Settings**: Shows "Your site is published at..."
3. **Website**: Loads at `https://manohar3000.github.io/murlix`
4. **Updates**: New pushes automatically update the site

## 📞 Getting Help

If you're still having issues:

1. **Check the Actions logs** for specific error messages
2. **Verify repository permissions** - you need admin access
3. **Try the workflow manually** using "Run workflow" button
4. **Contact GitHub Support** if Pages enablement fails

---

**Once set up, your beautiful Murlix documentation will be automatically deployed to GitHub Pages with every push to main!** 🚀