# What Can You Check About a Custodian?

*What a company that holds your bitcoin, or a key to it, should let you see*

This note sets out the public materials that a person in the United States should be able to find about a company that offers to hold bitcoin, or one key to it, before they sign up. It names no company and does not rate any.

| Document | what-can-you-check-about-a-custodian.md |
| :---- | :---- |
| **Version** | 0.2 — draft |
| **Audience** | People in the United States who are researching a company that offers custody, collaborative custody, or inheritance for bitcoin: read [Start here](#start-here). Technical reviewers: read the full note. |
| **Method** | Separate two roles a service can play. List the materials a prospective holder can find without a sales call. Read the federal and state records that a holder can use to check some of those materials, and tie each statement to a dated or hashed source. |
| **Changes** | See the [changelog](#changelog). |
| **Scope** | FinCEN guidance FIN-2019-G001, the FinCEN registration rule at 31 CFR 1022.380 and the FinCEN registrant search, the NMLS Consumer Access lookup, the New York Department of Financial Services custody guidance of 30 September 2025, OCC Interpretive Letter 1170, and the AICPA's description of SOC 3 reports, read on 2 November 2026. This is not legal advice, a finding about any company, or a survey of what companies publish. |

## Contents

- [Start here](#start-here)
- [1. What the note establishes](#1-what-the-note-establishes)
  - [1.1 Evidence](#11-evidence)
  - [1.2 Terms](#12-terms)
- [2. Two roles, three levels](#2-two-roles-three-levels)
- [3. Public records](#3-public-records)
  - [3.1 FinCEN guidance on wallet services](#31-fincen-guidance-on-wallet-services)
  - [3.2 FinCEN registration and the registrant search](#32-fincen-registration-and-the-registrant-search)
  - [3.3 State licensing lookup](#33-state-licensing-lookup)
  - [3.4 One state's written custody standard: New York](#34-one-states-written-custody-standard-new-york)
  - [3.5 Custody by a national bank](#35-custody-by-a-national-bank)
  - [3.6 Independent controls reports](#36-independent-controls-reports)
- [4. The baseline](#4-the-baseline)
- [5. Reading what you find](#5-reading-what-you-find)
- [6. Questions that make a claim reviewable](#6-questions-that-make-a-claim-reviewable)
- [7. Limits and source use](#7-limits-and-source-use)
- [8. References](#8-references)
- [Changelog](#changelog)

## Start here

This section is for anyone in the United States who is looking at a company that offers to hold bitcoin for them, or to hold one key in a shared wallet. You do not need to read code or law to use it. The rest of the note is the record behind each question.

**Two kinds of company.** Some companies hold your bitcoin. They can move it without you. Other companies hold one key in a wallet that needs more than one key, and cannot move your bitcoin alone. The technical sections call either kind a "service". Both may call themselves a custodian. The rules that apply to each are different, so first find out which kind you are looking at.

**Why it matters.** A company's website is written by the company. Some of what it says can be checked in records that someone else keeps: a state's business registry, a federal registration list, a state license list, or an auditor's report. A company that wants to show it follows the rules can point you to those records. A company that only describes itself gives you nothing to check.

**The questions that matter.**

1. **Who exactly is the company?** Look for a full legal name, the state where it was formed, and a street address. A brand name and an email address are not enough to know who you have a contract with. See [§4](#4-the-baseline).
2. **What can the company do with your bitcoin?** Ask whether it can move your bitcoin alone, sign together with you, or take part in a recovery or inheritance plan. Read the terms of service, not only the marketing pages. See [§2](#2-two-roles-three-levels) and [§3.1](#31-fincen-guidance-on-wallet-services).
3. **Which rules does the company say it follows, and can you look them up?** FinCEN, a federal agency, treats a company that holds and moves bitcoin for its customers as a money transmitter, and a money transmitter must register with FinCEN. States have their own license rules. A company that only co-signs may say that these rules do not apply to it. Either way, ask for the statement in writing, and look up any registration yourself. A listing is not an approval. FinCEN says so on its own search page. See [§3.1](#31-fincen-guidance-on-wallet-services), [§3.2](#32-fincen-registration-and-the-registrant-search) and [§3.3](#33-state-licensing-lookup).
4. **Who checked the company's controls?** An outside accountant can examine a company's security controls and write a report. One kind of report is meant to be shared with anyone. Ask whether a report exists, which kind it is, what period it covers, and which systems it covers. See [§3.6](#36-independent-controls-reports).
5. **What happens if the company stops?** Ask what you can still do if the company shuts down, refuses to sign, or loses your account. Ask for the written steps to get your bitcoin back without the company. See [§4](#4-the-baseline).
6. **What does the company know about you?** Read the privacy policy. Check that it says the same thing as the marketing pages. See [§4](#4-the-baseline).

**How to judge an answer.** For each item, ask three things. Is it missing? Is it only stated by the company? Or can you check it in a record that someone else keeps? A company that "can show it" has items in the third group. A missing item does not prove a problem. It shows that the claim is not shown yet.

**What this note does not do.** It does not tell you which company to choose, whether a company needs a license, or whether it follows the law. Only a regulator or a court can decide that. The note tells you what to look for, and where to look.

## 1. What the note establishes

A claim that a service "follows the rules" needs a defined object: one legal entity, playing one stated role, under named rules, with records that a holder can look up. "We are a custodian", "we are regulated", and "we are audited" describe different things. None follows from the others.

This note reads federal guidance, one federal rule, two public lookups, one state's written custody guidance, one federal banking letter, and one description of audit report types. It lists what a holder should be able to find, and which of those items can be checked against an outside record. It does not decide whether any service needs a registration or a license. It does not search for or assess any service. Rules and guidance change, so a later reading can differ.

### 1.1 Evidence

Each record in §3 has: **claim; object and date; public source; what was read; result; unresolved.** The fixed entry "Not read for this note" has the meaning in the [release note §1.1](what-can-you-check-about-a-release.md#11-evidence). A statement by a service about itself is recorded as that service's statement. The rows "An audit applies" and "Insurance covers the claimed loss" in the [custody note §1.1](who-can-move-your-bitcoin.md#11-evidence-and-verdicts) state what those two claims need, and this note does not repeat them.

### 1.2 Terms

Terms from the [custody note §1.2](who-can-move-your-bitcoin.md#12-terms-and-boundaries) keep their meaning, including **key**, **spending path**, and **freeze**. This note adds the following.

| Term | Meaning here |
| :---- | :---- |
| **Custodian** | The word a service uses about itself. This note does not use it as a defined role. It uses the two roles below. |
| **Full-custody service** | A service that can move a holder's bitcoin without the holder's signature. The custody note's [Scenario H](who-can-move-your-bitcoin.md#28-scenario-h--an-account-with-external-spending-authority) describes this arrangement. |
| **Co-signing service** | A service that holds one key in a wallet that needs more than one key, and cannot move the bitcoin alone on any spending path. The custody note's [Scenario B](who-can-move-your-bitcoin.md#22-scenario-b--collaborative-custody-with-a-holder-quorum) describes one such arrangement. |
| **Legal entity** | The company, with its exact registered name and the state where it was formed, that is the party to the holder's contract. A brand name or a footer can differ from it. |
| **Regulatory position** | What a service states about the rules that apply to it: a registration, a license, a charter, or a reason none is needed. |
| **Outside record** | A record kept by someone other than the service, which a holder can read: a government registry or lookup, or a report signed by an independent accountant. |
| **Controls report** | A report by an independent accountant on a service's controls over a stated system and period. [§3.6](#36-independent-controls-reports) covers the SOC 2 and SOC 3 types. |

## 2. Two roles, three levels

**Two roles.** The role decides which items in §4 apply. FinCEN's guidance does not decide the role from what a service calls itself. It looks at who owns the value, where it is stored, whether the owner deals with the payment system directly, and whether the service has "total independent control over the value" ([§3.1](#31-fincen-guidance-on-wallet-services)).

| Role | Can the service move bitcoin alone? | What a holder should look for first |
| :---- | :---- | :---- |
| **Full-custody service** | Yes | The legal entity, its registration and licenses, and terms that say the bitcoin stays the holder's property |
| **Co-signing service** | No, on every spending path | The legal entity, a written role statement that covers every spending path, and the steps to recover without the service |

A service can play both roles in different products. A co-signing service can also take part in recovery or inheritance paths, in which its key and its records decide who can move the bitcoin after a date or an event. The custody note's [§2.5](who-can-move-your-bitcoin.md#25-scenario-e--joint-signing-with-delayed-unilateral-recovery) and [§3](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle) cover these paths. A role statement that leaves them out does not describe the whole role.

**Three levels.** Each item in §4 is at one of three levels.

| Level | Meaning |
| :---- | :---- |
| **Missing** | The holder cannot find the item in the service's public materials. |
| **Stated** | The service states the item in its own materials, such as its terms of service, its privacy policy, or its help pages. |
| **Checkable** | The item can be compared with an outside record: a state business registry, the FinCEN registrant search, a state license lookup, or a controls report. |

A stated item is a claim by the service. A checkable item is a claim that an outside record can contradict. The levels say what a holder can see. They do not say whether the service follows the law.

## 3. Public records

### 3.1 FinCEN guidance on wallet services

**Claim.** FinCEN's 2019 guidance treats a service that holds and moves the value for its customers as a money transmitter. It treats a multiple-signature wallet service that only adds a second authorization as not a money transmitter, if it restricts its role to that. The label a service gives itself does not decide which.

**Object and date.** FinCEN guidance FIN-2019-G001, "Application of FinCEN's Regulations to Certain Business Models Involving Convertible Virtual Currencies", issued 9 May 2019, a PDF on FinCEN's website with SHA-256 `7f4ffebd7d86d940d0c397d8331b2bf8d88e0e9a3aa39654ec4e9a98c3fb3e1f`. Read 2 November 2026.

**Public source.** Listed in [§8](#8-references).

**What was read.** The opening statement of purpose, section 4.2 on wallets, section 4.2.1 on hosted and unhosted wallet providers, and section 4.2.2 on multiple-signature wallet providers.

**Result.**

- **Four criteria.** The treatment of a wallet intermediary "depends on four criteria: (a) who owns the value; (b) where the value is stored; (c) whether the owner interacts directly with the payment system where the CVC runs; and, (d) whether the person acting as intermediary has total independent control over the value."
- **Hosted wallets.** "Hosted wallet providers are account-based money transmitters that receive, store, and transmit CVCs on behalf of their accountholders". In this model, the host "has total independent control over the value (although it is contractually obligated to access the value only on instructions from the owner)."
- **Multiple-signature wallets.** For an un-hosted multiple-signature wallet, the guidance says the party that provides "additional validation at the request of the owner does not have total independent control over the value."
- **The condition.** "If the multiple-signature wallet provider restricts its role to creating un-hosted wallets that require adding a second authorization key to the wallet owner's private key in order to validate and complete transactions, the provider is not a money transmitter because it does not accept and transmit value."
- **When the condition fails.** A person that "combines the services of a multiple-signature wallet provider and a hosted wallet provider" will "qualify as a money transmitter". So will a provider where the value is an entry in its accounts, the owner does not deal with the payment system directly, or the provider "maintains total independent control of the value", "regardless of the label the person applies to itself or its activities."
- **What the guidance is.** The guidance says it "does not establish any new regulatory expectations or requirements" and that it "covers only certain business models".

**Unresolved.** The note read FinCEN's guidance only. It did not read state money transmission laws, which use their own definitions, or any later FinCEN guidance or ruling. The guidance's multisig section does not address recovery or inheritance paths in which the provider's key or records take part. The note does not say how the four criteria apply to any such path. The PDF was read through a text extraction. Each quote in this section was checked against the extracted text.

### 3.2 FinCEN registration and the registrant search

**Claim.** A money services business must register with FinCEN, whether or not a state licenses it. A holder can search current registrations, but FinCEN states that a listing is not an approval, and that not every current registrant is listed.

**Object and date.** 31 CFR 1022.380 in the Electronic Code of Federal Regulations, and the FinCEN MSB Registrant Search at msb.fincen.gov. Both read 2 November 2026, as web pages without a fixed version link.

**Public source.** Listed in [§8](#8-references).

**What was read.** Paragraphs (a) and (b) of the rule. The text of the search page above the search form.

**Result.**

- **Registration.** "each money services business (whether or not licensed as a money services business by any State) must register with FinCEN." Registration is renewed every two calendar years.
- **Not an approval.** The search page says: "You should not trust a company only because it is listed in the MSB Registrant Search." It also says: "FinCEN does not approve or endorse any business that has registered as an MSB."
- **Not complete.** The page says that the search "contains most entities that have a current registration", and that "Not every entity that has a current registration with FinCEN as an MSB is listed". It lists reasons FinCEN may remove an entity from the public list.
- **How to search.** The page says search terms "must be entered exactly as submitted" on the registration form, and that "Variations in abbreviations or spellings could result in negative search results."

**Unresolved.** The note did not read the registration form or the search page's FAQ answers. A search that finds nothing is not proof that a service is not registered, because of the limits above. A search that finds an entry shows a registration, not the service's role or its compliance. Both pages were read through the browser's page text, not through a summarizer. Each quote in this section was checked against that text.

### 3.3 State licensing lookup

**Claim.** State regulators publish license records through a shared lookup, which the lookup describes as a way to confirm that a financial services company is authorized to do business in a state.

**Object and date.** The home page of NMLS Consumer Access. Read 2 November 2026, as a web page without a fixed version link.

**Public source.** Listed in [§8](#8-references).

**What was read.** The home page text.

**Result.**

- **Purpose.** The page calls the lookup "a free service for consumers to confirm that the financial-services company or professional with whom they wish to conduct business is authorized to conduct business in their state."
- **Who runs it.** The page says the data comes from NMLS, which "is owned and operated by the State Regulatory Registry LLC (SRR), a wholly owned subsidiary of CSBS", the Conference of State Bank Supervisors.

**Unresolved.** The note did not run a search. A search requires accepting the lookup's terms of use and passing a check that tells people apart from programs, so an agent did not complete one. The note did not read which states record which license types in NMLS, or which states require a license for a co-signing service. A holder should look up the service's exact legal name, and read which license types and states the record shows. The page was read through the browser's page text, and each quote was checked against that text.

### 3.4 One state's written custody standard: New York

**Claim.** New York's financial regulator expects a licensed virtual currency custodian to keep each customer's assets separate from its own, to state in the customer agreement that the relation is custody and not a debt, and to publish its standard disclosures and customer agreement on its website.

**Object and date.** New York State Department of Financial Services, Industry Letter of 30 September 2025, "Updated Guidance on Custodial Structures for Customer Protection in the Event of Insolvency", which replaces the letter of 23 January 2023. Read 2 November 2026, as a web page without a fixed version link.

**Public source.** Listed in [§8](#8-references).

**What was read.** The whole letter, including its notes.

**Result.**

- **Who it applies to.** The letter is addressed to entities licensed under 23 NYCRR Part 200, or chartered as limited purpose trust companies under the New York Banking Law, "That Custody Virtual Currency Assets".
- **Separation.** A custodian "is expected to separately account for and segregate customer virtual currency from the corporate assets of the VCE Custodian and its affiliated entities, both on-chain and on the VCE Custodian's internal ledger accounts."
- **Custody, not debt.** The custodian should "not thereby establish a debtor-creditor relationship with the customer", and the customer agreement "should make clear the parties' intentions to enter into a custodial relationship, rather than a debtor-creditor relationship."
- **What to disclose.** The custodian "should clearly disclose how it segregates and accounts for customer virtual currency, the property interest the customer retains in custodied assets, how the VCE Custodian may use custodied virtual currency while in its possession, and what limitations on the use of custodied virtual currency by the VCE Custodian apply."
- **Where.** The Department "expects a VCE Custodian to make its standard disclosures and customer agreement readily accessible to customers on its website".

**Unresolved.** The letter states one state's expectations for the entities it regulates. The note does not claim that it applies to a service outside New York, or to a co-signing service. The note uses it as an example of the written terms a full-custody service can publish. The note did not read 23 NYCRR Part 200 itself, or other states' rules. The page was read through the browser's page text, not through a summarizer. Each quote in this section was checked against that text.

### 3.5 Custody by a national bank

**Claim.** The OCC, the federal regulator of national banks, concluded in 2020 that a national bank may hold cryptographic keys for customers as a custody service.

**Object and date.** OCC Interpretive Letter 1170, dated 22 July 2020, a PDF on the OCC's website with SHA-256 `5744d4872636a04566d08904e28156d65479d7e49d9eed0407983c075f16acd3`. Read 2 November 2026.

**Public source.** Listed in [§8](#8-references).

**What was read.** The introduction and summary conclusion.

**Result.**

- **Conclusion.** The letter concludes "a national bank may provide these cryptocurrency custody services on behalf of customers, including by holding the unique cryptographic keys associated with cryptocurrency." A note says the conclusion also applies to federal savings associations.

**Unresolved.** The note read only the letter's opening section. It did not read later OCC letters that may modify or confirm this one, state trust charters, or how a holder can confirm that a bank holds a charter. A service that says it uses a bank or trust company to hold keys has named a second party. That party's role needs the same checks.

### 3.6 Independent controls reports

**Claim.** The AICPA defines a SOC 3 report as a general-use report that can be freely distributed, with less detail than a SOC 2 report on the same kinds of controls.

**Object and date.** The AICPA page "SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report". Read 2 November 2026, as a web page without a fixed version link.

**Public source.** Listed in [§8](#8-references).

**What was read.** The page's summary paragraph.

**Result.**

- **SOC 3.** "Like SOC 2, SOC 3 reports address controls relevant to security, availability, processing integrity, confidential and privacy. However, they do not provide the same level of detail. Therefore, they are considered general use reports and can be freely distributed."

**Unresolved.** The note did not read the AICPA's SOC 2 guide, the trust services criteria, or the AICPA's terms on who may receive a SOC 2 report. It does not state those terms. It records only that the AICPA describes SOC 3, and not SOC 2, as a general-use report. A controls report covers a named system and period. The note did not read how often a service's report covers its key-holding systems. The page was read as HTML through a text extraction, not through a summarizer. The quote was checked against the extracted text.

## 4. The baseline

These are the items that a prospective holder should be able to find without a sales call or a confidentiality agreement. The last column says which outside record, if any, can move an item from stated to checkable.

| Item | What it answers | Applies to | Outside record that can check it |
| :---- | :---- | :---- | :---- |
| **1. Legal entity** | Exact legal name, state where formed, and a street address. Who the holder has a contract with, and who a regulator or court can reach. | Both roles | The business registry of the state where the entity was formed. Not read for this note. |
| **2. Governing terms** | Which state's law governs the terms of service, where disputes go, and the date of the current terms. | Both roles | None; the terms are the record |
| **3. Role statement** | Which keys the service holds, whether it can move bitcoin alone, and every spending path its key or records take part in, including recovery and inheritance. | Both roles | The wallet's own output policy, as the [custody note §2](who-can-move-your-bitcoin.md#2-configuration-assessments) describes |
| **4. Regulatory position** | For a full-custody service, its FinCEN registration and state licenses, or a charter. For a co-signing service, a written statement of why it needs none, that matches the role statement. | Both roles, in different forms | The FinCEN registrant search ([§3.2](#32-fincen-registration-and-the-registrant-search)) and the state license lookup ([§3.3](#33-state-licensing-lookup)). This note gives no record for confirming a charter ([§3.5](#35-custody-by-a-national-bank)). |
| **5. Property terms** | That the bitcoin stays the holder's property, how it is kept apart from the service's own, and what the service may do with it. | Full-custody service | None directly; [§3.4](#34-one-states-written-custody-standard-new-york) shows one state's expected wording |
| **6. Controls report** | Whether an independent accountant reported on the service's controls, which type of report, which system, and which period. | Both roles | A published SOC 3 report, or a SOC 2 report if the service provides one ([§3.6](#36-independent-controls-reports)) |
| **7. Insurance statement** | Whether any policy covers the holder's loss. If one is claimed: the insured party, the covered event, and the limits. | Both roles | The policy itself, under the custody note's insurance row |
| **8. Exit without the service** | What the holder can do if the service stops, refuses to sign, or freezes the account, and written steps to recover with other software. | Both roles | A recovery that someone ran with only the written steps, as the [custody note §1.1](who-can-move-your-bitcoin.md#11-evidence-and-verdicts) describes |
| **9. Data the service keeps** | What the service collects and keeps about the holder and the wallet, and who it shares that with. | Both roles | None directly; the privacy policy can be compared with the sign-up steps and the [custody note §5](who-can-move-your-bitcoin.md#5-privacy-and-coercion) |
| **10. Security contact and incident record** | How to report a security problem, and where the service publishes past incidents and what it did. | Both roles | None directly |
| **11. Accountable people** | Named officers, or a stated reason none are named, and a contact that is not only a web form. | Both roles | The state business registry, where it lists officers. Not read for this note. |

Items 1 to 4 decide who the holder is dealing with and what that party can do. A holder who cannot find them cannot check the rest.

## 5. Reading what you find

This section walks one kind of public website through the baseline. It describes a pattern, not a company.

A service offers a shared wallet in which the holder has two keys and the service has one. It also offers an inheritance plan. Its website has product pages, a help page, terms of service, and a privacy policy.

| Item | What the holder finds | Level |
| :---- | :---- | :---- |
| **1. Legal entity** | A company name in the footer, with no state or address | Stated, in part |
| **2. Governing terms** | Terms with no governing-law clause and no date | Missing, in part |
| **3. Role statement** | Product pages say the service cannot move bitcoin alone. The terms describe an inheritance plan in which, after a date, the service co-signs for whoever presents certain secrets. | Stated, across two documents |
| **4. Regulatory position** | The terms say the service is not a money transmitter. No registration is listed. | Stated |
| **6. Controls report** | No mention | Missing |
| **8. Exit without the service** | Guides to recover the wallet with other software | Stated; checkable by running the guide |

The table leaves out five items. Item 5 applies only to a full-custody service, and this service co-signs. The pattern's pages say nothing about items 7, 10, and 11, so those are missing, like item 6. Item 9 needs the privacy policy compared with the sign-up steps, which the pattern does not describe.

The pattern shows the difference between a website with pages and a website with checkable items. Every row above is present in some form. Only the exit guide can be checked without the service, and only by running it. The role statement needs the most attention. The inheritance path is a spending path in which the service's key and records decide who can move the bitcoin, and a holder sees it only by reading the terms beside the product pages. A holder can ask the service which spending paths its key takes part in, and what stops it from co-signing on each one.

## 6. Questions that make a claim reviewable

| If the claim is | Request | If the artifact is missing |
| :---- | :---- | :---- |
| **We're a regulated custodian** | The legal entity's exact name, its FinCEN registration number, and the states and license types it holds | A word on a website is not a registration; FinCEN states that even a listing is not an approval |
| **We're not a money transmitter, so we don't need a license** | The role statement for every spending path, including recovery and inheritance | FinCEN's guidance ties the answer to the role, "regardless of the label" |
| **We can never move your bitcoin** | The wallet's output policy, and every path in which the service's key or records take part | A path the help pages leave out is still a spending path |
| **Your bitcoin is always yours** | The customer agreement's terms on property, separation, and the service's use of the bitcoin | Marketing text does not state the contract terms |
| **We're SOC 2 compliant** | The report type, the system it covers, the period, and the accountant's name; or a published SOC 3 report | A SOC report covers a named system and period, not the whole company at all times |
| **Your funds are insured** | The insured party, the covered event, the limits, and the exclusions | A policy that insures the service does not show that it pays the holder |
| **You can recover without us** | The written recovery steps, and a run of them with other software | Steps that no one has run show what the service intends, not what works |
| **We collect no personal data** | The privacy policy's own list of what is collected | Marketing text does not limit collection; the privacy policy states what the service may collect |

## 7. Limits and source use

- This note reads federal and state guidance, one rule, two lookups, one federal banking letter, and one description of report types. It is not legal advice and does not decide whether any service needs a registration, license, or charter.
- No service is assessed. The example in §5 is a pattern, not a company.
- The note covers holders in the United States only. Other countries have different rules.
- One state's written custody guidance was read. Other states' rules were not, and they can differ in scope and in what they require.
- The note makes no claim about how many services publish each item, or how often a stated item turns out to be wrong.
- The FinCEN search, the NMLS lookup, the eCFR, the New York letter, and the AICPA page are web pages without a fixed version link. They were read on the date given, and can change. The two PDFs are identified by their SHA-256 hashes.
- A missing item means only that a holder could not find it. The item may exist and not be published.

## 8. References

Each source is listed once with the version consulted and the sections that cite it.

**FinCEN**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [FIN-2019-G001](https://www.fincen.gov/system/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf), issued 9 May 2019, SHA-256 `7f4ffebd…3e1f`, read 2 November 2026 | FinCEN's treatment of hosted, unhosted, and multiple-signature wallet providers | Start here, §2, §3.1, §6 |
| [31 CFR 1022.380](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022/subpart-C/section-1022.380), read 2 November 2026 | The registration requirement for money services businesses | §3.2 |
| [MSB Registrant Search](https://msb.fincen.gov/), read 2 November 2026 | The public list of current registrations, and its stated limits | Start here, §3.2, §4, §6 |

**State regulators**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [NMLS Consumer Access](https://www.nmlsconsumeraccess.org/), read 2 November 2026 | The state license lookup and who runs it | Start here, §3.3, §4 |
| [New York DFS Industry Letter, 30 September 2025](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20250930-updated-guidance-custodial-structures), read 2 November 2026 | New York's expectations for virtual currency custodians on separation, property, and disclosure | §3.4, §4 |

**OCC**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Interpretive Letter 1170](https://www.occ.gov/topics/charters-and-licensing/interpretations-and-decisions/2020/int1170.pdf), 22 July 2020, SHA-256 `5744d487…acd3`, read 2 November 2026 | A national bank's authority to provide custody by holding cryptographic keys | §3.5, §4 |

**AICPA**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [SOC 3® - SOC for Service Organizations: Trust Services Criteria for General Use Report](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3), read 2 November 2026 | The SOC 3 report as a general-use report | Start here, §1.2, §3.6, §4, §6 |

**This repository**

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md) | Terms, scenarios, the audit and insurance rows, recovery, and privacy | §1.1, §1.2, §2, §4 |
| [What Can You Check About a Software Release?](what-can-you-check-about-a-release.md) | The fixed entries | §1.1 |

## Changelog

Newest first. Versioning follows [STYLE.md](STYLE.md). Version tags use the prefix `custodian-v`, and each version links to its tagged text.

| Version | Change |
| :---- | :---- |
| [0.2](https://github.com/more-eyes/notes/blob/custodian-v0.2/what-can-you-check-about-a-custodian.md) — 3 November 2026 | Review fixes. Adds the OCC letter to the §7 source list. Links §3.5 from baseline item 4, and states there that the note gives no record for confirming a charter. Removes the statements in Start here and §4 about how a SOC 2 report is given out, which §3.6 does not source. Names the five baseline items that §5 leaves out, and why, and matches the item 8 label to §4. Drops the unused "Not applicable" entry from §1.1. Fixes wording in the §3.3 Unresolved line, and names the publisher of the SOC 3 page as the AICPA in §3.6, as STYLE.md does. Adds §4 to the OCC letter's "Cited in" entry. |
| [0.1](https://github.com/more-eyes/notes/blob/custodian-v0.1/what-can-you-check-about-a-custodian.md) — 2 November 2026 | First draft. Two roles, full-custody and co-signing, and three levels for each item: missing, stated, checkable. Records for FinCEN guidance FIN-2019-G001, the FinCEN registration rule and registrant search, the NMLS Consumer Access lookup, New York's 2025 custody guidance, OCC Interpretive Letter 1170, and the AICPA's description of SOC 3, dated or hashed. An eleven-item baseline, a pattern walked through it, and reviewable claims. |
