# more eyes

*Open is not the same as looked at.*

Notes that take a common claim about software or custody, state what evidence would support it, and read the public record against that. Each note gives questions to ask and the artifact that would answer each one.

**New here?** Open any note below and read its **Start here** section. It is written in plain language and needs no technical background. The rest of each note is the record behind it.

## What a note is

A note is a versioned, sourced document that follows one question. Every note has the same parts:

- **Start here.** The questions that matter, for a general reader.
- **Records.** What a public source says, with the source, the date it was read, and a pinned version where one exists.
- **Unresolved.** What the note did not check. Every record has this line.
- **Questions that make a claim reviewable.** A claim you may hear, and the artifact to ask for.
- **References and a changelog.** Each version stays citable.

## What these notes are not

- **Not rankings or verdicts.** A note states what a public record shows and what evidence a claim needs. It does not say that a product or a project is safe or unsafe.
- **Not findings about anyone.** No organization or person is assessed. Where a record involves a person, the note names the role.
- **Not the last word.** A missing artifact means only that the note does not show the claim. The evidence may exist and not have been read.

## The notes

### Two general notes

**[Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md)**
*Questions to ask about any way of holding it*

Version 0.18, peer review draft. Comments on this version can cite the [fixed v0.18 text](https://github.com/more-eyes/notes/blob/v0.18/who-can-move-your-bitcoin.md); see the [changelog](who-can-move-your-bitcoin.md#changelog).

A framework for reviewing a custody arrangement. It separates what a custody claim says from what the protocol enforces and what a deployment would have to prove. It works through a single-signature baseline and nine configurations, then the full custody lifecycle. It describes kinds of arrangements and names no company.

**[What Can You Check About a Software Release?](what-can-you-check-about-a-release.md)**
*Questions to ask about a published file*

Version 0.4, peer review draft. See the [changelog](what-can-you-check-about-a-release.md#changelog).

A comparison of release processes. It separates three checks: whether a change was public, who signed the release file, and whether another builder rebuilt it. It reads Bitcoin Core's process beside the Linux kernel, Tor Browser, and the Debian archive, and it covers provenance records. It compares processes and does not rank them.

### Notes that apply the method

**[What Can You Check About an embit Release?](embit-release-records.md)**
*The release note's questions, put to one library*

Version 0.6, peer review draft. See the [changelog](embit-release-records.md#changelog).

A worked example for one Bitcoin library that other projects build on. It records the file on the Python Package Index, the signed tags in the source repository, and the project's written release process. It does not assess the library's code.

**[Which Code Actually Runs?](which-code-actually-runs.md)**
*Questions to ask when software has more than one way to do a job*

Version 0.3, peer review draft. See the [changelog](which-code-actually-runs.md#changelog).

A note on fallbacks in software that makes or uses keys. It defines the selection between two ways to do a job, and the difference between code that is present and code that is reached. It reads two public records and states what the release checks leave open.

## Corrections

Corrections are wanted. That is the reason for the name.

- **Found an error, or a source the note missed?** Open an [issue](https://github.com/more-eyes/notes/issues) or a pull request. Say which note, which section, and what the source shows.
- **Maintain a project that a note describes?** Say so in the issue. A correction from the people who do the work carries the most weight.
- **How a fix lands.** A change to a claim, a consequence, or a citation gets a new version and a changelog row. Earlier versions stay available through their tags.

## How the notes are produced

One person maintains these notes. The drafting and the source checks are AI-assisted, and the maintainer reviews every change before it is merged. Each note states what was verified and what was not. Treat every statement here as a claim to check, not a fact to accept.

## Other files

- [STYLE.md](STYLE.md) holds the editing rules that every note follows.
- [AGENTS.md](AGENTS.md) holds the instructions for AI agents that draft or check notes.
- [what-a-custody-pitch-has-to-show.md](what-a-custody-pitch-has-to-show.md) is a pointer. The custody note used that filename before version 0.18, and the pointer keeps old links working.

This repository moved from `johnzilla/notes` in October 2026. Old links redirect here.
