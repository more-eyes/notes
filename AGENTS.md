# Instructions for AI agents

This file is for AI agents that draft, check, or edit notes in this repository. People should start with the [README](README.md).

The notes are AI-assisted. One maintainer reviews every change before it is merged. An agent's job is to make that review fast and safe: small changes, every claim tied to a source, and a plain record of what the agent did not check.

## Read first

1. [STYLE.md](STYLE.md). The rules there apply to every change. This file does not repeat them. Where the two disagree, STYLE.md wins.
2. The note you are changing, including its Start here, Unresolved lines, References, and Changelog.
3. The note's last tagged version, so you know what reviewers can already cite.

## What an agent may do

- Work on a branch. Do not commit to `main`.
- Commit with a message that names the note and the version, such as `Release note 0.5: review fixes`. End the message with the attribution trailers your tool requires.
- Open a pull request for the maintainer to review.

## What an agent must not do

- **Do not create, move, delete, or push tags.** The maintainer creates signed tags after a merge. A tag is a citation, so it must not change.
- **Do not merge or push to `main`.** Do not change repository settings, Pages, DNS, or `CNAME`.
- **Do not renumber sections or scenarios, and do not rename a note's file.** Reviewers cite numbers and paths.
- **Do not rewrite a released changelog row.** A changelog row is open only until its version is merged and tagged. A fix after that is a new version.
- **Do not state that you verified something you did not.** Do not supply a quote, figure, commit, or date from memory.

## Sources

- **Open what you cite.** Read every source you cite in this session. If you cannot open a source, do not cite it as read. Record it under Unresolved.
- **Pin it.** Cite a repository at a full commit or a tag, not a branch. Give a web page that cannot be pinned with the date it was read.
- **Quote exactly.** Copy quoted wording from the source. If you read a page through a summarizer or page reader rather than its raw text, say so in Unresolved. The quote then needs a check against the page.
- **Keep the limit with the claim.** When a source supports only part of a claim, narrow the claim or add the limit to Unresolved. Do not widen a claim beyond what a source states.
- **Name only what STYLE.md allows.** Check the name rules in STYLE.md, and the exceptions for each note, before you name a project, product, or role.

## A versioned change

When a change touches a claim, consequence, citation, or reader-facing text (STYLE.md, Structure rules 2 and 3):

1. Raise the note's version line.
2. Add a changelog row at the top. Link the version to `https://github.com/more-eyes/notes/blob/<prefix><X.Y>/<file>`, using the note's prefix from the "Version tags" table in STYLE.md. The link will resolve once the maintainer creates the tag.
3. Update the version line for the note in the README.
4. In the pull request, state the tag the maintainer should create and the commit it should point to.

Typo-only edits, and link changes with the same target, do not change the version.

## Before you open a pull request

Run the "Before you push" list in STYLE.md, and also check these:

- Every relative link and `#anchor` resolves. Heading IDs follow GitHub's rules: lowercase, punctuation removed, spaces become hyphens.
- Every `blob/<tag>/<file>` link names a tag that exists and a file present at that tag, except the new version's own link.
- The text contains no pair of opening curly braces, and no opening curly brace followed by a percent sign. The Pages site builds with Jekyll, which treats both as template code, even inside code spans.
- The diff holds only the files the change needs. Leave out scratch files, scripts, and local tool output.

In the pull request description, list:

- what changed, by note and section;
- each source added or re-read, with the date read;
- what you could not check;
- the tag to create.

## The site

The notes are published at [more-eyes.org](https://more-eyes.org) from `main`, through GitHub Pages with its default Jekyll build. `_config.yml` and `CNAME` configure the site. Earlier versions are not on the site. They are read on GitHub through their tags.
