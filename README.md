# Stacja IT - OpenClaw - szkolenie

Pliki do szkolenia dla Stacja IT: Autonomiczni Agenci AI z OpenClaw
https://stacja.it/produkt/autonomiczni-agenci-ai-z-openclaw/

---

## Update po szkoleniu

### Błąd `trim` naprawiony w wersji 4.15

Błąd jaki pojawił się na szkoleniu dla onboardingu w wersji 4.14 został już naprawiony w wersji 4.15 (póki co w beta testach, jutro powinien być release stabilny):
- https://github.com/openclaw/openclaw/releases
- PR z fixem: https://github.com/openclaw/openclaw/pull/66736

To jest piękne w społeczności OpenClaw, błędy są naprawiane bardzo szybko. Wystarczy przyjąć politykę instalowania aktualizacji z opóźnieniem kilku dni i ryzyko problemów jest niewielkie.
Jak na skalę i ilość aktualizacji błędów wcale nie ma dużo.

### Bootstrap i personalizacja agenta

Konfiguracja plików agenta powinna automatycznie się uruchomić przy pierwszej rozmowie - agent zada Ci pytania i na podstawie odpowiedzi spersonalizuje pliki w swoim worspace.

Jeśli z jakiegoś powodu się on nie uruchomi, możesz wskazać mu ręcznie plik `/home/<user>/.openclaw/workspace/BOOTSTRAP.md` i poprosić aby wykonał instrukcje z niego i skonfugurował pliki. Więcej o tym tutaj:
https://docs.openclaw.ai/start/bootstrapping

Po zakończeniu możesz skasować plik `BOOTSTRAP.md` jeśli agent sam tego nie zrobi.

Możesz również wszystkie pliki agenta edytować ręcznie w razie potrzeby, prosić o to agenta lub użyć GUI tutaj: http://127.0.0.1:18789/agents (zakładka "files")

Traktuj te pliki jako wstępne templates, do pełnego dostosowania według Twojego pomysłu.
Potęga OpenClaw tkwi w jego elastyczności, każdy może go poukładać po swojemu, wymyślić nowe sposoby używania go. Wymaga to kreatywności ale daje też sporą satysfakcję :)

---

### Backups - kopia zapasowa plików i konfiguracji

Rekomenduję 4 poziomy backupu dla użądzenia, na którym pracuje agent:

1. Backup całego systemu, najlepiej co 1 godzinę, inkrementacyjny (dodaje tylko zmiany) i z mechanizmami znacznie zmniejszącymi ilość potrzebnego miejsca na dysku / w chmurze.
  - polecam tutaj Restic https://restic.net/
  - w połączeniu z RClone do synchronizacji plików w chmurze https://rclone.org/commands/rclone_serve_restic/
  - dodatkowo warto przemyśleć dobry plik do wykluczeń, np. folderów `node_modules`, `.next`, cache (np. cache npm, pnpm, rust cargo itd.) aby nie backupować zbędnych rzeczy, https://restic.readthedocs.io/en/latest/040_backup.html#excluding-files - przykładowy plik dla Linux https://gist.github.com/MatthewVance/0d228dbe85bccb2836ba72194ef6dcb5
2. Backup plików konfiguracyjnych Systemu - na Windows punkt przywracania, na Linux polecam: http://snapper.io/
3. GIT repo - zarówno dla plików agenta (polecam cały folder `.openclaw` z wykluczeniami - o czym dalej), oraz plików projektów z którymi agent pracuje (część projektów może być w `workspace` agenta, ale często są to osobne repo z kodem gdzie pracujemy z różnymi agentami, np. Claude Code / Codex CLI / OpenCode, Cursor itd.)
4. OneDrive / Google Drive / itp. chmury dla plików z dokumentami, do których dajemy agentowi dostęp (pamiętaj aby ograniczyć możliwość kasowania, stosować np. soft delete, upewnij się, że dysk w chmurze trzyma kopie z możliwością przywrócenia)

---

### Przykładowe zaawansowane pliki konfiguracyjne

Zgodnie z obietnicą w root repo dodaje moje przykładowe pliki, nieco uproszczone i zanonimizowane, ale z bardziej zaawansowanymi konfiguracjami (np. multi-agents, fallback models, allow lists, itd.) oraz skrypt do anonimizacji pliku `openclaw.json`

- plik konfiguracyjny `openclaw.template.json` jako przykład dla pliku `openclaw.json`
- plik `.gitignore` z przykładowymi folderami i plikami do wykluczenia z `.openclaw` jeśli zdecydujecie się trzymać w repo cały folder a nie tylko workspace agenta.
- skrypt do anonimizacji pliku `openclaw.json`: `anonimize-config.py` (odpalamy np. przez `python anonimize-config.py` w folderze w którym znajduje się config - można np. podpiąć pod hook z Husky przed push do git repo) - poprawiłem go aby usuwał także `api-key` ;)
