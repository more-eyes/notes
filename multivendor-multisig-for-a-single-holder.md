# What Does Multivendor Multisig Take for One Holder?

*You have decided to do it. Now what?*

It describes kinds of setups, not companies.

| Document | multivendor-multisig-for-a-single-holder.md |
| :---- | :---- |
| **Version** | 0.2 — draft |
| **Audience** | People who hold their own bitcoin and have decided on a multivendor multisig: read [Start here](#start-here), then §2 to §10 as the job reaches each step. Technical reviewers: read the full note and its [References](#12-references). |
| **Method** | Take the setup as it is usually pitched: several keys, devices from different makers, backups in different places. Write down every thing a single holder has to make, place, check, and keep doing for the pitch's promises to hold. Tie each step to the promise it serves. |
| **Changes** | See the [changelog](#changelog). |
| **Scope** | One holder, a plain 2-of-3 or 3-of-5 multisig, no other spending paths, no other people. Not a review method: for that, see [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md). Not a ranking of setups or devices. |

## Contents

- [Start here](#start-here)
- [1. What the note covers](#1-what-the-note-covers)
  - [1.1 Terms](#11-terms)
- [2. What the numbers give you](#2-what-the-numbers-give-you)
- [3. Places: where the keys go](#3-places-where-the-keys-go)
- [4. The setup record](#4-the-setup-record)
- [5. Setup day](#5-setup-day)
- [6. What a spend looks like](#6-what-a-spend-looks-like)
- [7. Practice](#7-practice)
- [8. Upkeep, and when something goes wrong](#8-upkeep-and-when-something-goes-wrong)
- [9. The whole job on one page](#9-the-whole-job-on-one-page)
- [10. Questions to ask a device maker](#10-questions-to-ask-a-device-maker)
- [11. Limits and source use](#11-limits-and-source-use)
- [12. References](#12-references)
- [Changelog](#changelog)

## Start here

This section is for anyone who has decided to hold bitcoin in a "multivendor multisig, keys in different places" setup. You do not need technical knowledge to use it.

**What the words mean.** Secret numbers called keys control bitcoin. A multisig wallet has several keys and needs some of them to spend. "2-of-3" means three keys exist and any two can spend. "Multivendor" means the keys live on signing devices from different makers. "Keys in different places" means the backups of the keys are stored apart, so that one fire or one burglary does not reach them all.

**What the pitch promises.** The pitch makes three promises:

1. A thief who gets one key, or gets into one place, cannot spend.
2. If you lose one key, or one place, you can still spend.
3. A problem with one maker's devices does not take down the whole wallet.

**What it actually takes.** Each promise holds only if you do the work behind it. In a solo setup, nobody else makes, stores, checks, or uses the keys. The job is:

- **Check each maker's claims first.** You are choosing a maker because of what it says about its devices. Check the claims you rely on before you build the wallet around them. See [§10](#10-questions-to-ask-a-device-maker).
- **Make separate keys.** Each device makes its own key. You write down each key's backup words. See [§5](#5-setup-day).
- **Keep the setup record.** The wallet needs a file that lists every key and the rules. Without it, the backups alone may not be enough to get your bitcoin back. Keep enough copies that the losses you plan for still leave one. See [§4](#4-the-setup-record).
- **Pick the places.** No single place may hold enough keys to spend. Count devices as well as backups. See [§3](#3-places-where-the-keys-go).
- **Check on the device, not the computer.** Your computer touches every key. Each device has to show you the wallet and the payment, and you have to read it. Devices from different makers do not protect you from a computer you do not check. See [§5](#5-setup-day) and [§6](#6-what-a-spend-looks-like).
- **Plan the trip.** To spend, you have to reach enough keys. With keys in different places, a spend means travel, or bringing keys together for a while. See [§6](#6-what-a-spend-looks-like).
- **Practice.** Recover a key, and spend with a place missing, before you put real money in. Do it again after anything changes. See [§7](#7-practice).
- **Keep it up.** Devices get updates, makers stop support, people move house. Each change is work. See [§8](#8-upkeep-and-when-something-goes-wrong).

**2-of-3 or 3-of-5?** More keys do not give you more protection unless you also use more places, more trips, and more practice. A 3-of-5 kept in three places protects against lost places no better than a 2-of-3 kept in three places. The table in [§3](#3-places-where-the-keys-go) shows why.

**What this note does not do.** It does not say that multisig is right for you, or name any device or company. It does not cover inheritance, sharing keys with family, or wallets with timed recovery paths. Adding any other person or company to the setup changes what each promise depends on. See [§1](#1-what-the-note-covers). It lists the work so you can see the whole job before you start.

## 1. What the note covers

The note covers one holder and a plain threshold multisig: t of n keys can spend, and the wallet has no other spending path. It covers 2-of-3 and 3-of-5, written as `wsh(sortedmulti(...))` descriptors. [Multisig descriptors (BIP 383)](https://bips.dev/383/)

The pitch is a set of promises about a deployment. The protocol enforces only the threshold: the output can be spent by valid signatures from t of the listed keys. Where the keys are, who made the devices, and whether the holder can reach them are not things the protocol checks. They are the holder's job, and that job is what this note describes.

**Adding another person changes the setup, whoever they are.** A person or company becomes part of the setup if they hold a key, backup words, a copy of the setup record, or access to a place. What they can do depends on what they hold. With t keys, they can spend. With fewer, they can refuse, delay, or lose what they hold. They can also be the route by which a thief, or someone forcing a spend, reaches it. Each promise in Start here then depends partly on that party: their honesty, their security, their availability, and whether they still exist when needed. This is true whether the party is a relative, a friend, a lawyer, or a company that holds a key as a service. A party can also add a recovery route that the holder does not have alone. Whether that trade is worth making is the holder's decision. The custody note covers how to review it. [Scenario B](who-can-move-your-bitcoin.md#22-scenario-b--collaborative-custody-with-a-holder-quorum), [§4](who-can-move-your-bitcoin.md#4-independence-quorum-size-and-shared-failures)

The mechanisms behind each step are described in more detail in [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md). That note is a method for reviewing a custody claim. This note is the work list for one person who builds the setup. Where a step rests on a mechanism, the section links to the custody note or to the specification.

The note makes no claim about how often any step fails. It does not say that a setup that follows every step is safe. It says what each promise depends on.

### 1.1 Terms

| Term | Meaning here |
| :---- | :---- |
| **Holder** | The one person whose bitcoin it is, and who does every step in this note. |
| **Key** | A private key that can sign for the wallet. A 2-of-3 has three keys. |
| **Backup words** | The written words (a BIP 39 mnemonic) from which a device can make the same key again. A backup is a copy of a key: whoever has the words has the key. [Mnemonic to seed (BIP 39)](https://bips.dev/39/) |
| **Signing device** | A small device that makes a key, stores it, and signs with it. A device that stores a key is a copy of that key, protected by the device's PIN and its maker's design. |
| **Device maker** | The company that designs a signing device and its software. This note calls them Maker A, Maker B, and Maker C. "Multivendor" in the pitch means devices from more than one device maker. |
| **Place** | A location where one or more copies of keys are stored: a home, a safe in another building, a deposit box. Two places are separate only if one event (a fire, a burglary, a move) cannot reach both. |
| **Setup record** | The wallet descriptor: a short text that lists every key's public part, where each key came from, the threshold, and the address type. A wallet needs it to find and spend the coins. See [§4](#4-the-setup-record). [Descriptor format (BIP 380)](https://bips.dev/380/) |
| **Coordinator** | The wallet app on the holder's computer or phone. It builds the wallet from the setup record, shows the balance, and builds transactions for the devices to sign. It touches every key's public part and every transaction. |
| **Unsigned transaction** | A file (a PSBT) that carries a payment from the coordinator to each device, and carries each device's signature back. [Partially signed transaction format (BIP 174)](https://bips.dev/174/) |

## 2. What the numbers give you

For a plain t-of-n wallet with separate keys and the setup record available:

| | 2-of-3 | 3-of-5 |
| :---- | :---- | :---- |
| **Keys needed to spend** | 2 | 3 |
| **Keys you can lose and still spend** | 1 | 2 |
| **Keys a thief needs** | 2 | 3 |
| **Keys left to you after a thief gets enough to spend** | 1, too few to move the coins first | 2, too few to move the coins first |
| **Devices to buy, set up, and update** | 3 | 5 |
| **Backups to make and store** | 3 | 5 |

These counts hold only while the setup record survives ([§4](#4-the-setup-record)) and only while the keys are truly separate ([§5](#5-setup-day)). They count keys, not places. A promise about places depends on where the keys are, which [§3](#3-places-where-the-keys-go) covers. The custody note gives the general rule. [Independence and quorum size](who-can-move-your-bitcoin.md#4-independence-quorum-size-and-shared-failures)

In both setups, a thief who gets enough keys to spend leaves you too few to race them. The only defense against theft is that the thief never reaches t keys.

## 3. Places: where the keys go

**Count every copy.** Each key can exist in more than one copy: the backup words, and the device that stores the key. List each place and every copy in it. A place holds a key if any copy of that key is there.

**The two rules.**

1. **No place holds t keys.** Otherwise one burglary at that place is a spend. For a 2-of-3, no place may hold two different keys. That counts devices, not just backups: two devices for different keys in one drawer is two keys in one place. If you do keep several devices together, that place's safety rests on the devices' PINs and designs instead of on distance. Write that down as a choice.
2. **Losing the places you plan for leaves t keys.** Decide which losses you are planning for: one place, or two. Then check that every such loss leaves t keys and a copy of the setup record.

**Keep each device with its own backup, or count the key twice.** A device at home and its backup words at Place 2 put the same key in two places. That helps against loss, because both copies must be lost. It hurts against theft, because either copy gives the key.

**What the places give you.** Each place in these examples holds no more than t−1 keys, and a copy of the setup record:

| Setup | Keys per place | Places a thief must reach | Places you can lose and still spend |
| :---- | :---- | :---- | :---- |
| **2-of-3 in 3 places** | 1, 1, 1 | 2 | 1 |
| **3-of-5 in 3 places** | 2, 2, 1 | 2 | 1 |
| **3-of-5 in 4 places** | 2, 1, 1, 1 | 2 | 1 |
| **3-of-5 in 5 places** | 1, 1, 1, 1, 1 | 3 | 2 |

The arithmetic follows from §2. A 3-of-5 in fewer than five places gives the same protection against lost and broken-into places as a 2-of-3 in three. It still covers more losses of single copies, such as one set of backup words that is damaged while its place is fine. The extra protection against places comes only with five separate places.

**What makes places separate.** For each pair of places, ask what single event reaches both: the same building, the same street in a flood, the same household, the same person with keys to both. A place you cannot reach for a month, such as a box at a bank that has closed for a holiday, is a place you have lost for that month.

**Places that belong to someone else.** A deposit box, or a drawer at a relative's house, is a place where another person controls access. With fewer than t keys there, that person cannot spend. They can refuse or delay your access, and a thief who gets into their place gets that key. Count it as a place that can be lost or broken into, and record who controls access. [§1](#1-what-the-note-covers) covers what any added party changes.

**Distance has a cost.** The farther apart the places are, the longer a spend takes ([§6](#6-what-a-spend-looks-like)), and the harder a check of each place is ([§8](#8-upkeep-and-when-something-goes-wrong)). Pick distances you can travel to when you need to, including when you are ill or away.

## 4. The setup record

**What it is.** The setup record lists every key's public part (an xpub), each key's fingerprint and derivation path, the threshold, and the address type. With it, any compatible coordinator can rebuild the wallet. [Descriptor format (BIP 380)](https://bips.dev/380/)

**Why the backups are not enough without it.** Backup words make one key. They do not say which wallet the key belongs to, which other keys are in it, or how many must sign. BIP 380 states the problem for any wallet restored from its keys alone: "it is not possible for restored wallets to know which kinds of output scripts and addresses to produce." [Descriptor format (BIP 380)](https://bips.dev/380/)

In a 2-of-3, two sets of backup words give two keys, but not the public part of the third key. Every address uses all three public parts. So two backups, without the setup record and without the third backup, cannot rebuild the addresses, even though two keys are enough to sign. Before deciding that the coins are lost, look for every other record of the third key's public part: another copy of the setup record, a coordinator export, or a wallet stored on a device. [Wallet metadata](who-can-move-your-bitcoin.md#24-scenario-d--holder-controlled-2-of-3)

**How many copies.** The setup record has to survive every loss the setup plans for. Keeping it in one separate place adds a single place whose loss, together with one key, can lock the wallet. One way to meet the rule is a copy with each set of backup words.

**What a copy costs.** The setup record does not let anyone spend, but it lets anyone who reads it see every address in the wallet, and so the balance and the payment history. A thief who finds one place learns the balance as well as one key. Weigh that against the risk of losing the wallet, and record the choice. [Extended keys and privacy (BIP 32)](https://bips.dev/32/), [Multisig descriptors (BIP 383)](https://bips.dev/383/)

**Make it complete.** Check that the copy includes each key's fingerprint and path, not only the xpubs. BIP 48 sets out a common path for multisig keys, `m/48'/0'/0'/2'` for this address type. A common path does not prove that a given wallet used it, so record the path the wallet actually used. [Multisig derivation (BIP 48)](https://bips.dev/48/)

**Check that it works.** A copy you have never rebuilt the wallet from is a copy you have not checked. [§7](#7-practice) includes this.

## 5. Setup day

Do these steps in order, with a small amount of bitcoin, before you move savings into the wallet.

1. **Check each maker's claims.** For each maker you plan to use, list the claims that made you choose it, and put each one to the questions in [§10](#10-questions-to-ask-a-device-maker). Do this before you buy, or at least before any key is made on the device. A claim that has no checkable answer is not established. Decide whether to use that maker anyway, and write the decision down, or choose another maker.
2. **Get the devices.** No one maker's devices may hold t keys, or a defect at that maker reaches enough keys to spend or to lock the wallet. For a 2-of-3, that means one device each from Maker A, Maker B, and Maker C. For a 3-of-5, it means at least three makers, with no more than two devices from any one. Record where each came from, and how you checked that its software is the maker's real software. The custody note lists what to record. [Creation and supply chain](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle)
3. **Let each device make its own key.** Never type one key's backup words into another device or into a computer. A key made on one device and copied to another is one key in two places, not two keys.
4. **Write each set of backup words on durable material.** Read each set back against the device as stored, so that a missing or wrong word shows up now, not on recovery day.
5. **Decide about passphrases.** A BIP 39 passphrase adds a second secret to a key. If you use one, it is a further item to back up for that key. Every passphrase makes a valid key: a typo makes a different key, with no error message. If you use the same passphrase for every key, losing it can lock every key at once. Check each key's fingerprint against the setup record after you enter a passphrase. [Mnemonic to seed (BIP 39)](https://bips.dev/39/), [Shared passphrase](who-can-move-your-bitcoin.md#4-independence-quorum-size-and-shared-failures)
6. **Build the wallet.** Export each device's xpub and fingerprint to the coordinator. The coordinator builds the setup record. Save copies as [§4](#4-the-setup-record) describes.
7. **Register the wallet on each device that supports it, and read the screen.** The device should show the threshold and each key's fingerprint. Compare them with the setup record. Wallet registration exists because the computer running the coordinator "is considered untrusted": the device, not the computer, must show you the policy and check that change returns to the same wallet. Whether a given device does this is something to check on that device. [Wallet policies (BIP 388)](https://bips.dev/388/)
8. **Check an address on more than one device.** Ask for the first receive address on the coordinator and on at least two devices. They must match. Then send a small amount to it.
9. **Check that each key can move to another maker's device.** If Maker B stops supporting its device, you will need to restore key B on some other device. That works only if the backup words use a standard format and the path is recorded. Backup words are a separate standard (BIP 39) from the setup record and unsigned transactions. A wallet can read the setup record and sign or combine transactions without being able to restore a key from backup words. Check that each device or program you plan to restore with reads them, and test it. [Mnemonic to seed (BIP 39)](https://bips.dev/39/), [Descriptor format (BIP 380)](https://bips.dev/380/), [Partially signed transaction format (BIP 174)](https://bips.dev/174/) Test it now with a spare device: restore one key and compare its fingerprint with the setup record. This is the third promise of the pitch, for a maker that goes away rather than a maker with a defect.
10. **Do one practice spend** of the small amount, by the route you will use for real ([§6](#6-what-a-spend-looks-like)).

**What "multivendor" does and does not cover.** Devices from different makers mean that a defect in one maker's device or software reaches only the keys on that maker's devices. That protects the wallet only while those keys number fewer than t ([step 2](#5-setup-day)). The coordinator is not one of the devices. It reaches every key's public part and every transaction. If you approve what the computer shows instead of what each device shows, one bad computer, or one bad coordinator update, can mislead every device at once. The protection comes from reading each device's own screen at setup ([step 7](#5-setup-day)) and at every spend ([§6](#6-what-a-spend-looks-like)). [Shared components](who-can-move-your-bitcoin.md#4-independence-quorum-size-and-shared-failures)

## 6. What a spend looks like

To spend, you need signatures from t devices. With the keys in different places, there are two ways to get them.

**Carry the unsigned transaction.** The coordinator makes an unsigned transaction. You take it, on a memory card or as QR codes, to each place in turn, and the device there adds its signature. Back home, the coordinator combines the signatures and sends the transaction. The format is built for this: a device that signs it does not need to be online, and the file carries what the device needs. The keys never leave their places. The file does show the payment and parts of the wallet, so treat it as private. [Partially signed transaction format (BIP 174)](https://bips.dev/174/)

**Bring the keys together.** You bring t devices, or t sets of backup words, to one place, sign, and take them back. This is quicker. While they are together, that one place holds enough keys to spend. Record where they meet and for how long. [Signing location and exposure](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle)

**What a spend costs in travel.** If home is one of the places, a 2-of-3 spend is one trip to a second place. A 3-of-5 spend is two trips. A spend you need on short notice depends on reaching those places on short notice.

**What to read on each device.** At each signature, read the device's screen: the address you are paying, the amount, the fee, and whether the change goes back to the same wallet. The device shows you what it signs, and the coordinator may not. [Wallet policies (BIP 388)](https://bips.dev/388/), [Signer policy validation](who-can-move-your-bitcoin.md#24-scenario-d--holder-controlled-2-of-3)

**Someone forcing you to spend.** In a solo setup you alone can reach t keys. A person who forces you to spend can get what you can get. Distance can slow a forced spend, and it slows your own spends by the same amount. [Privacy and coercion](who-can-move-your-bitcoin.md#5-privacy-and-coercion)

## 7. Practice

A step that has not been practiced is a step you do not know works. Practice with a small amount, before the wallet holds savings, and again after anything in §8 changes.

1. **Rebuild from the setup record.** On a clean install of a coordinator, rebuild the wallet from one copy of the setup record. Check that it shows the same first address and the same balance. Do this for each copy you keep, or check that each copy is identical.
2. **Restore a key.** Wipe a device, or use a spare, and restore one key from its backup words. Check its fingerprint against the setup record.
3. **Spend with a place missing.** For each loss you plan for, act as if those places were gone, and spend using only what is left. For a 2-of-3 in three places, that is three practice spends, one with each place missing. For a 3-of-5 in five places with two losses planned, list the pairs and practice at least the ones that leave you the hardest trip.
4. **Write the steps down.** Write down how you did each step, in words you could follow after a year away from it. A procedure that lives only in your head is not a backup.

## 8. Upkeep, and when something goes wrong

**Regular upkeep.**

- **Device updates.** Each maker updates its devices on its own schedule. After an update, check that the device still shows the wallet, still shows the right fingerprint, and can still sign. Record who can issue updates for each device. [Update authority](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle)
- **A maker stops support.** Restore that key on another device, as tested in [§5 step 9](#5-setup-day), and register the wallet there. Use a device or program that you have checked reads backup words.
- **Visiting the places.** On a schedule you choose, check that each place still holds what your list says and shows no sign of tampering. Check that the backup material is still readable.
- **A place changes.** You move house, a box is closed, a relative moves. Redo the count in [§3](#3-places-where-the-keys-go) before you move anything.

**When something is lost.** After losing one key in a 2-of-3, you can still spend, with no spare. Losing one more locks the coins. Make a new wallet with new keys, and move the coins to it while you still have t keys. If only one copy of a key is lost, such as its backup words while its device still works, ask whether someone else could have found it. If they could, treat that key as stolen. [Rotation and exit](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle)

**When something may be stolen.** If one place may have been broken into, treat its keys and its setup record as taken. The thief now needs t keys minus the ones they have. Move the coins to a new wallet before they reach another place.

**Old backups.** After moving to a new wallet, the old backup words and old setup record still control any coins at the old addresses. Decide what to do with them, and check that the old wallet is empty.

## 9. The whole job on one page

| | 2-of-3 | 3-of-5 |
| :---- | :---- | :---- |
| **Makers whose claims you checked (§10)** | 3 | At least 3 |
| **Devices, so no maker holds t keys** | 3, one each from Makers A, B, C | 5, from at least 3 makers, no more than 2 from one |
| **Sets of backup words** | 3 | 5 |
| **Copies of the setup record** | One with each set of backup words, or enough to survive every planned loss | Same |
| **Places, so no place holds t keys** | At least 3 | At least 3 |
| **Places, so any two can be lost** | Not possible: losing two places leaves at most one key | 5 |
| **Trips per spend, if home is one place** | 1 | 2 |
| **Checks on each device's screen at setup** | Threshold, fingerprints, first address | Same |
| **Practice spends with a place missing** | 3, one per place | One for each planned loss |
| **Upkeep** | 3 devices to update, 3 places to visit | 5 devices to update, up to 5 places to visit |

## 10. Questions to ask a device maker

The third promise of the pitch rests on the device makers. You choose Maker A because of what Maker A says: about its keys, its software, its backups, its multisig support. Each claim you rely on is a claim to check before Maker A's device goes into the wallet. The other more eyes notes are written for that check. This section points to them.

**How to judge an answer.** A good answer shows you something you can open: a document, a signed file, a build report, a test you ran yourself. A weak answer repeats the claim in different words. A weak answer does not prove a problem. It shows that the claim is not established yet. Makers publish different things, so expect different answers from Maker A, Maker B, and Maker C.

| If the maker claims | Ask for | Read more |
| :---- | :---- | :---- |
| **Keys never leave the device** | What crosses the cable, card, or QR codes in each direction. Every backup, export, and debug path, and whether any of them puts a key outside the device. A key can also leak through signatures without leaving as a key. | [Custody note §6](who-can-move-your-bitcoin.md#6-questions-that-make-a-claim-reviewable), [§3](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle) |
| **Air-gapped** | Which medium carries data to and from the device. A card or QR code changes how data crosses, not whether it crosses. | [Custody note §1.2, transfer channel](who-can-move-your-bitcoin.md#12-terms-and-boundaries) |
| **The device shows you what you sign** | A demonstration, for this multisig address type, that the device shows the threshold and every key's fingerprint at setup, and the address, amount, fee, and change at each spend. Run it yourself in [§5](#5-setup-day) before funding. | [Custody note §6](who-can-move-your-bitcoin.md#6-questions-that-make-a-claim-reviewable), [Scenario D](who-can-move-your-bitcoin.md#24-scenario-d--holder-controlled-2-of-3), [Wallet policies (BIP 388)](https://bips.dev/388/) |
| **Works with any multisig wallet** | Whether it signs a `wsh(sortedmulti(...))` wallet, exports its xpub with fingerprint and path, signs unsigned transactions (PSBTs), and registers the wallet. Test it with your coordinator. | [Scenario D](who-can-move-your-bitcoin.md#24-scenario-d--holder-controlled-2-of-3) |
| **Standard backup, restore anywhere** | Whether the backup is standard BIP 39 words. A restore of the same words on another maker's device that gives the same fingerprint. If there are no words, what the backup is and what reads it. | [§5 step 9](#5-setup-day), [Custody note §6](who-can-move-your-bitcoin.md#6-questions-that-make-a-claim-reviewable), [Mnemonic to seed (BIP 39)](https://bips.dev/39/) |
| **Open source** | The tag or commit the firmware you install was built from, and the public history behind it. A license does not identify the file you install. | [Release note §6](what-can-you-check-about-a-release.md#6-questions-that-make-a-claim-reviewable) |
| **Reproducible or verified firmware** | Which of the four levels of build evidence is shown, for the firmware actually on the device, and by whom. A second builder's signed report of the same hash. | [Custody note §6](who-can-move-your-bitcoin.md#6-questions-that-make-a-claim-reviewable), [Release note §2](what-can-you-check-about-a-release.md#2-three-checks) |
| **Signed firmware and updates** | What the signature covers, how you tie the key to the maker, and who can sign an update. | [Release note §6](what-can-you-check-about-a-release.md#6-questions-that-make-a-claim-reviewable), [Custody note §3](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle) |
| **Keys come from a true hardware random source** | The build setting and the function that key creation calls, and a check that fails if another source is used. Code that is present is not proof that it runs. | [Which Code Actually Runs? §6](which-code-actually-runs.md#6-questions-that-make-a-claim-reviewable) |
| **Built on a well-reviewed library** | Which library and version, how it was obtained, and which implementation inside it does the job. | [Which Code Actually Runs? §2](which-code-actually-runs.md#2-kinds-of-fallback), [the embit note](embit-release-records.md#7-questions-that-make-a-claim-reviewable) as a worked example |
| **Audited** | The report: its subject, scope, date, and exclusions. A code review and a security test of one model answer different questions. | [Custody note §1.1](who-can-move-your-bitcoin.md#11-evidence-and-verdicts) |

Put the same questions to each maker. A maker whose answers you have checked still covers only the keys on its own devices ([§5](#5-setup-day)). The shared parts, such as the coordinator and the places, are checked in the other sections of this note.

## 11. Limits and source use

- This note covers one holder and a plain t-of-n `wsh(sortedmulti(...))` wallet with no other spending path. It does not cover Taproot wallets, timed recovery paths, keys held by a service or by other people, or inheritance. For those, see [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md).
- If the holder dies or cannot act, every step in this note falls to someone who did not build the setup. That is outside this note. The custody note covers it under recovery and succession. [Recovery and succession](who-can-move-your-bitcoin.md#3-review-the-complete-custody-lifecycle)
- This note names no device, coordinator, or company. "Maker A" and "Maker B" are labels, not products.
- The note makes no claim about how often any step goes wrong. A setup that follows every step is not shown to be safe, and a setup that skips one is not shown to be unsafe. A skipped step means the promise that depends on it is not shown.
- Statements about what a specification requires describe the specification. Whether a given device or coordinator does what the specification describes is something to check on that device or coordinator.
- The counts in §2, §3, and §9 are arithmetic from the threshold. They assume separate keys, a surviving setup record, and no other spending path.

**Unresolved.**

- No signing device or coordinator was tested for this note. Whether a given device registers a wallet, shows the threshold and fingerprints, or checks change ([§5](#5-setup-day), [§6](#6-what-a-spend-looks-like)) has to be checked on that device.
- The steps in §5 to §8 have not been carried out end to end for this note. They are drawn from the specifications and the custody note, not from a recorded run.
- The counts in the §3 and §9 tables were worked by hand and have not had a second check.
- The questions in §10 have not been put to any device maker for this note.

## 12. References

Each source is listed once with the version consulted and the sections that cite it. The BIPs were read on 23 October 2026 at the commit given, the same commit the custody note cites.

| Reference | What it defines | Cited in |
| :---- | :---- | :---- |
| [BIP 32](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0032.mediawiki) | Hierarchical Deterministic Wallets: extended keys, and what sharing an extended public key reveals | §4 |
| [BIP 39](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0039.mediawiki) | Mnemonic code for generating deterministic keys, including the optional passphrase | §1.1, §5, §10 |
| [BIP 48](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0048.mediawiki) | Multi-Script Hierarchy for Multi-Sig Wallets: the `m/48'` derivation path and script type levels | §4 |
| [BIP 174](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0174.mediawiki) | Partially Signed Bitcoin Transaction format and its roles | §1.1, §5, §6 |
| [BIP 380](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0380.mediawiki) | Output Script Descriptors: general format, and key origin information | §1.1, §4, §5 |
| [BIP 383](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0383.mediawiki) | Multisig Output Script Descriptors: `multi()` and `sortedmulti()` | §1, §4 |
| [BIP 388](https://github.com/bitcoin/bips/blob/927b6de9915c9262615a6399de51b200f81e5aa4/bip-0388.mediawiki) | Wallet Policies for Descriptor Wallets, including policy registration on a signing device | §5, §6, §10 |
| [Who Can Move Your Bitcoin?](who-can-move-your-bitcoin.md) | Review method; Scenario D (holder-controlled 2-of-3); the custody lifecycle; independence and quorum size; coercion; questions for device claims | §1, §2, §3, §4, §5, §6, §8, §10, §11 |
| [What Can You Check About a Software Release?](what-can-you-check-about-a-release.md) | The three checks, and questions for release claims | §10 |
| [Which Code Actually Runs?](which-code-actually-runs.md) | Fallbacks in software that makes or uses keys, and questions for those claims | §10 |
| [What Can You Check About an embit Release?](embit-release-records.md) | A worked example of the release questions put to one library | §10 |

## Changelog

Newest first. Versioning follows [STYLE.md](STYLE.md). Version tags use the prefix `multisig-v`, and each released version links to its tagged text.

| Version | Change |
| :---- | :---- |
| [0.2](https://github.com/more-eyes/notes/blob/multisig-v0.2/multivendor-multisig-for-a-single-holder.md) — 23 October 2026 | First release. The work a single holder does to set up, place, spend from, practice, and keep up a plain 2-of-3 or 3-of-5 multisig with devices from different makers, and questions to put to each device maker that point to the other notes. Names no device or company. The text is the 0.1 draft with only the version line and this changelog changed. |
| 0.1 — 23 October 2026 | Not released. The tag `multisig-v0.1` was created on commit `fc1ee71` before the note was merged, and does not contain this note. Tags are not moved or deleted, so the note is released as 0.2. |
