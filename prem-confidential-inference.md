# What Can You Check About a Prem Confidential Inference Request?

*The release and fallback notes' questions, put to one confidential AI service*

This note reads what one company publishes about its confidential inference service, and what a customer can check. It records what each source says. It does not assess the service's security.

| Document | prem-confidential-inference.md |
| :---- | :---- |
| **Version** | 0.1 — peer review draft |
| **Audience** | People deciding what a confidential AI service's claims are evidence of: read [Start here](#start-here). Technical reviewers: read the full note. |
| **Method** | Follow the chain a customer would need, from hardware evidence to the code that answers the request. For each link, record what the company's security page says, what its documentation says, and what its published code does. Tie each statement to a public source and the date it was read. |
| **Changes** | See the [changelog](#changelog). |
| **Scope** | Prem AI's encrypted inference service and the verification tooling it publishes, as read on 12 October 2026. This is not a security assessment, a finding about any person, or a review of the company's compliance. The maker has not reviewed this draft. |

## Contents

- [Start here](#start-here)
- [1. What the note establishes](#1-what-the-note-establishes)
  - [1.1 Evidence](#11-evidence)
  - [1.2 Terms](#12-terms)
- [2. The verification chain](#2-the-verification-chain)
- [3. Public records](#3-public-records)
  - [3.1 The security page](#31-the-security-page)
  - [3.2 The documentation](#32-the-documentation)
  - [3.3 The verifier](#33-the-verifier)
  - [3.4 The default policies](#34-the-default-policies)
  - [3.5 Builds, image source, and transparency logs](#35-builds-image-source-and-transparency-logs)
- [4. The three sources, side by side](#4-the-three-sources-side-by-side)
- [5. Questions that make a claim reviewable](#5-questions-that-make-a-claim-reviewable)
- [6. Limits and source use](#6-limits-and-source-use)
- [7. References](#7-references)
- [Changelog](#changelog)

## Start here

This section is for anyone weighing a confidential AI service. You do not need to read code to use it. The rest of the note is the record behind each point.

**What the service offers.** You send a prompt to an AI model. The service says the model runs inside protected hardware, so that the company and its cloud providers cannot read your prompt. Before your prompt is sent, your software asks the hardware for a signed report about itself. That report is called an attestation.

**What an attestation can show.** A signed report can show that real protected hardware answered, and that the report is fresh. It can also contain measurements: fingerprints of the software that the hardware started. A measurement is useful only if someone compares it with a known value for approved software. Without that comparison, the report shows protected hardware, not which software ran.

**Three things the public record shows.** Each one was read on 12 October 2026.

1. **The company publishes its verifier as open source.** Its documentation says the software development kit checks an attestation before it sends a request, unless the developer turns that check off. See [§3.2](#32-the-documentation) and [§3.3](#33-the-verifier).
2. **The default rules do not compare the software measurements with approved values.** The company's documentation says so directly, and lists the comparison as roadmap work. See [§3.2](#32-the-documentation) and [§3.4](#34-the-default-policies).
3. **The security page describes some items in the present tense that the documentation lists as not ready.** These are transparency logs, open-source images, and build matching. See [§4](#4-the-three-sources-side-by-side).

**How to read the difference.** The documentation is detailed and candid about these gaps. The security page is a summary for a general audience. This note puts the two beside each other so a reader can see which statements describe today and which describe a plan.

**What you can check today.** Ask which rules your verifier applies, and who wrote them. A check that passes against rules that compare nothing about the software tells you about the hardware only.

**What this note does not do.** It does not say whether the service is safe to use. It does not compare the company with other providers.

## 1. What the note establishes

A claim about confidential inference needs a defined object: one request, one attestation, one set of rules that judged it. "Encrypted", "attested", and "verifiable" describe different properties. None follows from the others.

The custody note lists four levels of build evidence. The last is "evidence that the device runs that binary." An attestation with measurements compared to approved values is that evidence for a remote machine. The fallback note asks which code runs inside a file. This note asks which software a remote machine ran, and what a customer can confirm about it. See [Who Can Move Your Bitcoin? §3](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle) and [Which Code Actually Runs? §1](which-code-actually-runs.md#1-what-the-note-establishes).

This note uses public web pages, public documentation, and public source code. No request was sent to the service, no attestation was verified, and no build was reproduced.

### 1.1 Evidence

Each record in §3 has: **claim; object and date; public source; what was read; result; unresolved.** A statement by the company about its own service is recorded as the company's statement. The fixed entries "Not applicable" and "Not read for this note" have the meanings in the [release note §1.1](what-can-you-check-about-a-release.md#11-evidence).

### 1.2 Terms

Terms from the [release note §1.2](what-can-you-check-about-a-release.md#12-terms) keep their meaning. This note adds the following.

| Term | Meaning here |
| :---- | :---- |
| **Trusted execution environment (TEE)** | Hardware that runs a virtual machine whose memory the host cannot read. The CPUs named here are AMD SEV-SNP and Intel TDX. The GPUs are NVIDIA parts in confidential-computing mode. |
| **Attestation** | A report about a TEE, signed by a key that chains to the chip vendor. It can carry a fresh nonce and measurements. |
| **Measurement** | A hash of software or configuration that the hardware recorded at start-up. Examples are MRTD and the RTMRs on Intel TDX, and the launch measurement on AMD SEV-SNP. |
| **Reference value** | The measurement expected for approved software. A measurement is **pinned** when the verifier requires it to equal a reference value. |
| **Policy** | The rules a verifier applies to an attestation after the signature checks. Here the policies are written in Rego, the language of Open Policy Agent (OPA). |
| **Collateral** | Certificates and status data from the chip vendor that a verifier needs to check a signature chain. |
| **Transparency log** | An append-only public log. For TEE images, it lets a customer see every image the operator has published and notice an unannounced one. |

## 2. The verification chain

The company's documentation divides a full assurance decision into stages. The table below uses those stages. The second column states what a customer would need at each stage. The last column points to the record.

| Stage | What a customer would need | Record |
| :---- | :---- | :---- |
| **Authenticity** | A signature that chains to the chip vendor's root | §3.3 |
| **Freshness** | A nonce from the customer, echoed in the signed report | §3.3 |
| **Configuration** | Debug off, a minimum firmware level, production mode | §3.4 |
| **Identity** | Measurements equal to reference values for approved software | §3.2, §3.4 |
| **Provenance** | A way to tie each reference value to public source and a reproducible build | §3.5 |
| **Route** | Evidence that the attested machine is the one that served this request | §3.2 |

Each stage depends on the ones above it. A pass at the authenticity and freshness stages shows real protected hardware answered now. Only the identity stage connects that hardware to particular software.

## 3. Public records

### 3.1 The security page

**Claim.** The company's security page describes the service's protections, verification, and transparency in the present tense.

**Object and date.** The page at `premai.io/security`, read 12 October 2026. The page carries no date.

**Public source.** `https://www.premai.io/security`.

**What was read.** The page's statements on attestation, verification, open source, transparency logs, and builds. The page was read through a page reader, not as raw text (see Unresolved).

**Result.**

- **Verification.** The page says: "The SDK performs attestation verification by default before every request." It also says: "Cryptographic attestation verifies hardware integrity and enclave state before payload transmission."
- **Builds.** In a table that compares the service with conventional AI services, the page lists: "Deterministic builds with PCR (Platform Configuration Register) matching."
- **Open source and logs.** The page says: "Open-source codebase and public transparency logs ensure no hidden backdoors." Elsewhere it refers to "Open-source inference codebases combined with immutable public transparency logs."
- **Links.** The page links one source repository, `prem-research/reticle`, the verifier in §3.3. It links no transparency log, build record, or image source.
- **Limits the page states.** The page lists side-channel attacks on TEE hardware, compromise of a chip vendor's signing keys, and metadata such as timing and payload size as limits.
- **Compliance.** The page describes the architecture as supporting several frameworks, among them SOC 2, ISO 27001, and HIPAA. It does not claim a certification. Compliance is outside this note's scope.

**Unresolved.** The page was read through a page reader. Each quotation needs a check against the page's raw text. The page links two whitepapers, which this note did not read.

### 3.2 The documentation

**Claim.** The company's developer documentation describes what the verifier checks today, and lists what is not yet in place.

**Object and date.** The Attestation, Security Model, Platform Status, and How It Works pages at `docs.prem.io`, read 12 October 2026. The pages carry no dates.

**Public source.** `https://docs.prem.io/attestation`, `/security-model`, `/platform-status`, `/how-it-works`.

**What was read.** Each page's statements on default verification, failure behavior, policies, measurements, image source, transparency logs, and routing. The pages were read through a page reader.

**Result.**

- **Default verification.** The Attestation page says: "With the default `attest: true`, `@premai/api-sdk` performs this sequence:". It adds: "`attest: false` and the proxy flag `--no-attest` bypass this gate", and warns against using them for "a workflow that claims attested confidential inference."
- **Failure behavior.** The Attestation page says: "A non-transient failure, or a missing session ID, throws before the protected inference request is sent." That is fail-closed behavior, in the terms of the fallback note.
- **Signatures and identity are separate.** The documentation says a valid manufacturer signature proves the evidence came from the hardware trust chain, and that approving software is policy work.
- **Default policy.** The Attestation page says: "the shipped golden policy leaves image measurements unpinned by default", and that "approving a specific release image requires operator-supplied reference values." The Security Model page says: "The shipped golden policy pins no image measurements by default."
- **Platform status, not ready.** The Platform Status page lists these under not ready: "Reference measurements are unpinned by default"; "The deployed CVM base image cannot yet be inspected against public source"; and route assurance, the evidence that a request's model and path match the attested machine.
- **Platform status, roadmap.** The roadmap includes an open-source confidential VM base image, golden policies "with reference measurements pinned", and "Publish public transparency logs for CVM images so customers can audit changes." It also includes a third-party security audit with a published report.
- **Builds.** The Platform Status page names "Reproducible provenance" as the last stage of its trust model, which connects approved measurements to source and build inputs. The page has no roadmap item for that stage.
- **GPU scope.** The Security Model page says the checks establish the reported GPUs' attested state, but do not prove that those GPUs served a particular request.

The documentation records each gap in §4 in its own words. This note relies on that candor.

**Unresolved.** The pages were read through a page reader, so the quotations need a check against the raw pages. The Confidential Proxy and Quickstart pages were not read.

### 3.3 The verifier

**Claim.** The company publishes its verifier, Reticle, as open source. The verifier checks signatures and freshness, then applies a policy that it fetches from a URL.

**Object and date.** The `prem-research/reticle` repository at commit `1608446`, read 12 October 2026.

**Public source.** `reticle/src/lib.rs` and `nvidia-attest/src/keychain.rs` in that repository.

**What was read.** The client builder, the four end-to-end attestation functions, the module discovery function, and the NVIDIA key fetch.

**Result.**

- **Where the policy comes from.** The client builder sets a default policy source, `const PREM_POLICIES: &str = "https://policies.prem.io";`, and fetches the policy when the client is built. A developer can replace it with `with_policies_url` or `with_policy_provider`. The default is served by the company that operates the attested machines.
- **Where the collateral comes from.** The defaults for Intel and AMD collateral are `https://pccs.prem.io/` and `https://kcds.prem.io`, both company-run caches. A developer can replace them. Collateral is signed by the chip vendor. This note did not read where the verifier anchors the vendor root certificates (see Unresolved).
- **NVIDIA keys.** The NVIDIA module fetches its key set from NVIDIA's attestation service, at a `.well-known/jwks.json` path.
- **End-to-end functions.** `attest_sev`, `attest_tdx`, and `attest_nvidia` each generate a nonce, check the vendor signature chain, then evaluate the fetched policy. Each returns an error if the policy does not allow the claims.
- **Lower-level functions.** `request_sev`, `request_tdx`, and `request_nvidia` carry this warning: "does not perform cryptographic or measurement checks on the attestation."
- **Which modules are attested.** The top-level `attest()` function first asks the attestation server which modules it has. It attests the CPU module the server names, and an NVIDIA GPU only if the server names one. If the server names no GPU, no GPU attestation runs.

Two of these points are the questions from the other notes. The rules that decide a pass come from the operator of the machine being judged. The machine being judged also reports which of its parts to check. A developer can supply both independently, by pointing the client at their own policy and by checking the module list against what they expect.

**Unresolved.** The note did not build or run the verifier. It did not read where the verifier anchors the AMD and Intel root certificates. It could not read the published `@premai/api-sdk` package, which wraps the verifier, so the SDK's own code was not read.

### 3.4 The default policies

**Claim.** The policies that the verifier fetches by default check configuration, and leave software measurements unpinned.

**Object and date.** The `prem-research/confidential-policies` repository at commit `61ea413`, read 12 October 2026. The file `policies.json` at `policies.prem.io`, read the same day.

**Public source.** The four policy files in that repository, its deployment workflow, and the index at `https://policies.prem.io/policies.json`.

**What was read.** Each policy's `allow` rule, the TDX reference values, and the index file.

**Result.**

- **Served copy.** The index at `policies.prem.io` lists the same four policy files as the repository's `policies.json`. The repository deploys its contents to GitHub Pages on each push to `main`. The policy files themselves were not compared between the two locations.
- **AMD SEV-SNP.** The policy allows a report when `policy.debug_allowed == false` and `policy.microcode >= 72`. It checks no launch measurement.
- **Intel TDX.** The policy checks configuration invariants, such as debug off, a production TDX module, and a minimum security version. Its reference values for `mrtd`, `mrseam`, and the four RTMRs are empty strings, and its matching rule accepts any value when the reference is empty: `hex_match(ref, got) if ref == ""`. The file records observed baseline values in comments, and explains: "mrtd, mrseam and the RTMRs are left unpinned by default because they legitimately vary per host". It asks operators to "pin them once your fleet's values are catalogued."
- **Azure.** The policy checks that 24 PCR digests are present and well formed. It compares no PCR value with a reference.
- **NVIDIA.** The policy requires NVIDIA's own measurement result, `claims.measres == "success"`, and valid certificate chains. NVIDIA's attestation compares GPU firmware and driver measurements with NVIDIA's published reference values. The GPU stage therefore has a reference comparison by default; the CPU stages do not.

The CPU policies establish that a report came from protected hardware with debug off and current firmware. They do not establish which software image that hardware started. The documentation in §3.2 says the same.

**Unresolved.** The policy files were not compared byte for byte with the copies served at `policies.prem.io`. The note did not establish which policy the production service's own clients use, or whether any customer pins its own reference values.

### 3.5 Builds, image source, and transparency logs

**Claim.** The security page describes deterministic builds with PCR matching, an open-source codebase, and public transparency logs. This record lists what this note found for each.

**Object and date.** The public repositories of the `prem-research` organization, listed 12 October 2026, and the sources in §3.1 to §3.4.

**Public source.** The organization page at `github.com/prem-research`, and the documentation in §3.2.

**What was read.** The names and descriptions of the repositories listed on the organization page.

**Result.**

- **Open source.** The verifier and the policies are public (§3.3, §3.4). The Platform Status page says the deployed confidential VM base image "cannot yet be inspected against public source." The organization page listed 10 of its 14 public repositories. None of the 10 is described as an image, a build definition, or an inference server for the confidential service.
- **Deterministic builds.** No build definition, build record, or published reference measurement for a release image was found. The documentation names reproducible provenance as a trust-model stage without a roadmap item (§3.2).
- **Transparency logs.** No log was found or linked. The documentation lists a transparency log for confidential VM images as roadmap item seven (§3.2).

**Unresolved.** Four of the organization's repositories were not listed on the page read. The whitepapers linked from the security page were not read, and may describe the build process. The company's trust center at `trust.prem.io` did not render in the page reader, so its contents were not read.

## 4. The three sources, side by side

Each row takes one statement from the security page and sets the documentation and the code beside it. The rows record what each source says. They are not verdicts.

| Security page | Documentation | Published code | What a customer can check today |
| :---- | :---- | :---- | :---- |
| "The SDK performs attestation verification by default before every request." | `attest: true` is the default, and a failure throws before the request is sent. | The end-to-end functions check signatures and freshness, then apply the fetched policy. | That attestation ran and the default policy passed. Not read for this note: the SDK package itself. |
| Attestation verifies "hardware integrity and enclave state". | A signature proves the hardware chain. Approving software is policy work, and the shipped policy leaves image measurements unpinned. | The CPU policies pin no image measurement. The GPU policy relies on NVIDIA's reference comparison. | Hardware, freshness, configuration, and GPU firmware state. Not the CPU software image, unless the customer supplies reference values. |
| "Deterministic builds with PCR (Platform Configuration Register) matching" | Pinned measurements are on the roadmap. Reproducible provenance is named as a stage, with no roadmap item. | No build definition or published reference measurement was found. The TDX policy records observed values in comments. | Not established by the records read. |
| "Open-source codebase and public transparency logs ensure no hidden backdoors." | The deployed base image "cannot yet be inspected against public source." Transparency logs are on the roadmap. | The verifier and policies are public. No image source or log was found. | The verifier and its rules. Not the image that runs the model. |
| Content is protected from the operator by hardware, not by policy. | Route assurance is not ready, and GPU checks do not prove which GPUs served a request. | Module discovery is answered by the attestation server. | That some attested hardware exists behind the endpoint. Not that it served this request. |

The security page and the documentation are both the company's statements. They describe the same service at different levels of detail. Where they differ, the documentation is the more specific of the two, and it describes the gaps as current.

## 5. Questions that make a claim reviewable

| If the claim is | Request | If the artifact is missing |
| :---- | :---- | :---- |
| **The request is attested** | The policy that judged it, who wrote that policy, and where the verifier fetched it from | A pass against unknown rules shows only that some rules passed |
| **The enclave runs approved code** | The reference measurements for the approved image, and the policy that pins them | Hardware evidence without a pinned measurement shows protected hardware, not which software |
| **Builds are deterministic** | The build definition, the published measurement for each release, and a second builder's matching result | A build that only the operator can run is not a reproducible build |
| **The code is open source** | The source for the image that runs the model, tied to the measurement it produces | Open-source tooling around a closed image leaves the image unexamined |
| **Changes are logged publicly** | The log's address, and an entry for the current image | A planned log is not a log |
| **The GPU is attested** | Whether the client requires a GPU, or accepts the server's report that none is present | A check the server can opt out of is the server's choice |
| **Nobody can read your data** | The route evidence that ties this request to the attested machine | Attestation of a machine does not show which machine served the request |
| **You can verify it yourself** | How to run the verifier with your own policy and your own reference values | Verification with the operator's defaults checks the operator's rules |

## 6. Limits and source use

- This note reads the company's public statements and published code. It does not assess the service's security, and it does not say whether the service is fit for any use.
- No person is assessed. The note names the company and its products because their public claims are the subject.
- Hardware side channels, vendor key compromise, and metadata exposure are limits the company states itself (§3.1). They are outside this note.
- Compliance, certifications, retention, and the trust center are outside this note.
- The company's documentation lists most of the gaps recorded here as current and plans fixes for several. A later reading can differ. Read the sources for the date you need.
- A missing artifact means only that this note does not show the claim. An artifact may exist and not have been read.

## 7. References

Each source is listed once with the version or date consulted and the sections that cite it.

**Prem AI web pages**, read 12 October 2026. These pages are not pinned to a version.

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Security page](https://www.premai.io/security) | The company's security, verification, and transparency claims | §3.1, §4 |
| [Attestation](https://docs.prem.io/attestation) | Default verification, failure behavior, and the default policy | §3.2, §4 |
| [Security Model](https://docs.prem.io/security-model) | The trust model, measurement policy, and stated limits | §3.2, §4 |
| [Platform Status](https://docs.prem.io/platform-status) | What is available, what is not ready, and the roadmap | §3.2, §3.5, §4 |
| [How It Works](https://docs.prem.io/how-it-works) | The service architecture | §3.2 |
| [Policy index](https://policies.prem.io/policies.json) | The default policy index the verifier fetches | §3.4 |
| [prem-research organization](https://github.com/prem-research) | The organization's public repositories | §3.5 |

**Source repositories**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [reticle/src/lib.rs, commit 1608446](https://github.com/prem-research/reticle/blob/1608446bb7f0b86c50fd35bcd967134b9c26c658/reticle/src/lib.rs) | The client builder, default policy and collateral sources, and the attestation functions | §3.3, §4 |
| [nvidia-attest/src/keychain.rs, commit 1608446](https://github.com/prem-research/reticle/blob/1608446bb7f0b86c50fd35bcd967134b9c26c658/nvidia-attest/src/keychain.rs) | The NVIDIA key fetch | §3.3 |
| [confidential-policies, commit 61ea413](https://github.com/prem-research/confidential-policies/tree/61ea413bb991b729c96433a1d43cd0838f7c2bfc) | The default SEV-SNP, TDX, Azure, and NVIDIA policies, and their deployment workflow | §3.4, §4 |

## Changelog

Newest first. Versioning follows [STYLE.md](STYLE.md).

| Version | Change |
| :---- | :---- |
| 0.1 — 12 October 2026 | First draft. Records the security page, the documentation, the verifier, and the default policies, read 12 October 2026. Sets out the verification chain and sets the three sources side by side. Not yet reviewed by the maker. |
