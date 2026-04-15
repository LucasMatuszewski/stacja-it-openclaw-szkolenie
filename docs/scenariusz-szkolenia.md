# Scenariusz warsztatu — Autonomiczni Agenci AI z OpenClaw
**Godz. 17:00–21:00 | Warsztat zdalny | ok. 19 uczestników**
**Mieszana grupa: programiści, PM, CEO, analitycy, marketingowcy**

> 🎬 = co mówię (dosłownie lub prawie dosłownie)
> 📺 = co pokazuję na ekranie
> 💬 = wklejam na chat (gotowy tekst do skopiowania)
> 🏋️ = ćwiczenie dla uczestników
> ⏱️ = czas bloku
> 💡 = wskazówka / uwaga dla prowadzącego (nie mów tego głośno)
> 🔵 = zadanie dodatkowe dla zaawansowanych (opcjonalne)

---

## AGENDA (wklej na start)

💬 WKLEJ NA CHAT:
```
Warsztat: Autonomiczni Agenci AI z OpenClaw — 17:00–21:00

17:00  Start + ankieta + weryfikacja środowiska
17:20  Moduł 1 — Możliwości, ograniczenia i zagrożenia OpenClaw
17:45  Moduł 2 — Instalacja i konfiguracja
18:35  ☕ PRZERWA (10 min)
18:45  Moduł 3 — Bezpieczny dostęp zdalny: Tailscale, SSH
19:10  Moduł 4 — Komunikator (WhatsApp)
19:30  Moduł 5 — Personalizacja instrukcji i pamięć agenta
19:55  ☕ PRZERWA (10 min)
20:05  Moduł 6 — Automatyzacja: Cron, Heartbeat, Skills, MCP, Search
20:40  Moduł 7 — Koszty, optymalizacja, logi, monitoring + podsumowanie
21:00  Koniec (mogę zostać chwilę dłużej jeśli ktoś ma problem z uruchomieniem agenta)
```

---

## 17:00–17:20 — Start, ankieta startowa, weryfikacja środowiska
⏱️ 20 min

🎬 **CO MÓWIĘ:**

„Cześć, dobry wieczór! Dajcie znać na czacie czy mnie słychać i widać dobrze.

Kilka słów zanim zaczniemy.

Będę cały czas udostępniał ekran i wklejał linki na czat — starajcie się robić to samo co ja, krok po kroku. Będę pytał czy wszystkim się udało, ale jeśli coś nie idzie — mówcie głosem albo dajcie reakcję ręki w górę na Zoomie, zatrzymam się i pomożemy razem.

Krótkie pytania mogę odpowiadać na bieżąco. Pytania poza programem albo bardziej zaawansowane — zostawmy proszę na koniec, żebyśmy zdążyli ze wszystkim.

Cel dzisiejszego warsztatu: pokazać możliwości OpenClaw, nauczyć podstaw i wspólnie uruchomić prostego agenta. 4 godziny to za mało żeby wejść głęboko w każdy temat — OpenClaw to ogromny projekt. Pokażę najprostszą drogę, omówię najważniejsze elementy, postaram się żeby każdy miał działającego agenta na koniec.

Mam was 19, więc zamiast pytać każdego indywidualnie — zrobię szybką ankietę na Zoomie. Zajmie nam to 3-4 minuty i od razu wiem z kim mam do czynienia."

📺 **CO POKAZUJĘ:**
- Ankieta Zoom (Polls) — uruchom przygotowaną wcześniej ankietę

💡 **Przygotuj wcześniej ankietę Zoom z pytaniami:**
- System operacyjny na urządzeniu dla agenta: Linux / macOS / Windows / Inne / Nie mam jeszcze
- Dostęp do LLM: API (OpenAI/Anthropic/itp.) / ChatGPT Plus lub Pro / Z.ai / Lokalne modele (Ollama) / Nie mam jeszcze
- Doświadczenie z CLI/terminalem: Brak / Podstawowe / Średnie / Zaawansowane
- Specjalizacja: Programista/Tech / PM/CEO/COO / Analityk/Marketing / Inne

🎬 „Dziękuję za odpowiedzi. Widzę że..."

💡 **Skomentuj wyniki ankiety na bieżąco. Zaadaptuj tempo i przykłady do grupy. Jeśli dużo osób ma Windows — poświęć więcej czasu na WSL2. Jeśli dużo osób nie ma jeszcze dostawcy LLM — omów opcje szerzej w module 2.**

🎬 „Teraz weryfikacja techniczna. Potrzebuję żebyście otworzyli terminal na urządzeniu, na którym chcecie uruchomić agenta — nie na swoim głównym laptopie jeśli macie osobne urządzenie. I wkleili po kolei te komendy."

💬 WKLEJ NA CHAT:
```
Weryfikacja środowiska — wpisz w terminalu:

node --version    ← potrzebujesz 22.14+
npm --version
git --version

Wyniki wrzuć na chat!
Jeśli node nie jest w wersji 22.14+ — instalacja:
https://docs.openclaw.ai/install/node
```

🎬 „Kto ma Node.js w wersji 22 lub wyżej — 👍 na chat. Kto ma problem — 🐛 i napisz co się dzieje, pomożemy zanim przejdziemy dalej.

Na Windows: jeśli używacie PowerShell i coś nie działa — odpalcie Git Bash lub WSL2. OpenClaw zdecydowanie lepiej działa na Linuxie lub macOS, ale na Windows z WSL2 też da radę."

💬 WKLEJ NA CHAT:
```
Windows — rekomendowana konfiguracja:
• WSL2 (Ubuntu) — najlepiej działa: https://learn.microsoft.com/pl-pl/windows/wsl/install
• Git Bash — jako minimum: https://git-scm.com/downloads/win
• PowerShell — może działać, ale mogą być problemy

Jeśli masz WSL2 — wszystkie komendy wykonuj wewnątrz WSL!
```

💡 **Max 5 minut na rozwiązywanie problemów środowiskowych. Powiedz pozostałym żeby po cichu przejrzeli agendę na czacie. Pomagaj 1:1 przez screen share jeśli potrzeba.**

---

## 17:20–17:45 — Moduł 1: Możliwości, ograniczenia i zagrożenia OpenClaw
⏱️ 25 min

🎬 **CO MÓWIĘ:**

„Zanim zainstalujemy OpenClaw — chcę żebyście wiedzieli z czym macie do czynienia. Co to jest, co potrafi, i — co równie ważne — czego nie potrafi i gdzie jest niebezpieczny.

OpenClaw to autonomiczny agent AI działający 24/7 na Waszym urządzeniu. Uruchamia się w terminalu, ma dostęp do systemu plików, może wykonywać komendy, wysyłać wiadomości, przeglądać sieć, zarządzać harmonogramem. Możecie mu powiedzieć 'sprawdzaj moje maile co godzinę i podsumowuj ważne' — i będzie to robił bez Waszego udziału.

To jest fundamentalna różnica między OpenClaw a czymś takim jak ChatGPT. ChatGPT to asystent — odpowiada na pytania. OpenClaw to agent — działa."

📺 **CO POKAZUJĘ:**
- Strona główna / dokumentacja OpenClaw — krótki rzut oka na możliwości

💬 WKLEJ NA CHAT:
```
OpenClaw — co potrafi:
• Heartbeat — cykliczne działanie co X minut/godzin
• Cron — harmonogram zadań (jak systemowy cron)
• Memory — pamięć długoterminowa (REM, Deep Memory)
• Skills — gotowe umiejętności / integracje
• Web Search — przeglądanie internetu
• MCP — integracje z zewnętrznymi narzędziami
• Komunikatory — WhatsApp, Slack, Teams
• ACP Agents — komunikacja między agentami
• Media — generowanie obrazów, wideo, audio (przez API)

Dokumentacja: https://docs.openclaw.ai
```

🎬 „Teraz ważna kwestia — **kto może być dostawcą LLM dla OpenClaw**.

I tu muszę powiedzieć coś czego nie było w opisie szkolenia, bo to zmieniło się niedawno: **Claude Code od Anthropic banuje konta za używanie w OpenClaw**. Podobnie Google. To wynika z warunków ich usług — nie życzą sobie żeby ich subskrypcje były używane przez zewnętrzne narzędzia agentowe.

Bezpieczne opcje to:"

💬 WKLEJ NA CHAT:
```
Bezpieczni dostawcy LLM dla OpenClaw:

✅ API bezpośrednie (OpenAI, Anthropic, Azure, AWS, GCP, OpenRouter)
   — płacisz za tokeny, pełna kontrola, żadnych banów
✅ Z.ai Coding Plan — oficjalnie wspiera agentów
   — od $18/m (3x więcej niż Claude Pro za $20)
   — link z 10% rabatem: https://z.ai/subscribe?ic=IA5VBRGQV4
✅ ChatGPT Plus/Pro z Codex CLI
   — nieoficjalnie, ale nikt dotąd nie był banowany
   — OpenAI siedzi w zarządzie fundacji OpenClaw
✅ Lokalne modele przez Ollama (Gemma 4 26B lub 31b+)
   — za darmo, zero ryzyka bana, działa lokalnie
   — Gemma 4 całkiem nieźle radzi sobie z agentami!
   — https://ollama.com/

⛔ Claude Code (subskrypcja Anthropic) — ban!
⛔ Google AI Studio / Gemini (subskrypcja) — ban!
```

🎬 „Dobra — zagrożenia i bezpieczeństwo. To nie jest straszenie — to jest rzetelna wiedza którą musicie mieć zanim uruchomicie coś co działa autonomicznie na Waszym urządzeniu.

Agent ma dostęp do systemu. Może usuwać pliki, wysyłać wiadomości, robić requesty HTTP. Jeśli coś pójdzie nie tak — albo napiszecie złą instrukcję — może zrobić coś czego nie chcieliście.

Dlatego kilka żelaznych zasad:"

💬 WKLEJ NA CHAT:
```
Zasady bezpieczeństwa — podstawy:

🔒 URZĄDZENIE
• Najlepiej dedykowane urządzenie (stary laptop, mini PC)
• Tylko dane i narzędzia których agent potrzebuje
• Nie trzymaj na nim prywatnych kluczy, haseł do banku itp.

🔒 DOSTĘP
• Osobne konta API / tokeny tylko dla agenta
• Drafts only — agent tworzy szkice, Ty akceptujesz
• Soft Delete — agent nie usuwa, tylko przenosi do kosza
• Dedykowany user na systemie operacyjnym (opcjonalnie)

🔒 SIEĆ
• Tailscale do prywatnego dostępu (nie otwieraj portów na świat)
• SSH zamiast haseł

🔒 BACKUP
• Git dla projektów i konfiguracji agenta
• Backup przyrostowy co godzinę (ideał)

Omówimy szczegóły przy Tailscale i SSH za chwilę.
```

🎬 „I na koniec tego modułu — **ograniczenia**.

OpenClaw jest potężny, ale nie jest magią. Agent nie 'myśli' — on generuje tekst na podstawie instrukcji i kontekstu. Będzie robił błędy. Im lepsza instrukcja i im lepszy model — tym mniej błędów, ale nigdy zero.

4 godziny to żeby zrozumieć podstawy i uruchomić pierwszego agenta. Pełne możliwości odkryjecie przez tygodnie eksperymentowania. Mam to wbudowane w program — zostańmy realistami, ale zaciekawieni."

---

## 17:45–18:35 — Moduł 2: Instalacja i konfiguracja OpenClaw
⏱️ 50 min

💡 **To jest serce warsztatu. Idź powoli. Czekaj na każdym kroku na potwierdzenie od uczestników. Masz rezerwę — jeśli tracisz czas, skróć moduł 6 (automatyzacja).**

🎬 **CO MÓWIĘ:**

„Instalujemy OpenClaw. Robimy to razem, krok po kroku. Na każdym etapie będę czekał na 👍 od Was zanim przejdziemy dalej.

Zaczynamy od instalacji przez npm:"

💬 WKLEJ NA CHAT:
```
Krok 1 — Instalacja OpenClaw:

npm install -g openclaw

Po instalacji sprawdź:
openclaw --version

Dokumentacja instalacji: https://docs.openclaw.ai/install
```

🎬 „Kto ma zainstalowane — 👍. Kto ma błąd — napisz co dostałeś.

Teraz inicjalizacja — to jest moment kiedy OpenClaw tworzy swoją strukturę katalogów i pyta o podstawową konfigurację:"

💬 WKLEJ NA CHAT:
```
Krok 2 — Inicjalizacja:

openclaw init

OpenClaw zapyta o:
• Katalog roboczy agenta (zostaw domyślny lub wybierz swój)
• Dostawcę LLM (wybierz zgodnie z tym co masz)
• Klucz API lub dane logowania

Wskazówka: możesz to zmienić później w pliku konfiguracyjnym.
```

📺 **CO POKAZUJĘ:**
- Demo `openclaw init` — pokazuję każdy krok, co wpisuję, co wybieram

🎬 „Przy wyborze dostawcy — wybierzcie to co macie. Pokażę konfigurację dla API Anthropic jako przykład, ale zaraz omówię też Z.ai i Ollama."

💬 WKLEJ NA CHAT:
```
Krok 3 — Konfiguracja dostawcy LLM:

Plik konfiguracyjny znajdziesz w:
~/.openclaw/config.json  (Linux/macOS)
%APPDATA%\openclaw\config.json  (Windows)

Przykład dla API Anthropic:
{
  "provider": "anthropic",
  "model": "claude-opus-4-6",
  "apiKey": "sk-ant-..."
}

Przykład dla Z.ai:
{
  "provider": "openai-compatible",
  "model": "glm-4.7",
  "baseUrl": "https://api.z.ai/v1",
  "apiKey": "..."
}

Przykład dla Ollama (lokalne):
{
  "provider": "ollama",
  "model": "gemma4:26b",
  "baseUrl": "http://localhost:11434"
}
```

📺 **CO POKAZUJĘ:**
- Plik konfiguracyjny w edytorze tekstowym
- Jak wygląda po poprawnej konfiguracji

🎬 „Dajcie znać gdy macie konfigurację gotową — 👍. Jeśli nie jesteście pewni klucza API — chwila żeby go znaleźć lub stworzyć."

💬 WKLEJ NA CHAT:
```
Gdzie wziąć klucz API:

Anthropic: https://console.anthropic.com/settings/keys
OpenAI:    https://platform.openai.com/api-keys
Z.ai:      https://z.ai — po zalogowaniu → API Keys
OpenRouter: https://openrouter.ai/keys

Ollama (lokalne, bez klucza):
  Instalacja: https://ollama.com/download
  Uruchom model: ollama pull gemma4:26b
  Ollama startuje automatycznie na localhost:11434
```

🎬 „Teraz pierwsze uruchomienie agenta:"

💬 WKLEJ NA CHAT:
```
Krok 4 — Pierwsze uruchomienie:

openclaw start

Jeśli wszystko ok, zobaczysz prompt agenta.
Wpisz testową wiadomość:

Cześć, jak masz na imię i co potrafisz?

Jeśli agent odpowiada — 👍 na chat!
```

📺 **CO POKAZUJĘ:**
- Demo pierwszej rozmowy z agentem

🎬 „Świetnie — mamy działającego agenta. Teraz ważna rzecz: **struktura katalogów OpenClaw**."

💬 WKLEJ NA CHAT:
```
Struktura katalogów OpenClaw:

~/.openclaw/
├── config.json          ← konfiguracja główna (LLM, klucze)
├── instructions.md      ← instrukcja główna agenta (tu będziemy pisać!)
├── memory/
│   ├── core.md          ← pamięć podstawowa (zawsze ładowana)
│   └── ...              ← inne pliki pamięci
├── skills/              ← umiejętności / wtyczki
├── logs/                ← logi działania agenta
└── workspace/           ← domyślny katalog roboczy agenta
```

🎬 „Plik `instructions.md` to serce agenta — to tam piszemy kim jest, co ma robić, jak ma działać. Za chwilę to zrobimy razem.

Ale najpierw — sprawdźmy czy agent poprawnie widzi swoje środowisko:"

💬 WKLEJ NA CHAT:
```
Krok 5 — Diagnostyka:

openclaw status

Pokaże:
• wersję OpenClaw
• aktywny model i dostawcę
• status połączenia z API
• załadowane skills
• aktywne crony i heartbeaty

Wrzuć na chat wynik — szczególnie jeśli widzisz błąd!
```

🏋️ **MINI-ĆWICZENIE — Pierwsze zadanie dla agenta (5 min):**

💬 WKLEJ NA CHAT:
```
Ćwiczenie: Zadaj agentowi pierwsze zadanie

W sesji openclaw wpisz:

"Sprawdź jaka jest teraz godzina i data,
a następnie napisz mi krótkie podsumowanie
czym jest OpenClaw w 3 zdaniach."

Jeśli agent odpowiedział poprawnie — 👍
Jeśli coś poszło nie tak — 🐛 i napisz co się stało
```

🎬 „Jak widzi działający agent — to jest właśnie podstawa. Mamy zainstalowane, skonfigurowane i uruchomione środowisko. Teraz idziemy na przerwę."

---

## 18:35–18:45 — PRZERWA ☕
⏱️ 10 min

💬 WKLEJ NA CHAT:
```
☕ Przerwa 10 minut → wracamy 18:45

Po przerwie:
→ Tailscale + SSH — bezpieczny zdalny dostęp do agenta
→ Podłączenie komunikatora (WhatsApp)
→ Personalizacja i pamięć agenta

Jeśli masz problem z instalacją — napisz teraz, pomogę!
```

---

## 18:45–19:10 — Moduł 3: Bezpieczny dostęp zdalny: Tailscale, SSH
⏱️ 25 min

🎬 **CO MÓWIĘ:**

„Wracamy. Teraz Tailscale i SSH.

Po co nam to? Agent ma działać 24/7 na dedykowanym urządzeniu. Wy jesteście w domu, w biurze, w kawiarni. Musicie mieć bezpieczny sposób żeby się do niego połączyć, sprawdzić co robi, wysłać nowe polecenie albo po prostu zobaczyć logi.

Tailscale to prywatna sieć VPN oparta na WireGuard. Wszystkie Wasze urządzenia — laptop, telefon, serwer z agentem — są w jednej prywatnej sieci. Bez otwierania portów, bez publicznego IP, bez ryzyka że ktoś z zewnątrz się dostanie.

Konto jest całkowicie darmowe do 3 urządzeń."

💬 WKLEJ NA CHAT:
```
Krok 1 — Konto i instalacja Tailscale:

1. Załóż konto (darmowe): https://tailscale.com/
2. Zainstaluj na urządzeniu z agentem:
   Linux:  curl -fsSL https://tailscale.com/install.sh | sh
   macOS:  brew install tailscale
           lub: App Store → Tailscale
   Windows: https://tailscale.com/download/windows

3. Uruchom i zaloguj się:
   sudo tailscale up

4. Zainstaluj też na swoim głównym laptopie / telefonie
   (tym z którego będziesz zarządzać agentem)
```

📺 **CO POKAZUJĘ:**
- Panel Tailscale — jak wygląda po zalogowaniu, lista urządzeń
- Jak znaleźć adres IP urządzenia w sieci Tailscale (100.x.x.x)

💬 WKLEJ NA CHAT:
```
Krok 2 — Sprawdź adres Tailscale:

Na urządzeniu z agentem wpisz:
tailscale ip -4

Dostaniesz adres 100.x.x.x — to Twój prywatny adres w sieci Tailscale.
Zanotuj go — będzie potrzebny do SSH.

Test połączenia z innego urządzenia (po zalogowaniu do Tailscale):
ping 100.x.x.x
```

🎬 „Teraz SSH. Zakładam że macie zainstalowane SSH na urządzeniu z agentem — na Linuxie i macOS jest domyślnie. Na Windows możecie użyć wbudowanego OpenSSH.

Dla bezpieczeństwa — logujemy się przez klucz, nie przez hasło:"

💬 WKLEJ NA CHAT:
```
Krok 3 — SSH przez Tailscale:

Na swoim głównym laptopie (z którego zarządzasz):

# Wygeneruj klucz SSH jeśli nie masz:
ssh-keygen -t ed25519 -C "openclaw-agent"

# Skopiuj klucz na urządzenie z agentem:
ssh-copy-id user@100.x.x.x

# Połącz się przez SSH:
ssh user@100.x.x.x

# Opcjonalnie — skrót w ~/.ssh/config:
Host agent
  HostName 100.x.x.x
  User twoj_user

# Teraz możesz po prostu:
ssh agent
```

🎬 „Dlaczego klucz zamiast hasła? Hasło można podsłuchać, zgadnąć, wykraść. Klucz kryptograficzny — praktycznie niemożliwy do złamania, i wygodniejszy bo nie musisz go wpisywać.

Mała podpowiedź praktyczna — jak chcecie obserwować agenta na żywo przez SSH, przyda się `tmux` albo `screen` — żeby sesja nie znikała gdy się rozłączycie:"

💬 WKLEJ NA CHAT:
```
Bonus — tmux dla stabilnych sesji:

Instalacja:
sudo apt install tmux  (Ubuntu/Debian)
brew install tmux      (macOS)

Użycie:
tmux new -s agent      ← nowa sesja o nazwie "agent"
openclaw start         ← uruchom agenta w sesji tmux

# Odłącz się (agent działa w tle): Ctrl+B, D
# Wróć do sesji później:
tmux attach -t agent

Agent działa 24/7 nawet gdy jesteś rozłączony.
```

📺 **CO POKAZUJĘ:**
- Demo połączenia SSH przez Tailscale
- Sesja tmux z działającym agentem

🎬 „Kto ma Tailscale zainstalowany na obu urządzeniach i widzi je w panelu — 👍. SSH możecie przetestować w domu — na warsztacie zakładamy że mamy jedno urządzenie, ale mechanizm jest dokładnie ten sam."

---

## 19:10–19:30 — Moduł 4: Komunikator (WhatsApp)
⏱️ 20 min

🎬 **CO MÓWIĘ:**

„Teraz jeden z najbardziej praktycznych elementów — podłączenie komunikatora. Po co? Żebyście mogli pisać do agenta i dostawać od niego wiadomości tak samo jak piszecie do człowieka. Na telefonie, w dowolnym miejscu, bez otwierania terminala.

OpenClaw ma wbudowaną integrację z WhatsApp — ale żeby to działało, potrzebujecie konta WhatsApp które możecie poświęcić dla agenta. Najlepiej osobne, nie Wasze prywatne."

💡 **Upewnij się że masz przygotowane demo tej integracji. WhatsApp wymaga skanowania QR kodu — pokaż to na ekranie.**

💬 WKLEJ NA CHAT:
```
WhatsApp dla agenta — co potrzebujesz:

• Numer telefonu dla agenta (może być ten sam co Wasze,
  ale wtedy agent i Wy dzielicie jedną sesję WhatsApp)
• Lub: osobna karta SIM / numer wirtualny (np. Google Voice,
  numer prepaid) — rekomendowane!

Integracja w OpenClaw:
openclaw skills install whatsapp

Dokumentacja: https://docs.openclaw.ai/skills/whatsapp
```

📺 **CO POKAZUJĘ:**
- Instalacja skilla WhatsApp
- Skanowanie QR kodu

💬 WKLEJ NA CHAT:
```
Krok 1 — Instalacja i konfiguracja WhatsApp:

openclaw skills install whatsapp
openclaw skills configure whatsapp

Przy konfiguracji pojawi się QR kod — zeskanuj go
aplikacją WhatsApp na telefonie:
WhatsApp → ⋮ → Połączone urządzenia → Połącz urządzenie

Agent jest teraz połączony z WhatsApp!
```

🎬 „Jak to działa w praktyce? Piszecie do numeru agenta na WhatsApp i agent odpowiada. Możecie też ustawić żeby agent sam inicjował wiadomości — np. codziennie rano wysyłał Wam podsumowanie ważnych wydarzeń.

Kilka ważnych konfiguracji:"

💬 WKLEJ NA CHAT:
```
Krok 2 — Ustawienia bezpieczeństwa WhatsApp:

W pliku konfiguracyjnym:
~/.openclaw/skills/whatsapp/config.json

Ważne opcje:
{
  "allowedSenders": ["+48TWOJNUMER"],  ← tylko Ty możesz pisać
  "allowedGroups": [],                 ← brak dostępu do grup (na start)
  "maxResponseLength": 1000,
  "requireConfirmation": true          ← agent pyta zanim wyśle do innych
}

Uwaga: bez allowedSenders agent odpowiada KAŻDEMU kto pisze!
```

🎬 „`allowedSenders` to kluczowa opcja. Bez niej każdy kto zna numer agenta może nim sterować. Wpisujcie tam swój numer i tylko swój — przynajmniej na start.

Przetestujmy:"

💬 WKLEJ NA CHAT:
```
Test integracji:

1. Wyślij wiadomość do agenta przez WhatsApp:
   "Cześć, działasz?"

2. Agent powinien odpowiedzieć w ciągu kilku sekund.

3. Wyślij kolejne:
   "Co jest teraz w moim katalogu roboczym?"
   "Która godzina?"

Jeśli działa — 👍 na czacie (lub na WhatsAppie do agenta 😄)
```

💡 **Jeśli ktoś nie ma osobnego numeru — powiedz że to ćwiczenie można zrobić też przez Slack lub Teams (jeśli mają dostęp admina). Alternatywnie zostaje CLI — WhatsApp to wygoda, nie obowiązek na tym warsztacie.**

🎬 „Analogicznie można podłączyć Slack czy Teams — też są jako skills. Podstawowy mechanizm jest taki sam: skill instalujesz, konfigurujesz, i agent dostaje nowy kanał komunikacji."

💬 WKLEJ NA CHAT:
```
Inne komunikatory:

openclaw skills install slack
openclaw skills install teams

Wymagają dostępu admina do workspace'u!
Slack: potrzebny Bot Token i Webhook URL
Teams: potrzebna aplikacja w Azure AD

Dokumentacja:
https://docs.openclaw.ai/skills/slack
https://docs.openclaw.ai/skills/teams
```

---

## 19:30–19:55 — Moduł 5: Personalizacja instrukcji i pamięć agenta
⏱️ 25 min

🎬 **CO MÓWIĘ:**

„Teraz mój ulubiony element — personalizacja. To jest różnica między agentem który jest ogólnym asystentem, a agentem który naprawdę działa dla Ciebie.

Wszystko zaczyna się od pliku `instructions.md`. To jest instrukcja którą agent dostaje przy każdym starcie. Możecie napisać tam kim jest, jak ma reagować, jakie ma priorytety, jakich zasad przestrzegać.

Otwórzcie ten plik:"

💬 WKLEJ NA CHAT:
```
Edycja instrukcji agenta:

nano ~/.openclaw/instructions.md
# lub
code ~/.openclaw/instructions.md
# lub
vim ~/.openclaw/instructions.md

Podstawowa struktura pliku:
```

📺 **CO POKAZUJĘ:**
- Otwieram swój plik `instructions.md` jako przykład

💬 WKLEJ NA CHAT:
```
Przykładowy plik instructions.md:

# Kim jesteś

Jesteś moim osobistym asystentem AI. Mam na imię [Twoje imię].
Pracujesz 24/7 na moim dedykowanym urządzeniu.

# Twoje priorytety

1. Bezpieczeństwo — nigdy nie usuwaj plików bez potwierdzenia
2. Oszczędność tokenów — bądź zwięzły, chyba że proszę o szczegóły
3. Proaktywność — jeśli zauważysz coś ważnego, powiedz mi przez WhatsApp

# Styl komunikacji

- Komunikuj się po polsku, chyba że piszę po angielsku
- Bądź bezpośredni, bez zbędnych grzeczności
- Nie zaczynaj każdej odpowiedzi od "Oczywiście!" ani "Jasne!"

# Zasady

- Drafts only: emaile i posty twórz jako szkice, nie wysyłaj
- Nie usuwaj plików — przenoś do ~/.trash/
- Commituj regularnie jeśli pracujesz z git
- Loguj ważne akcje do ~/.openclaw/logs/actions.log

# Kontekst

Pracuję jako [Twoja rola]. Mój główny projekt to [projekt].
Preferowane narzędzia: [lista].
```

🎬 „Napiszcie swój własny plik — nawet 5-10 linii. Nie musi być idealny, możecie go edytować w dowolnym momencie. Kluczowe żeby agent wiedział czym się zajmujecie i jakie są Wasze priorytety.

Dajcie 3 minuty na napisanie podstawowej instrukcji."

🏋️ **ĆWICZENIE — Personalizacja instrukcji (4 min):**

💬 WKLEJ NA CHAT:
```
Ćwiczenie: Napisz swój instructions.md

Minimum czego potrzebuje Twój agent:
1. Kim jest (Twoje imię, Twoja rola)
2. Jeden priorytet (np. "bezpieczeństwo" / "oszczędność" / "szybkość")
3. Jedna zasada (np. "nigdy nie usuwaj plików")
4. Jeden element stylu (np. "komunikuj się po polsku")

Zapisz plik i zrestartuj agenta:
openclaw restart

Zadaj agentowi: "Przypomnij mi swoje główne zasady pracy."
Wrzuć na chat co agent odpowiedział!
```

🎬 „Świetnie. Teraz **pamięć agenta** — to jest coś co odróżnia naprawdę użytecznego agenta od jednorazowego narzędzia.

OpenClaw ma kilka typów pamięci:"

💬 WKLEJ NA CHAT:
```
Typy pamięci w OpenClaw:

📝 Core Memory (pamięć podstawowa)
   Plik: ~/.openclaw/memory/core.md
   Zawsze ładowana. Tu agent trzyma najważniejsze fakty o Tobie.
   Przykład: "Użytkownik pracuje w strefie czasowej CET.
              Preferowany język: polski. Urodziny: 15 marca."

🧠 REM Memory (pamięć robocza)
   Automatycznie zapisywana podczas sesji.
   Agent pamięta kontekst rozmowy nawet po restarcie.

💾 Deep Memory (pamięć długoterminowa)
   Archiwum ważnych informacji i wniosków.
   Agent sięga do niej gdy potrzebuje kontekstu historycznego.

Zarządzanie pamięcią:
openclaw memory list       ← lista wszystkich wpisów
openclaw memory show core  ← pokaż core memory
openclaw memory clear rem  ← wyczyść REM memory
```

📺 **CO POKAZUJĘ:**
- Plik core.md — jak wygląda moja pamięć agenta
- Przykład jak agent używa pamięci w rozmowie

🎬 „Możecie ręcznie edytować `core.md` — to jest zwykły plik Markdown. Albo poprosić agenta żeby sam coś zapamiętał:

'Zapamiętaj: mój główny projekt to [nazwa], repo jest tutaj: [url]'

Agent doda to do swojej pamięci i będzie korzystał przy kolejnych zadaniach."

💬 WKLEJ NA CHAT:
```
Przykładowe wpisy do core memory:

Powiedz agentowi:
"Zapamiętaj że pracuję głównie wieczorami, między 18:00 a 23:00."
"Zapamiętaj że mój główny projekt to [nazwa] i jest w katalogu [ścieżka]."
"Zapamiętaj że preferuję krótkie odpowiedzi, maksimum 3-4 zdania."

Agent zaktualizuje swój core.md automatycznie.
```

---

## 19:55–20:05 — PRZERWA ☕
⏱️ 10 min

💬 WKLEJ NA CHAT:
```
☕ Przerwa 10 minut → wracamy 20:05

Po przerwie:
→ Automatyzacja: Cron, Heartbeat, Skills, MCP, Search
→ Koszty, optymalizacja, logi i monitoring
→ Pytania i podsumowanie

Jeśli coś nie działa — napisz teraz, zerknę!
```

---

## 20:05–20:40 — Moduł 6: Automatyzacja: Cron, Heartbeat, Skills, MCP, Search
⏱️ 35 min

🎬 **CO MÓWIĘ:**

„Wracamy — ostatnia duża część. Automatyzacja. To jest to po co tu jesteście.

Zaczniemy od dwóch mechanizmów które sprawiają że agent działa naprawdę autonomicznie: **Heartbeat** i **Cron**."

💬 WKLEJ NA CHAT:
```
Heartbeat vs Cron — różnica:

💓 HEARTBEAT — agent budzi się regularnie co X minut i sprawdza
   "Czy jest coś do zrobienia? Czy jest coś nowego?"
   Działa jak ciągły monitoring.
   Przykład: co 15 minut sprawdza skrzynkę i ważne powiadomienia.

⏰ CRON — konkretne zadanie o konkretnej godzinie / dniu
   Działa jak systemowy cron (harmonogram zadań).
   Przykład: codziennie o 8:00 wysyła podsumowanie dnia na WhatsApp.

Konfiguracja w ~/.openclaw/config.json:
{
  "heartbeat": {
    "enabled": true,
    "intervalMinutes": 15,
    "prompt": "Sprawdź czy są nowe pilne sprawy. Jeśli tak — napisz do mnie na WhatsApp."
  }
}
```

📺 **CO POKAZUJĘ:**
- Konfiguracja heartbeat w pliku config.json
- Przykładowy log z działającego heartbeat

💬 WKLEJ NA CHAT:
```
Konfiguracja Cron:

W ~/.openclaw/config.json dodaj sekcję "crons":
{
  "crons": [
    {
      "name": "morning-briefing",
      "schedule": "0 8 * * 1-5",
      "prompt": "Przygotuj krótkie podsumowanie na dziś: dzień tygodnia, ważne rzeczy z wczoraj z logów, przypomnienie o ewentualnych zaplanowanych zadaniach. Wyślij na WhatsApp.",
      "enabled": true
    },
    {
      "name": "weekly-cleanup",
      "schedule": "0 20 * * 0",
      "prompt": "Zrób porządek w katalogu workspace — usuń pliki tymczasowe, skompresuj stare logi, zrób commit jeśli są zmiany.",
      "enabled": true
    }
  ]
}

Format harmonogramu: minuta godzina dzień miesiąc dzień_tygodnia
0 8 * * 1-5 = każdy dzień roboczy o 8:00
```

🎬 „Skills — o jednym już mówiliśmy (WhatsApp). Sprawdźmy jakie inne skills są dostępne:"

💬 WKLEJ NA CHAT:
```
Popularne Skills:

openclaw skills list              ← lista zainstalowanych
openclaw skills search <nazwa>    ← szukaj dostępnych

Przydatne skills:
• web-search    ← przeszukiwanie internetu
• gmail         ← integracja z Gmail
• github        ← operacje na repozytoriach
• calendar      ← Google Calendar / Outlook
• files         ← operacje na plikach (już wbudowane)
• whatsapp      ← (zainstalowaliśmy)
• slack / teams ← komunikatory firmowe

Instalacja:
openclaw skills install web-search
```

🎬 „Web Search — to jest szczególnie przydatne. Agent może samodzielnie przeszukiwać internet gdy potrzebuje aktualnych informacji. Bez tego jest ograniczony do swojej wiedzy treningowej."

💬 WKLEJ NA CHAT:
```
Konfiguracja Web Search:

openclaw skills install web-search
openclaw skills configure web-search

Obsługiwane wyszukiwarki:
• Perplexity API — najlepsza jakość wyników dla AI
• Grok Search (X.com) — świetny dla trendów i aktualności
• Brave Search API — darmowy tier dostępny!
• DuckDuckGo — działa bez klucza API (fallback)

Brave Search (darmowy): https://api.search.brave.com/

W konfiguracji:
{
  "provider": "brave",
  "apiKey": "BSA..."
}
```

📺 **CO POKAZUJĘ:**
- Demo: proszę agenta o wyszukanie czegoś aktualnego
- Agent używa web search i zwraca wynik z źródłem

🎬 „Na koniec tego modułu — **MCP**, czyli Model Context Protocol. To jest standard który pozwala agentowi korzystać z zewnętrznych narzędzi i danych w ustandaryzowany sposób.

Prosto mówiąc: MCP to wtyczki dla agenta, tylko zrobione porządnie."

💬 WKLEJ NA CHAT:
```
MCP — Model Context Protocol:

Co to jest: standard od Anthropic (teraz Linux Foundation)
Pozwala agentowi korzystać z zewnętrznych narzędzi przez API.

Różnica od Skills:
• Skills — wbudowane integracje OpenClaw
• MCP — zewnętrzne serwery narzędziowe, dowolnego dostawcy

Przykłady MCP serverów:
• filesystem — operacje na plikach przez MCP
• github — pełne API GitHuba przez MCP
• postgres / sqlite — zapytania do baz danych
• browser — sterowanie przeglądarką

Lista MCP serverów: https://github.com/modelcontextprotocol/servers

Konfiguracja w OpenClaw:
openclaw mcp add filesystem
openclaw mcp list
```

🎬 „ACP (Agent Communication Protocol) — to kolejny krok po MCP. Pozwala agentom OpenClaw komunikować się między sobą. Jeden agent może być 'szefem' i delegować zadania innym specjalistycznym agentom. To zaawansowany temat — jeśli chcecie więcej: https://docs.openclaw.ai/tools/acp-agents"

---

## 20:40–21:00 — Moduł 7: Koszty, optymalizacja, logi, monitoring + Podsumowanie
⏱️ 20 min

🎬 **CO MÓWIĘ:**

„Ostatni moduł — koszty i monitoring. Agent który działa 24/7 kosztuje — chcemy mieć kontrolę nad tym ile.

Zacznijmy od tego jak sprawdzić co już wydaliśmy:"

💬 WKLEJ NA CHAT:
```
Monitoring kosztów:

openclaw stats              ← statystyki ogólne (tokeny, koszty)
openclaw stats --today      ← koszty dzisiaj
openclaw stats --month      ← koszty w tym miesiącu

Logi działania:
openclaw logs               ← ostatnie zdarzenia
openclaw logs --follow      ← live monitoring (jak tail -f)
openclaw logs --filter error ← tylko błędy

Plik logów: ~/.openclaw/logs/
```

📺 **CO POKAZUJĘ:**
- Wyjście `openclaw stats` z przykładowymi danymi
- Jak wygląda log z działającego agenta

🎬 „Kilka zasad które pozwalają trzymać koszty w ryzach:"

💬 WKLEJ NA CHAT:
```
Optymalizacja kosztów:

💡 Model do zadania:
   • Proste zadania (synteza, klasyfikacja) → tańszy model (Haiku, Gemma 4)
   • Złożone zadania (analiza, kod) → mocniejszy model (Opus, Sonnet)
   • Możesz skonfigurować różne modele dla heartbeat i dla rozmów

💡 Heartbeat pod kontrolą:
   • Krótszy interval = więcej wywołań = wyższy koszt
   • Zacznij od 30-60 minut, nie od 5 minut
   • Wyłącz heartbeat na noc jeśli nie potrzebujesz

💡 Instrukcja = oszczędność:
   • "Bądź zwięzły" w instructions.md realnie zmniejsza zużycie tokenów
   • Dobra instrukcja = mniej pytań wyjaśniających = mniej tokenów

💡 Fallback na lokalne modele:
   • Skonfiguruj Ollama jako fallback dla prostych zadań
   • "Dla heartbeat używaj modelu lokalnego, dla ważnych zadań API"

💡 Budżety i limity:
   • Ustaw miesięczny limit w panelu dostawcy API
   • OpenClaw: opcja max_daily_cost w config.json
```

🎬 „Na koniec — kilka słów o tym co możecie zrobić dalej, żebyście wychodzili z konkretnym planem:"

💬 WKLEJ NA CHAT:
```
Co dalej — pierwsze kroki po warsztacie:

Tydzień 1 — Podstawy:
□ Uruchom agenta na docelowym urządzeniu
□ Skonfiguruj Tailscale + SSH
□ Napisz własny instructions.md
□ Podłącz komunikator (WhatsApp lub inny)
□ Ustaw jeden prosty heartbeat
□ Monitoruj logi i koszty przez tydzień

Tydzień 2 — Automatyzacja:
□ Dodaj pierwszy Cron (np. poranne podsumowanie)
□ Zainstaluj Web Search
□ Skonfiguruj core memory dla agenta
□ Eksperymentuj z różnymi modelami

Tydzień 3+ — Ekspansja:
□ Dodaj Skills dopasowane do Twojej pracy
□ Sprawdź MCP servery które mogą Ci się przydać
□ Zastanów się nad multi-agent setup (ACP)
□ Wróć do dokumentacji i odkryj co pominęliśmy

Dokumentacja: https://docs.openclaw.ai
```

🎬 „Podsumowanie tego co dzisiaj zrobiliśmy:"

💬 WKLEJ NA CHAT:
```
✅ Podsumowanie warsztatu:

□ OpenClaw zainstalowany i skonfigurowany
□ Dostawca LLM podłączony
□ Tailscale skonfigurowany (lub plan jak to zrobić)
□ SSH gotowy (lub plan)
□ WhatsApp / komunikator podłączony (lub plan)
□ instructions.md — personalizacja agenta
□ Pamięć agenta (core memory) skonfigurowana
□ Heartbeat i Cron — wiemy jak to ustawić
□ Web Search podłączony
□ Wiemy jak monitorować koszty i logi

Jeśli nie wszystko udało się dzisiaj — to jest w porządku.
Dokumentacja jest dobra, a to co masz daje solidną bazę.
```

🎬 „Kilka słów ode mnie na koniec.

OpenClaw to naprawdę ogromny projekt i ciągle się rozwija. To co pokazałem to fundament — najprostsza droga żeby mieć działającego agenta. Reszta to tygodnie eksperymentowania i odkrywania.

Nie bójcie się prób i błędów — po to mamy oddzielne urządzenie, Tailscale, backupy i logi. Agent może zrobić coś głupiego — i zrobi. Ale jeśli macie bezpieczne środowisko, to jest to tylko nauka, nie katastrofa.

Jeśli ktoś ma problem z uruchomieniem agenta i chce spróbować jeszcze raz — mogę zostać kilka minut dłużej. Napiszcie na czacie."

💬 WKLEJ NA CHAT:
```
Dziękuję za udział! 🎯

Jeśli masz pytania po warsztacie — znajdziesz mnie na LinkedIn.
Słownik pojęć AI znajdziesz w materiałach do szkolenia.

Zasoby:
📖 Dokumentacja OpenClaw: https://docs.openclaw.ai
🌐 Tailscale: https://tailscale.com
🤖 Ollama (lokalne modele): https://ollama.com
💰 Z.ai (agentowy plan, 10% rabat): https://z.ai/subscribe?ic=IA5VBRGQV4

Do zobaczenia! 👋
```

---

## 💡 Notatki dla prowadzącego

### Jeśli zostaje czas
- Pokaż demo ACP Agents — jak dwa agenty ze sobą rozmawiają
- Pokaż generowanie mediów (obrazy, audio) przez API: https://docs.openclaw.ai/tools/media-overview
- Wejdź głębiej w zaawansowane opcje pamięci (Deep Memory, wyszukiwanie semantyczne)

### Jeśli brakuje czasu
- Skróć Moduł 6 — zostaw tylko Heartbeat + Cron, resztę daj jako materiały do samodzielnej nauki
- Moduł 3 (Tailscale/SSH) możesz zbić do 10 minut i dać linki do dokumentacji

### Częste problemy
- **Node.js za stara wersja** → `nvm install 22` lub ręczna instalacja z nodejs.org
- **Windows bez WSL2** → Git Bash jako minimum, ale zachęć do WSL2
- **Brak klucza API** → zaproponuj Ollama z Gemma 4 jako darmową opcję na start
- **WhatsApp QR wygasa** → trzeba być szybkim ze skanowaniem, QR ważny ok. 60 sekund
- **Agent nie odpowiada** → sprawdź `openclaw status` i logi: `openclaw logs --filter error`

### Ankieta startowa — jak interpretować wyniki
- Dużo Windows → więcej czasu na WSL2, zaznacz GitBash jako fallback
- Dużo osób bez API → omów Ollama + Gemma 4 szerzej, pokaż że to realnie działa
- Dużo nietech (PM, CEO) → tłumacz więcej analogiami, mniej technicznych szczegółów konfiguracji
- Mała znajomość CLI → zwolnij przy instalacji, wyjaśniaj każdą komendę