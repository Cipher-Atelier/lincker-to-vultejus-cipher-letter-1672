# Lincker’s cipher letter to Vultejus (May 1672)

A cipher letter from Lincker to Vultejus, written in Hamburg in May 1672 and catalogued as HCP494. A related historical key from 1666 survives.

## What has been found?

The surviving key supports two short sequences, with source corrections and unresolved word codes. The main-block literal is shown below. The available vocabulary does not contain the higher-number codes needed for a complete reading.

A small example from the recorded result:

```text
disgustirtundertanin[634]
```

This is the literal output before deciding word boundaries or syntax. [634] stays an unresolved code; Holstein is not an established dictionary value for it.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Saved outputs for sequences A and B](verification/readings/VERIFIED_REPLAY_RESULTS.json) to inspect the saved text or test result itself.
3. Read the [research account](lincker-1672/README.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/494); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Two short sequences reconstructed using the surviving 1666 key. Existing historical glosses are not new plaintext; high-number word codes remain unresolved.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
