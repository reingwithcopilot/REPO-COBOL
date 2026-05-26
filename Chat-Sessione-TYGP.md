User: Devo analizzare tre programmi COBOL LEGACY: PDSIO05.txt, PDSIO13.txt. PDSIOX41.txt per produrre documentazione utile alla riscrittura su nuova piattaforma. Le istruzioni per te sono contenute nel file Istruzioni-TISM.md.

GitHub Copilot: Ran terminal command: cd reingCOBOL; Get-ChildItem PDSIO05.txt,PDSIO13.txt,PIOSX41.txt | Select-Object Name,Length,@{n='Lines';e={(Get-Content $_.FullName | Measure-Object -Line).Lines}}

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "=== $f ==="; $c = Get-Content $f; Write-Host "--- DIVISION/SECTION headers ---"; $c | Select-String -Pattern '^\s{6,}(IDENTIFICATION DIVISION|ENVIRONMENT DIVISION|DATA DIVISION|PROCEDURE DIVISION|WORKING-STORAGE SECTION|LINKAGE SECTION|FILE SECTION|INPUT-OUTPUT SECTION)\.' | Select-Object LineNumber,Line -First 20 | Format-Table -AutoSize -Wrap }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f - PROCEDURE DIVISION start ==="; (Get-Content $f | Select-String -Pattern '^\s*PROCEDURE DIVISION' | Select-Object -First 3) | Format-Table LineNumber,Line -AutoSize -Wrap }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f - PROCEDURE/CICS ==="; Get-Content $f | Select-String -Pattern 'PROCEDURE DIVISION|EXEC CICS|EXEC SQL' | Select-Object -First 5 | Format-Table LineNumber,Line -AutoSize -Wrap }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f === Procedure markers"; (Select-String -Path $f -Pattern 'PROCEDURE\s+DIVISION' -CaseSensitive:$false) | Format-Table LineNumber,Line -AutoSize -Wrap }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f === Stats"; $c = Get-Content $f; $par = $c | Select-String -Pattern '^\s{7}[A-Z0-9][A-Z0-9\-]+\s*\.\s*$' ; Write-Host ("Paragrafi (approx): " + $par.Count); Write-Host "--- COPY ---"; ($c | Select-String -Pattern '^\s*COPY\s+|EXEC\s+SQL\s+INCLUDE' | ForEach-Object { ($_.Line -replace '\s+',' ').Trim() } | Sort-Object -Unique) -join "`n" | Write-Host; Write-Host "--- CALL targets ---"; ($c | Select-String -Pattern "CALL\s+['""]([A-Z0-9]+)" | ForEach-Object { $_.Matches[0].Groups[1].Value } | Sort-Object -Unique) -join ', ' | Write-Host; Write-Host "--- XCTL/LINK targets (CICS) ---"; ($c | Select-String -Pattern "XCTL\s+PROGRAM|LINK\s+PROGRAM" | ForEach-Object { ($_.Line -replace '\s+',' ').Trim() } | Sort-Object -Unique) -join "`n" | Write-Host; Write-Host "--- SQL tables (FROM/INTO/UPDATE/INSERT/DELETE) ---"; ($c | Select-String -Pattern "(FROM|UPDATE|INSERT\s+INTO|DELETE\s+FROM)\s+([A-Z][A-Z0-9_]+)" | ForEach-Object { foreach($m in $_.Matches){$m.Groups[2].Value} } | Sort-Object -Unique) -join ', ' | Write-Host }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f === CICS LINK/XCTL (all) and CALLs"; (Select-String -Path $f -Pattern 'EXEC\s+CICS\s+(LINK|XCTL|RETURN)' -CaseSensitive:$false) | ForEach-Object { ($_.Line -replace '\s+',' ').Trim() } | Sort-Object -Unique; Write-Host "--- variable CALL refs ---"; (Select-String -Path $f -Pattern '\bCALL\s+' -CaseSensitive:$false) | ForEach-Object { ($_.Line -replace '\s+',' ').Trim() } | Sort-Object -Unique }

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL)

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; foreach ($f in 'PDSIO05.txt','PDSIO13.txt','PIOSX41.txt') { Write-Host "`n=== $f === First 20 lines after PROCEDURE DIVISION + GOBACK/RETURN/STOP RUN"; $c = Get-Content $f; $pd = ($c | Select-String -Pattern 'PROCEDURE\s+DIVISION' -CaseSensitive:$false | Select-Object -First 1).LineNumber; $c[($pd-1)..($pd+30)]; Write-Host "--- terminations ---"; $c | Select-String -Pattern 'GOBACK|STOP\s+RUN|EXEC\s+CICS\s+RETURN' -CaseSensitive:$false | Select-Object -First 8 | Format-Table LineNumber,Line -Wrap }

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/2026.05.13.TISC-AnalisiFunzionale.md#1-1), lines 1 to 80

# STEP 0 — Riconoscimento strutturale e domande preliminari

Seguo la metodologia in Istruzioni-TISM.md. Mi fermo a questo step in attesa di validazione prima di passare a STEP 1 (pseudocodifica).

> Nota preliminare: nella tua richiesta è citato `PDSIOX41.txt`; nello workspace il file è PIOSX41.txt. Procedo su questo, confermami se è corretto.

## Vincoli metodologici dichiarati

1. **Fedeltà al codice**: nessuna normalizzazione; bypass/flag enigmatici → marcati `[DA_CHIARIRE]`.
2. **Riferimenti di riga** in formato `[righe XXXX-YYYY]` su ogni paragrafo pseudo.
3. **Black-box**: sottoprogrammi non disponibili nel workspace documentati solo per contratto I/O.
4. **Dettaglio proporzionato**: variabili tecniche, contatori, indici → fuori dalla pseudo principale.
5. **Osservazione ≠ interpretazione**: in Fase A solo ciò che il codice fa.

## Inventario strutturale

### PDSIO05.txt — 8.057 righe

- **PROGRAM-ID**: `PDSIO05` — *Programma Disoccupazione Interv.Occupaz. n.05* (elabora biglietto contabile)
- **Chiamante dichiarato**: `PDSIO01`
- **DIVISION**: IDENTIFICATION [2], ENVIRONMENT [308], DATA [321], WORKING-STORAGE [324], LINKAGE [1992], PROCEDURE [2014]
- **Entry**: `PROCEDURE DIVISION USING COMMAREADS` → `MAIN` → `I00-INIZIALI` / `C00-CENTRALI` / `F00-FINALI`
- **Exit**: `GOBACK` (riga 5429, oltre alcuni `goback` condizionali)
- **Paragrafi (approx)**: ~131
- **CALL esterne (attive)**: `PDSPD13`, `PDSPD16`, `RDSPD05`, `RDSPD06`
- **CALL commentate / storiche**: `POPCF74`, `RDSTART`, `POPWMAIN` (LINK CICS commentato)
- **Copybook / INCLUDE SQL**: `CDSTART1`, `CNPYEAR`, `DSWABNDB`, `CDSABNDB`, `SQLCA`, `TDSRPG00`, `TDSAPIO0`, `TDSASUR1`, `TDSASUR2`, `TDSCONTB`, `TDSREPOR`, `TDSSINDA`, `TDSSUSST` (commentato), `TDSSX00`, `TDSWEBFV` (commentato)
- **Tabelle SQL referenziate**: `TDSAPIO0`, `TDSASUR1`, `TDSASUR2`, `TDSCONTB`, `TDSREPOR`, `TDSRPG00`, `TDSSINDA`, `TDSSUSST`, `TDSSX00`, `TDSVPIO0`, `TDSWEBFV`, più tabelle storiche menzionate (`ANF7x`, `ASU*`, `LPU7x`, `LSU7x`, `IRPEF`, `EL`, `DEBITIINC`, `TOTAV`, `TOTDA`) — verificare se ancora in uso
- **CICS**: solo un `LINK PROGRAM('POPWMAIN')` commentato → modulo che non risulta più attivare CICS LINK

### PDSIO13.txt — 14.739 righe (il più grosso)

- **PROGRAM-ID**: `PDSIO13` — pagamenti centralizzati / orchestratore prestazioni
- **DIVISION**: IDENTIFICATION [1], ENVIRONMENT [529], DATA [545], WORKING-STORAGE [549], LINKAGE [2430], PROCEDURE [2491]
- **Entry**: `PROCEDURE DIVISION USING COMMAREADS` → `MAIN` (con copia di K-AREA, KARAMETRI-IN, KAREA-D in aree locali, perform `I00-INIZIALI`/`C00-CENTRALI`/`F00-FINALI`, restituisce `COMMAREADS-OUT`)
- **Exit**: `GOBACK` (riga 2517)
- **Paragrafi (approx)**: ~365
- **CALL esterne (attive)**:
	- Calcoli: `PIOSX41`, `PIOSU41`, `PIOSU42`, `PIOSU43`, `PIOSU44`, `PIOLP41`
	- Print/contabilità: `PDSPD04`, `PDSPD06`, `PDSPD07`, `PDSPD13`, `PDSPD16`
	- Lock/utility: `PDSLOCK` (anche via `EXEC CICS LINK`), `PDSIO21`, `RDSCONT`, `RDSIO12`, `RDSIO13`, `RDSTART`
	- Utility tecniche: `RDSUT11`, `RDSUT14`, `RDSUT27`, `RDSUT28`
	- IBAN / CF: `PITIBAN2`, `PNBTBLC2`, `PNBTCFIB`
- **CICS**: `EXEC CICS LINK PROGRAM(PDSLOCK)`, `LINK PROGRAM(POPWMAIN)` commentato
- **Copybook / INCLUDE SQL**: `CDSERR0`, `CDSIO13`, `CDSTART1`, `CDSUT14`, `CDSUT27`, `CNPGF001`, `CNPYEAR`, `DSGFCOPY`, `DSWABNDB`, `POPCSIN`, `CDSABNDB`, `SQLCA`, `TDSANFDI`, `TDSAPIO0`, `TDSASU`, `TDSASU2`, `TDSATTSU`, `TDSDATAN`, `TDSDATCO`, `TDSDELSI`, `TDSLAV`, `TDSLAVPU`, `TDSLIST`, `TDSMODAN`, `TDSPAG`, `TDSPEERE`, `TDSPERIO`, `TDSRECUP`, `TDSREPOR`, `TDSRPG00`, `TDSSITDO`, `TDSSOSPE`, `TDSSUSST`, `TDSSX00`
- **Tabelle SQL referenziate**: tutte le precedenti più nomi sospetti (`CTR`, `OC`, `W8`, `WIC`, `THRU`) → quasi sicuramente falsi positivi nel mio regex (parole adiacenti a FROM in commenti); da rivalidare a STEP 1.

### PIOSX41.txt — 9.771 righe

- **PROGRAM-ID**: `PIOSX41` — *calcolo sussidio straordinario*
- **Chiamante dichiarato**: `PDSIO13`
- **DIVISION**: IDENTIFICATION [1], ENVIRONMENT [344], DATA [353], WORKING-STORAGE [358], LINKAGE [837], PROCEDURE [842]
- **Entry**: `PROCEDURE DIVISION USING COMMAREADS` → `MAIN-CALCOLO` → `A00-APRI`, `B00-CONTROLLA`, poi gigantesca selezione per `IC-SSTCODIND` (TRAC/TRAF/TRAS/TRAP/CRED/TYGM/TIPO/DL76/TYRG/TYBL/TYCR/RATA/RATM/TEIG/…)
- **Exit**: `GOBACK` multipli (riga 927 “normale”, più diversi `GOBACK` di uscita anticipata in branch — da censire come [DA_CHIARIRE] se non sono giustificati da errore)
- **Paragrafi (approx)**: ~60
- **CALL esterne (attive)**: `PNPGF8E`, `RDSSX41`, `RDSUT17`, `RDSUT20`, `RDSUT21`, `RDSUT27`, `RDSUT29`, `RDSUT55`
- **CALL commentate / storiche**: `POPCF61`, `POPWMAIN`, `RDSUT55` (LINK CICS commentato)
- **Copybook / INCLUDE SQL**: `CDSGFOLD`, `CDSIO13`, `CDSSX41`, `CDSUT27`, `DSGFCOPY`, `DSWABNDB`, `CDSABNDB`, `SQLCA`, `TDSASPI`, `TDSDATAN` (commentato), `TDSDATCO`, `TDSINDIM`, `TDSNASPI`, `TDSSOSPE`, `TDSSPIO0` (commentato), `TDSSUSST`, `TDSSX00`, `TDSTAMAO`, `TDSWSCRR` (commentato), `TDSPEERE`/`TDSPEERT`/`TDSANTAS` (commentati datati)
- **Tabelle SQL referenziate**: `TDSANTAS`, `TDSAPIO0`, `TDSASPI`, `TDSDATAN`, `TDSDATCO`, `TDSINDIM`, `TDSNASPI`, `TDSPEERE`, `TDSPEERT`, `TDSSOSPE`, `TDSSPIO0`, `TDSSX00`, `TDSTAMAO`, `TDSWSCRR`, `VCAPSEDI` (più rumori `DATE`/`IC`/`IMPORTO`/`PERIODO`/`WK`/`FACIMPNETTA` dal regex, da scartare in STEP 1)

## Punti d'ingresso / uscita complessivi

- Tutti e tre i programmi sono **sotto-programmi CICS chiamati** con `COMMAREADS` come area di comunicazione (formato definito in copybook `CDSIO13`/`CDSSX41`, da rileggere puntualmente in STEP 1).
- Il flusso atteso è: `PDSIO01` → `PDSIO05` (biglietto contabile) e `PDSIO13` (orchestratore pagamento) → `PIOSX41` (calcolo importi sussidio straordinario).

## Black-box che dichiaro a priori

Sottoprogrammi non presenti nel workspace, da trattare solo per contratto I/O salvo che mi indichi diversamente:

- **CICS / sistema**: `PDSLOCK`, `POPWMAIN`, `RDSTART`.
- **Stampa/contabilità**: `PDSPD04`, `PDSPD06`, `PDSPD07`, `PDSPD13`, `PDSPD16`, `RDSPD05`, `RDSPD06`.
- **Calcoli sussidi (paralleli a PIOSX41)**: `PIOSU41`, `PIOSU42`, `PIOSU43`, `PIOSU44`, `PIOLP41`.
- **Utility tecniche / lookup**: `RDSCONT`, `RDSIO12`, `RDSIO13`, `RDSIO21`/`PDSIO21`, `RDSUT11`, `RDSUT13`, `RDSUT14`, `RDSUT17`, `RDSUT20`, `RDSUT21`, `RDSUT27`, `RDSUT28`, `RDSUT29`, `RDSUT50`, `RDSUT55`, `RDSSX41`, `RPNPERR`.
- **IBAN/codice fiscale**: `PITIBAN2`, `PNBTBLC2`, `PNBTCFIB`.
- **Fiscale**: `PNPGF8E`, `POPCF61` (commentata), `POPCF74` (commentata).
- **Copybook non presenti nel workspace** (sono dichiarazioni di record DB2/area comuni): tutti i `TDS*`, `CDS*`, `CNP*`, `DSG*`, `DSW*`, `POPCSIN`. Posso ricostruire i campi solo dalle USE nel codice (non dalle definizioni).

Impatto qualità: per la pseudocodifica posso descrivere fedelmente i **flussi** e i nomi di colonna usati nelle `EXEC SQL`, ma non posso garantire tipi/lunghezze dei campi senza i copybook. Lo segnerò come limite metodologico ricorrente.

## Materiale di supporto già presente

- 2026.05.13.TISC-AnalisiFunzionale.md — analisi funzionale TISC (esiste già un template / stile da seguire?).
- full_call_graph-parte1.mmd, full_call_graph-parte2.mmd — utili per estrazione dipendenze in Fase B.
- CHGMBAS.AS20.SRC.PDSNA13.txt, PDSNA13bis-senza-righe-vuote.txt — programma fratello `PDSNA13`, non in scope ma utile come riferimento di pattern.

## Avvertenza sulla dimensione

Totale 3 programmi = **~32.500 righe** di COBOL. Una pseudocodifica completa al livello richiesto è un deliverable molto grande. Per rispettare il vincolo di "fermata a validazione" proporrei di trattare un programma alla volta (in ordine `PIOSX41` → `PDSIO13` → `PDSIO05`, partendo dal più “foglia” e risalendo all'orchestratore, o nell'ordine che preferisci).

---

## Domande preliminari (prima di STEP 1)

1. **Conferma file**: il terzo programma è PIOSX41.txt (non `PDSIOX41`), giusto?
2. **Ordine di analisi**: procedo programma per programma (suggerito: `PIOSX41` → `PDSIO13` → `PDSIO05`) o in parallelo?
3. **Focus su una prestazione**: nel codice c’è gestione di decine di sussidi (`TISC`, `TISM`, `TIRA`, `PIAC`, `TGOP`, `TGOS`, `TGOV`, `TYGP`, `FT**`, `APA*`, `POR*`, `BRIO`, `DLI2`, `bonus E107/E109/…`). La TISC ha già la sua analisi; **vuoi che una specifica prestazione faccia da filo conduttore** (es. TISM o TIRA/PIAC più recenti) oppure analisi “generica multi-prestazione”?
4. **Copybook / schemi DB2**: sono disponibili da qualche parte i sorgenti dei copybook `TDS*`, `CDS*`, `CNP*` o lo schema DDL delle tabelle? Senza, la sezione “Modello dati” di Fase B sarà inferita dalle USE.
5. **Sottoprogrammi**: oltre a quelli del workspace, hai accesso ad almeno i sorgenti dei "fratelli" (`PIOSU41–44`, `PIOLP41`, `RDSPD06`, `PDSPD13`, `RDSUT27`)? Altrimenti restano black-box.
6. **Documentazione collaterale**: oltre alla TISC esistente, ci sono specifiche storiche (`SPCL3_INPS-AnalisiFunzionale` citato in TISC) accessibili? Mi servirebbe per non duplicare la parte "comune a tutte le prestazioni".
7. **Sezioni a bassa priorità**: ci sono blocchi che consideri **codice morto / già migrati** (es. il LINK a `POPWMAIN` commentato, vecchie tabelle ANF7x/LPU7x/LSU7x in `PDSIO05`)? Se sì, li tratto sinteticamente con `[DA_CHIARIRE]` invece che paragrafo per paragrafo.
8. **Output deliverable**: confermi `pseudocodice.md` (uno per programma) come deliverable di Fase A, e `.docx` istituzionale per la Fase B (template Sirio/INPS come la TISC esistente)?

Appena rispondi (anche solo punti 2-3-4) parto con STEP 1 sul primo programma.

User: Risposta 1: sì
Risposta 2:fai come suggerisci, programma per programma
Risposta 3: il codice del sussidio da analizzare deve essere TYGP e verificare se quali comportamenti sono uguali a TISC e dove sono diversi
Risposta 4: no
Risposta 5: restano black-box
Risposta 6: no non sono accessibili
Risposta 7: non lo so
Risposta 8: si 


GitHub Copilot: OK, parto con STEP 1 su PIOSX41.txt. Visto il focus su **TYGP** con confronto **TISC**, prima di scrivere la pseudocodifica mappo tutti i punti di codice che citano i due codici, così la pseudo avrà uno scheletro generale + dettaglio sulle ramificazioni TYGP/TISC con annotazioni di confronto. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; Write-Host "=== PIOSX41: TYGP occurrences ==="; Select-String -Path PIOSX41.txt -Pattern '"TYGP"|''TYGP''|TYGP' -CaseSensitive | Format-Table LineNumber,Line -AutoSize -Wrap; Write-Host "`n=== PIOSX41: TISC occurrences ==="; Select-String -Path PIOSX41.txt -Pattern '"TISC"|''TISC''|TISC' -CaseSensitive | Format-Table LineNumber,Line -AutoSize -Wrap

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PIOSX41.txt; Write-Host "=== Paragrafi (header) ==="; ($c | Select-String -Pattern '^\s{7}[A-Z][A-Z0-9\-]*\.\s*$') | Format-Table LineNumber,Line -AutoSize

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PIOSX41.txt; foreach ($ln in 1660,2206,4004,7480,7520,7615,7630) { Write-Host "`n--- Context around line $ln ---"; $c[($ln-1)..($ln+19)] | ForEach-Object { '{0,5} {1}' -f (++$script:i),$_ } | Out-Null; for ($i=$ln-1; $i -lt [Math]::Min($ln+25,$c.Length); $i++){ '{0,5} {1}' -f ($i+1),$c[$i] } }

Trovate le divergenze TYGP↔TISC chiave (concentrate in `B00-CONTROLLA` e `T20-CALCOLA-PERIODO`). Procedo con la lettura dei paragrafi principali per produrre la pseudocodifica. Visto il volume (9.771 righe / 56 paragrafi), uso un subagent per estrarre i flussi in parallelo, poi sintetizzo il deliverable. 

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#358-358), lines 358 to 850

Created 7 todos

Map PIOSX41 paragraphs

Searched for files matching `**/*PIOSX41*`, 1 match

Searched for files matching `**/*Analisi*.md`, 1 match

Searched for regex `MAIN-CALCOLO|EX-CNTR-PAGDUPLI|T20-CALCOLA-PERIODO` (`**/*.md`), no results

Searched for regex `EXEC SQL|END-EXEC|SELECT |INSERT |UPDATE |DELETE |FETCH ` (`**/PIOSX41.txt`), 200 results

Searched for regex `\bCALL\b` (`**/PIOSX41.txt`), 68 results

Searched for regex `TYGP|TISC` (`**/PIOSX41.txt`), 70 results

Searched for regex `MAIN-CALCOLO|EX-CNTR-PAGDUPLI|EX-CONTROLLI|A00-APRI|B00-CONTROLLA|B98-ECCEZIONE-CALCOLOAL|B99-ECCEZIONE-CALCOLOAL|M00-CALCOLA-MENSILE|F01-CALCOLA-TERMINE|F02-CALCOLA-RET-SET-MOB|F03-CALCOLA-RET-SET-NASPI|F04-CALCOLA-RET-SET-ASPI|F00-CALCOLA-MENSILE-FONDI|F10-CALCOLA-FTA-DEL22|C10-CREDITO|M10-CALCOLA-ANNO-IN-CORSO|C20-CALCOLA-ANNO-IN-CORSO|C21-CALCOLA-ANNO-IN-CORSO-RIP|F20-CALCOLA-ANNO-IN-CORSO|T00-CALCOLA-TRANCHES|D00-DETRAGGO-RECUPERO|D10-DETRAGGO-ACCONTO|I10-IMPOSTA-IRPEF|I20-IMPOSTA-IRPEF-R|I00-IRPEF|I30-CALCOLA-GG-PREST|M22-CALCOLA-ANTICIPO|T30-IRPEF|T40-NO-IRPEF|T50-13-IRPEF|T60-RA-IRPEF|T70-SS-IRPEF|B30-RISPONDI|B50-SCRIVI-PAG|B60-SCRIVI-ASU|B70-730|M20-CALCOLA-PERIODO|C30-CALCOLA-PERIODO|C31-CALCOLA-PERIODO-RIP|F30-CALCOLA-PERIODO|M30-SCORRI-SOSPENSIONI|M35-SCORRI-SOSPENSIONI-DS|M31-NON-SCORRERE|M40-ANF|M41-CALCOLA-ANF|T20-CALCOLA-PERIODO|T21-COVID-SOSPE|R00-TOGLI-UNO|R10-AGGIUNGI-UNO|B00-DB2-SELECT|PNPGF-CC-NUOVO|PNPGF-AL-NUOVO|PNPGF-DAL-NUOVO|PNPGF-RP-NUOVO` (`**/PIOSX41.txt`), 200 results

Searched for regex `PNPGF-RP-NUOVO|PNPGF-RP-NUOVO-EX` (`**/PIOSX41.txt`), 8 results

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#845-845), lines 845 to 2109

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#2110-2110), lines 2110 to 3481

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#3482-3482), lines 3482 to 5189

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#5190-5190), lines 5190 to 7176

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#7177-7177), lines 7177 to 9302

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/PIOSX41.txt#9303-9303), lines 9303 to 9808

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_017gTEhS9kF3LmnijptATzNw__vscode-1779784650449/content.txt#1-1), lines 1 to 200

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_017gTEhS9kF3LmnijptATzNw__vscode-1779784650449/content.txt#200-200), lines 200 to 450

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_017gTEhS9kF3LmnijptATzNw__vscode-1779784650449/content.txt#450-450), lines 450 to 510

Ho la mappa completa dal subagent. Genero il deliverable STEP 1: pseudocodifica AS-IS in Markdown. 

Created [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PIOSX41.md)

Completed: *STEP 1 - Pseudocodifica PIOSX41 (focus TYGP vs TISC)* (2/7)

Deliverable STEP 1 pronto in Pseudo_PIOSX41.md.

## Sintesi di quello che ho prodotto

- **56 schede paragrafo** con range righe, scopo, I/O, DB, CALL, decisioni, e annotazioni TYGP/TISC.
- **Sintesi del programma** + diagramma di flusso Mermaid dell'orchestratore.
- **Tabella variabili globali** significative (working + COMMAREADS).
- **Sezione 5 — Confronto TYGP ↔ TISC**: tabella punto-per-punto con tutte le 17 posizioni dove i due codici compaiono nel sorgente.
- **26 questioni aperte** PA-01 … PA-26.

## Risultato chiave dell'analisi TYGP vs TISC

> ⚠️ **Unica divergenza funzionale netta**: TYGP triggera `B99-ECCEZIONE-CALCOLOAL` in tre punti (`B00-CONTROLLA` riga 1670, `M00-CALCOLA-MENSILE` riga 2216, `T00-CALCOLA-TRANCHES` riga 4014). TISC non lo triggera in nessuno dei tre. **Effetto pratico**: per TYGP il calcolo è sempre chiuso al **mese precedente** quello di elaborazione; per TISC può chiudere anche al mese corrente.

Tutte le altre 14 posizioni in cui i due codici compaiono producono lo stesso effetto. In 2 casi (`M30-SCORRI-SOSPENSIONI`) sono in branch `WHEN` sintatticamente diversi ma con istruzioni identiche — probabile heritage storico (TYGP raggruppato coi tirocini "vecchi" TYGM/DL76, TISC con i "nuovi" TGOL/TGOC/TGOS/TGOP).

## Domanda funzionale prioritaria per il business owner (PA-26)

Le altre prestazioni introdotte nello stesso periodo (TGOV, TGOC, TGOS, TGOP, TIRA, PIAC, TISM) sono tutte allineate a TISC, **non** a TYGP. Quindi la divergenza di TYGP su `B99` è un'anomalia: o è voluta (TYGP è un'eccezione regionale Puglia con vincolo di chiusura mensile diverso), o è un **errore di inserimento** quando la prestazione è stata aggiunta il 14/03/2025.

## Prossimi passi possibili

Mi fermo qui per la validazione, come da metodologia. Quando confermi posso:

1. Procedere a **STEP 2** (raffinamento `PIOSX41`: coerenza, diagramma più dettagliato, consolidamento PA-XX).
2. Oppure passare direttamente a **STEP 1 su `PDSIO13`** (l'orchestratore, ~14.700 righe — il più grande).
3. Oppure prima approfondire la sola **PA-26** sulla divergenza TYGP/B99 (verifica che non sia un effetto desiderato letto altrove, es. in `PDSIO13` o `PDSIO05`).

Made changes.

User: Procedi con STEP 2

GitHub Copilot: Procedo con STEP 2: raffinamento. Faccio prima alcune verifiche di coerenza (PA-01 enumerare GOBACK, PA-13 confermare condizione impossibile, mappare codici `OC-RETCODE`), poi aggiorno il file. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PIOSX41.txt; Write-Host "=== Tutti i GOBACK (non commentati) ==="; for($i=0;$i -lt $c.Length;$i++){ if($c[$i] -match '^\s{6}\s+GOBACK' -or $c[$i] -match '^\s{7,}GOBACK'){ if($c[$i] -notmatch '^\s*\*'){ $start=[Math]::Max(0,$i-6); $ctx = ($c[$start..($i-1)] -match 'OC-RETCODE|OC-MESSAGGIO' | Select-Object -Last 2) -join ' | '; "{0,5}: {1} <<< {2}" -f ($i+1),$c[$i].Trim(),$ctx } } }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PIOSX41.txt; Write-Host "=== FDATAAL > FDATAAL context ==="; for($i=0;$i -lt $c.Length;$i++){ if($c[$i] -match 'FDATAAL\s*>\s*FDATAAL'){ "{0,5}: {1}" -f ($i+1),$c[$i] } }; Write-Host "`n=== PERFORM PNPGF-RP-NUOVO sites ==="; (Select-String -Path PIOSX41.txt -Pattern 'PERFORM\s+PNPGF-RP') | ForEach-Object { for($i=[Math]::Max(0,$_.LineNumber-4);$i -lt [Math]::Min($c.Length,$_.LineNumber+1);$i++){ "{0,5}: {1}" -f ($i+1),$c[$i] }; "---" }; Write-Host "`n=== I10-IMPOSTA-IRPEF errore 24 site ==="; for($i=4370;$i -lt 4390;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i] }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PIOSX41.txt; foreach ($anchor in 1671,2217,4015) { Write-Host "`n=== Lista codici che triggerano B99 prima di riga $anchor ==="; $start = $anchor - 1; while ($start -gt 0 -and $c[$start] -notmatch 'IF\s+IC-SSTCODIND') { $start-- }; for($i=$start;$i -lt $anchor;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i] } }

Verifiche fatte. Ora raffino il documento con: tabella codici di ritorno, sub-flow di `B00-CONTROLLA`, conferma equivalenza delle 3 liste B99, merge PA-13/PA-25, e altre coerenze.  

Replacing 69 lines with 134 lines in [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PIOSX41.md)

Compacted conversation
```

```


Checked [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PIOSX41.md), no problems found

STEP 2 — raffinamento completato. Riepilogo delle modifiche apportate a Pseudo_PIOSX41.md:

**Sezioni aggiunte / arricchite**

1. **Indice aggiornato** (8 sezioni anziché 7).
2. **§2 Diagramma di flusso** — aggiunto sotto-flusso decisionale di `B00-CONTROLLA` (paragrafo critico, 17 uscite anticipate) con tutti i `RC` e le righe.
3. **§3 nuova sezione "Codici di ritorno `OC-RETCODE`"** — tabella completa con mapping `RC → significato → righe GOBACK → paragrafo → categoria`. Copre `RC = 0/11/12/13/14/15/16/17/18/19/20/22/24` con tutte le occorrenze enumerate.
4. **§5 paragrafo `B99-ECCEZIONE-CALCOLOAL`** — confermata equivalenza delle 3 liste di trigger nei paragrafi `B00`/`M00`/`T00` (35 codici, stesso set, **TYGP incluso, TISC escluso ovunque**) → la regola è una scelta per famiglia di prestazione, non un side-effect.
5. **§5 paragrafo `I10-IMPOSTA-IRPEF`** — confermato e dettagliato il dead code: `IF FDATAAL > FDATAAL` rende inattivo l'intero paragrafo `PNPGF-RP-NUOVO` e irraggiungibile il `RC=24`.
6. **§5 paragrafo `T20-CALCOLA-PERIODO`** — chiarito che i `WHEN TYGP/TISC` sono in `M30-SCORRI-SOSPENSIONI` (PA-21 risolto).

**Domande aperte (sezione §8)**

- PA-01 aggiornato: da "9 GOBACK" a "28 GOBACK su 11 RC distinti" con rinvio alla nuova tabella.
- PA-13 arricchito con conseguenze esplicite (4 effetti a cascata).
- PA-21 → marcato **RISOLTO** (barrato).
- PA-25 → marcato **MERGED in PA-13** (barrato).
- PA-27 nuovo: `GOBACK` riga 5029 senza assegnazione esplicita di `OC-RETCODE`.
- PA-28 nuovo: codici commentati nelle liste B99 (`APAF/APAR/APA2/DLIA/COIP/BRIO`) — significato storico da chiarire.

**Stato metodologico**: Fase A — STEP 2 (raffinata) completata su `PIOSX41`. Mi fermo qui per validazione come richiesto dalla metodologia in Istruzioni-TISM.md, **prima** di procedere allo STEP 1 di `PDSIO13`.

Confermi che posso procedere con `PDSIO13` (14.739 righe — proporrò suddivisione per ramo), oppure ci sono ulteriori raffinamenti o chiarimenti da fare su `PIOSX41`?

Made changes.

User: Procedi con PDSIO13

GitHub Copilot: Starting: *STEP 1 - Pseudocodifica PDSIO13* (4/8)

Procedo con la mappatura strutturale di `PDSIO13` (14.739 righe). Eseguo in parallelo: header/identification, mappa paragrafi, occorrenze TYGP/TISC, CALL principali, GOBACK/RETCODE. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; "TOT righe: $($c.Count)"; Write-Host "`n=== IDENTIFICATION + COMMENTI HEADER (prime 80 righe) ==="; $c[0..79] | ForEach-Object { $i++; "{0,5}: {1}" -f $i,$_ }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Occorrenze TYGP ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'TYGP') { "{0,5}: {1}" -f ($i+1),$c[$i] } }; Write-Host "`n=== Occorrenze TISC ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'TISC') { "{0,5}: {1}" -f ($i+1),$c[$i] } }

Il contatore `$i` era residuo della sessione precedente — le righe reali della IDENTIFICATION partono da 1. Rieseguo con indicizzazione corretta e mappo paragrafi/CALL/GOBACK. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; "TOT righe: $($c.Count)"; Write-Host "`n=== Prime 100 righe ==="; for($i=0;$i -lt 100;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i] }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== PROCEDURE DIVISION e DIVISIONI ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match '^\s+(IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE|WORKING-STORAGE|LINKAGE|FILE)\s+(DIVISION|SECTION)') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== CALL attive (non commentate) ==="; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match '\bCALL\s+') { "{0,5}: {1}" -f ($i+1),$l.TrimEnd() } }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Paragrafi (label COBOL aaa-nome) ==="; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{7}([A-Z][A-Z0-9-]{2,40})\.\s*$' -and $l -notmatch '^\s*\*') { "{0,5}: {1}" -f ($i+1),$matches[1] } } | Select-Object -First 200

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; $list = @(); for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{7}([A-Z][A-Z0-9-]{2,40})\.\s*$' -and $l -notmatch '^\s*\*') { $list += ("{0,5}: {1}" -f ($i+1),$matches[1]) } }; "Totale paragrafi: $($list.Count)"; $list | Select-Object -First 80

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Contesto TYGP/TISC linee 2900-2930 ==="; for($i=2899;$i -lt 2935;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== Contesto TYGP/TISC linee 9000-9020 ==="; for($i=8999;$i -lt 9025;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== GOBACK + RETCODE in dintorni ==="; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match '\bGOBACK\b') { $rc=""; for($j=[Math]::Max(0,$i-12);$j -lt $i;$j++){ if ($c[$j] -match 'OC-RETCODE\s*=\s*[\x27]?(\S+?)[\x27]?\s') { $rc=$matches[1] } }; "{0,5}: RC={1,-4} {2}" -f ($i+1),$rc,$l.TrimEnd() } } | Select-Object -First 60

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; $list = @(); for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{7}([A-Z][A-Z0-9-]{2,40})\.\s*$' -and $l -notmatch '^\s*\*') { $list += ,@(($i+1),$matches[1]) } }; Write-Host "Tot paragrafi: $($list.Count)"; Write-Host "`n=== Paragrafi 80-200 ==="; for($k=80;$k -lt [Math]::Min(200,$list.Count);$k++){ "{0,5}: {1}" -f $list[$k][0],$list[$k][1] }; Write-Host "`n=== Paragrafo che contiene linea 9012 ==="; for($k=0;$k -lt $list.Count;$k++){ if ($list[$k][0] -le 9012 -and ($k+1 -ge $list.Count -or $list[$k+1][0] -gt 9012)) { "Paragrafo: {0} (riga {1})" -f $list[$k][1],$list[$k][0]; break } }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; $rc=""; $results=@(); for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match 'OC-RETCODE\s*=\s*[\x27]?(\w+)') { $rc=$matches[1] }; if ($l -match '^\s{6}[^*]' -and $l -match '\bGOBACK\b') { $results += ("{0,5}: RC={1,-4} {2}" -f ($i+1),$rc,$l.TrimEnd()); $rc="" } }; "Totale GOBACK attivi: $($results.Count)"; $results

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Paragrafi 200-365 ==="; $cnt=0; $list=@(); for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{7}([A-Z][A-Z0-9-]{2,40})\.\s*$' -and $l -notmatch '^\s*\*') { $list += ,@(($i+1),$matches[1]) } }; for($k=200;$k -lt $list.Count;$k++){ "{0,5}: {1}" -f $list[$k][0],$list[$k][1] }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; # Trova inizio IF prima di 2912 e prima di 9012
foreach ($anchor in 2920, 9012){ Write-Host "`n=== IF list che termina a riga $anchor ==="; $start=$anchor-1; while($start -gt 0 -and $c[$start] -notmatch '^\s*\d*\s*IF\b' -and $c[$start] -notmatch '\bIF\s+IC-' -and $c[$start] -notmatch '\bif\s+\w'){ $start-- }; for($i=$start;$i -le $anchor;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_015rYTPumX9gVbyi2WbxyZQg__vscode-1779784650487/content.txt)

Ho mappato la struttura di `PDSIO13`. Trovata una seconda **divergenza chiave TYGP vs TISC** in `I39-DSPF-M9`: la lista "salta-check-blocco-pagamenti" include TYGP ma non TISC (al contrario di `E20` che include entrambi). Ora creo il file STEP 1. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== PROCEDURE DIVISION USING ==="; for($i=2490;$i -lt 2520;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== LINKAGE SECTION inizio ==="; for($i=2429;$i -lt 2495;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== MAIN orchestratore 2491-2570 ==="; for($i=2490;$i -lt 2570;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== C00-CENTRALI 2560-2585 ==="; for($i=2559;$i -lt 2585;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== E00-ELABORA 2645-2700 ==="; for($i=2644;$i -lt 2700;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== I39-DSPF-M9 inizio 8843-8920 ==="; for($i=8842;$i -lt 8930;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== Chi chiama I39-DSPF-M9 ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match '^\s{6}[^*]' -and $c[$i] -match 'I39-DSPF-M9|I39-EX') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Adesso ho tutto il necessario. Creo il file STEP 1 per `PDSIO13`. 

Created [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO13.md)

Checked [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO13.md), no problems found

Starting: *STEP 2 - Raffinamento pseudo PDSIO13* (5/8)

STEP 1 di `PDSIO13` completato → Pseudo_PDSIO13.md

**Sintesi della pseudocodifica**

| Voce | Dato |
| --- | --- |
| Righe totali | 14.818 |
| Paragrafi mappati | 365 |
| CALL attive | 28 (verso 18 sotto-programmi distinti) |
| GOBACK attivi | **1 solo** (`MAIN-EX` riga 2517 — pattern centralizzato) |
| Occorrenze TYGP | 2 in codice (linee 2918, 9012) |
| Occorrenze TISC | 1 in codice (linea 2912) |
| Cursori SQL dichiarati | 7 dedicati + ~50 paragrafi `*-DB2-*` tecnici |

**Architettura riconosciuta**
- `MAIN → I00-INIZIALI → C00-CENTRALI → F00-FINALI → GOBACK` (3 fasi).
- Doppio ramo: **calcolo** (`C00 → B20 → loop E00 → E20…E64`) vs **informazione** (`I32-SELEZIONI → I38 → I39-DSPF-M9`).
- Hub di calcolo `E23-CALCOLASU`: chiama `PIOSU41-44`, `PIOLP41` e **3 volte `PIOSX41`** (linee 6185, 6199, 6207).
- Output via `OUT-STATUS` / `OUT-MESSAGGIO` / `W-ERRORE` (no `OC-RETCODE` come in `PIOSX41`).

**Finding TYGP vs TISC — la divergenza chiave**
Trovate **due liste di prestazioni** per la `CALL RDSUT28` (verifica blocco pagamenti per Codice Fiscale):

| Lista | Paragrafo | Riga IF | TYGP | TISC | Codici 2024-2026 (TISM/TGOC/TGOV/TGOS/TGOP/TIRA/PIAC) |
| --- | --- | :---: | :---: | :---: | :---: |
| Lista A | `E20-ELABORA20` (calcolo) | 2819 | ✅ | ✅ | ✅ tutti presenti |
| Lista B | `I39-DSPF-M9` (informazione) | 8925 | ✅ | ❌ | ❌ tutti assenti |

→ Nel **ramo informazione** TYGP salta il check blocco CF mentre TISC (e fratelli) lo eseguono sempre. Catalogato come **PA-29** (probabile bug latente: lista non aggiornata per i ~10 codici 2023-2026 eccetto TYGP).

**Lavoro pianificato STEP 2 (prossima fase, dopo validazione)**
- Approfondire i 3 punti `CALL PIOSX41` in `E23-CALCOLASU` (criteri di discriminazione).
- Mappare regole di `J22/J24/J26-*EURO` (quadrature 200+ righe ciascuno).
- Rispondere/consolidare 31 PA-XX raccolte.
- Catalogare valori di `OUT-STATUS` (PA-08).

Mi fermo qui come da metodologia. Procedo con STEP 2 di `PDSIO13` o preferisci che salti direttamente a `PDSIO05` (più piccolo) e poi torni qui?

Made changes.

User: Procedi con STEP 2 di PDSIO13

GitHub Copilot: Procedo con le verifiche di coerenza per STEP 2 di `PDSIO13`. Punti da approfondire: (a) 3 CALL `PIOSX41` in `E23-CALCOLASU`, (b) catalogo `OUT-STATUS`, (c) struttura `E23-CALCOLASU`, (d) trigger ramo informazione, (e) `H-NEWSUSS`, (f) regole `J22/J24/J26`. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== E23-CALCOLASU completo 6037-6280 ==="; for($i=6036;$i -lt 6280;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Catalogo OUT-STATUS valori (MOVE 'xx' TO OUT-STATUS) ==="; $vals=@{}; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match "^\s{6}[^*]" -and $c[$i] -match "MOVE\s+[\x27](\S+?)[\x27]\s+TO\s+OUT-STATUS|move\s+[\x27](\S+?)[\x27]\s+to\s+OUT-STATUS|move\s+[\x27](\S+?)[\x27]\s+to\s+out-status") { $v=$matches[1]+$matches[2]+$matches[3]; if (-not $vals.ContainsKey($v)) { $vals[$v]=@() }; $vals[$v] += ($i+1) } }; foreach ($k in $vals.Keys | Sort-Object) { "{0,-4} -> {1} occorrenze, righe: {2}" -f $k,$vals[$k].Count,(($vals[$k] | Select-Object -First 8) -join ',') }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Occorrenze K-RICHIESTA / L-RICHIESTA ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match '^\s{6}[^*]' -and $c[$i] -match '[KL]-RICHIESTA') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== Occorrenze H-NEWSUSS / H_NEWSUSS ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'H[-_]NEWSUSS') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== Occorrenze ***RIVEDERE ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'RIVEDERE') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_01Sp4jgt1txTkSWu1THvLNpd__vscode-1779784650495/content.txt)

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Chi chiama I32-SELEZIONI / I38-DSPFM-M8 / I39-DSPF-M9 ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match '^\s{6}[^*]' -and $c[$i] -match 'I32-SELEZIONI|I38-DSPFM-M8|PERFORM\s+I39-DSPF-M9') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== I32-SELEZIONI testa 8617-8690 ==="; for($i=8616;$i -lt 8690;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== I38-DSPFM-M8 testa 8688-8790 ==="; for($i=8687;$i -lt 8790;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO13.txt; Write-Host "=== Catalogo completo OUT-STATUS (regex larga) ==="; $vals=@{}; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match '(?i)to\s+OUT-STATUS') { if ($l -match "(?i)(?:move|MOVE)\s+[\x27`""](\S+?)[\x27`""]\s+to\s+OUT-STATUS") { $v=$matches[1]; if (-not $vals.ContainsKey($v)) { $vals[$v]=@() }; $vals[$v] += ($i+1) } elseif ($l -match "(?i)move\s+(\S+)\s+to\s+OUT-STATUS") { $v="VAR:"+$matches[1]; if (-not $vals.ContainsKey($v)) { $vals[$v]=@() }; $vals[$v] += ($i+1) } } }; foreach ($k in $vals.Keys | Sort-Object) { "{0,-25} -> {1} occorr." -f $k,$vals[$k].Count }

Read [](file:///c%3A/Users/felice/AppData/Roaming/Code/User/workspaceStorage/4e54b592fe98b3967b8538019c5289ca/GitHub.copilot-chat/chat-session-resources/e3c7beba-58ab-454d-990c-d1f11ac4d094/toolu_01EPRntAji7WkSqRkKVYBPTN__vscode-1779784650499/content.txt)

Verifiche complete. Trovate **3 correzioni importanti rispetto a STEP 1**:

1. Le 3 CALL `PIOSX41` sono in **`E24-CALCOLO`** (non `E23-CALCOLASU` come scritto in STEP 1).
2. `I39-DSPF-M9` non è il "ramo informazione": è triggerato da `I32-SELEZIONI` riga 8682 quando **`TIPO-ELABO-IN=3 AND L-TIPOCALCOLO='S'`** (elaborazione **singola in simulazione**).
3. `K-RICHIESTA`/`L-RICHIESTA` sono **dichiarati ma mai testati** nel codice procedurale → incoerenza con commenti header.

Applico le correzioni e i raffinamenti STEP 2:   

Replacing 62 lines with 169 lines in [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO13.md)


```

```


Checked [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO13.md), no problems found

Completed: *STEP 2 - Raffinamento pseudo PDSIO13* (5/8)

STEP 2 di `PDSIO13` completato → Pseudo_PDSIO13.md

**Correzioni e raffinamenti applicati**

1. **Correzione STEP 1**: le 3 CALL `PIOSX41` sono in `E24-CALCOLO` (non in `E23-CALCOLASU`). Aggiornati §6 mappa paragrafi e §8 tabella dipendenze.
2. **Nuova §4 "Discriminazione chiamate sotto-programmi di calcolo"** con tre tabelle:
    - **E24** discrimina su `W-CODICEDUE`: 42 (ASU)→`E23`, 44 (LPU)→`PIOLP41`, 45 (SUS)→`PIOSX41`.
    - **E23** discrimina su `W-OPZIONE`: 1→`PIOSU43`, 2→`PIOSU42`, 3→`PIOSU44`, 4→`PIOSU41` (5/6 commentati).
    - Le 3 CALL `PIOSX41` discriminano su `W-SXCOVID19`/`L-TIPOCALCOLO`/`W-NIK`. **Il ramo TYGP/TISC è esclusivamente la riga 6207** (`W-SXCOVID19='N'`).
3. **Chiarimento ramo `I39-DSPF-M9`**: non è un "ramo informazione" come ipotizzato in STEP 1. È **elaborazione singola in simulazione** (`TIPO-ELABO-IN=3 AND L-TIPOCALCOLO='S'`).
4. **Nuova §9 "Catalogo `OUT-STATUS` e codici di ritorno"** con 3 valori letterali confermati (`00`/`96`/`99`) + `OC-RETCODE=98` specifico di `PDSIO13` (non presente in `PIOSX41`).
5. **§3 Modi operativi rivista** con tabella `TIPO-ELABO-IN` × `TIPOCALCOLO` (6 combinazioni).

**PA aggiornate / risolte**
- ~~PA-01~~ (`K-RICHIESTA`): risolto via PA-32.
- PA-03 (TIPO=3): parzialmente risolto — caso `TIPO=3 AND R` resta scoperto.
- ~~PA-06~~ ~~PA-07~~ (discriminazione CALL): risolte in §4.
- PA-08 (OUT-STATUS): parzialmente risolta in §9.
- PA-18 (`H_NEWSUSS`): risolta — usato solo in 1 SQL SELECT (riga 13545).
- ~~PA-30~~ (ramo informazione): risolto.

**Nuove PA aggiunte**
- **PA-32**: incoerenza documentazione `K-RICHIESTA`/codice (dichiarato e descritto ma mai testato).
- **PA-33**: come è popolato `W-SXCOVID19`?
- **PA-34**: come è popolato `W-NIK`?
- **PA-35**: `OC-RETCODE=98` introdotto da `PDSIO13` (non in tabella `PIOSX41`).
- **PA-36**: 7 punti TODO `RIVEDERE` lasciati in codice.

Mi fermo per validazione. Posso procedere con `PDSIO05` (~8.057 righe, biglietto contabile interv. occupazione)?

Made changes.

User: Si

GitHub Copilot: Procedo con STEP 1 di `PDSIO05`. Mappatura iniziale parallela.   

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; "TOT righe: $($c.Count)"; Write-Host "`n=== Header 1-100 ==="; for($i=0;$i -lt 100;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== DIVISIONI/SECTION ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match '^\s+(IDENTIFICATION|ENVIRONMENT|DATA|PROCEDURE|WORKING-STORAGE|LINKAGE|FILE)\s+(DIVISION|SECTION)') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== CALL attive ==="; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match '\bCALL\s+|\bcall\s+') { "{0,5}: {1}" -f ($i+1),$l.TrimEnd() } }; Write-Host "`n=== Occorrenze TYGP ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'TYGP') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== Occorrenze TISC (codice) ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match "[`"']TISC[`"']") { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; $list=@(); for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{7}([A-Z][A-Z0-9-]{2,40})\.\s*$' -and $l -notmatch '^\s*\*') { $list += ,@(($i+1),$matches[1]) } }; "Tot paragrafi: $($list.Count)"; foreach ($p in $list) { "{0,5}: {1}" -f $p[0],$p[1] }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Contesto TISC linea 3795 ==="; for($i=3780;$i -lt 3870;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== LINKAGE 1992-2020 ==="; for($i=1991;$i -lt 2020;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== MAIN 2015-2030 ==="; for($i=2014;$i -lt 2030;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== C00-CENTRALI 2508-2555 ==="; for($i=2507;$i -lt 2555;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== E70-BIGSX header 3407-3470 ==="; for($i=3406;$i -lt 3470;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== GOBACK + ABEND ==="; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match '\bGOBACK\b|\bSTOP RUN\b') { "{0,5}: {1}" -f ($i+1),$l.TrimEnd() } }; Write-Host "`n=== Catalogo OUT-STATUS letterali ==="; $vals=@{}; for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6}[^*]' -and $l -match "(?i)to\s+OUT-STATUS") { if ($l -match "(?i)move\s+'(\S+?)'\s+to\s+OUT-STATUS") { $v=$matches[1]; if (-not $vals.ContainsKey($v)) { $vals[$v]=@() }; $vals[$v] += ($i+1) } } }; foreach ($k in $vals.Keys | Sort-Object) { "{0,-6} -> {1} occorr.  righe: {2}" -f $k,$vals[$k].Count,(($vals[$k] | Select-Object -First 5) -join ',') }

Adesso ho il dato cruciale: TYGP e TISC in `PDSIO05` ricadono in **due rami diversi** dello stesso `EVALUATE` con **conti contabili diversi**. Cerco solo il `WHEN` label che precede la TISC per essere preciso.     

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Cerca WHEN che precede linea 3795 ==="; for($i=3794;$i -gt 3460;$i--){ if ($c[$i] -match 'WHEN\s+["''"]([A-Z])["''"]') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd(); break } }; Write-Host "`n=== Tutti i WHEN dentro E71-BIGSX-CONTINUA 3456-4467 ==="; for($i=3455;$i -lt 4467;$i++){ if ($c[$i] -match '\bWHEN\s+["''"]') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== EVALUATE in E71-BIGSX-CONTINUA ==="; for($i=3455;$i -lt 4467;$i++){ if ($c[$i] -match '\bEVALUATE\b') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== Definizione EL-FINANZ-SX (working) ==="; for($i=0;$i -lt 2000;$i++){ if ($c[$i] -match 'EL-FINANZ-SX') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } } | Select-Object -First 6

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Tutti i WHEN in E71-BIGSX-CONTINUA 3456-4467 ==="; for($i=3455;$i -lt 4467;$i++){ if ($c[$i] -match '\bWHEN\b') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } } | Select-Object -First 30; Write-Host "`n=== EVALUATE in E71-BIGSX-CONTINUA ==="; for($i=3455;$i -lt 4467;$i++){ if ($c[$i] -match '\bEVALUATE\b') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Compacted conversation

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== WHEN/EVALUATE in E71-BIGSX-CONTINUA 3456-4467 ==="; $res = for($i=3455;$i -lt 4467;$i++){ if ($c[$i] -match '\b(EVALUATE|WHEN)\b') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; $res | Select-Object -First 50; Write-Host "`n=== Working EL-FINANZ-SX ==="; $res2 = for($i=0;$i -lt 2000;$i++){ if ($c[$i] -match 'EL-FINANZ-SX|FINANZ-SX') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; $res2 | Select-Object -First 6

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Header 1-40 ==="; for($i=0;$i -lt 40;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== Tutti i 131 paragrafi (PARA. all'inizio riga col 7) ==="; $paras = for($i=0;$i -lt $c.Count;$i++){ $l=$c[$i]; if ($l -match '^\s{6,7}([A-Z][A-Z0-9\-]+)\.\s*$' -and $l -notmatch '^\s*\*') { $name=$matches[1]; if ($name -notmatch '^(IF|END|ELSE|EXIT|GO|PERFORM|MOVE|ADD|COMPUTE|EVALUATE|WHEN|CONTINUE|SUBTRACT|INITIALIZE|DISPLAY|ACCEPT|SEARCH|SET|READ|WRITE|REWRITE|DELETE|OPEN|CLOSE|UNSTRING|STRING|INSPECT|CALL|RETURN|GOBACK|STOP|MULTIPLY|DIVIDE|LINKAGE|DATA|FILE|PROGRAM-ID|AUTHOR|DATE-WRITTEN|DATE-COMPILED|INSTALLATION|SOURCE-COMPUTER|OBJECT-COMPUTER|SPECIAL-NAMES|INPUT-OUTPUT|FD|SD|RD|SELECT|FILLER|VALUE|PIC|REDEFINES|OCCURS|USAGE|COPY|SECTION|DIVISION|ENVIRONMENT|CONFIGURATION|WORKING-STORAGE)') { "{0,5}: {1}" -f ($i+1),$name } } }; $paras | Measure-Object | Select-Object Count; $paras

Created [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO05.md)

File creato: Pseudo_PDSIO05.md.

**STEP 1 PDSIO05 completato.** Sintesi del risultato più importante:

**Divergenza TYGP ↔ TISC in `PDSIO05` è strutturalmente diversa rispetto agli altri due programmi.** In `E71-BIGSX-CONTINUA` (3456-4467), l'`EVALUATE EL-FINANZ-SX(IND-SX)` ha 4 rami (`"F"` / `"R"` / `"E"` / OTHER). Le due prestazioni ricadono in **rami separati**:

| | **TISC** (`WHEN "F"`, Fondo) | **TYGP** (`WHEN "R"`, Regionale) |
|---|---|---|
| Raggruppata con | `TISM` | `TYGM` + `TYAD` |
| Voce contabile | "DEBITO AZIONI POL. ATTIVA DLGS 148/2015" | "DEBITI INDENNITA TIROCINIO GIOVANI" |
| Conto Avere | `GAU 10/281` (riga 155) | `GPZ 11/195` (riga 156) |
| Credito v/Regione | **No** | **Sì**: `GPZ 25/195` Avere + `GPZ 00/195` Dare (riga 160) |
| Data introduzione | 06/05/2024 | 14/03/2025 |

Inferenza coerente con `PIOSX41` (B99) e `PDSIO13` (I39): **TYGP è implementato come tirocinio regionale (famiglia TYGM/TYAD/TYRG), TISC come azione di politica attiva nazionale (famiglia TISM)** — le divergenze osservate negli altri due programmi riflettono questa classificazione di fondo.

26 punti aperti `[PA-XX]` registrati. Mi fermo qui per validazione prima di procedere a **STEP 2 (raffinamento PDSIO05)** o **STEP 3 (consolidamento regole TYGP↔TISC sui 3 programmi)**.

Made changes.

User: Procedi

GitHub Copilot: Procedo con **STEP 2 — Raffinamento PDSIO05**. Approfondisco i punti aperti: rami `WHEN "E"`/`WHEN OTHER` dell'`EVALUATE`, mappa completa codici in `WHEN "F"` e `WHEN "R"`, F00-FINALI (doppio GOBACK), STAMPA-BIGLIETTO, popolamento `EL-FINANZ-SX`. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Ramo WHEN F completo: tutti i codici H-O0SXCODIND 3466-3817 ==="; for($i=3465;$i -lt 3817;$i++){ if ($c[$i] -match 'H-O0SXCODIND\s*=\s*"([A-Z0-9]+)"|OR\s+"([A-Z0-9]+)"|OR\s+H-O0SXCODIND\s*=\s*"([A-Z0-9]+)"') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }; Write-Host "`n=== Ramo WHEN R: tutti i codici 3818-4296 ==="; for($i=3817;$i -lt 4296;$i++){ if ($c[$i] -match 'H-O0SXCODIND\s*=\s*"([A-Z0-9]+)"|OR\s+"([A-Z0-9]+)"|OR\s+H-O0SXCODIND\s*=\s*"([A-Z0-9]+)"') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== WHEN E (4297-4307) ==="; for($i=4296;$i -lt 4311;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== F00-FINALI 5406-5430 ==="; for($i=5405;$i -lt 5432;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== STAMPA-BIGLIETTO 4908-4956 ==="; for($i=4907;$i -lt 4956;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }

 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== Cerca popolamento EL-FINANZ-SX (move/value/load) ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match 'EL-FINANZ-SX|FINANZ-SX|LEGGI-TAB' -and $c[$i] -notmatch '^\s*\*') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Risultati cruciali per lo STEP 2. Ora aggiorno il file con il raffinamento. 

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; $c = Get-Content PDSIO05.txt; Write-Host "=== LEGGI-TAB 8010-8045 ==="; for($i=8009;$i -lt 8046;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== Contesto MOVE H-FINANZ 5760-5790 ==="; for($i=5759;$i -lt 5790;$i++){ "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() }; Write-Host "`n=== OUT-STATUS = 99 o 91 occorrenze ==="; for($i=0;$i -lt $c.Count;$i++){ if ($c[$i] -match "(?i)OUT-STATUS\s*=\s*'9[19]'|to\s+OUT-STATUS|'91'\s+to|'99'\s+to" -and $c[$i] -notmatch '^\s*\*') { "{0,5}: {1}" -f ($i+1),$c[$i].TrimEnd() } }

Ora aggiungo la sezione STEP 2 al file.  

Replacing 1 lines with 1 lines in [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO05.md)

 

Replacing 7 lines with 343 lines in [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Pseudo_PDSIO05.md)


```

```

```

```
**STEP 2 PDSIO05 completato.** File aggiornato: Pseudo_PDSIO05.md.

Sintesi del raffinamento:

**Punti aperti risolti** (`PA-01 ÷ PA-09`, `PA-12 ÷ PA-15`, `PA-17`, `PA-18`, `PA-21`, `PA-22`, `PA-25`, `PA-26`):

1. **`EL-FINANZ-SX`** popolato in `I05-AZZERO` (riga 5768) da `H-FINANZ` letto dalla tabella DB2 categorie contabili → classificazione **tabellare** del codice indennità (non scelta del programma).
2. **`WHEN "F"` Fondo** = ~70 codici (CIG/Mobilità/Fondi solidarietà/Esoneri/DL76/SOMM/TISC/TISM).
3. **`WHEN "R"` Regionale** = ~30 codici (TY*/POR*/APA*/DLI*/TG*/TIRA/PIAC).
4. **`WHEN "E"`** = categoria omogenea (Estero/Esonero), slot 157+159 partita doppia.
5. **`WHEN OTHER`** = catch-all neutro su slot 157 — potenziale fonte di squadrature `'91'`.
6. **Slot riservati** `EL-*`: 155=Fondo, 156=Regionale, 157=E/OTHER, 159=contropartita E, 160=credito v/Regioni.
7. **`OUT-STATUS`** = `'00'` ok / `'91'` squadratura / `'96'` errore funzionale / `'99'` errore tecnico ereditato.
8. **`GOBACK` riga 5408** = bypass per sede `"VALTOZAC"` (ambiente speciale).
9. **`STAMPA-BIGLIETTO`** dispatch via `WTIPODOM`: B→ASU, D→LPU, E→SX → output DSPF + INSERT `TDSREPORT`.

**Nuovi punti aperti emersi**: `PA-27` (sede VALTOZAC), `PA-28` (doppio IF `SSEP` in WHEN "R"), `PA-29` (TYGP senza data fine validità nell'header).

**Insight di dominio consolidato**:
- **TYGP** è classificato come tirocinio **regionale** (Regione Puglia anticipa, INPS rivalsa) → famiglia TYGM/TYAD/TYRG/TG*/POR*/APA*.
- **TISC** è classificato come **azione politica attiva nazionale** DLGS 148/2015 (Fondo INPS finanzia) → famiglia TISM.
- **Le 3 divergenze** (PIOSX41 B99, PDSIO13 I39, PDSIO05 EVALUATE) sono manifestazioni coerenti della **stessa classificazione di dominio** (ente finanziatore). Quindi `[PA-29 PDSIO13]` (TYGP in I39 ma non TISC) **non è un bug**, ma comportamento corretto: I39-DSPF-M9 gestisce specificamente i tirocini regionali in simulazione.

Mi fermo per validazione. Pronto per **STEP 3** (consolidamento regole TYGP↔TISC sui 3 programmi) o eventuali approfondimenti su PA-XX rimasti aperti.

Made changes.

User: Procedi con Step 3

GitHub Copilot: Per impostare correttamente lo STEP 3 verifico il formato richiesto da Istruzioni-TISM.md e leggo i 2 file di pseudocodifica esistenti per consolidare i dati.  

Searched for regex `STEP 3|Step 3|Fase C|estrazione regole|regole di business` (`reingCOBOL` · `Istruzioni-TISM.md`), 4 results

Searched for files matching `reingCOBOL` · `Pseudo_*.md`, 3 matches

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Istruzioni-TISM.md#100-100), lines 100 to 180

Creo il deliverable STEP 3 come **gap analysis** (non documento finale) con le 5 sezioni richieste, focalizzato sul confronto TYGP↔TISC sui 3 programmi. 

Created [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/STEP3-RegoleBusiness.md)

**STEP 3 completato.** Deliverable creato: STEP3-RegoleBusiness.md.

Sintesi del contenuto (gap analysis testuale, NON documento finale):

**§1 — Quadro funzionale**: tabella comparativa TYGP↔TISC su 9 dimensioni (ente finanziatore, categoria contabile, voce, conti, etc.).

**§2 — Entità dati**: tabelle DB2 (`TDSSUSST`, `TDSREPORT`, cursori `E30`/`I25`), struttura `COMMAREADS`, schema slot `EL-*(1..160)`, convenzioni naming.

**§3 — 27 regole di business classificate**:
- **5 RE** (eligibilità): RE-01÷05 — date introduzione, classificazione finanziamento, match key
- **7 RC** (calcolo): RC-01÷07 — formula `WK-DEBITO`, partita doppia TYGP, partita semplice TISC, raggruppamenti TYGM/TYAD vs TISM, trigger B99
- **5 RX** (esclusione): RX-01÷05 — VALTOZAC bypass, ristampa, errore, esclusione TISC da I39
- **3 RS** (soglia): RS-01÷03 — limite 160 slot, slot riservati, squadratura
- **7 RD** (dato/contabile): RD-01÷07 — voci, conti, sigle GAU/GPZ, codici regione 195/232/281
- **6 RO** (operative): RO-01÷06 — CICS LINK, discriminanti L-RETCODE, codici di ritorno

**§4 — Dipendenze**: diagramma Mermaid catena CALL inter-programma + tabella CALL in/out + lista 21 sotto-programmi black-box.

**§5 — Aspetti operativi**: codici ritorno (incoerenza convenzione `OC-RETCODE` vs `OUT-STATUS`), gestione errori, transazionalità (`WITH UR`), modalità online CICS.

**§6 — 20 domande funzionali per business owner** organizzate in 6 cluster:
- Classificazione contabile (Q-01÷04)
- Integrità modello (Q-05÷08): doppio `IF SSEP`, sede VALTOZAC, categoria "E"
- Coerenza tra programmi (Q-09÷11): bug latente I39, uniformazione retcode
- Sotto-programmi (Q-12÷14)
- Dati mancanti (Q-15÷18): tabella categorie, copybook O0, semantica recuperi
- Evoluzione sistema (Q-19÷20): refactoring tabellare

**§7 — Sintesi narrativa in 3 paragrafi** pronta per cap. 2 del `.docx` finale.

**Mapping pseudocodifica → capitoli `.docx`** pre-impostato per STEP 4.

Mi fermo per validazione utente delle 27 regole classificate e delle 20 domande aperte. Una volta confermato il quadro, posso procedere allo **STEP 4** (documento `.docx` stile Sirio/INPS).

Made changes.

User: Procedi STEP 4

GitHub Copilot: Per lo STEP 4 verifico lo stile del documento di riferimento e le convenzioni grafiche richieste.      

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/Istruzioni-TISM.md#175-175), lines 175 to 218

Read [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/2026.05.13.TISC-AnalisiFunzionale.md#1-1), lines 1 to 120

Verifico se `pandoc` è disponibile per la conversione `.md → .docx` (template stile TISC), oppure se serve generare via Python. 

Ran terminal command: Get-Command pandoc -ErrorAction SilentlyContinue | Select-Object Source,Version; Write-Host "---"; python -c "import docx; print('python-docx', docx.__version__)" 2>&1
Completed with input: Get-Command pandoc -ErrorAction SilentlyContinue | Select-Object Source,Version; Write-Host "---"; python -c "import docx; print('python-docx', docx.__version__)" 2>&1

Pandoc disponibile. Creo il documento di Analisi Funzionale TYGP in Markdown strutturato secondo template TISC, poi converto in `.docx`. 

Created [](file:///h%3A/Software%20Engineering/Copilot/Innovaway/REPO-COBOL/reingCOBOL/2026.05.26.TYGP-AnalisiFunzionale.md)

Ora converto in `.docx` con pandoc.  

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; pandoc "2026.05.26.TYGP-AnalisiFunzionale.md" -o "2026.05.26.TYGP-AnalisiFunzionale.docx" --toc --toc-depth=3 --number-sections -f gfm+yaml_metadata_block 2>&1; if (Test-Path "2026.05.26.TYGP-AnalisiFunzionale.docx") { Get-Item "2026.05.26.TYGP-AnalisiFunzionale.docx" | Select-Object Name, Length, LastWriteTime }

Ran terminal command: cd "h:\Software Engineering\Copilot\Innovaway\REPO-COBOL\reingCOBOL"; pandoc "2026.05.26.TYGP-AnalisiFunzionale.md" -o "2026.05.26.TYGP-AnalisiFunzionale.docx" --toc --toc-depth=3 --number-sections -f markdown 2>&1; if (Test-Path "2026.05.26.TYGP-AnalisiFunzionale.docx") { Get-Item "2026.05.26.TYGP-AnalisiFunzionale.docx" | Select-Object Name, Length, LastWriteTime }

**STEP 4 completato.** Documento `.docx` generato (37 KB):

- Sorgente Markdown strutturato: 2026.05.26.TYGP-AnalisiFunzionale.md
- **Documento finale Word**: 2026.05.26.TYGP-AnalisiFunzionale.docx

Struttura del documento (stile parallelo al 2026.05.13.TISC-AnalisiFunzionale.md):

| Capitolo | Contenuto |
|----------|-----------|
| **Premessa** | Inquadramento + link a deliverable intermedi |
| **Cap. 1** Introduzione | Scopo, ambito, glossario (con 11 termini chiave) |
| **Cap. 2** Quadro generale | Inquadramento funzionale, posizionamento nel flusso (diagramma), interlocutori |
| **Cap. 3** Input e trigger | Modalità esecuzione, **Caso d'Uso TYGP** (tabella stile TISC), scenari principale + alternativi (Ristampa + VALTOZAC), tabella `COMMAREADS` con 13 campi, condizioni di partenza |
| **Cap. 4** Flusso AS-IS | 3 fasi macro (A=Calcolo SX, B=Calcolo pagamenti, C=Biglietto contabile), pseudocodice di ogni fase, EVALUATE 4 rami, **scritture contabili TYGP (partita doppia su slot 156 e 160)** con tabella riassuntiva, diagramma Mermaid `E71-BIGSX-CONTINUA` |
| **Cap. 5** Modello dati | 8 tabelle DB2, 13 campi `H-O0SX*`, struttura `EL-*(1..160)` con 14 sotto-campi, schema slot riservati, convenzioni naming |
| **Cap. 6** Regole di business | **27 regole classificate**: 5 RE + 7 RC + 4 RX + 3 RS + 5 RD + 6 RO |
| **Cap. 7** Dipendenze | CALL in entrata, CALL in uscita, 25 sotto-programmi black-box |
| **Cap. 8** Aspetti operativi | Codici ritorno (3 convenzioni divergenti), gestione errori, transazionalità `WITH UR`, modalità CICS, tracciamenti |
| **Cap. 9** Considerazioni TO-BE | **6 aree di refactoring** (R-01÷R-06), 6 debiti tecnici, dipendenze da rompere, opportunità parametrizzazione |
| **App. A** | 10 PA-XX residui |
| **App. B** | 13 domande funzionali per business owner organizzate in 5 cluster |
| **App. C** | Mapping pseudocodifica → capitoli (tracciabilità) |

**Convenzioni rispettate**:
- Italiano (terminologia tecnica EN tollerata).
- Riferimenti `[righe XXXX-YYYY]` su tutti i punti tecnici.
- Codifica `PA-XX` conservata dalla pseudocodifica.
- Distinzione osservato/interpretato (tag "by-design", "inferenza", "Da chiarire").
- TOC automatico + numerazione gerarchica nel `.docx`.

**Note pandoc**: il `.docx` è prodotto con stile pandoc default. Se serve applicare il template **Sirio Design System** (font Titillium Web, palette istituzionale INPS, header colorati), basta fornire un `reference.docx` template e rilanciare con `pandoc … --reference-doc=reference.docx`.

Tutti gli STEP 0÷4 della metodologia Istruzioni-TISM.md sono ora completati. Pronto per eventuali rifiniture (es. applicare template Sirio, o estendere singoli capitoli su richiesta).

Made changes.

User: Grazie, puoi terminare.

GitHub Copilot: Compacted conversationAggiorno la todo list per riflettere lo stato finale. 

Completed: *STEP 1-2 - Pseudocodifica PDSIO05* (6/8)

Tutti gli STEP 0÷4 completati. Deliverable finali nella cartella reingCOBOL:

- Pseudo_PIOSX41.md
- Pseudo_PDSIO13.md
- Pseudo_PDSIO05.md
- STEP3-RegoleBusiness.md
- 2026.05.26.TYGP-AnalisiFunzionale.md
- 2026.05.26.TYGP-AnalisiFunzionale.docx

Buon lavoro!