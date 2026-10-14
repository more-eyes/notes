# What Can You Check About a Package You Install?

*Questions to ask about the step between a project and your machine*

This note compares how two package registries and their install tools handle that step. It does not rank them.

| Document | what-can-you-check-about-a-package.md |
| :---- | :---- |
| **Version** | 0.1 — peer review draft |
| **Audience** | People who depend on software built from many packages, including wallets: read [Start here](#start-here). Technical reviewers: read the full note. |
| **Method** | Follow one package from its maintainer's publish step to the installer on your machine. At each step, put the same question to two registries and record what each registry's own documentation says. Tie each statement to a pinned source. |
| **Changes** | See the [changelog](#changelog). |
| **Scope** | The Python Package Index (PyPI) with its installer pip, and the npm registry with the npm command-line tool, as documented on 14 October 2026. This is not a finding about any project published there, a review of any registry's operations, or a survey of attacks. |

## Contents

- [Start here](#start-here)
- [1. What the note establishes](#1-what-the-note-establishes)
  - [1.1 Evidence](#11-evidence)
  - [1.2 Terms](#12-terms)
- [2. Six steps from maintainer to machine](#2-six-steps-from-maintainer-to-machine)
- [3. Public records](#3-public-records)
  - [3.1 PyPI and pip](#31-pypi-and-pip)
  - [3.2 The npm registry and npm](#32-the-npm-registry-and-npm)
- [4. The two registries side by side](#4-the-two-registries-side-by-side)
- [5. What a provenance record answers](#5-what-a-provenance-record-answers)
- [6. Questions that make a claim reviewable](#6-questions-that-make-a-claim-reviewable)
- [7. Limits and source use](#7-limits-and-source-use)
- [8. References](#8-references)
- [Changelog](#changelog)

## Start here

This section is for anyone who uses software that is built from other people's packages. Most wallets are. You do not need to read code to use it. The rest of the note is the record behind each question.

**What a package registry is.** A registry is a public service that stores packages: small pieces of software that other software is built from. A project's maintainer uploads a package. An install tool downloads it onto a developer's machine, together with the packages it depends on. A wallet can depend on hundreds of packages this way.

**Why it matters.** The release note asks what a project publishes. This note asks what happens between that project and your machine. The package you install passed through an account, a registry, and an install tool. Each one is a place where a package could change, or where a different package could take its place.

**The questions that matter.**

1. **Who could publish this version?** Ask whether a person's account, a saved password-like token, or an automated build published it. See [§3](#3-public-records).
2. **What ties the file to its source?** Some packages carry a signed record that names the source code and the build that produced them. Ask whether this one does, and whether anything checked it. See [§5](#5-what-a-provenance-record-answers).
3. **Can the file change after you first saw it?** Ask whether the registry lets a version be replaced. See [§4](#4-the-two-registries-side-by-side).
4. **What runs when you install it?** Installing some packages runs code on your machine before you ever use them. Ask whether that is allowed, and who decided. See [§4](#4-the-two-registries-side-by-side).
5. **Is the version pinned, and by hash?** A pinned version with a recorded hash installs the same file every time. A version range can install a new file tomorrow. See [§4](#4-the-two-registries-side-by-side).
6. **What happens after a bad release?** Ask how a version is withdrawn, and whether its name can be used again. See [§4](#4-the-two-registries-side-by-side).

**How to judge an answer.** A good answer shows you something you can check: a lockfile with hashes, a provenance record, a registry setting. A weak answer repeats the claim in different words. A weak answer does not prove a problem. It shows that the claim is not proved yet.

**What this note does not do.** It does not rank the registries or say which to use. It does not say whether any package is safe. A signed record shows where a package came from, not whether to trust what it does.

## 1. What the note establishes

A claim about an installed package needs a defined object: one file, at one version, from one registry, installed by one tool with one set of options. "Published by the maintainer", "built from source", and "verified" describe different properties. None follows from a package's name or download count.

This note uses each registry's own documentation and the documentation of its install tool, read in their source repositories and pinned to a commit. It does not inspect any package, account, or registry operation. The registries' mechanisms change, so a later reading can differ.

### 1.1 Evidence

Each record in §3 has: **claim; object and date; public source; what was read; result; unresolved.** The fixed entries "Not applicable" and "Not read for this note" have the meanings in the [release note §1.1](what-can-you-check-about-a-release.md#11-evidence). A statement by a registry about its own service is recorded as that registry's statement.

### 1.2 Terms

Terms from the [release note §1.2](what-can-you-check-about-a-release.md#12-terms) keep their meaning. This note adds the following.

| Term | Meaning here |
| :---- | :---- |
| **Registry** | A public service that stores packages and serves them to install tools. |
| **Install tool** | The program that resolves, downloads, and installs packages: pip for PyPI, the npm command-line tool for the npm registry. |
| **Dependency** | A package that another package needs. A **transitive** dependency is a dependency of a dependency. |
| **Long-lived token** | A secret, saved by a maintainer or a build system, that lets its holder publish until someone revokes it. |
| **Trusted publishing** | A registry feature in which an automated build proves its identity with a short-lived OpenID Connect (OIDC) token, and the registry accepts a publish from that build without a saved token. |
| **Provenance record** | A signed statement that ties a published file to the source and the build that produced it. PyPI calls these attestations; npm calls them provenance statements. |
| **Install-time code** | Code from a package that runs while the package is installed, before anyone uses it. |
| **Lockfile** | A file that records the exact version, and a hash, of every package in a project's dependency tree. |
| **Pinning** | Requiring one exact version. A **hash pin** also requires the file's hash. |

## 2. Six steps from maintainer to machine

| Step | The question | What would answer it |
| :---- | :---- | :---- |
| **1. Publish** | Who could publish this version? | The credential the registry accepted: an interactive login with a second factor, a long-lived token, or a short-lived build identity |
| **2. Provenance** | What ties this file to its source? | A provenance record naming a source commit and a build, signed and logged publicly |
| **3. Storage** | Can this file be replaced after it was published? | The registry's rule on replacing a file at an existing version and name |
| **4. Install** | What runs when the file is installed? | The install tool's default for install-time code, and the option that changes it |
| **5. Pinning** | Will the same file be installed next time? | A lockfile or requirements file with exact versions and hashes for the whole tree |
| **6. Withdrawal** | What happens after a bad release? | The registry's rules on withdrawing a version, and on reusing a version or a name |

The release note's three checks cover the project's side of step 2. This note adds the registry and the install tool around it.

## 3. Public records

### 3.1 PyPI and pip

**Claim.** PyPI offers trusted publishing and attestations, requires a second factor on accounts, and keeps file names unique even after deletion. pip, by default, does not check files against tampering and can run code from source packages; options change both.

**Object and date.** PyPI's user documentation and help page in the `pypi/warehouse` repository at commit `8a4943e`; pip's documentation in the `pypa/pip` repository at commit `c889090`; PEP 592 and PEP 740 in the `python/peps` repository at commit `145bee8`. All read 14 October 2026.

**Public source.** Listed in [§8](#8-references).

**What was read.** PyPI's pages on trusted publishers, attestations and their security model, consuming attestations, and yanking. The help page sections on two-factor authentication, deletion, and file name reuse. pip's page on secure installs. The status lines of the two PEPs.

**Result.**

- **Publishing credentials.** PyPI describes trusted publishing as using OIDC "to exchange short-lived identity tokens between a trusted third-party service and PyPI." The token PyPI issues is "only valid for 15 minutes from time of creation." PyPI calls trusted publishing a mechanism "*complementing* API tokens", so saved tokens remain available.
- **Accounts.** PyPI's help page says: "Two-factor authentication **is required** on your PyPI account."
- **Attestations.** PyPI implements PEP 740, which has the status Final. Attestations "bind each release distribution (such as an individual sdist or wheel) to a strong cryptographic digest of its contents." PyPI accepts two kinds: a publish attestation and SLSA provenance. They are signed by trusted publisher identities, and served through the package index. PyPI's security model page says attestations "are not considered verified unless they include an inclusion proof from Rekor", Sigstore's public transparency log.
- **Checking an attestation.** PyPI's documentation names a separate command-line tool that downloads a file and its attestations and verifies them against an expected source repository. pip's secure-installs page, read for this note, does not describe checking attestations.
- **What an attestation says.** PyPI's security model page says: "An attestation will tell you **where** a PyPI package came from, but not **whether** you should trust it."
- **File immutability.** The help page says: "Deletion of a project, release or file on PyPI is permanent and irreversible, without exception." It adds that deleted files "cannot be re-uploaded", and that deleting a project "releases the project name for use by any other PyPI user."
- **Withdrawal.** PyPI calls yanking "a non-destructive alternative to deletion." A yanked release "is always ignored by an installer, unless it is the only release that matches a version specifier (using either `==` or `===`)." PEP 592, which defines yanking, has the status Final.
- **Install defaults.** pip's documentation says: "By default, pip does not perform any checks to protect against remote tampering and involves running arbitrary code from distributions."
- **Install options.** pip names two changes: hash-checking mode, with `--require-hashes`, and disallowing source distributions, with `--only-binary :all:`. In hash-checking mode, "Hashes are required for _all_ dependencies", and requirements must be pinned.
- **The index's own hash.** pip checks the hash in each download link from the index. Its documentation says that because "this hash originates remotely, it is not a useful guard against tampering".

**Unresolved.** The note did not read PyPI's pages on API tokens or organization accounts, or any PyPI feature for approving a release before it is public. It did not read whether pip or any other Python installer verifies attestations by default. It did not read the build-backend standard in detail; "running arbitrary code from distributions" is pip's own summary.

### 3.2 The npm registry and npm

**Claim.** The npm registry offers trusted publishing, provenance statements, and a staged publishing step, and it never reuses a name and version. Since npm 12.0.0, the command-line tool blocks dependency install scripts unless the project allows them.

**Object and date.** npm's documentation in the `npm/documentation` repository at commit `f8a3253`; the npm command-line documentation and changelog in the `npm/cli` repository at commit `83ea1a1`, where the latest release listed is 12.2.0. All read 14 October 2026.

**Public source.** Listed in [§8](#8-references).

**What was read.** npm's pages on trusted publishing, generating and viewing provenance, requiring two-factor authentication, staged publishing, and the unpublish policy. The command-line pages on lifecycle scripts, the lockfile, `npm audit signatures`, and script approval. The 12.0.0 changelog entry.

**Result.**

- **Publishing credentials.** npm's trusted publishing uses OIDC, "eliminating the need for long-lived npm tokens." The registry accepts publishes from an authorized workflow "in addition to traditional authentication methods like npm tokens and manual publishes." The page says self-hosted runners are not currently supported.
- **Accounts and tokens.** npm's documentation says all packages require two-factor authentication "or a granular access tokens with bypass 2FA enabled" for publishing. A package-level setting, "Require two-factor authentication and disallow tokens", which npm marks as recommended, removes the token route.
- **A review step before publication.** With staged publishing, a package goes to a staging area, and "A maintainer must then review and explicitly approve the staged package — with two-factor authentication (2FA)". npm's page says trusted publisher configurations created after 3 September 2026 are set to allow staged publishing, with direct publishing as an option.
- **Provenance.** npm describes two attestations: a provenance attestation, which links to "a package's source code and build instructions", and a publish attestation from the registry. A package published with provenance "is signed by Sigstore public good servers and logged in a public transparency ledger". With trusted publishing, provenance is generated automatically.
- **What provenance says.** npm's page says provenance "does not guarantee the package has no malicious code."
- **Checking provenance.** `npm audit signatures` "checks the registry signatures and provenance attestations" of installed packages. It is a separate command. The registry's website also shows a mark for packages published with provenance, and warns if the linked source can no longer be found.
- **File immutability.** npm's unpublish policy says: "Once `package@version` has been used, you can never use it again." A version can be unpublished within 72 hours if no other package depends on it. After 72 hours, unpublishing requires no dependents, fewer than 300 downloads in the last week, and a single maintainer. Otherwise npm recommends deprecation, which keeps the package installable and shows a warning.
- **Install-time code.** The 12.0.0 changelog lists as a breaking change: "Dependency lifecycle scripts are now blocked by default unless allowed by the root package's `allowScripts` policy." The command-line documentation says install commands "silently skip lifecycle scripts for any dependency that does not have a matching entry in `allowScripts`, and end with a list of the packages whose scripts were skipped". Approvals are pinned to the reviewed version by default. The same release changed the defaults for installing from git repositories and from user-supplied tarball URLs to "none".
- **Lockfile.** `package-lock.json` "describes the exact tree that was generated". For each package it records `resolved`, where the package came from, and `integrity`, "A `sha512` or `sha1` Standard Subresource Integrity string for the artifact".

**Unresolved.** The note did not read how many projects have moved to npm 12, or how earlier versions behave beyond the changelog entry. It did not read whether `npm install` verifies provenance by default; the documentation read describes `npm audit signatures` as the check. It did not read npm's rules on reusing a package name after a whole package is unpublished.

## 4. The two registries side by side

Each row puts one question to both registries. The entries come from §3. A cell is a summary; the record in §3 has the source.

| Question | PyPI and pip | npm registry and npm |
| :---- | :---- | :---- |
| **Short-lived build identity for publishing** | Yes, trusted publishing. Saved tokens remain available. | Yes, trusted publishing. Tokens remain available unless a package-level setting disallows them. |
| **Second factor on accounts** | Required | Required for publishing, unless a granular token with bypass is used |
| **Review step before a version is public** | Not read for this note | Staged publishing, with maintainer approval under a second factor |
| **Provenance record** | Attestations under PEP 740: publish attestation and SLSA provenance | Provenance attestation and publish attestation |
| **Public log of provenance** | Recorded in Sigstore's public transparency log; PyPI does not treat an attestation as verified without an inclusion proof | Logged in a public transparency ledger |
| **Install tool checks provenance by default** | Not described in the pip documentation read | Not described; `npm audit signatures` is a separate command |
| **A file at a published name can be replaced** | No. Deleted files cannot be re-uploaded. | No. A name and version can never be used again. |
| **Name released after deletion** | Yes. Deleting a project releases the name to any user. | Not read for this note |
| **Install-time code by default** | pip can run code from source distributions. `--only-binary :all:` disallows them. | Since 12.0.0, dependency install scripts are blocked unless the project allows them |
| **Hash pinning** | Opt-in hash-checking mode, covering every dependency | Recorded for every package in the lockfile |
| **Withdrawing a release** | Yanking: ignored unless pinned with `==` or `===`. Deletion is permanent. | Unpublish under limited conditions; otherwise deprecation with a warning |

Five differences explain most of the table.

- **Where the hash comes from.** pip's hash-checking mode uses hashes the project wrote down; pip says the index's own hash is not a guard against tampering. npm's lockfile records a hash when the tree is first resolved. Both protect against a change after that first resolution. Neither shows that the first file was the right one.
- **Who runs install-time code.** pip's documented default runs build code from source distributions. npm's current default blocks dependency scripts until the project approves them. The two tools made opposite default choices for the same risk.
- **When the check happens.** Both registries record provenance at publish time. In the documentation read, neither install tool checks it during a normal install. A provenance record helps only if something reads it.
- **Withdrawal and names.** Both registries refuse to serve a different file under a published name and version. PyPI releases a deleted project's name to other users. A name can therefore outlive its original project.
- **Tokens remain.** Both registries offer short-lived build identities. Both still accept saved tokens unless the maintainer restricts them. Under both registries' documentation, provenance comes from a supported build service, so a version published with a saved token from a maintainer's own machine carries no provenance record. The absence of a record is itself the signal.

## 5. What a provenance record answers

Both registries say the same thing about their own provenance records. PyPI: an attestation tells you "**where** a PyPI package came from, but not **whether** you should trust it." npm: provenance "does not guarantee the package has no malicious code."

In the terms of the release note's §5, a registry provenance record is the build platform's statement about its own build. It ties a file to a source commit and a workflow. It answers the signed check for the build identity. It does not answer the rebuilt check, because no second party built the file. See [What Can You Check About a Software Release? §5](what-can-you-check-about-a-release.md#5-provenance-records).

PyPI's security model page names a use that needs no trust decision about the code: watching for change. A reader who records which identity published past versions can notice when a new version comes from a different identity, or from none. That turns a provenance record into a check that runs over time.

## 6. Questions that make a claim reviewable

| If the claim is | Request | If the artifact is missing |
| :---- | :---- | :---- |
| **It's published by the maintainer** | Which credential published this version: an interactive login, a saved token, or a build identity | A maintainer's name on the package page is not a record of who published each version |
| **It has provenance** | The provenance record for the exact file you installed, and the source commit it names | A mark on a package page covers one version, not every version or every dependency |
| **We verify our dependencies** | The command that checks provenance or signatures, and where it runs | Provenance that no tool reads is a record, not a check |
| **Our builds are reproducible** | A lockfile or hashed requirements file covering every transitive dependency | A version range installs whatever the registry serves on the day |
| **Installing it is safe** | Which packages ran install-time code, and who approved each one | A default that runs every package's install code approves all of them |
| **That bad version was removed** | Whether it was yanked, deprecated, unpublished, or deleted, and whether your lockfile still names it | A withdrawn version can remain in lockfiles and caches |
| **It's the same package as before** | The publishing identity of this version compared with earlier versions | A familiar name is not a familiar publisher |

## 7. Limits and source use

- This note compares documented mechanisms. It is not an assessment of either registry's security, and it does not rank them.
- No package, project, maintainer, or account is assessed.
- Attacks on registries and the frequency of malicious packages are outside this note. The note makes no claim about how often any failure occurs.
- Each registry is described through its own documentation and its install tool's documentation, pinned to a commit. Documentation in a repository's main branch can describe a feature before it reaches every user; the npm records rely on the changelog for the release that introduced each default.
- Other install tools for the same registries can behave differently from pip and the npm command-line tool. They are outside this note.
- A missing artifact means only that this note does not show the claim.

## 8. References

Each source is listed once with the version consulted and the sections that cite it. The registries publish these pages on their websites; the links below point to the source files at the commit read.

**PyPI**, at [pypi/warehouse commit 8a4943e](https://github.com/pypi/warehouse/tree/8a4943e82c7f5f3e26ab1c9688f5cb141030050e).

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Trusted publishers: getting started](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/trusted-publishers/index.md) | Trusted publishing and its short-lived tokens | §3.1, §4 |
| [Attestations: introduction](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/attestations/index.md) | Attestations and the kinds PyPI accepts | §3.1, §4 |
| [Attestations: security model](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/attestations/security-model.md) | What an attestation does and does not show, and the transparency-log requirement | §3.1, §4, §5 |
| [Attestations: producing](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/attestations/producing-attestations.md) | Producing attestations, and the public transparency log | §3.1 |
| [Attestations: consuming](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/attestations/consuming-attestations.md) | How attestations are served and verified | §3.1 |
| [Yanking](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/docs/user/project-management/yanking.md) | Yanking a release | §3.1, §4 |
| [Help page](https://github.com/pypi/warehouse/blob/8a4943e82c7f5f3e26ab1c9688f5cb141030050e/warehouse/templates/pages/help.html) | Two-factor requirement, deletion, and file name reuse | §3.1, §4 |

**pip**, at [pypa/pip commit c889090](https://github.com/pypa/pip/tree/c88909029b3ad43e3e9bd7d47078f4548d59c348).

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Secure installs](https://github.com/pypa/pip/blob/c88909029b3ad43e3e9bd7d47078f4548d59c348/docs/html/topics/secure-installs.md) | pip's defaults, hash-checking mode, and disallowing source distributions | §3.1, §4 |

**Python Enhancement Proposals**, at [python/peps commit 145bee8](https://github.com/python/peps/tree/145bee803f08ed68c225c185dc40d4f40a089e1c).

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [PEP 592](https://github.com/python/peps/blob/145bee803f08ed68c225c185dc40d4f40a089e1c/peps/pep-0592.rst) | Adding "Yank" Support to the Simple API | §3.1 |
| [PEP 740](https://github.com/python/peps/blob/145bee803f08ed68c225c185dc40d4f40a089e1c/peps/pep-0740.rst) | Index support for digital attestations | §3.1, §4 |

**npm registry**, at [npm/documentation commit f8a3253](https://github.com/npm/documentation/tree/f8a32535facbd448b26736b627537fd17db40293).

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Trusted publishing](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/packages-and-modules/securing-your-code/trusted-publishers.mdx) | Trusted publishing and supported build services | §3.2, §4 |
| [Generating provenance statements](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/packages-and-modules/securing-your-code/generating-provenance-statements.mdx) | Provenance and its limits | §3.2, §4, §5 |
| [Viewing package provenance](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/packages-and-modules/getting-packages-from-the-registry/viewing-package-provenance.mdx) | Provenance on the website, and `npm audit signatures` | §3.2 |
| [Requiring 2FA](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/packages-and-modules/securing-your-code/requiring-2fa-for-package-publishing-and-settings-modification.mdx) | Two-factor requirements and token settings | §3.2, §4 |
| [Staged publishing](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/packages-and-modules/securing-your-code/staged-publishing.mdx) | Review before a version is public | §3.2, §4 |
| [Unpublish policy](https://github.com/npm/documentation/blob/f8a32535facbd448b26736b627537fd17db40293/content/policies/unpublish.mdx) | Unpublishing, version reuse, and deprecation | §3.2, §4 |

**npm command-line tool**, at [npm/cli commit 83ea1a1](https://github.com/npm/cli/tree/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b).

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Changelog](https://github.com/npm/cli/blob/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b/CHANGELOG.md) | The 12.0.0 change to dependency install scripts | §3.2, §4 |
| [Script approval](https://github.com/npm/cli/blob/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b/docs/lib/content/commands/npm-approve-scripts.md) | `allowScripts` and blocked scripts | §3.2 |
| [Scripts](https://github.com/npm/cli/blob/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b/docs/lib/content/using-npm/scripts.md) | Lifecycle scripts during install | §3.2 |
| [package-lock.json](https://github.com/npm/cli/blob/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b/docs/lib/content/configuring-npm/package-lock-json.md) | The lockfile, `resolved`, and `integrity` | §3.2, §4 |
| [npm audit](https://github.com/npm/cli/blob/83ea1a1c19648a6b4f5e52a498d8a6aaaf60e52b/docs/lib/content/commands/npm-audit.md) | `npm audit signatures` | §3.2, §4 |

**This repository**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [What Can You Check About a Software Release?](what-can-you-check-about-a-release.md) | The three checks, the fixed entries, and provenance records | §1.1, §1.2, §2, §5 |

## Changelog

Newest first. Versioning follows [STYLE.md](STYLE.md). Version tags use the prefix `package-v`, and each version links to its tagged text.

| Version | Change |
| :---- | :---- |
| [0.1](https://github.com/more-eyes/notes/blob/package-v0.1/what-can-you-check-about-a-package.md) — 14 October 2026 | First draft. Six steps from maintainer to machine. Records for PyPI with pip and for the npm registry with the npm command-line tool, from their own documentation pinned to commits. A side-by-side table, what a provenance record answers, and reviewable claims. |
