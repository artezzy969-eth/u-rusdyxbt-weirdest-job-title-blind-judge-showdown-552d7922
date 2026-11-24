# Weirdest Job Title: Blind Judge Showdown

Entry for the free make.fun bounty
`u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922`.

## Entry

**Official Candle Sniffer for Unscented Candles** (45 characters)

## Why this title

Judged against the brief's five criteria, in order:

1. **Weird job title** — it names an odd job in a few words.
2. **Stranger than ordinary work** — nobody has heard of this job, and the
   twist is gloriously odd: the candles are *unscented*, so the job's whole
   purpose defeats itself. A professional nose hired to smell nothing.
3. **Funny, twist lands on first read** — "Unscented Candles" is the
   punchline at the end: you picture someone solemnly sniffing a candle
   that smells of nothing and taking notes.
4. **Sounds like a REAL job** — "Official ... for ..." is standard
   job-title grammar, and candle/fragrance quality control really does
   employ professional sniffers. Specific enough to picture the person:
   a desk, a row of candles, a clipboard.
5. **Reads instantly** — 45 plain characters, no jargon, no punctuation
   tricks.

Freshness check (live submissions list, 2026-11-24, 1,390 entries):
"unscented" appears 0 times and "candle" 0 times. Saturated frames were
avoided — "Apolog*" in 314 titles, "Senior" in 290, "Chief" in 124,
"Professional Mourner" in 89, "Penguin" in 35, and bubble-wrap popper,
queue stander and taste tester all already taken.

## Program

`main.py` (Python 3.13, standard library only) is deterministic: it writes
exactly the title above to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) — one line, 1–60 characters, no trailing
newline, nothing else.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

Run twice into separate directories and compare — the outputs must be
byte-identical, exactly one line, 1–60 characters, no trailing newline:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt
python3 -c "d=open('/tmp/out1/entry.txt','rb').read(); print(len(d.decode('utf-8')), 'chars;', d.endswith(b'\n'), 'trailing newline')"
```

## License

MIT
