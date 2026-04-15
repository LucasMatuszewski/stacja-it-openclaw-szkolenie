## Szybkie podsumowanie

Szkolenie to miało na celu zapoznanie uczestników z OpenClave, autonomiczną platformą agentów, która zyskała ostatnio znaczną popularność. Łukasz Matuszewski, trener i programista z ponad piętnastoletnim doświadczeniem, poprowadził sesję poświęconą instalacji, konfiguracji oraz zagadnieniom bezpieczeństwa agentów działających. Szkolenie obejmowało dyskusje na temat różnych opcji modeli, w tym Genma 4, najlepszych praktyk bezpieczeństwa oraz metod komunikacji za pośrednictwem platform takich jak Telegram i WhatsApp. Uczestnicy napotkali pewne trudności techniczne, w szczególności przy instalacji systemu Mac OS, które Łukasz rozwiązał poprzez zaproponowanie alternatywnych rozwiązań, w tym wykorzystanie starszych wersji oprogramowania. Podczas sesji omówiono również pliki konfiguracyjne, ustawienia dostawcy oraz znaczenie używania dedykowanych urządzeń dla uruchamianych agentów w celu zapewnienia bezpieczeństwa.

## Kolejne kroki

- Łukasz: Prześlij przykładowe pliki konfiguracyjne i dodatkowe instrukcje do wspólnego repozytorium w celach informacyjnych dla uczestników.
- Łukasz: Udostępniaj linki i dokumentację dotyczącą umiejętności, dostawców, zarządzania pamięcią oraz odpowiednich praktyk bezpieczeństwa w repozytorium.
- Łukasz: Udostępnij uczestnikom link do ankiety i poproś o jej wypełnienie po szkoleniu.
- Wszyscy uczestnicy: Wypełnij ankietę po szkoleniu zgodnie z prośbą Łukasza.
- Wszyscy uczestnicy: Skonfiguruj listy dozwolonych użytkowników/identyfikatorów telefonów w ustawieniach OpenClowd/WhatsApp/Telegram, aby ograniczyć dostęp agenta, zgodnie z omówionymi najlepszymi praktykami bezpieczeństwa.
- Jacek/Uczestnicy z problemami z Gateway/Instalacją: Pozostań po szkoleniu (lub skontaktuj się z Łukaszem mailowo) w celu indywidualnego rozwiązywania problemów związanych z usługą Gateway i instalacją.
- Łukasz: Zapewnij wsparcie Jackowi i innym osobom pozostającym po szkoleniu w zakresie problemów związanych z uruchamianiem Gateway/agentów.
- Łukasz: Zbadaj i zaktualizuj informacje na temat problemów z instalacją specyficznych dla komputerów Mac oraz udostępnij je dotkniętym uczestnikom.
- Wszyscy uczestnicy: Okresowo przeprowadzajcie audyty bezpieczeństwa i rozważcie możliwość regularnego (np. cogodzinnego) tworzenia kopii zapasowych/wakapów na urządzeniu z uruchomionym agentem, zgodnie z zaleceniami Łukasza.
- Łukasz: Zaktualizuj repozytorium o zaawansowane przykłady konfiguracji i zanonimizowane pliki szablonów do wykorzystania w przyszłości.
- Wszyscy uczestnicy: Przejrzyj i, jeśli to konieczne, zaktualizuj zarządzanie pamięcią agenta oraz konfigurację „marzeń” w celu poprawy wydajności, o czym wspomniano pod koniec szkolenia.
- Łukasz: Rozważ planowanie i ogłaszanie bardziej zaawansowanych/kontynuacyjnych sesji szkoleniowych oraz poinformuj zainteresowanych uczestników o przyszłych terminach.

## Podsumowanie

### Sesja szkoleniowa dla agentów autonomicznych OpenClaw

Łukasz przeprowadził szkolenie na temat autonomicznych agentów z OpenClaw, przedstawiając 4-godzinny program obejmujący instalację, konfigurację, bezpieczeństwo i automatyzację. Sesję rozpoczęły wstępy, podczas których uczestnicy podzielili się swoimi doświadczeniami technicznymi i preferencjami dotyczącymi systemów operacyjnych: Patryk wspomniał, że kieruje zespołami programistycznymi i używa systemu Mac OS, a Jacek zidentyfikował się jako networker aspirujący do DevOps. Łukasz podkreślił, że chociaż istnieją opcje Windows i Dockera, szkolenie skupiłoby się na instalacjach Linux przy użyciu dedykowanych urządzeń dla optymalnej wydajności, szczególnie zauważając, że nawet starsze laptopy mogą obsługiwać podstawowe operacje agentów.

### Dyskusja na temat konfiguracji technicznej projektu OpenClaw

Łukasz poprowadził dyskusję na temat konfiguracji technicznej podczas warsztatów, prosząc uczestników o weryfikację swojego środowiska poprzez sprawdzenie wersji Node.js, npm i Git. Wyjaśnił korzyści i aktualny status projektu OpenClaw, podkreślając jego szybki rozwój i wszechstronność w porównaniu z innymi platformami asystentów AI, takimi jak Claude. Łukasz omówił również różne opcje dostępu i wykorzystania modeli AI, ostrzegając przed korzystaniem z niektórych dostawców chmury ze względu na ograniczenia dostępu oraz rekomendując wykorzystanie bezpośredniego dostępu API jako najbezpieczniejszej, ale najdroższej opcji.

### Lokalne vs chmurowe modele AI

Łukasz omówił zalety i ograniczenia modeli lokalnych w porównaniu z modelami chmurowymi, wyjaśniając, że chociaż modele lokalne oferują prywatność i potencjalnie szybszą wydajność, mogą nie być odpowiednie do złożonych zadań wymagających logicznego planowania lub zarządzania wieloma agentami. Podkreślił znaczenie uwzględnienia wymagań sprzętowych, zwłaszcza pojemności procesora graficznego, dla optymalnej wydajności modeli takich jak Gemma 4. Grupa omówiła również kwestie bezpieczeństwa podczas udzielania agentom AI dostępu do systemów, a Łukasz podzielił się przykładem incydentu, w którym agent AI przypadkowo usunął e-maile z powodu niewłaściwych uprawnień. Wreszcie zbadali możliwości dostępu do różnych modeli sztucznej inteligencji i korzystania z nich, w tym zarówno bezpłatnych, jak i płatnych wersji za pośrednictwem platform takich jak Ollama.

### Instalacja zabezpieczeń OpenClaw AI

Łukasz omówił kwestie bezpieczeństwa instalacji agentów OpenClaw AI, podkreślając znaczenie równoważenia uprawnień w celu zapewnienia funkcjonalności przy jednoczesnym zachowaniu bezpieczeństwa. Zalecił użycie zewnętrznego urządzenia do uruchamiania agenta i odradzał udzielanie dostępu do wrażliwych kont, takich jak Chrome. Łukasz podkreślił również potrzebę regularnych kopii zapasowych i wspomniał, że agent może pomóc zidentyfikować i rozwiązać problemy bezpieczeństwa. Rozmowa zakończyła się instrukcją instalacji agenta przy użyciu dostarczonych skryptów dla różnych systemów operacyjnych, z planami kontynuacji procesu instalacji po przerwie.

### Nolda Wersja 22.14 Dyskusja instalacyjna

Jacek i Łukasz omówili instalację Nolda w wersji 22.14, a Łukasz udzielił wskazówek dotyczących metod instalacji i zasugerował bezpośrednie pobranie dla systemów Linux. Łukasz doradził Mariuszowi, aby zamiast czekać zainstalował oprogramowanie natychmiast, ponieważ pomoże to w pamięci mięśniowej i przyszłych transferach na inne urządzenia. Dyskusja obejmowała proces instalacji, w tym wykorzystanie skryptu automatyzującego instalację i konfigurację pakietów, podkreślając jednocześnie, że kontener Docker można łatwo wyłączyć w razie potrzeby.

### Spotkanie instalacyjne i konfiguracyjne OpenClaw

Spotkanie dotyczyło instalacji i konfiguracji OpenClaw, narzędzia do zarządzania agentami oraz uzyskiwania dostępu do różnych usług. Łukasz wyjaśnił proces instalacji, w tym tworzenie folderów w katalogu użytkownika oraz użycie polecenia `openclaw onboard`. Omówił najlepsze praktyki bezpieczeństwa, rekomendując użycie dedykowanego urządzenia i oddzielnych kont dla lepszego bezpieczeństwa. Grupa zbadała również opcje modeli chmurowych, takich jak Z.ai i Minimax, biorąc pod uwagę koszty i konsekwencje dla bezpieczeństwa. Jacek zapytał o parametry instalacji, a Łukasz udzielił wskazówek dotyczących rozwiązywania problemów i ponownego uruchomienia procesu konfiguracji w razie potrzeby.

### Konfiguracja integracji platformy komunikacyjnej

Zespół omówił opcje konfiguracji integracji różnych platform komunikacyjnych i modeli AI z ich systemem. Łukasz polecił Telegram lub WhatsApp jako najprostsze opcje do natychmiastowego wdrożenia, zauważając jednocześnie, że Teams i Yy wymagałyby bardziej złożonej konfiguracji. Dyskusja dotyczyła różnych dostawców modeli AI, w tym Claude’a, Minimax i Dpsic, a Łukasz zasugerował Claude 5.4 jako najlepszą aktualną opcję. Jacek pytał o wykorzystanie API i wybór modeli, a Łukasz wyjaśniał jak konfigurować dostawców i modele za pomocą plików konfiguracyjnych systemu. Rozmowa obejmowała szczegółowe wyjaśnienie, jak skonfigurować i zorganizować różne modele i dostawców w systemie konfiguracyjnym, a Łukasz jako przykład podał własne zaawansowane podejście do konfiguracji.

### Demo konfiguracji agenta OpenClaw AI

Łukasz zademonstrował proces tworzenia i konfigurowania agenta OpenClaw AI, koncentrując się na środkach bezpieczeństwa oraz kanałach komunikacji. Wyjaśnił znaczenie korzystania z bezpiecznej sieci lokalnej i omówił opcję użycia tunelu VPN lub SSH dla dodatkowego bezpieczeństwa. Grupa postanowiła wykorzystać Telegram jako główny kanał komunikacji dla agenta, a Łukasz udzielił instrukcji jak skonfigurować bota Telegram i uzyskać niezbędny token. Wspomniał również, że bardziej zaawansowane tematy bezpieczeństwa i dodatkowe opcje połączeń zostaną omówione w przyszłych sesjach.

### Integracja Telegramu Problemy z konfiguracją systemu macOS

Zespół omówił problemy z konfiguracją integracji Telegrama w OpenClaw na macOS. Patryk zgłosił napotkanie błędów podczas konfigurowania kanałów Telegram i WhatsApp, które według Łukasza mogą być związane z problemami specyficznymi dla macOS. Grupa stwierdziła, że obniżenie wersji do 2026.4.12 może rozwiązać problemy z konfiguracją, a Łukasz zauważył, że chociaż OpenClaw szybko się rozwija, takie problemy są zazwyczaj rozwiązywane w ciągu 24 godzin. Dyskusja dotyczyła również alternatywnych metod komunikacji z agentami, w tym wykorzystania API OpenClaw i protokołów do wewnętrznej integracji aplikacji, choć Łukasz zastrzegł, że chociaż OpenClaw jest odpowiedni dla użytkowników technicznych, może nie być jeszcze w pełni gotowy do wdrożenia w przedsiębiorstwach.

### Konfiguracja kanałów komunikacyjnych OpenClaw

Łukasz poprowadził dyskusję na temat konfiguracji kanałów komunikacji i wyszukiwarek dla agentów OpenClaw. Wyjaśnił znaczenie tworzenia list zezwoleń w celu ograniczenia tego, kto może komunikować się z botami, szczególnie na platformach takich jak Telegram i WhatsApp. Łukasz zademonstrował, jak skonfigurować te ustawienia i zalecił ponowne uruchomienie bramki po wprowadzeniu zmian. Zespół napotkał pewne problemy techniczne z najnowszą wersją bramy, co Łukasz przyznał i obiecał zbadać dalej. Przedstawił również przegląd różnych opcji wyszukiwania w Internecie dostępnych dla agentów, w tym bezpłatnych i płatnych alternatyw, takich jak Grok i Prepecty.

### Umiejętności w OpenClaw Dyskusja

Łukasz omówił wyzwania związane z udziałem firm w szkoleniach ze względu na złożoność i ryzyko. Wyjaśnił koncepcję umiejętności w OpenClaw, opisując je jako moduły, które mogą rozszerzyć możliwości agenta, choć ostrzegł przed potencjalnymi problemami bezpieczeństwa związanymi z umiejętnościami tworzonymi przez użytkowników. Dyskusja obejmowała informacje na temat wyszukiwania i instalowania Umiejętności, w tym sposobu oceny ich bezpieczeństwa.

### Sesja szkoleniowa OpenClaw AI Agent

Łukasz przeprowadził szkolenie z OpenClaw, demonstrując jak założyć i skonfigurować agenta AI. Omawiał różne aspekty, w tym tworzenie agentów, pliki konfiguracyjne, zarządzanie pamięcią i integrację z usługami takimi jak WhatsApp. Sesja obejmowała dyskusje na temat ustawień zabezpieczeń, rozwiązywania typowych problemów oraz korzystania z różnych narzędzi do wdrażania agentów. Łukasz podkreślił elastyczność i potencjał agentów OpenClaw, ale zwrócił uwagę na złożoność narzędzia, sugerując, że w przyszłości może być potrzebne bardziej kompleksowe szkolenie. Uczestnicy zadawali pytania dotyczące konkretnych konfiguracji i użytkowania, a Łukasz udzielił wskazówek i rekomendował zasoby do dalszej nauki.
