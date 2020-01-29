# Committing Changes

## Purpose Statement

The purpose of this repository is to hold information useful for clubs at ASU.

## Format

Most notes should be in GitHub Flavored (Markdown)[https://github.github.com/gfm/] for consistency and so they can be rendered directly on GitHub.

That said, if some information is available in a different format and it is not practical to convert it to Markdown, it is fine to leave as is.

Please create directories within this repo that organize your docs hierarchically. This will keep the repo less cluttered and it will be easier to find information.

## Committing Changes

### Prerequisites

1. (Install Git (docs))[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]
2. Fork this repository by clicking the "Fork" button on the GitHub page
  - This will create your own copy of this repo to work on

### Cloning (Command Line; find instructions for your GUI if you are using one)

1. Go to your repository page on GitHub
2. Click the green "Clone or download" button and copy the clone URL
3. Open a command terminal with Git
4. `git clone {forked repo url}`

### Creating Changes

Create changes in the repo as you wish. The repo is a standard directory on your filesystem

### Pushing Changes

1. Stage your changes to commit to the repo:
  - Specific Changes: `git add {files}`
  - All Changes: `git add -a`
2. Commit your changes:
  - `git commit -m "{message describing what you are committing to the repo}"`
3. Push your changes:
  - `git push -u origin {current branch}`
    - Find the current branch by running `git branch`
4. Upstream your changes (Better Docs from GitHub)[https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork]:
  1. Upstreaming pushes your changes to the root repo for everyone to access
  2. On the GitHub page for your fork of the root repo, click "New pull request"
  3. Click "Compare across forks"
  4. For the "base repository", choose "yash101/ASU-Random-Club-Info"
  5. For the "base" next to the "base repository" field, choose "master"
  6. For the "head repository", choose your forked version ('your username/repo name')
  7. For the "base" next to "head repository" field, choose the branch you want to upstream, probably 'master'

If you have any questions, please create an issue on this repository (using the issues tab) on the base repository.
(Link to the issue tracker on the base repository)[https://github.com/yash101/ASU-Random-Club-Info/issues]
