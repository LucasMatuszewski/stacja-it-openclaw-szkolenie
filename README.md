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

Konfiguracja plików agenta powinna uruchomić się automatycznie przy pierwszej rozmowie - agent zada Ci pytania i na podstawie odpowiedzi spersonalizuje pliki w swoim worspace.

Jeśli z jakiegoś powodu się on nie uruchomi, możesz wskazać mu ręcznie plik `/home/<user>/.openclaw/workspace/BOOTSTRAP.md` i poprosić aby wykonał instrukcje z niego i skonfugurował pliki. Więcej o tym tutaj:
https://docs.openclaw.ai/start/bootstrapping

Po zakończeniu możesz skasować plik `BOOTSTRAP.md` jeśli agent sam tego nie zrobi.

Możesz również wszystkie pliki agenta edytować ręcznie w razie potrzeby, prosić o to agenta lub użyć GUI tutaj: http://127.0.0.1:18789/agents (zakładka "files")

Traktuj te pliki jako wstępne templates, do pełnego dostosowania według Twojego pomysłu.
Potęga OpenClaw tkwi w jego elastyczności, każdy może go poukładać po swojemu, wymyślić nowe sposoby używania go. Wymaga to kreatywności ale daje też sporą satysfakcję :)

---

### Backups - kopia zapasowa plików i konfiguracji

Dla bezpieczeństwa rekomenduję 4 poziomy backupu dla użądzenia, na którym pracuje agent:

1. Backup całego systemu, na przykład co 1-6 godzin, inkrementacyjny (dodaje tylko zmiany) i z mechanizmami znacznie zmniejszącymi ilość potrzebnego miejsca na dysku / w chmurze.
  - polecam tutaj Restic https://restic.net/
  - w połączeniu z RClone do synchronizacji plików w chmurze https://rclone.org/commands/rclone_serve_restic/
  - dodatkowo warto przemyśleć dobry plik do wykluczeń, np. folderów `node_modules`, `.next`, cache (np. cache npm, pnpm, rust cargo itd.) aby nie backupować zbędnych rzeczy, https://restic.readthedocs.io/en/latest/040_backup.html#excluding-files - przykładowy plik dla Linux https://gist.github.com/MatthewVance/0d228dbe85bccb2836ba72194ef6dcb5
2. Backup plików konfiguracyjnych Systemu - na Windows punkt przywracania, na Linux polecam: http://snapper.io/
3. GIT repo - zarówno dla plików agenta (polecam cały folder `.openclaw` z wykluczeniami - o czym dalej), oraz plików projektów z którymi agent pracuje (część projektów może być w `workspace` agenta, ale często są to osobne repo z kodem gdzie pracujemy z różnymi agentami, np. Claude Code / Codex CLI / OpenCode, Cursor itd.)
  - osobiście pozwalam agentom robić commits z opisem, granuralnie, aby była historia ich zmian na bieżąco widoczna, łatwa do cofnięcia
  - ale nie pozwalam agentom robić push, a na pewno nie na master / main branch, ewentualnie na feature branche np. z prefix `openclaw/branch-name` 
4. OneDrive / Google Drive / itp. chmury dla plików z dokumentami, do których dajemy agentowi dostęp (pamiętaj aby ograniczyć możliwość kasowania, stosować np. soft delete, upewnij się, że dysk w chmurze trzyma kopie z możliwością przywrócenia)

---

### Przykładowe zaawansowane pliki konfiguracyjne

Zgodnie z obietnicą w root repo dodaje moje przykładowe pliki, nieco uproszczone i zanonimizowane, ale z bardziej zaawansowanymi konfiguracjami (np. multi-agents, fallback models, allow lists, itd.) oraz skrypt do anonimizacji pliku `openclaw.json`

- plik konfiguracyjny `openclaw.template.json` jako przykład dla pliku `openclaw.json`
- plik `.gitignore` z przykładowymi folderami i plikami do wykluczenia z `.openclaw` jeśli zdecydujecie się trzymać w repo cały folder a nie tylko workspace agenta.
- skrypt do anonimizacji pliku `openclaw.json`: `anonimize-config.py` (odpalamy np. przez `python anonimize-config.py` w folderze w którym znajduje się config - można np. podpiąć pod hook z Husky przed push do git repo) - poprawiłem go aby usuwał także `api-key` ;)

---

## Next Steps - co po szkoleniu?

Po szkoleniu polecam wykonać poniższe kroki dla Waszych agentów

1. Dokończyć konfigurację plików w workspace, najpierw z Bootstrap przy pierwszej rozmowie, potem ręcznie je dopracować i przemyśleć, ustawić zasady jakimi agent ma sie kierować, jego osobowość, co ma wiedzieć o systemie/narzędziach (TOOLS.md), jaki ma mieć workflow (AGENTS.md, HEARTBEATS.md)
2. Wyłączyć niepotrzebne skills: http://127.0.0.1:18789/skills (im więcej agent ma skills czy MCP tym trudniej mu wybrać właściwe + niepotrzebnie zapychają one okno kontekstowe)
3. Dodać nowe skills jakie mogą się przydać agentowi wg. Waszych potrzeb, https://docs.openclaw.ai/tools/skills
  - stwórz swój własny skill (agent w tym pomoże) np. uczący agenta jak wykonywać jakiś element Twojej pracy (np. pisanie artykułów na bloga i ich publikacja przez skrypt z dostępem przez API do dodawania draftów): https://docs.openclaw.ai/tools/creating-skills
  - poszukaj skills jakie mogą Ci się przydać w https://clawhub.ai (pamiętaj o weryfikacji bezpieczeństwa skilla, przeczytaj co on robi lub poproś o weryfikację agenta), np. do pracy z dokumentami MS Word: https://clawhub.ai/ivangdavila/word-docx
4. Dodać kilka dodatkowych providerów dla AI inference jako fallbacks (np. Ollama Cloud, Codex, OpenRouter, Z.ai Coding Plan, Azure, etc.) - przykład dla Azure AI Foundry jest w moim przykładowym pliku konfiguracyjnym
5. Skonfigurować tunel Tailscale aby mieć prywatny dostęp do swojego urządzania i agenta np. z komórki: https://docs.openclaw.ai/gateway/tailscale
  - polecam również rozważyć Cloudflare Tunnel jeśli potrzebowalibyście udostępnić jakiś endpoint publicznie, np. dla agenta MS Teams: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/
  - dodatkowo warto rozważyć dostęp do urządzania na którym jest agent przez SSH oraz ewentualnie również dostęp do plików przez `sshfs` (jest to wolne, ale czasem przydatne)
6. Skonfigurować wyszukiwarkę Grok oraz Perplexity: https://docs.openclaw.ai/tools/grok-search, https://docs.openclaw.ai/tools/perplexity-search
7. Skonfigurować zadania CRON (konkretne większe zadania wykonywane regularnie lub jednorazowe przypomnienia/zadania, z możliwością dostosowania modelu LLM wedle trudności zadania, wybrania agenta, kanału komunikacji itd.) oraz zrozumieć różnicę między Cron a Heartbeat (małe czynności wykonywane bardzo często np. co 30-60m, np. kontrola działania agenta, czy robi co powinien + komunikat jeśli coś jest nie tak): https://docs.openclaw.ai/automation , https://docs.openclaw.ai/automation/cron-jobs
8. Poczytać o Sub-agents oraz ACP (możliwość delegowania zadań do agentów Codex CLI, Claude Code CLI, itd.): https://docs.openclaw.ai/tools/subagents , https://docs.openclaw.ai/tools/acp-agents
9. Poczytać o Memory (jeden z najważniejszych elementów aby agent był przydatny i spersonalizowany): https://docs.openclaw.ai/concepts/memory
  - Dodaj konfigurację modelu do embedding oraz własny RAG w oparciu o memory: https://docs.openclaw.ai/concepts/memory-search
  - Poczytaj o dreaming / snach - nowym automatycznym mechaniźmie konsolidacji wspomnień: https://docs.openclaw.ai/concepts/dreaming
  - Rozważ opcjonalny QMD memory - bardziej zaawansowany system RAG do wspomnień/pamięci, zawierający reranking do lepszego dopasowywania najlepiej pasujących wspomnieć do kontekstu zadania agenta: https://docs.openclaw.ai/concepts/memory-qmd
