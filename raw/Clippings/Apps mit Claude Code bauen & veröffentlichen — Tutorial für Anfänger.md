---
title: "Apps mit Claude Code bauen & veröffentlichen — Tutorial für Anfänger"
source: "https://www.youtube.com/watch?v=XkgkqBkwA9c"
author:
  - "[[Julian Ivanov | KI-Automatisierung]]"
published: 2026-05-24
created: 2026-06-20
description: "🚀 Die schnellste Abkürzung um KI Automatisierung zu meistern: https://skool.com/ki-automatisierung🟣 Web-Apps schnell & günstig hosten: https://www.hostg.xy..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=XkgkqBkwA9c)

## Transcript

### Einleitung

**0:00** · In diesem Video zeige ich dir Schritt für Schritt, wie du als absoluter Anfänger eine komplette Webapplikation mit Cloud Code entwickelst und am Ende auf einem Server in Deutschland deployst, sodass sie auch wirklich live im Internet ist. Wir bauen dabei keine simple Website, sondern eine richtige Webapp mit Logins, User Accounts und

**0:19** · einer richtigen Datenbank im Hintergrund, in der deine Daten persistent gespeichert werden, denn dieser Teil wird in den meisten Tutorials einfach weggelassen, weil er vermeintlich zu komplex ist, was aber überhaupt nicht mehr stimmt, denn mittlerweile sind wir an dem Punkt angekommen, wo die KI die gesamte Programmierung der Anwendung und die Einrichtung der Datenbank vollständig für uns übernimmt und wir das Ganze einfach nur korrekt orchestrieren müssen. Wie das konkret funktioniert, schauen wir uns jetzt an.

**0:43** · Wir gehen jeden Schritt gemeinsam durch, sodass du am Ende deine eigene Webapp bauen kannst mit Nutzerverwaltung, Datenbank und auch Hosting, ohne eine einzelne Zeile Code zu schreiben. Also lass uns direkt loslegen. Um das Ganze anhand einer Webapp zu demonstrieren, habe ich mir jetzt eine App überlegt, in der man Gewohnheiten trackt. Das heißt, du logst dich bei der App ein, legst deine Gewohnheiten an, also z.B. will 20 Minuten am Tag joggen oder 30 Seiten am Tag lesen, hast sie täglich ab und siehst dann dabei deine Streak.

### Was wir heute bauen

**1:10** · Das Beispiel habe ich gewählt, weil es kompakt genug ist, dass wir es in der Zeit jetzt schaffen, aber gleichzeitig wirklich alle wichtigen Bausteine drin hat. Wir werden eine Datenbank anlegen, um unsere Fortschritte persistent zu speichern. Wir werden eine Nutzerverwaltung einbauen. Das heißt, wir können verschiedene Nutzer erstellen als Admin. Die können sich dann mit ihrem Account einloggen und sehen dann ihre eigenen Gewohnheiten und können diese tracken. Wir werden natürlich auch eine Art Dashboard einbauen mit verschiedenen Ansichten und natürlich auch verschiedenste Funktionen, um eben Gewohnheiten anzulegen und auch abzuhaken.

**1:41** · Das heißt, die App wird auch mehrere Seiten und Ansichten haben, durch die man klicken kann. Diese Bausteine hier, also Datenbank, Nutzerverwaltung und Dashboards sowie weitere Funktionalitäten, sind eigentlich Bausteine, die du in fast jeder App so wiederfindest. Das heißt, wenn du das Prinzip einmal verstanden hast, kannst du den gleichen Ablauf für jegliche anderen Appen, die du hast, anwenden. Ich würde dir auch immer empfehlen, am Anfang deine App mal so ein bisschen zu skizzieren, um zu verstehen, welche Funktionalitäten enthalten sein sollen, denn das wird dir dann noch später bei der Kommunikation mit Cloud Code helfen.

**2:11** · Bevor wir loslegen, sollten wir uns auch kurz Gedanken über den Text machen. Das heißt, was brauchen wir überhaupt und vor allem, was kostet das Ganze? Im Prinzip brauchen wir drei Bausteine, ein KI Coding Tool, eine Datenbank und einen Hoster, der die App ins Internet bringt.

### Tech-Stack und Kosten (Claude Code, Supabase, Hostinger)

**2:27** · Bei allen drei Punkten gibt es viele Optionen. Ich zeige dir heute einfach die Kombination, die ich für Anfänger am sinnvollsten halte, weil sie günstig ist, technisch sauber funktioniert und auch Server in Deutschland nutzt, ne?

**2:38** · Stichwort DSGVO. Als ersten Baustein haben wir Cloud Code in der Cloud Desktop App. Cloud Code ist Anthopics offizielles Tool für KI Coding und das Schöne ist, es ist direkt in der Clot Desktop App integriert. Das heißt, du lädst dir einfach die Desktop App für Mac oder Windows herunter, logst dich mit deinem Anthropic Account ein und im Codebereich kannst du dann mit Cloud Code gemeinsam entwickeln. Das heißt, als Anfänger brauchst du auch überhaupt keine Entwicklungsumgebung zu nutzen oder ein Terminal oder so.

**3:03** · Du sagst einfach in normaler Sprache hier in der App, was du möchtest und Cloud Code legt los, legt Dateien an, füllt Befehle aus und so weiter. Alles direkt in der Desktop App und du musst dafür keine einzelne Zeile Code tippen. Du musst ja jetzt auch nicht unbedingt Cloud Code nutzen, wenn du lieber Codex nutzt und die Codex App, ne? Falls du jetzt z.B.

**3:22** · ein CHGBT Abo hast, dann kannst du das natürlich auch machen. Das wird genauso funktionieren. Um Cloud Code zu nutzen, brauchen wir mindestens den Pro Plan und den kriegst du schon für 18 € im Monat.

**3:32** · Als zweiten Baustein brauchen wir eine Datenbank und ich würde dir dafür Superbase empfehlen. Es gibt viele Datenbanken da draußen, aber ich finde Superbase einfach sehr praktikabel, vor allem für Anfänger und das aus drei Gründen. Erstens ist es komplett kostenlos hier im Freeter und der Freetier reicht auch für die meisten Anwendungen komplett aus. Zweitens kannst du hier auch Server wählen, die in Deutschland stehen, das heißt in Frankfurt z.B. das ist natürlich dann relevant, wenn du dies GVO konform bleiben möchtest. Und drittens, und das ist ein riesiger Punkt, Anthropic und Superbase haben einen offiziellen Connector gebaut. Das heißt, Cloud kann direkt mit Superbase kommunizieren.

**4:03** · Du musst dafür einmal hier so ein Connektor einrichten. Das schauen wir uns dann auch gleich an. Und ab dann kann Claud praktisch deine gesamte Superbase Instanz steuern. Das heißt, Cloud kann für dich Projekte anlegen, Tabellen erstellen, Sicherheitsregeln einrichten, User anlegen und so weiter. Und du musst dafür nichts selber machen. Also, wir werden gar nichts selbst in Superbase konfigurieren. Das wird alles cloud für uns steuern. Der dritte Baustein ist das Hosting. Das heißt, wie bekommen wir die App ins Internet? Die muss ja irgendwie auf dem Server laufen und da würde ich dir ganz klar Hostinger empfehlen als Anbieter.

**4:34** · Und zwar nutzen wir dort das Node GS Web Hosting. Auch beim Hosting gibt es viele Optionen, ne? Wie z.B. bei Versel oder auch Railway. Aber als Anfänger und vor allem, wenn man DSGVO konform bleiben möchte, würde ich einfach Hostinger empfehlen. Wir können wieder Server in Deutschland nutzen. Wir haben einen festen Monatspreis, also keine Usage Gebühren oder so. Bei Versell halt zum Hobbyplan zwar nichts, aber sobald deine App User bekommt und auch mehr Nutzung sozusagen über die App entsteht, dann kommen Verbrauchsgebühren dazu und insgesamt bist du da bei Hostinger deutlich günstiger dran.

**5:03** · Zudem kannst du bis zu fünf von diesen Apps gleichzeitig in einem Plan hosten. Du brauchst also nicht für jede App einzeln bezahlen und du bekommst sogar eine Domain und auch eine Business E-Mail fürs erste Jahr kostenlos dazu. Das ist natürlich praktisch, weil du willst natürlich, dass deine App nicht einfach irgendeinen komischen Namen hat wie App.hosting hostinger.de oder so, sondern deine Domain von deiner Firma z.B. Und falls du über deine App auch E-Mails versenden willst, kannst du das dann auch direkt machen. Und das Ganze kriegst du ab 4 € im Monat. Das ist absolut gar nichts für eine App, die dann sicher im Internet läuft.

**5:34** · Das heißt, im Prinzip zahlen wir nur 18 € im Monat für die Entwicklung und wenn wir die Entwicklung fertig haben, könnten wir das auch pausieren und ca. 4 € im Monat für das Hosting. Das heißt, wie du schon merkst, ist es mittlerweile extrem günstig geworden, eigenes Software zu erstellen. Früher musstest du hierfür eigene Softwareentwickler beauftragen.

**5:52** · So viiel zum Text. Ich würde sagen, wir fangen jetzt an und starten erstmal mit Cloud Code. Falls du die Cloud Desktop App noch nicht hast, kannst du über den Link in der Videobeschreibung hier einfach zu dieser Seite kommen und dort kannst du dann für dein Betriebssystem jeweils die Version auswählen. Das startet dann Download und dann kannst du die App installieren. In der Desktop App hast du im Prinzip drei Programme, nämlich ganz normal den Cloud Chat, Cloud Cowork und eben auch Cloud Code.

### Claude Code starten und Planmodus

**6:15** · Das heißt, wir wollen jetzt hier Cloud Code auswählen und wechseln damit hier in dieser Ansicht. Bei Cloud Code arbeiten wir immer in einem bestimmten Ordner auf deinem Rechner. Das heißt, erstelle dir am besten für deine App, die du bauen willst, einen Ordner und wähle den dann hier unten unter Ordner öffnen aus. Ich habe jetzt einfach auf meinem Desktop ein Ordner erstellt und den Habit Tracker genannt. Cloud kann jetzt in diesem Ordner Dateien erstellen, Befehle ausführen, Dateien verändern und so weiter. Und bevor wir jetzt hier irgendwas über unsere App sagen, gehen wir erstmal hier unten in den Planmodus.

**6:43** · Dort wollen wir jetzt die App erstmal gemeinsam mit Claud planen und mit ihm erstmal diskutieren, damit er auch wirklich versteht, was wir bauen wollen. In diesem Modus kann Claud nur Dateien lesen, im Internet recherchieren und eben nachdenken. Und was ich dir auch noch dringendst empfehlen würde, ist Cloud Code wie einen erfahrenen Senior Developer oder eben Sparingspartner zu behandeln. Das heißt, wir lassen ihn Rückfragen stellen, Alternativen vorschlagen und eben ehrlich sein, wenn er bei unseren Ideen Bedenken hat.

**7:10** · Das macht einen massiven Unterschied im Endergebnis, weil Claud in seinen Trainingsdaten natürlich auf Unmengen an Code trainiert wurde und versteht, wie Apps gebaut werden sollen.

**7:21** · Das heißt, wir können dann mit ihm diskutieren und ihn wirklich fragen, ob das, was wir tun wollen, noch richtig ist. Das heißt, nicht nur irgendwelche Befehle geben, sondern offen mit ihm diskutieren und auch Fragen stellen. Und ich zeige dir das jetzt auch anhand eines konkreten Prompts. Übrigens kannst du hier unten jederzeit mit der Diktierfunktion deine Prompts einfach reinsprechen. Das würde ich dir auch empfehlen, weil du dadurch deutlich besser kommunizieren kannst, was du haben möchtest, als alles immer reinzutippen. Also, das geht auch deutlich schneller. Und ich werde ihm jetzt folgenden Prompt stellen und ich würde dir auch empfehlen, beim ersten Prompte wirklich ein bisschen Zeit zu nehmen und wirklich gut zu kommunizieren, was du haben möchtest.

**7:52** · Ich habe jetzt folgendes geschrieben.

**7:53** · Ich möchte gemeinsam mit dir eine Webapp bauen, einen Habit Tracker. User können sich einloggen, Gewohnheiten anlegen, sie täglich abhaken und ihre Streak sehen. Als Admin kann ich User Accounts mit Default Passwort anlegen. Neue User müssen beim ersten Login das Passwort ändern. Und hier kommt jetzt der wichtige Prompt. Bitte sieh dich als mein Sparings und Diskussionspartner.

**8:12** · Stell mir Rückfragen, damit du genau verstehst, was ich meine. Frag mich zu Funktionsumfang, Design und allem, was du brauchst, um eine saubere App zu bauen. Wenn ich bei einer Frage unsicher bin, gib mir gerne deine Empfehlung mit kurzer Begründung. Du darfst auch ehrlich sein und mir widersprechen, wenn du Bedenken zu meiner Antwort hast. Das heiß, er soll mich wirklich interviewen und verstehen, was ich haben möchte.

**8:32** · Damit holst du deutlich mehr raus als deiner App und sparst dir sehr viel hin und her, als wenn du jetzt einfach reinschreiben würdest, ja, bau mir bitte eine Webapp und zwar einen Habitracker.

**8:40** · Punkt. Und hier unten gehen wir jetzt noch mal wichtige Text Anforderungen.

**8:43** · Die App soll später bei Hostinger gehostet werden über Noe GS Webhosting.

**8:47** · Hier habe ich jetzt einen kleinen Hinweis hinzugefügt, welches Framework er nutzen soll. Das würde ich dir auch immer empfehlen. NextJS ist eigentlich so das beliebteste Framework, um Webapplikationen zu bauen. Als Datenbank möchte ich Superbase nutzen mit Serverstand Frankfurt, weil du als Cloud einen direkten Connector dorthin hast und damit die gesamte Instanz steuern kannst. So ungefähr sollte dein erster Prompt aussehen. Stelle Cloud Code wie gesagt hier in den Planmodus und jetzt können wir das Ganze abschicken. Und jetzt fängt Cloud erstmal an jede Menge Fragen zu stellen. Wie häufig und flexibel sollen Gewohnheiten getrackt werden? Wir machen es jetzt erstmal nur täglich für die erste Version.

**9:17** · Das empfehlt er hier auch. Wie streng soll die Streak sein? Also ne, wenn man jetzt einmal vergisst, die Gewohnheit zu machen, soll das dann direkt zurückgesetzt werden auf null oder eben nicht. Ich würde sagen, man darf einen Tag auch mal verpassen. Was soll der Admin können, außer User anzulegen?

**9:32** · Eigentlich soll er nur User anlegen können. Die Gewohnheiten der anderen Nutzer sollen privat bleiben. Welche Sprache soll die UI haben? Machen wir mal auf Deutsch. Das wird jetzt auch ein bisschen dauern mit den Fragen, deswegen werde ich jetzt hier nach vorne spulen, damit ich dich damit nicht langweile.

**9:44** · Aber ich kann dir jetzt schon versichern, dass wir mit dieser Methode eine deutlich bessere erste Version unserer App erstellen können, die von den Funktionen wirklich durchdacht ist, wenige Fehler hat und auch wirklich gut aussieht. So, das hat jetzt gute 10 bis 15 Minuten gedauert, was aber total normal ist, weil Claud mich wirklich viele Sachen gefragt hat. Ich glaube insgesamt 16 Fragen. Das heißt, li den Plan dann noch immer ungefähr durch.

**10:04** · Falls du irgendwie merkst, da sind Funktionen nicht enthalten, die du gerne haben möchtest oder irgendwelche anderen Sachen wurden vielleicht falsch aufgefasst, dann kannst du den Plan hier links überarbeiten und dann einfach weiter mit claud chatten. Mir ist z.B.

**10:15** · jetzt hier aufgefallen, dass er die App sofort bei Hostinger deployen möchte, was er aber so noch nicht direkt kann.

**10:20** · Deswegen möchte ich ihm das so auch kommunizieren. Ich gehe auf überarbeiten. Die App soll erstmal lokal laufen und Superbase als Datenbank nutzen. Das Hosting Deployment machen wir später. Und zusätzlich sage ich ihm auch noch, dass er für die Nutzerauthentifizierung ebenfalls Superbase nutzen soll und er soll mich schon mal als Admin anlegen.

**10:36** · Und dann können wir jetzt hier das Ganze auch wieder überarbeiten. Und Cloud fängt jetzt nicht an irgendwas zu programmieren, sondern er ändert jetzt einfach den Plan und er fragt mich jetzt hier auch z.B., soll er das Superbase Projekt selbst schon anlegen oder habe ich eins angelegt? Wir haben jetzt noch nichts in Superbase gemacht. Er soll das Projekt selber anlegen, in Frankfurt gehostet und auch das ganze Datenbankschema konfigurieren und mich als Adminuser anlegen und so weiter. Wir wollen da nicht selber machen. Und während Cloud jetzt den Plan anpasst, würde ich sagen, verbinden wir doch mal Superbase. Dafür musst du dir erstmal natürlich ein Account bei Superbase erstellen.

### Supabase verbinden und Datenbank live anlegen

**11:05** · Wie gesagt, ist kostenfrei und dann kannst du hier oben rechts ins Dashboard gehen. Hier kannst du dann eine neue Organisation anlegen und in dieser Organisation siehst du dann hier deine Projekte und mehr müssen wir nicht machen. Cloud wird hier nämlich eigenständig das Projekt für uns anlegen. Was wir jetzt aber noch machen müssen, ist Superbase zu verbinden und dafür gehen wir hier oben links auf Customize und dann hier auf Konnektoren.

**11:25** · Hier kannst du dann verschiedenste Konnektoren zu anderen Apps hinzufügen, unter anderem auch Superbase. Und hier sehe ich jetzt Superbase und kann mich hier oben verbinden. Dann öffnet sich hier der Browser und hier musst du dich dann einmal mit deinem Superbase Account einloggen. Und dann sehen wir hier auch, das ist eine MCP Connection. Also wir nutzen hier das Model Context Protocol.

**11:41** · Das ist ein einheitlicher Standard, damit KI-Agenten mit verschiedensten Tools arbeiten können. Und wir können jetzt hier wieder zurück zu unserer Session gehen. Und wenn wir jetzt zufrieden sind mit dem Plan, können wir hier sagen akzeptieren und Automodus, denn in diesem Modus fragt uns Cloud nicht immer wieder, ob er einen Befehl ausführen darf, sondern führt diesen einfach aus. Bei gefährlicheren Operationen wie z.B. löschen, fragt er aber trotzdem vorab. Wir sehen jetzt, dass er sich verschiedene Tasks anlegt und parallel auch das Superbase Setup überprüft. Er sieht z.B. meine Organisation und dass wir auch im Freet hier sind und erstellt jetzt auch schon das Projekt.

**12:11** · Wenn ich jetzt zurück zu Superbase gehe und hier einmal refreshe, dann sehe ich hier auch unsere App Habit Tracker gehostet in EU Central. Das ist nämlich hier genau in Frankfurt und er wird jetzt die komplette Datenbank einrichten und wir müssen hier nichts machen. Er weiß ganz genau, was für Tabellen er in der Datenbank anlegen muss, damit so eine App hier auch funktioniert. Und das wird jetzt hier auch wieder eine Weile dauern. Deswegen spule ich jetzt wieder nach vorne. Cloud hat die Entwicklung in Phasen aufgeteilt und hat die erste Phase jetzt auch schon durch, nämlich den Login Part. Und wir können h in der Desktop App sehen.

**12:37** · Ich kann mich jetzt hier mit der E-Mail und dem Passwort anmelden und auch direkt ein neues Passwort setzen. Wenn ich jetzt \[räuspern\] hier in Superbase zu Authentication gehe, dann sehe ich hier, dass ich schon als Nutzer angelegt wurde und falls wir dann später neue Nutzer anlegen, werden die hier auch hinzugefügt. Das heiß Superbase nutzen wir eigentlich für zwei Sachen, nämlich einmal für die Authentifizierung der Nutzer und für das Speichern von Daten, ne? Also in unserem Fall unsere Gewohnheiten und unser Tracking. Wenn ich hier links auf Database gehe, sehe ich auch übrigens schon das Datenbankschema, das sich Cloud überlegt hat und auch direkt hier in Superbase bereits eingetragen hat.

**13:09** · Hier unter dem Table Editor kann man genau sehen, welche Tabellen er erstellt hat. Z.B.

**13:14** · eine Tabelle für die Gewohnheiten und dann eben pro User, welche Gewohnheiten existieren und eben noch andere Tabellen, die für die App benötigt werden. Das heißt, die gesamte Datenbank wird von Cloudcode verwaltet und bis jetzt finde ich sieht das super aus. Ich kann ihm jetzt hier sagen, er soll einfach weitermachen. Er wird jetzt in die nächste Phase springen und die anderen Funktionen einbauen. So, er hat jetzt alle Phasen abgearbeitet und die App ist jetzt fertig. Ich werde jetzt hier malim Browser öffnen, damit wir uns die noch genauer anschauen können. Wenn ich mich hier jetzt einlogge, sehe ich jetzt hier mein Dashboard. Er hat jetzt hier beispielhaft schon eine Gewohnheit eingetragen, nämlich 15 Minuten am Tag lesen.

### Fertige App testen

**13:44** · Das habe ich gestern und heute gemacht. Hier oben sehe ich die Habits, ne? Also, wir haben jetzt hier eine Habit. Ich kann jetzt hier auch eine neue anlegen. Was willst du dir angewöhnen? Schreiben wir mal joggen.

**13:54** · Ich finde das auch richtig cool mit den Icons hier. Das hat er direkt schon richtig gut eingefügt. Beschreibung: 5 km pro Tag joggen. Dann können wir das Ganze anlegen und sehen dann auch die zweite Habit hier unten. Ich kann ja jetzt immer 7 Tage rückwirkend eintragen, ob ich was gemacht habe. Also z.B. kann ich jetzt sagen hier, ich war jetzt die letzten drei Tage joggen. Wir sehen die Streak ist ja auch auf drei gesetzt. Wenn ich jetzt die Habit anklicke, sehe ich auch noch mal den gesamten Kalender, wann ich die Gewohnheit hier ausgeführt habe. Wenn ich was nicht mehr mache, kann ich es hier oben archivieren und natürlich kann ich das Ganze ja auch jederzeit noch mal bearbeiten.

**14:23** · Wenn ich jetzt neue Nutzer anlegen möchte, kann ich hier oben in den Adminbereich gehen. Hier sehe ich mich jetzt als Admin und hier oben kann ich jetzt ein User anlegen. Das heißt, ich gebe hier einfach eine E-Mail ein und ein Default Passwort. Ich kann hier sogar so einen Vorschlag generieren. Das finde ich ziemlich cool. Ich lege jetzt mal ein Beispielen an, also hier max@gmail.com anlegen. Max wurde jetzt hier angelegt und ich kann jetzt hier die Loginaten kopieren und z.B. ihm das per WhatsApp oder Mail oder wie auch immer schicken. Beim ersten Login muss er dann sowieso das Passwort wechseln.

**14:50** · Hier steht auch, dass Passwort Change noch ausstehend ist und die Admin Aktivitäten werden auch dokumentiert.

**14:55** · Wenn ich hier unter Superbase unter Authentication reinschaue, sehe ich auch, dass ein neuer Nutzer angelegt wurde. Und wenn ich meinen Table Editor gehe und dann hier unter Habits schaue, sehe ich hier auch meine Habits, nämlich joggen und lesen. Und das hier ist meine User ID. Diese User ID ist praktisch verbunden mit meinem Nutzer hier unter Authentication. Das heißt, hier werden dann die ganzen Daten gespeichert. Hier unter Profiles sehe ich dann auch die Profile und wer jetzt Admin ist und wer nicht. Das heißt, Cloud hat das perfekt gemacht, hat hier alles angelegt und die App beim ersten Mal schon direkt so gut hinbekommen.

**15:25** · Und das liegt eben vor allem daran, dass wir ihn ganz am Anfang einen guten Prompt gegeben haben, ihn als Diskussionspartner gesehen haben, statt einfach eine Maschine, die Befehle ausführt und er eben sehr viele Rückfragen gestellt hat, damit er das genauso gut beim ersten Mal hinbekommt.

**15:39** · Ich bin total zufrieden damit. Ich muss jetzt auch gar nicht zurück in den Chat gehen und sagen, nee, mach das noch mal anders oder füg das noch mal ein, weil er hat's genauso, wie ich es mir vorgestellt habe, jetzt umgesetzt. Das heißt, wenn ich dir hier eine Sache mitgeben müsste bei der Arbeit mit Cloud Code ist lass dir Zeit beim Planmodus und stelle sicher, dass Cloud wirklich versteht, was du haben möchtest. Also lass dich interviewen und nutzt ihn wirklich wie einen Partner. Damit wirst du dir enorm viel Zeit und auch Tokens sparen. Denn je mehr hin und her du hier mit Cloudcode hast, desto schneller verbrauchst du auch deinen Nutzungskontingent. Das hat doch schon wunderbar geklappt. So schnell geht's.

### Code auf GitHub bringen

**16:09** · Ich bin total zufrieden mit der ersten Version und möchte das Ganze jetzt auf einen Server deployen, denn aktuell läuft diese App nur lokal auf unserem Rechner. Das siehst du daran, dass hier oben Local Host steht. Das heißt, die App ist noch nicht im Internet erreichbar. Und bevor wir jetzt die App auf einem Server deployen, müssen wir unseren Code erstmal bei GitHub hochladen. Gitub ist im Prinzip ein Cloudspeicher für Code. Das heißt, stell dir einfach Google Drive vor, aber eben für Code. Dort legst du dein Projekt rein und jedes Mal, wenn du eine Änderung machst, landet diese Änderung auch in der Cloud. Das hat zwei Vorteile. Erstens hast du einen Backup deines Codes.

**16:40** · Das heißt, selbst wenn dein Laptop kaputt geht, ist die App nicht verloren und es wird auch automatisch mit Hilfe von Git ein Versionierungssystem eingebaut, was einfach nur bedeutet, dass du zu verschiedenen Stellen in deinem Code zurückspringen kannst, sage ich mal.

**16:53** · Angenommen du hast irgendeine Funktion gebaut und hast deine App irgendwie zerschossen, dann kannst du einfach zurück zum vorherigen Stand springen.

**17:00** · Und falls du jetzt auch von anderen Geräten aus mit deiner App arbeiten willst, dann kannst du den Code von GitHub herunterladen und dann z.B. z.B.

**17:07** · von deinem Computer weiterarbeiten oder deinem Laptop oder wie auch immer. Und fast alle Server bieten eben auch eine GitHub Schnittstelle an. Das heißt, der Server holt sich den Code nicht von deinem Rechner, sondern von GitHub. Das heißt, es läuft genau folgendermaßen ab.

**17:21** · Wir entwickeln hier auf unserem Computer mit Cloud Code die App weiter. Das heißt, wir legen jetzt z.B. neue Funktionen an und so weiter, dann sind diese Änderungen ja auch erstmal nur lokal auf unserem Rechner und wir müssen das Ganze ja dann auch irgendwie auf einem Server kriegen, damit unsere App, die dann im Internet läuft, ebenfalls die neuen Funktionen abbekommt, die wir jetzt hier programmiert haben. Und das funktioniert dann so, dass der Code erstmal auf GitHub gepusht wird. Keine Sorge, das macht alles Cloud Code und GitHub sagt unserem Server dann Bescheid: "Hey, es gibt eine neue Version von unserem Code. Bitte nimm die neue Version und deploy sie hier."

**17:50** · Falls das zu kompliziert klingt, keine Sorge, Cloud Code wird all das für uns übernehmen, genauso wie es auch mit Superbase gemacht wurde. Merkt ihr einfach nur, Gitter bist dazu da, um einen Backup von deinem Code zu machen und um das Ganze dann auf einem Server zu deployen. Und Gitub ist ebenfalls kostenfrei. Das heißt, geh einfach auf gitub.com und erstell einen Account.

**18:09** · Wenn du dir dann einen Account erstellt hast, müssen wir genau wieder so wie mit Superbase hier GitHub erstmal verbinden, damit Cloud Code darauf zugreifen kann.

**18:17** · Das machen wir wieder, indem wir hier unter Customize gehen und diesmal nicht unter Konnektoren, sondern hier unter Plugins. Das heißt, wir gehen hier auf Plugins durchsuchen und schreiben hier oben GitHub rein. Wir klicken hier aufs Plus. Damit wird GitHub installiert und ist auch einsatzbereit. Und dann sehen wir hier links auch das Gitup Plugin und können dann hier auf die Konnektoren zugreifen. Hier können wir uns dann mit dem Gitup Account verbinden. Das heißt, hier logst du dich dann ein. Wenn du das dann gemacht hast, siehst du hier unter den Konnektoren auch die Gitub Integration und damit hat Cloud Code jetzt Zugriff auf deinen Gitub Account.

**18:45** · Jetzt können wir zurück zu Cloud Code gehen und ihm sagen, er soll ein Gitupp Projekt anlegen und unseren Code pushen.

**18:52** · Pushen heißt einfach hochladen auf Gitub. Kurzer Hinweis auch noch an der Stelle, damit das Ganze mit der Versionierung deines Codes auch wirklich klappt, musst du auch noch zusätzlich Git installieren. Das ist das eigentliche Versionierungssystem, damit wenn du lokal mit deinem Code arbeitest bzw. Cloud damit arbeitet, man Snapshots von dem Code machen kann, um dann eben zurückzuspringen, falls man mal einen Fehler macht oder irgendwie ein Backup haben möchte. Und falls du es noch nicht hast, wird bei Cloud Code sowieso auch angezeigt, dass es benötigt wird.

**19:17** · Und du kannst dann entweder sagen, Cloud soll das direkt installieren oder falls das nicht funktioniert, kannst du auch einfach auf die offizielle Website von Git gehen und hier einfach für dein Betriebssystem Git herunterladen. Wenn du Git dann installiert hast, kannst du hier zu Cloud Code gehen und ihm folgendes sagen: "Ich habe dir Zugang zu meinem Gitub Account gegeben, erstelle ein neues Repository für meine App und pushe den Code auf GitHub." Repository heißt dabei einfach nur einen neuen Ordner bzw. ist ein neues Projekt. Das heißt, Cloud wird jetzt ein Projekt anlegen bei GitHub, wird unseren Code dahin pushen und damit ist er dann in der Cloud abgespeichert.

**19:48** · Er fragt mich jetzt auch, ob ich das Repository öffentlich oder privat haben möchte. Das hätte ich vorher auch schreiben können.

**19:54** · Also gut, dass er das noch mal gefragt hat. Das soll natürlich privat sein, das heißt nur du siehst deinen Code und als Name lasse ich auch einfach Habit Tracker. Er hat den Code jetzt auch auf GitHub gepusht und hier sehen wir jetzt den Link zum Repository und hier sehen wir jetzt unseren gesamten Code und sogar eine Read Me Datei, wo genau drin steht, was unsere App macht, wie sie gebaut wurde, wie das Superbase Setup funktioniert und damit können wir jetzt auch auf anderen Geräten mit unserem Code hier arbeiten. Das heißt, ne, ich könnte jetzt z.B. meinen Laptop nehmen und dann Cloud Code starten und sagen: "Hey, hol dir bitte den Code von GitHub."

**20:24** · Und dann haben wir den Code auch auf einem anderen Gerät. Das heißt, auf GitHub pushen ist den Code hochladen und von GitHub pullen ist den Code herunterladen. Jetzt können wir unseren Code auch auf einem Server deployen und ich empfehle dir hier wie gesagt das Node js Webhosting. Ich hinterlasse dir auch den Link zu der Webseite in der Videobeschreibung. Hier sehen wir auch noch mal den Plan, ne? 4 € im Monat und wir kriegen all diese Sachen hier automatisch dazu. Ich klicke hier also auf Plan wählen. Du kannst jetzt den Zeitraum einstellen, wie lange du dieses Hosting haben möchtest. Du kannst auch z.B. sagen, du willst es erst nur 12 Monate haben.

### Auf Hostinger deployen

**20:53** · Kannst hier unten dann direkt auch schon eine Domain dazu holen und kriegst dann auch ein Postfach. Und mit dem Code Jujan Ivanov kannst du dir auch noch mal 10 % bei deinem Kauf sparen. Das heißt, wenn du das jetzt hier für 12 Monate holst, zahlst du nicht mal 60 € und das ist schon sehr billig dafür, dass du dann für ein Jahr fünf Webapps im Internet hosten kannst.

**21:10** · Nach der Zahlung wirst du dann sofort weitergeleitet und kannst hier deine Domain angeben. Und dann können wir hier die Webapp bereitstellen, indem wir über GitHub gehen. Hier musst du dich dann einmal mit deinem GitHub Account verknüpfen und dann siehst du hier auch deine App. Hier sehe ich jetzt den Habit Tracker. Klicke dann noch weiter. Hier kann ich dann einstellen, auf was für ein Framework das basiert. Der hat jetzt hier schon erkannt, dass das NextJ ist.

**21:29** · Das ist auch richtig. Und hier musst du jetzt eigentlich nichts weiter einstellen, außer dass du hier unten noch Umgebungsvariablen hinzufügst. Das sind wichtige geheime Variablen, damit unsere Webapp auch wirklich funktioniert. Das heißt, da ist dann sowas wie z.B. der Projekt Token von Superbase hinterlegt und andere geheime Tokens. Und solche Geheimenvariablen werden immer in einer ENFDatei abgespeichert und die hat Cloud Code natürlich auch für uns erstellt. Wir können hier oben rechts unter diesem Symbol hier zu den Dateien gehen und sehen hier dann alle Dateien, die Cloud erstellt hat.

**21:59** · Unter dieser ENFDatei hier sehen wir z.B. die zwei Superbase Variablen, die wichtig sind, damit unsere App hier mit Superbase verknüpft ist. Und diese Enddatei können wir jetzt bei Hostinger importieren. Ich klicke hier also auf importieren, gehe in meinen Projektordner und wähle hier diese ENFDatei aus. Damit werden die Werte hier sofort eingetragen und wenn ich hier unten jetzt auf bereitstellen klicke, sehe ich hier, dass die App von Gitup bereitgestellt wird.

**22:23** · Bereitstellung abgeschlossen. Ich kann jetzt hier über diese Domain meine App erreichen und mich hier direkt einloggen. Mal schauen, ob das Ganze funktioniert.

**22:30** · Und zack, bin ich jetzt auch drin. Ich bin jetzt hier wieder eingeloggt. Ich sehe meine Gewohnheiten, die wurden auch persistent gespeichert. Deswegen sehen wir jetzt hier dasselbe wie vorhin. Und unsere App ist jetzt öffentlich im Internet erreichbar über unsere eigene Domain. Falls bei dir jetzt hier ein Fehler auftreten sollte, was ja immer mal passieren kann, ist das kein Problem. Du kannst dann einfach nur den Fehler, der hier angezeigt wird, kopieren, den in Cloud Code eingeben und einfach sagen: "Hey, ich habe diesen Fehler, bitte hilf mir." Der wird das dann für dich regeln. Kann jetzt hier auch zum Dashboard gehen und kann jetzt hier verschiedenste Sachen von meiner App einsehen. Ich kann meine Domain verwalten, E-Mails einrichten.

**23:01** · Ich sehe hier die letzte Bereitstellung, kann auch sehen, dass die hier eben erfolgreich abgeschlossen wurde. Kann mir das auch noch mal genauer ansehen, was hier passiert ist. Es wird also alles dokumentiert. Ich kann mir die Leistung anschauen, Analyse und so weiter und so fort. Und das war's im Prinzip auch schon. Unsere App ist jetzt live im Internet.

### Updates live pushen

**23:18** · Wir können jetzt hier weiter mit Cloud Code an der App arbeiten und wenn ich dann eine neue Funktion implementiert habe und diese dann auch auf dem Server pushen möchte, damit sie ebenfalls in der App im Internet eingebaut ist, da muss ich Cloud Code einfach nur sagen: "Hey, push meinen Code of Gitub oder pushe meine Änderungen." Und damit wird die App dann auch aktualisiert. Ich habe jetzt z.B.

**23:38** · für eine neue Funktion eingefügt, dass wenn man alle Gewohnheiten an einem Tag erledigt hat, so eine kleine Konfetti Animation kommt. Und diese neue Funktion ist jetzt erstmal nur hier in der lokalen Version meiner App verfügbar. In der App, die live im Internet ist, ist die Funktion noch nicht da. Also schreibe ich jetzt Cloud Code einfach, pushe meinen Code auf GitHub oder lad meine Änderung hoch oder aktualisiere meine App oder wie auch immer. Und was Cloud Code im Hintergrund macht, ist er macht erstmal einen Snapshot von dem aktuellen Stand, lädt den neuen Code bei Gitub hoch. Gitub sagt dann dem Server: "Hey, es gibt einen neuen Code. Bitte nimm dir die neue Version."

**24:08** · Und der Server deploy Ganze. Dann hier steht jetzt auch gepusht und welche Dateien geändert wurden. Wenn ich jetzt meine App zurück zum Dashboard gehe, dann sehe ich hier gerade, dass eine neue Bereitstellung läuft und dann steht hier auch Bereitstellung abgeschlossen. Wenn ich jetzt die App hier neu lade, dann sehe ich jetzt hier auch die neue Funktion aktualisiert in der App. Wenn du es bis hierhin geschafft hast, dann herzlichen Glückwunsch. Du hast jetzt eigentlich alles, was du brauchst, um deine eigenen Webapps zu bauen mit Hilfe von Cloud Code. Du weißt, wie du eine eigene Datenbank anbindest, wie du die App dann wirklich auf einem Server deployst und das Ganze dann im Internet verfügbar machst.

### Community

**24:40** · Und du hast sogar gelernt, wie Gitub funktioniert, damit du jetzt Backups von deinem Code machen kannst und diesen auch von überall nutzen kannst auf verschiedenen Geräten.

**24:48** · Das heißt, falls du jetzt schon eine App Idee hast und diese umsetzen willst, wünsche ich dir auf jeden Fall schon mal viel Spaß. Falls du dich noch tiefer mit dem Thema Cloud Code auseinandersetzen möchtest und wirklich einen Deep Dive machen möchtest, denn Cloud Code hat noch einiges mehr zu bieten, dann kannst du natürlich auch jederzeit in meiner Community vorbeischauen, Link dazu in der Videobeschreibung. Hier haben wir einen Cloud Code Kurs, indem wir noch mal deutlich tiefer ins Detail gehen.

**25:08** · Das heißt, wenn du Cloud Code wirklich meistern möchtest und das Ganze im Business Kontext einsetzen willst, kann ich dir den Kurs sehr empfehlen. Wir haben hier auch neben dem Cloud Code Kurs zahlreiche Kurse zu N8N und OpenCla und wie man sein KI Business aufbaut, wie man mit der DSGO und dem AI Act umgeht. und natürlich wie man verschiedenste Programme auf seinem eigenen Server hosten kann. Und natürlich kannst du dich hier jederzeit mit mir und anderen Unternehmern austauschen. Wir haben ja auch zweimal in der Woche einen Live Call, wo man einfach mal ins Gespräch kommt, über verschiedenste Themen spricht, Probleme löst und so weiter. Das heißt, hier kann man auch immer eine Menge lernen.

**25:36** · Das heißt, falls du das Thema noch mal tiefer angehen möchtest, bist du natürlich herzlich willkommen. Link dazu in der Videobeschreibung. Ansonsten würde ich sagen, vielen Dank fürs Zuschauen. Ich wünsche dir ganz viel Spaß bei der Appentwicklung und würde sagen, wir sehen uns im nächsten Video wieder. Bis dann. M.