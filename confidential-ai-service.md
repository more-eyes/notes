# What Can You Check About a Confidential AI Service?

*Questions to ask before you trust an attested AI request*

It describes kinds of deployments, not companies.

| Document | confidential-ai-service.md |
| :---- | :---- |
| **Version** | 0.1 — peer review draft |
| **Audience** | People deciding whether to send private data to an AI service that runs in protected hardware: read [Start here](#start-here). Technical reviewers, including anyone who reviews such a service for an organization: read the full note. |
| **Method** | Follow the chain from a hardware signature to the software that answered one request. For each link, state what the evidence shows, what it leaves open, and what a customer can check. |
| **Changes** | See the [changelog](#changelog). |
| **Scope** | AI inference services that run models in trusted execution environments and offer remote attestation to customers. This is not a finding about any organization, an assessment of any product, or a review of hardware side channels or compliance. |

## Contents

- [Start here](#start-here)
- [1. What the note establishes](#1-what-the-note-establishes)
  - [1.1 Evidence](#11-evidence)
  - [1.2 Terms](#12-terms)
- [2. The verification chain](#2-the-verification-chain)
- [3. Where a pass can mean less than it appears](#3-where-a-pass-can-mean-less-than-it-appears)
  - [3.1 Measurements that are not compared](#31-measurements-that-are-not-compared)
  - [3.2 Rules supplied by the party being judged](#32-rules-supplied-by-the-party-being-judged)
  - [3.3 The server chooses what to attest](#33-the-server-chooses-what-to-attest)
  - [3.4 Verification that can be turned off](#34-verification-that-can-be-turned-off)
  - [3.5 A client-side component that holds plaintext](#35-a-client-side-component-that-holds-plaintext)
  - [3.6 The attested machine and the serving machine](#36-the-attested-machine-and-the-serving-machine)
  - [3.7 Image source, builds, and logs](#37-image-source-builds-and-logs)
- [4. Reading a service's own sources](#4-reading-a-services-own-sources)
- [5. Questions that make a claim reviewable](#5-questions-that-make-a-claim-reviewable)
- [6. Limits and source use](#6-limits-and-source-use)
- [7. References](#7-references)
- [Changelog](#changelog)

## Start here

This section is for anyone weighing an AI service that promises to keep prompts private. You do not need to read code to use it. The rest of the note is the record behind each question.

**What these services offer.** You send a prompt to an AI model. The service says the model runs inside protected hardware, so that the company and its cloud providers cannot read your prompt. Before your prompt is sent, your software asks the hardware for a signed report about itself. That report is called an attestation.

**What an attestation can show.** A signed report can show that real protected hardware answered, and that the report is fresh. It can also contain measurements: fingerprints of the software that the hardware started. A measurement helps only if someone compares it with a known value for approved software. Without that comparison, the report shows protected hardware, not which software ran.

**The questions that matter.**

1. **Does the check compare the software, or only the hardware?** Ask whether your software compares the measurements with values for an approved release. See [§3.1](#31-measurements-that-are-not-compared).
2. **Who wrote the rules for a pass?** If the company you are checking also writes and serves the rules, the check depends on that company. See [§3.2](#32-rules-supplied-by-the-party-being-judged).
3. **Who decides what gets checked?** If the server tells your software which parts to check, a part it leaves out is not checked. See [§3.3](#33-the-server-chooses-what-to-attest).
4. **Is the machine that was checked the machine that answered?** A check of one machine does not show which machine served your request. See [§3.6](#36-the-attested-machine-and-the-serving-machine).
5. **Can you see the software that runs?** Ask for its source, a build that others can repeat, and a public log of each release. See [§3.7](#37-image-source-builds-and-logs).
6. **Does the summary page match the technical documents?** A summary page and a status page can describe the same feature differently. See [§4](#4-reading-a-services-own-sources).

**How to judge an answer.** A good answer shows you something you can check: a published reference value, a policy you can read and replace, a log entry. A weak answer repeats the claim in different words. A weak answer does not prove a problem. It shows that the claim is not proved yet.

**What this note does not do.** It does not rank services or say which one to use. It does not cover attacks on the hardware itself. The right weight for each check depends on what you need protection from.

## 1. What the note establishes

A claim about confidential inference needs a defined object: one request, one attestation, one set of rules that judged it. "Encrypted", "attested", and "verifiable" describe different properties. None follows from the others.

The custody note lists four levels of build evidence. The last is "evidence that the device runs that binary." For a remote machine, an attestation whose measurements are compared with approved values is that evidence. The fallback note asks which code runs inside a file. This note asks which software a remote machine ran, and what a customer can confirm about it. See [Who Can Move Your Bitcoin? §3](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle) and [Which Code Actually Runs? §1](which-code-actually-runs.md#1-what-the-note-establishes).

This note describes kinds of deployments. It is drawn from the public documentation and source code of confidential AI services, read in October 2026, and names none of them. The roles and terms follow the IETF architecture for remote attestation, RFC 9334.

### 1.1 Evidence

A finding about a specific service should record: **claim; service and date; public source or inspected artifact; verification performed; result; unresolved.** Use the result terms and the fixed entries in the [release note §1.1](what-can-you-check-about-a-release.md#11-evidence). A statement by a service about itself is recorded as that service's statement.

### 1.2 Terms

Terms from the [release note §1.2](what-can-you-check-about-a-release.md#12-terms) keep their meaning. This note adds the following.

| Term | Meaning here |
| :---- | :---- |
| **Trusted execution environment (TEE)** | Hardware that runs a virtual machine whose memory the host cannot read. Current CPU forms include AMD SEV-SNP and Intel TDX. Some GPUs have a confidential-computing mode. |
| **Attestation** | A signed report about a TEE. RFC 9334 calls its content Evidence: "A set of Claims generated by an Attester to be appraised by a Verifier." |
| **Measurement** | A hash of software or configuration that the hardware recorded at start-up. |
| **Reference value** | The measurement expected for approved software. In RFC 9334, reference values are what a verifier compares claims against. A measurement is **pinned** when the verifier requires it to equal a reference value. |
| **Appraisal policy** | The rules a verifier applies to the evidence. RFC 9334 defines it as "A set of rules that a Verifier uses to evaluate the validity of information about an Attester." |
| **Verifier and relying party** | The verifier appraises the evidence. The relying party, here the customer's software, acts on the verifier's result. |
| **Collateral** | Certificates and status data from the chip vendor that a verifier needs to check a signature chain. |
| **Transparency log** | An append-only public log. For TEE images, it lets a customer see every image the operator has published and notice an unannounced one. |

## 2. The verification chain

A full assurance decision has stages. Each depends on the ones above it.

| Stage | What a customer would need | What it shows |
| :---- | :---- | :---- |
| **Authenticity** | A signature that chains to the chip vendor's root | Real protected hardware produced the report |
| **Freshness** | A nonce from the customer, signed into the report | The report is current, not replayed |
| **Configuration** | Debug off, a minimum firmware level, production mode | The hardware is set up to protect memory |
| **Identity** | Measurements equal to reference values for approved software | Which software the hardware started |
| **Provenance** | Each reference value tied to public source and a repeatable build | What that software is |
| **Route** | Evidence that the attested machine served this request | That the protected software handled your data |

A pass at the first three stages shows that protected hardware answered. Only the identity stage connects that hardware to particular software. Provenance and route connect the software to its source and to your request.

RFC 9334 describes freshness by nonce: "an unpredictable nonce is sent by the appraising entity and the nonce is then signed and included along with the Claims". [RFC 9334 §10.2](https://www.rfc-editor.org/rfc/rfc9334.html#section-10.2)

## 3. Where a pass can mean less than it appears

Each pattern below occurs in public documentation or code read for this note. Each is a design choice with a reason. None is a fault in itself. The question in each case is what a pass then establishes.

### 3.1 Measurements that are not compared

**The pattern.** The default appraisal policy checks configuration, such as debug mode and firmware level, and leaves the software measurements unpinned. A policy can accept any value for a measurement when its reference is empty.

**Why it happens.** Some measurements legitimately differ between hosts, firmware builds, and machine sizes. A policy that pins them must be kept current with every release and every host type.

**What a pass then shows.** Authenticity, freshness, and configuration. Not identity. The report shows protected hardware with debug off. It does not show which software image that hardware started.

**What to ask.** Which measurements does the default policy pin? Are reference values published for each release? Can the customer supply their own?

### 3.2 Rules supplied by the party being judged

**The pattern.** The verifier fetches its appraisal policy from a server that the service operator runs. The collateral may also come from operator-run caches.

**Why it happens.** It lets the operator update policies as releases change, without a new client.

**What a pass then shows.** That the evidence met the operator's current rules. A change to those rules changes what passes, without a change on the customer's side. Collateral is signed by the chip vendor, so an operator cache matters less than an operator policy, provided the verifier anchors the vendor root itself.

**What to ask.** Where does the verifier get its policy? Can the customer pin a copy, or host their own? Is each policy version public and dated? Where does the verifier anchor the vendor root certificates?

### 3.3 The server chooses what to attest

**The pattern.** The client first asks the server which modules it has, such as a CPU TEE and an optional GPU. It then attests only the modules the server names.

**Why it happens.** One client can then work with several hardware configurations.

**What a pass then shows.** That the named modules passed. If the server names no GPU, no GPU check runs, and the model's working memory on that GPU is outside the result.

**What to ask.** Can the customer require a GPU attestation, and fail if none is offered?

### 3.4 Verification that can be turned off

**The pattern.** The client verifies by default and stops before sending a request when verification fails. A setting or flag turns verification off.

**Why it happens.** Developers need to test without hardware, and some routes may not run in a TEE.

**What a pass then shows.** Nothing, if the setting was off. A request sent with verification off is not an attested request, though it may travel the same encrypted path.

**What to ask.** How would an organization know whether any of its clients turned verification off? Does the response record whether the request was attested?

### 3.5 A client-side component that holds plaintext

**The pattern.** For clients that cannot run the vendor's library, a local proxy encrypts outbound requests. The proxy holds the plaintext, the credentials, and the encryption keys.

**What a pass then shows.** Nothing about the proxy. The proxy is on the customer's side of the boundary. Its compromise exposes content regardless of the TEE.

**What to ask.** Does the proxy itself verify the attestation? Who maintains it, and how is it updated?

### 3.6 The attested machine and the serving machine

**The pattern.** The attestation describes a machine. A request may travel through a gateway and a scheduler, and may be served by a model route that is not attested at all.

**What a pass then shows.** That attested hardware exists behind the endpoint. Not that it served this request, and not that every model offered by the service runs in a TEE.

**What to ask.** Is the request's encryption key bound to the attested machine, so that only that machine can read it? Which model routes run in a TEE, and how does the response say which route served the request?

### 3.7 Image source, builds, and logs

**The pattern.** The verifier and its policies are public. The image that runs the model is not public, has no repeatable build, or has no public log of releases.

**What a pass then shows.** At most, that a measurement matched a value the operator chose. Without the image source and a repeatable build, a customer cannot tie that value to code they can read. Without a log, a customer cannot tell whether the operator published one image to everyone.

**What to ask.** Is the image source public? Can a second builder produce the same measurement from it? Is there a transparency log of image releases, and where? These are the release note's three checks, applied to a remote image. See [What Can You Check About a Software Release? §2](what-can-you-check-about-a-release.md#2-three-checks).

## 4. Reading a service's own sources

A service often publishes a summary security page, technical documentation, a status or roadmap page, and source code. They are all the service's own statements, and they can describe one feature at different levels of detail.

In the material read for this note, a summary page could describe in the present tense a feature that the same service's status page listed as planned. Examples are transparency logs, open-source images, and matched builds. The technical documentation was the more specific source, and in some cases the more candid one.

For each claim on a summary page:

- Find the same feature on the status or roadmap page, and note whether it is listed as available, partial, or planned.
- Find the code or artifact that implements it, and note whether it is linked.
- Record the three readings side by side, with the date of each. A difference between them is a question for the service, not a finding.

## 5. Questions that make a claim reviewable

| If the claim is | Request | If the artifact is missing |
| :---- | :---- | :---- |
| **Every request is attested** | The policy that judged it, who wrote it, and where the verifier fetched it from | A pass against unknown rules shows only that some rules passed |
| **The enclave runs approved code** | The reference values for each release, and the policy that pins them | Hardware evidence without a pinned measurement shows protected hardware, not which software |
| **Builds are deterministic** | The build definition, the published measurement for each release, and a second builder's matching result | A build that only the operator can run is not a repeatable build |
| **The code is open source** | The source for the image that runs the model, tied to the measurement it produces | Open-source tooling around a closed image leaves the image unexamined |
| **Changes are logged publicly** | The log's address, and an entry for the current image | A planned log is not a log |
| **The GPU is attested** | Whether the client requires a GPU, or accepts the server's report that none is present | A check the server can opt out of is the server's choice |
| **Nobody can read your data** | The binding between this request's key and the attested machine, and the route that served it | Attestation of a machine does not show which machine served the request |
| **You can verify it yourself** | How to run the verifier with your own policy and your own reference values | Verification with the operator's defaults checks the operator's rules |
| **Compliant with a named framework** | The audit report, its scope, and its date | Alignment with a framework is not an audit |

## 6. Limits and source use

- This note describes kinds of deployments. It names no service, and it is not a finding about any organization or person.
- Hardware side channels, compromise of a chip vendor's keys, and metadata exposure are outside this note.
- The patterns in §3 were drawn from public material read in October 2026. They are not a survey. The note makes no claim about how common any pattern is.
- A pattern in §3 is a design choice. Its presence does not show that a service is unsafe, and its absence does not show that a service is safe.
- A missing artifact means only that the claim is not shown. The evidence may exist and not have been read.

## 7. References

Each source is listed once with the version consulted and the sections that cite it.

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html) | Remote ATtestation procedureS (RATS) Architecture: roles, evidence, reference values, appraisal policy, and freshness. RFCs are immutable once published. | §1, §1.2, §2 |
| [What Can You Check About a Software Release?](what-can-you-check-about-a-release.md) | The three checks and the result terms | §1.1, §1.2, §3.7 |
| [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md) | The four levels of build evidence | §1 |
| [Which Code Actually Runs?](which-code-actually-runs.md) | Selection between two ways to do a job | §1 |

## Changelog

Newest first. Versioning follows [STYLE.md](STYLE.md).

| Version | Change |
| :---- | :---- |
| 0.1 — 14 October 2026 | First draft. The verification chain, seven patterns in which a pass can mean less than it appears, a method for reading a service's own sources side by side, and reviewable claims. Names no service. |
