---
title: "Die 10 besten Claude Code Skills & Plugins"
source: "https://www.youtube.com/watch?v=Vx6QlEhyybQ"
author:
  - "[[Julian Ivanov | KI-Automatisierung]]"
published: 2026-03-19
created: 2026-06-20
description: "🚀 Die schnellste Abkürzung um KI-Automatisierung zu meistern: https://skool.com/ki-automatisierungClaude Code ist out of the box schon stark, aber mit den richtigen Skills und Plugins wird es richt"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Vx6QlEhyybQ)

🚀 Die schnellste Abkürzung um KI-Automatisierung zu meistern: https://skool.com/ki-automatisierung  
  
Claude Code ist out of the box schon stark, aber mit den richtigen Skills und Plugins wird es richtig mächtig. In diesem Video zeige ich dir meine persönlichen Top 10 Plugins und Skills für Claude Code. Für jedes Tool erfährst du, warum es nützlich ist, wie du es installierst, wie es funktioniert und bekommst einen konkreten Use Case. Damit kannst du Claude Code auf ein ganz neues Level bringen.  
  
🔗 Alle erwähnten Skills & Plugins  
  
1️⃣ Excalidraw Diagram Skill (Cole Medin): https://github.com/coleam00/excalidraw-diagram-skill  
Excalidraw (kostenlos): https://excalidraw.com  
  
2️⃣ NotebookLM-py: https://github.com/teng-lin/notebooklm-py  
  
3️⃣ Remotion Best Practices Skill: https://skills.sh/remotion-dev/skills/remotion-best-practices  
Remotion Docs: https://www.remotion.dev/docs/ai/skills  
  
4️⃣ Context7 CLI: https://github.com/upstash/context7  
Context7 Dashboard: https://context7.com  
  
5️⃣ Firecrawl CLI + Skill: https://github.com/firecrawl/cli  
Firecrawl: https://firecrawl.dev  
  
6️⃣ Playwright CLI (Microsoft): https://github.com/microsoft/playwright-cli  
  
7️⃣ Obsidian Skills: https://github.com/kepano/obsidian-skills  
Obsidian herunterladen: https://obsidian.md  
  
8️⃣ Feature Dev Plugin (Anthropic): https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev  
  
9️⃣ Superpowers Plugin: https://github.com/obra/superpowers  
  
🔟 CLAUDE.md Management Plugin (Anthropic): https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management  
  
🔗 Weitere Links  
📌 n8n bei Hostinger installieren: https://www.hostg.xyz/julian (JULIANIVANOV für 10 % Rabatt)  
📌 OpenClaw bei Hostinger installieren: https://www.hostg.xyz/SHIpe (JULIANIVANOV für 10 % Rabatt)  
📌 n8n-Cloud: https://n8n.partnerlinks.io/fx8c63u1ztn3  
  
📬 Business Anfragen: ivanov@crystalflow.ai  
  
🕐 Zeitstempel  
00:00 Einleitung  
02:00 Grundprinzip: Skills vs. Plugins  
03:53 #1 Excalidraw Diagram Skill  
07:53 #2 NotebookLM-py  
13:24 #3 Remotion Skill  
18:04 #4 Context7 CLI  
20:51 #5 Firecrawl CLI + Skill  
24:23 #6 Playwright CLI  
27:42 #7 Obsidian Skills  
33:05 #8 Feature Dev Plugin  
36:01 #9 Superpowers Plugin  
40:23 #10 CLAUDE.md Management Plugin  
42:06 Outro  
  
🔍 Tags  
#claudecode #skills #claudeai #ki #deutsch #german #tutorial #claude #plugins #notebooklm #remotion #context7 #firecrawl #playwright #obsidian #featuredev #superpowers #claudemd #aiagents #agenticworkflows #coding #automation #kiautomatisierung #plugins #developer #programming #anthropic #top10

## Transcript

### Introduction

**0:00** · Wenn du Cloudcode nutzt, dann weiß du bereits, dass es out of the Box schon ein ziemlich gutes System ist. Was viele aber nicht wissen ist, dass Cloudcode besonders stark wird, wenn du ihm Zugang gibst zu guten Skills und Plugins, denn dadurch versteht Cloud, wie er bei bestimmten Aufgaben vorgehen soll, welche Tools er benutzen kann und worauf er bei deinem Projekt achten muss. Was agentische Systeme wie Cloudcode nämlich so stark macht, ist genau das.

**0:22** · Du gibst dem Agenten nicht nur einen Prompt und sagst einfach, ja hier mach mal, sondern du gibst ihm Zugang zu Informationen in Form von Textdateien, die er je nach Situation automatisch dazu lädt. Also quasi Anleitungen, die Cloudcode sich selbst rauszieht, wenn er merkt, dass er sie gerade braucht. Jetzt ist das Problem aber, mittlerweile kommen ständig neue Skills raus, neue MCP-Server, neue CLI-Tools, neue Plugins, gefühlt jeden Tag was Neues und es ist echt schwierig geworden zu filtern, was jetzt wirklich nützlich ist und was einfach nur Hype ist.

**0:51** · Und genau deswegen habe ich jetzt meine persönlichen Top 10 Plugins und Skills für dich zusammengestellt. Das sind alles Sachen, bei denen ich überzeugt bin, dass sie einen echten Mehrwert liefern. Und für jedes Tool zeige ich dir jetzt vier Dinge: warum es nützlich ist, wie du es installierst, wie es funktioniert und auch einen konkreten Use-Case, denn damit kannst du vielleicht Inspiration für deine eigenen Projekte bekommen. Und wenn du am Ende des Videos auch nur eines dieser nützlichen Tools für dich mitnimmst, dann hat sich das Video schon für dich gelohnt.

**1:16** · Diese zwei Animationen, die du gerade gesehen hast, sind übrigens auch von Cloudcode erstellt mit Hilfe eines Skills und das ist schon ziemlich beeindruckend. Ich habe das nicht selber gemacht und wir werden uns das gemeinsam anschauen. Kurzer Disclaimer an der Stelle, wir werden heute folgende drei Skills bzw. Plugins nicht betrachten, weil ich die schon in vorherigen Videos sehr oft angesprochen habe und erklärt habe. Das heißt, falls du die noch nicht kennst, schau gerne auch in meine vorherigen Videos rein.

**1:39** · Das sind eigentlich drei der Top Skills, die man so verwenden kann, nämlich um Clouds zu ermöglichen, gute Skills zu schreiben, Skills zu finden und Designs für deine Apps oder deine Websites zu erstellen, die eben nicht so KI-generiert aussehen.

**1:53** · Das machen die beiden Skills hier in Kombination. Wir schauen uns heute zehn andere Skills an, die neben diesen drei Skills auch sehr nützlich sind. Bevor wir mit dem ersten Skill bzw. Plugin starten, ganz kurz das Grundprinzip, damit wir alle auf dem gleichen Stand sind. Ein Skill ist einfach nur eine Textdatei, nämlich eine Markdown-Datei, in der Anweisungen hinterlegt sind. Das ist also praktisch wie ein fest hinterlegter Prompt. Und dieser Skill gibt Claude dann den nötigen Kontext für die jeweilige Aufgabe.

### Basic principle: Skills vs. Plugins

**2:17** · Ich z.B. nutze Claude Code auch sehr gerne, um mir meine Videoskripte für YouTube zu erstellen. ich habe jetzt z.B. einen Skill YouTube-Skript und immer wenn ich jetzt sage, "Hey Claude, schreib mir ein Videoskript", dann versteht Claude, "Aha, Videoskript, ich habe dafür ja einen Skill. Okay, ich lese den mal aus und schaue mir an, wie man so Videoskripte schreibt oder wie ich die gerne haben möchte." Das heißt, in dem Skill steht dann hier unten die Art und Weise, wie ich meine Hook am Anfang des Videos strukturiere, was meine Tonalität ist, worauf ich eingehe und so weiter.

**2:47** · Und damit muss ich ihm auch nicht jedes Mal aufs Neue erklären, wie ich denn gerne Videoskripte haben möchte. Das bedeutet, wir können Claude zusätzlichen Kontext hinterlegen als Dateien und er holt sich diesen Kontext dann in der jeweiligen Situation. Und das ist sehr, sehr stark. So, was ist jetzt der Unterschied zwischen einem Skill und einem Plugin? Ein Skill kann noch mit zusätzlichen Referenzdateien oder auch Python-Skripte oder auch sogar MCP-Server kombiniert werden.

**3:08** · Denn an sich ist ein Skill, wie gesagt, nur eine Textdatei, aber es kann ja sein, dass Claude, wenn er diesen Skill hier ausliest, auch gleichzeitig dann ein ganz bestimmtes Skript nutzen soll, das ich ihm dann auch hinterlegt habe, oder auch ganz bestimmte Referenzdateien, also z.B. irgendwelche PDF-Dokumente, die er sich erstmal durchlesen soll und dann mit dem Skill die Aufgabe machen soll. Das heißt, ein Skill mit zusätzlichen Komponenten ist ein Plugin.

**3:34** · Und wenn wir so ein Plugin installieren, dann werden neben der Skill-Datei auch eben diese ganzen anderen Referenzdateien oder auch sogar MCP-Server installiert. Und das war's auch schon, das ist der einzige Unterschied. Das heißt, nicht wundern, wenn ich manchmal Skill sage oder manchmal Plugin, ich meine wahrscheinlich dasselbe, nur dass halt bei einem Plugin noch zusätzliche Komponenten dabei sind. Und jetzt fangen wir auch schon mit dem ersten Skill an, nämlich dem Excalidraw Skill. Und das, was du hier gerade siehst, das habe ich nicht selbst hier dargestellt, sondern das hat Claude Code für mich gemacht mit diesem Excalidraw Skill.

### 1 Excalidraw Diagram Skill

**4:00** · Excalidraw ist einfach nur ein Whiteboard, das kannst du kostenfrei nutzen im Internet und das eignet sich super, um Prozesse abzubilden. Wenn ich z.B. einen N8N Workflow bauen möchte, dann notiere ich mir erstmal die einzelnen Schritte und den gesamten Prozess hier in Excalidraw.

**4:15** · Oder wenn ich jetzt hier dir etwas erklären möchte, dann eignet sich sowas natürlich super gut. Und früher musste ich das ganz manuell machen und diese ganzen Boxen hier eintragen und die Texte einfügen und so weiter und das hat natürlich viel Zeit gedauert. Aber jetzt kann ich Claude Code einfach sagen, er soll die Abbildung für mich erstellen und ich gebe dir dann einfach einen Text z.B. für das ich eine Abbildung haben möchte und schon generiert mir das Claude Code hier. Ich kann das dann kopieren und bei mir in Excalidraw eintragen. Er hat das aber hier auch direkt als PNG schon erstellt. Und dieser Skill ist einfach in einem GitHub Repository hinterlegt von Code Medien.

**4:45** · Code Medien ist übrigens ein sehr, sehr guter KI YouTuber auch im Bereich Agenten und agentisches Coden und Rex Systeme und so weiter, auch N8N. Das heißt, wenn du wirklich praktische AI Guides haben möchtest, dann schau auch unbedingt bei ihm vorbei. Und weil er für seine Erklärvideos natürlich auch immer wieder was zeigen muss, hat er sich so einen Excalidraw Diagram Skill erstellt.

**5:02** · Und für uns ist es mega leicht, solche Skills hier zu installieren, nämlich kopierst du einfach hier oben den Link zu dem GitHub Repository, fügst ihn hier in Claude ein und ich habe mir jetzt hier in meiner Claude MD Datei, die ja immer in den Kontext hier geladen wird von Claude, folgende Regel hinterlegt: Alle Skills und MCP Server werden immer auf Projektebene installiert. Das ist für mich jetzt wichtig, denn ich möchte nicht, dass Claude hier irgendwas global installiert auf User-Ebene, das dann in jedem Projekt ist, woran ich dann mit Claude arbeite, sondern alles, was er jetzt hier installiert, installiert er nur hier in diesem Ordner.

**5:31** · Du kannst diese Regel auch in deiner globalen Claude MD Datei speichern, dann macht er das immer. So, ich schicke das jetzt hier ab und habe ihn hier auch in den Bypass Permission Modus gesetzt, damit er jetzt einfach nur das Repository hier bzw. einfach nur den Skill hier installiert. Und jetzt schreibt er auch, der Excalidraw Diagram Skill ist vollständig installiert. Er hat alle Bibliotheken installiert und auch alle Dateien hier heruntergeladen. Und wenn ich jetzt hier in meinen Claude-Ordner gehe, sehe ich hier auch den Excalidraw Diagram Skill. Und in diesem Ordner sehe ich auch einen Ordner mit References.

**6:01** · Das heißt, wichtige Dateien, auch wieder einfach nur Textdateien, die Claude erklären, wie er z.B. bestimmte Farbpaletten erstellen soll, wie er bestimmte Elemente erstellen soll, wie er das richtige JSON-Schema erstellt und so weiter. Und hier auch z.B. ein Python-Script. Das heißt, genau genommen haben wir gerade hier ein Plugin installiert, weil wir hier eine Skill-MD-Datei haben, wo der Skill beschrieben wird, aber neben dem Skill auch noch ein paar andere Dateien vorhanden sind, die wichtig sind, damit Claude das ja alles richtig macht. So, was ist jetzt der eigentliche Clou an diesem Skill? Warum funktioniert er so gut?

**6:30** · Der Clou ist, dass Claude das Diagramm erstmal selber erstellt und dann eben auch als PNG erstellt, so wie wir es ja gerade hier gesehen haben. Und dann schaut sich Claude dieses Bild an, überlegt, okay, habe ich alles richtig erstellt? Wenn nicht, dann passe ich es noch mal an. Wenn sich z.B. Boxen überlappen oder irgendwelche Pfeile in die falsche Richtung gehen. Das heißt, er korrigiert sich selber, indem er sich das hier erstmal anschaut, was er generiert hat. Und ich habe mit diesem Skill schon sehr gute Erfahrungen gemacht. Und oftmals ist es nicht beim ersten Mal perfekt.

**6:57** · In dem Fall war es tatsächlich beim ersten Mal perfekt, aber manchmal hat er vielleicht noch nicht ganz das Design so schön, wie ich es haben möchte. Dann muss ich aber nur noch ein, zwei Prompts vielleicht hin und her schreiben und dann hat er das eigentlich perfekt abgebildet. Also, es ist meistens nur noch mal kurz Feedback geben und dann hast du eigentlich das Diagramm, das du haben willst. Bei so einfachen Abbildungen wie hier macht er das sofort. Also, das ist gar kein Thema. Und was ich dann mache, ne, er stellt dann hier einfach diese JSON-Datei und ich kopiere mir das Ganze so und gehe dann in mein Excalidraw und füge das einfach ein.

**7:27** · Und hier kann ich natürlich noch alles anpassen, ne, also das ist jetzt kein Foto. Ich kann alles jetzt hier noch bearbeiten, so wie ich es möchte. Das heißt, wenn du gerne mit Excalidraw arbeitest oder auch jetzt arbeiten möchtest, nutze unbedingt diesen Skill. Lass dir von Claude die ganzen Diagramme und Abbildungen hier generieren. Das ist extrem nützlich für Dokumentationen, Architektur Reviews, ne, Prozessabbildungen oder wenn du in irgendeinem Meeting bist und irgendwas visualisieren willst oder auch für irgendein Video, wie auch immer. Kommen wir zu Nummer 2 und zwar ist das Notebook LM Pi.

### 2 NotebookLM-py

**7:54** · Das ist eine Python Library, die Cloud Code vollen programmatischen Zugriff auf Googles Notebook LM gibt. Das heißt, Cloud Code kann Notebook LM als Tool nutzen, um z.B. Recherchen durchzuführen, eine Wissensdatenbank abzufragen, Podcast zu erstellen, Slide Decks, Quizze, Infografiken, ohne dass wir zig andere externe Anbieter nutzen müssen und das Ganze auch noch kostenfrei, denn Notebook LM kostet nix.

**8:18** · Was auch noch so besonders an Notebook LM ist, wenn du ihm jetzt hier zig Quellen zur Verfügung stellst und er daraus hier jetzt irgendwas generiert, dann sind diese Texte, die er generiert, immer Quellen-basiert. Das heißt, du hast praktisch ein ausgelagertes RAG-System, eine Research Engine und auch hier so eine Content Generation Engine aus den ganzen Informationen, die hier zusammengestellt werden. was wir jetzt wieder machen müssen, um das hier zu installieren, ist einfach nur den Link zu diesem Repository zu kopieren und Folgendes zu schreiben: "Installiere diesen Skill für mich."

**8:47** · Ich packe ihn wieder in Bypass Permissions und schick das ab. Er wird jetzt hier auf das Repository gehen und hier unten dann beim Agent Setup sehen, wie er das hier installieren soll. Jetzt hat er das installiert. Wenn ich jetzt hier in den Cloud-Ordner schaue, sehe ich hier auch den Notebook LM Skill. Das ist jetzt einfach hier nur eine skill.md-Datei und er hat die Python-Bibliothek hier auch installiert. Jetzt sagt er noch, dass ich mich erstmal bei Notebook LM einloggen muss. Das heißt, ich muss das hier ins Terminal eingeben. Das heißt, wir gehen hier oben aufs Terminal und fügen einfach nur den Command hier ein.

**9:17** · Dann öffnet sich auch automatisch ein Browserfenster, wo ich mich mit meinem Google Account einloggen muss. Ich bin jetzt hier schon eingeloggt. Das heißt, bei dir, log dich einfach nur ganz normal ein und wenn du dich da eingeloggt hast und das dann bei dir genauso aussieht, musst du hier unten einfach nur auf Enter klicken und damit wird dann auch die Authentifizierung gespeichert und jetzt hat Cloud Code vollen Zugriff auf Notebook LM und ich gebe dir jetzt direkt auch ein cooles Beispiel, damit du ein bisschen Inspiration bekommst.

**9:41** · Und zwar schreibe ich jetzt "Erstelle ein neues Notebook namens Cloudcode Skills und lasse Notebook LM die Top 10 YouTube Videos zu dem Thema recherchieren und dann auch analysieren, welche Skills besonders nützlich und beliebt sind. Anschließend erstellst du einen Podcast zu dem Thema als auch eine Infografik mit den Top 10 Skills." Du kannst übrigens auch Skills direkt aufrufen, indem du einfach Slash und dann den Namen des Skills eingibst, also z.B. Notebook LM. Aber Cloud würde es auch anhand des Kontextes jetzt hier verstehen. Ich schicke das jetzt ab und wir schauen einfach, was er macht.

**10:10** · Hier auch noch ein kleiner Hinweis: Füge auch hinzu, dass er die Recherche nicht selbst machen soll noch zusätzlich, sondern dass er das einfach mit Notebook LM machen soll. Wir sehen, er hat hier das Notebook erstellt und auch eine Tiefenrecherche zum Thema Notebook LM jetzt gestartet und hier sehen wir sieht man dann immer, welche Commands er ausführt. Und das Coole ist, während er das macht, können wir genau sehen, was er im Notebook LM macht. Und wenn wir das hier neu laden, siehst du auch hier unten das neue Notebook Cloudcode Skills.

**10:34** · Und was ich so cool finde, er hat hier selber Notebook LM gefragt, basierend auf allen Quellen, was sind die Top 10 beliebtesten und nützlichsten Cloudcode Skills? Erstelle ein Ranking mit Begründung, warum jeder Skill besonders wertvoll ist. Berücksichtige Skills, Hooks, Slash Commands, MCP Server und und und. Das habe ich nicht selber geschrieben, das hat Cloud hier einfach gerade Notebook LM gefragt. Und Notebook LM kann natürlich jetzt sehr gute quellenbasierte Antworten geben anhand dieser 41 Quellen hier links.

**10:59** · Und das kann Cloudcode dann auch wieder nutzen, um eine Antwort hier rechts, die Generation der Infografik ist hier fehlgeschlagen, aber Cloudcode wird das selber bemerken und dann auch lösen. Ich werde hier nicht selber machen. Hier sagt er das auch, die Infografik-Generierung ist leider fehlgeschlagen. Ich starte einen neuen Versuch. Also mittlerweile sitze ich eigentlich die meiste Zeit vor dem PC und schaue einfach nur, was Cloudcode da macht. Und er hat jetzt sowohl den Podcast als auch die Infografik erstellt und ich habe hier noch mal kurz gefragt, was er denn jetzt eigentlich gemacht hat mit Notebook LM.

**11:28** · Er hat ein Notebook erstellt, er hat eine Deep Research gestartet, Dann hat er mit Hilfe des Chats, indem er die Ask-Funktion hier genutzt hat, Notebook LM Fragen zu den beliebtesten Skills gestellt, um diese zu identifizieren und auch zu ranken.

**11:42** · Das Ergebnis hat er sich dann gespeichert als Notiz. Dann hat er einen Podcast generiert, in dem zwei KI-Stimmen die Top-10 Skills diskutieren und er hat eine Infografik erstellt mit einer Top-10 Ranking-Liste. Und er hat jetzt diese Infografik hier erstellt mit Hilfe des Nano Banana 2 Bildgenerierungsmodells, das ja auch nativ integriert ist im Notebook LM. Das heißt, wir müssen hier auch wieder keine externe API verbinden oder irgendein externes Tool, sondern er kann jetzt dieses Modell auch einfach über Notebook LM nutzen. Und ich finde, das sieht schon ziemlich gut aus, auch mit dem Text.

**12:12** · Ich sehe jetzt auch nicht direkt irgendwelche Verzerrungen oder Sonstiges. Also, man kann das ja hier auch schon ziemlich gut lesen und es sieht doch einfach richtig gut aus mit der Farbe und hier den einzelnen Skills.

**12:24** · Ich sehe jetzt gerade, das sind nicht alles Skills, ne? Also hier, wenn man mal ehrlich ist, hier so was wie Slash Permission oder Subagents, da hat er sich vielleicht jetzt ein bisschen vertan, aber ich finde trotzdem zeigt es, was möglich ist mit diesem Notebook LM Skill. Und folgender Podcast ist jetzt auch entstanden.

**12:40** · Stell dir mal vor, du baust ein Haus, also so richtig von Grund auf.

**12:44** · Oh je, das ist meistens ein ziemlicher Albtraum, ja.

**12:47** · Absolut. Und stell dir vor, du hast für all diese kleinen Aufgaben im Alltag immer diesen einen völlig verlässlichen Allround-Handwerker.

**12:55** · So einen, der alles ein bisschen kann?

**12:56** · Genau den. Also, der kann ein bisschen klempnern, der streicht der ganz passabel die Wände.

**13:01** · Ja.

**13:02** · Und wenn es echt sein muss, verlegt er dir auch mal so ein Stromkabel.

**13:05** · Und so weiter. Wir wissen genau, dass Claude Code damit gemeint ist. Also, ziemlich cool. Das heißt, jetzt haben wir sogar einen Podcast über Claude Code und die Skills-Funktion. Und ich finde es einfach extrem cool, wie Claude Code hier dann mit Notebook LM kommuniziert.

**13:16** · Also, wirklich richtig krass. Und ich glaube, wenn du viel mit Notebook LM arbeitest und auch mit Claude Code, dann kann das sehr nützlich für dich sein.

### 3 Remotion Skill

**13:24** · Kommen wir auch zum dritten Skill und das ist der Remotion Skill. Mit Remotion kann Claude Code Videos erstellen und zwar echte gerenderte MP4 Videos, also keine KI generierten Videos, sondern Videos, die mit Hilfe von Code generiert werden. Claude Code hat mit Remotion diese zwei Animationsvideos, die du am Anfang gesehen hast, generiert und ich habe ihm einfach nur gesagt, dass ich gerne eine Animation brauche für den und den Text und er hat es einfach gemacht.

**13:47** · Und es läuft so ab, dass du Claude Code einfach mal einen Prompt gibst, was für ein Video du generiert haben möchtest und er übernimmt das ganze Coden und erstellt das Videos. Wie installieren wir das jetzt? Es gibt auf der skills.sh Seite ganz viele verschiedene Skills, die man herunterladen kann und da findet man auch eben diesen Remotion Best Practices Skill. Der erklärt nämlich Claude Code, wie es am besten mit Remotion arbeitet. Das heißt, du kannst hier diesen Command einfach kopieren und dann in deinem Terminal ausführen oder du kannst auch wieder hier oben den Link hierzu kopieren und einfach Claude Code sagen, er soll es installieren. Der Skill wurde erfolgreich installiert.

**14:18** · Er liefert domänenspezifisches Wissen für die Arbeit mit Remotion Code. Also Animationen, Kompositionen, Timing, Medien, 3D, Charts etc. Und du kannst ihm jetzt einfach einen Prompt geben, was du generiert haben möchtest und ich mache jetzt einfach mal ein Beispiel. In meinem Video brauche ich ja für folgende Stelle eine Remotion-Animation. Und dann gebe ich ihm einfach nur den Text, den ich sage an einer bestimmten Stelle und er soll sich jetzt selbst überlegen, was vielleicht sinnvoll wäre da jetzt einzublenden, weil ich habe selber vielleicht keine Ahnung.

**14:45** · Wenn ich was weiß, dann kann ich ihm das hier natürlich noch als zusätzliche Info geben, wenn ich das in eine bestimmte Richtung haben möchte, aber ich lasse ihn das jetzt einfach mal selber überlegen. jetzt genau weißt, was du generieren möchtest, dann kannst du es natürlich auch einfach als Prompt reinschreiben. Ich schicke das jetzt ab.

**14:59** · So, er hat jetzt das komplette Video erstellt und guck mal bitte, wie krass das ist. Er hat jetzt hier ein neues Fenster geöffnet mit diesem Remotion Video Editor und folgendes hat er jetzt First Try generiert.

**15:11** · Erstmal hier die vier Dinge, die wir zeigen, dann auch schön mit dem Text und dann auch noch das hier. Also, First Try, ne? Also, ich könnte ihm jetzt natürlich noch Feedback geben und sagen, nee, mach das mal anders und so weiter, denn das hier ist absolut programmatisch erstellt mit Code. Also, ich kann jetzt genau auf bestimmte Stellen eingehen und sagen, änder das. Das ist eben genau der Vorteil gegenüber KI-generierten Videoanimationen über irgendwelche Videogenerierungsmodelle, weil da kannst du nicht einfach bestimmte Sektionen jetzt genau ändern, sondern meistens musst du das gesamte Video neu generieren. Aber ich kann ihm jetzt z.B.

**15:42** · sagen, er soll diese Sachen hier langsamer einblenden und hier werde ich ihm einfach sagen, er soll irgendeine Person einfügen, die ein Tool in der Hand hält und fröhlich ist. Mal gucken, ob er das hinbekommt. Bitte die vier Karten langsamer einblenden nacheinander und dann statt des Textes in Phase 3 eine fröhliche Person, die etwas in der Hand hält, einblenden. Mal gucken, was er daraus macht. Wir hätten ihm hier oben im Prompt auch noch sagen können, dass er eigentlich zuerst ein Konzept erstellen soll und wir dann noch mal das Go geben oder wir hätten ihn auch in den Planmodus packen können. Das wäre wahrscheinlich schlauer gewesen, aber er hat jetzt hier First Try auch was ziemlich Gutes schon generiert und das können wir jetzt einfach anpassen.

**16:12** · Und jetzt hat er die Animation neu generiert. Schauen wir uns das mal an.

**16:16** · Und zwar wurde jetzt Folgendes generiert: Die Karten werden jetzt langsamer nacheinander angezeigt, damit man das auch schön aussprechen kann. Und danach sehen wir jetzt hier die fröhliche Person, die jetzt hier was in der Hand hält. Also, mega cool, oder?

**16:30** · Einfach nur kurz noch mal Feedback gegeben, dann die bestimmten Stellen angepasst. Mega. Ich wollte mir jetzt eigentlich einen professionellen Editor hier einstellen, dass er die Videos ein bisschen schöner macht, aber ich glaube, das wird jetzt nicht mehr nötig sein.

**16:41** · Falls du dann zufrieden mit dem Video bist, kannst du hier unten einfach auf Render gehen und nachdem ich das Video hier gerendert habe, kann ich das einfach hier herunterladen. Das heißt, falls du solche Animationen für deine Projekte brauchst, nutz unbedingt Cloud Code und den Remotion Skill. Kurzer Einwurf an der Stelle, wenn du noch tiefer in das Thema Cloud Code einsteigen möchtest und das Ganze mal von Anfang bis Ende strukturiert lernen willst, dann kannst du auch gerne in meiner Community vorbeischauen. Link dazu in der Videobeschreibung. Wir haben hier neben den ganzen N nach N Kursen auch einen Kurs zu Cloud Code, wo du wirklich von Anfang bis Ende alles strukturiert lernst.

**17:10** · Das heißt, du musst nicht von YouTube Video zu YouTube Video springen, sondern hier hast du alle Inhalte didaktisch und strukturiert aufeinander aufgebaut. Das heißt, wenn du eine Abkürzung bei dem Thema brauchst, kannst du auch gerne hier vorbeischauen. Wir sind mittlerweile über 400 Selbstständige und Unternehmer, die sich hier gegenseitig unterstützen bei dem Thema. Und hier ist natürlich besonders der Fokus, dass wir das Ganze auch im Business-Kontext einsetzen können.

**17:29** · Und zweimal in der Woche tauschen wir uns auch aus, um die neuesten Themen zu besprechen, auch einfach mal Fragen zu klären, über Probleme zu schauen und einfach mal in den Austausch zu gehen, denn man kann hier extrem viel voneinander lernen und eben von den Erfahrungen von anderen auch profitieren. Das heißt, man muss nicht immer alle Fehler selber machen.

**17:45** · Man kann auch einfach von den Fehlern von anderen lernen. Dafür finde ich es eine Community sehr, sehr nützlich. Und alleine der Aspekt, dass man einfach mal jemanden fragen kann, wenn man nicht weiterkommt, ist Gold wert. Das heißt, falls du das Thema mit Claude Code, N8N und KI-Automatisierung etwas ernster angehen willst, dann kannst du auch gerne in meine Community vorbeischauen.

**18:00** · Link dazu in der Videobeschreibung.

**18:02** · Kommen wir zum vierten Plugin und zwar Context Seven. Context Seven löst ein großes Problem von Sprachmodellen, nämlich dass sie ja nur bis zu einem gewissen Datum trainiert wurden, also z.B.

### 4 Context7 CLI

**18:11** · irgendwann Ende 2025 z.B. Das Wissen ist ab dann gecuttet und alles, was danach kommt, müssen sie sich dann z.B. mit einem Web Search Tool im Internet recherchieren. Das heißt, es kann dazu kommen, dass Sprachmodelle Code generieren, welcher noch auf veralteten Trainingsdaten basiert und deswegen vielleicht gar nicht mal funktioniert.

**18:29** · Das heißt, Claude kann z.B. irgendwelche APIs halluzinieren oder irgendwelche API-Endpunkte von anderen Programmen, die vielleicht gar nicht mehr existieren. Und mit Context Seven kann sich jetzt Claude in unserem Fall die API-Dokumentationen von verschiedensten Frameworks und Tools direkt in den Kontext laden, wenn wir es benötigen. Das heißt, wir haben keine halluzinierten APIs mehr, kein veralteter Code. Und das ist auch ein Grund, warum dieses Repository jetzt hier auch in der letzten Zeit total beliebt geworden ist, weil es einfach in unserem Fall jetzt Claude Code mit zusätzlichem Wissen ausstattet.

**18:57** · Und hier ist noch wichtig zu erwähnen, es gibt sowohl die Möglichkeit, Context Seven als CLI-Tool mit Skills zu nutzen. Ein CLI-Tool ist einfach nur ein Tool, das im Terminal läuft, genauso wie Claude Code. Und deswegen funktioniert das natürlich zusammen sehr gut oder man kann das ganze über den MCP Server nutzen, aber ich würde die immer empfehlen so ein CLI Tool und auch einen Skill dann dazu zu nutzen, wenn es verfügbar ist, denn diese sind deutlich Token effizienter als MCP Server.

**19:22** · Das heißt, ich kopiere jetzt einfach hier wieder den Link zu dem GitHub Repository, füg das bei Claude ein und schreibe einfach installiere Context Seven CLI mit dem Skill, setzen hier auf Bypass Permissions und dann richtet er das für uns ein. Jetzt fragt er mich hier, ob ich einen API Key habe für Context Seven und Context Seven kann man auch ohne API Key nutzen, aber da hat man niedrigere Rate Limits.

**19:41** · Man kann sich aber hier einfach bei Context Seven im Dashboard einen API Key erstellen und dann hat man auch höhere Rate Limits, aber das lasse ich jetzt mal aus und in der Zwischenzeit habe ich mir jetzt hier mal kurz bei Context Seven einen Account eingerichtet, das ist auch komplett kostenlos und hier kann man dann einen API Key erstellen. Jetzt kann ich mir eigentlich immer sicher sein, dass wenn ich mit externen Diensten oder irgendwelchen Tools arbeite, dass Claude Code immer Zugriff auf die Dokumentation hat über Context Seven.

**20:05** · Das heißt, wenn ich jetzt hier z.B. schreibe, wie nutze ich die Stripe API, um eine Checkout Session zu erstellen und das abschicke und dann nutzt er sein CLI Tool, um eben genau die Stripe Dokumentation durchzuschauen. Und klar, in dem einfachen Beispiel hätte Claude jetzt auch einfach eine Web Search machen können und sich die Dokumentation ziehen können, aber für komplexere Beispiele, wo man vielleicht mehrere Seiten einer Dokumentation durchlesen muss, kann Claude jetzt einfach direkt das CLI Tool nutzen und muss nicht eine Internetsuche machen.

**20:32** · Hier die aktuelle Anleitung aus der Stripe Dokumentation via Context Seven und dann erklärt er eben genau, wie man das macht. Das ist ehrlich gesagt eines der Tools, das ich unbedingt empfehlen würde zu installieren, wenn man mit verschiedenen Frameworks immer wieder arbeitet in verschiedenen Projekten, denn damit hat Claude wirklich immer die Dokumentation up-to-date zur Verfügung. Kommen wir zum fünften Skill und zwar ist das der Fire Crawl Skill und die CLI.

### 5 Firecrawl CLI + Skill

**20:53** · Falls du Fire Crawl noch nicht kennst, das ist ein sehr gutes Scraping Tool, um verschiedenste Webseiten, die auch komplex strukturiert sind mit Unterseiten und so weiter zu scrapen und die Informationen dann in LLM ready Daten umzuwandeln. Das bedeutet einfach nur in gut lesbare Formate für Sprachmodelle wie Claude oder GPT oder Sonstiges.

**21:16** · Claude Code kann standardmäßig auch das Internet durchsuchen und bestimmte Webseiten scrapen, aber diese Scrape-Funktion ist deutlich eingeschränkter als z.B. bei Firecraw. Die Webfetch-Funktion von Claude kann nämlich nur einzelne Seiten auf einmal abrufen. Es kann kein JavaScript rendern, das heißt bei dynamischen Seiten bekommst du nur das rohe HTML. Es kann auch nicht über mehrere Unterseiten crawlen und es kann auch keine strukturierten Daten gezielt als JSON extrahieren. Das würde sich Claude Code dann selbst zusammenbasteln und natürlich wieder sehr viel Tokens verschwenden.

**21:47** · Und Firecraw geht da einfach deutlich weiter. Du kannst ganze Websites mit allen Unterseiten crawlen, JavaScript wird gerendert, du bekommst sauberes Markdown oder strukturiertes JSON zurück und kannst eben auch gezielt Daten extrahieren, also z.B. sagen, gib mir nur die Preise und Feature-Namen als JSON. Und dazu kommt auch noch Anti-Bot-Handling, das heißt, du kannst wirklich bestimmte Seiten scrapen, die vielleicht irgendwelche Blockaden extra drin haben, um nicht gescrapt zu werden.

**22:13** · Und hier siehst du auch die Kernbefehle, die Claude dann noch zusätzlich bekommt zum scrapen von Websites. Und natürlich gibt es mittlerweile neben dem MCP-Server von Firecraw auch die Kombination aus Skill und CLI, weil das gerade ein absoluter Trend ist bei der Arbeit mit agentischen Codingsystemen wie Claude Code, denn es ist einfach deutlich effizienter. Die Installation ist auch wieder ganz einfach, einfach den Link kopieren, hier einfügen und einfach sagen, soll die Firecraw CLI und den Skill installieren, aber nicht den MCP-Server.

**22:38** · Das bedeutet, wenn du jetzt irgendeinen Use-Case hast, wo du wirklich viele Seiten scrapen musst, um z.B. irgendwelche Leads z.B. zu finden oder auch andere Informationen von komplexen Seiten mit komplexen Strukturen zu extrahieren, dann solltest du unbedingt Claude Code die Möglichkeit geben, Firecraw zu nutzen, da es einfach noch mal deutlich besser Webseiten damit scrapen kann. Der hat es dann hier installiert und dann müssen wir uns auch noch kurz authentifizieren, also einfach diesen Command hier im Terminal eingeben, also einfach so, dann öffnet sich hier das Fenster und dann musst du einfach die CLI hier autorisieren mit deinem Account.

**23:09** · Firecrawl hat einen großzügigen Free Tier, mit dem du 500 Seiten pro Monat for free scrapen kannst. Und nachdem ich mich jetzt authentifiziert habe, kann ich Claude folgendes schreiben: "Suche mit Firecrawl nach 100 Handwerksbetrieben im Umkreis von Hamburg und extrahiere von jeder Seite Firmenname, Ansprechpartner, E-Mail-Adresse, angebotene Services und Standort. Gib mir das als Excel zurück."

**23:30** · Jetzt schauen wir mal, ob er das macht.

**23:31** · Er nutzt hier den Firecrawl Skill. So, das Ganze hat ca. 3 Minuten geladen und er hat jetzt hier die Excel erstellt. Er konnte einige Seiten nicht mehr scrapen, weil meine Tokens aufgebraucht waren, das ist dann mein Problem. Und hier sehen wir dann auch die Excel-Tabelle mit dem Firmennamen, dann auch, was das für ein Handwerksbetrieb ist, dann ein Ansprechpartner, falls er einen finden konnte, dann hier auch immer die E-Mail und klar, es ist jetzt oft auch eine Info-Mail, ne, weil er hat jetzt einfach das Impressum mit dem gescrapt, dann aber auch die Telefonnummer, Services, Adresse, Standort und auch die Website.

**24:01** · Er hat jetzt automatisch nicht nur die Website gefunden, sondern dann auch auf der Website das Impressum, um dann diese Informationen hier zu extrahieren und das in Nullkommanichts. Ich meine, das hat er jetzt alles selber gemacht. Ich weiß noch, als wir damals so was in N8N darstellen wollten, das war dann ein bisschen komplizierter. Das heißt, wenn du das Internet scrapen möchtest, dann nutz unbedingt Claude Code auch mit Firecrawl. Kommen wir zu Nummer 6 und zwar ist das die Playwright CLI. Das ist ein CLI-Tool von Microsoft, mit dem Claude den Browser steuern kann. Das heißt, Seiten öffnen, Buttons klicken, Formulare ausfüllen und so weiter.

### 6 Playwright CLI

**24:32** · Jetzt denkst du dir vielleicht, okay, aber es gibt doch auch die Claude Chrome Extension, das heißt, damit kann Claude auch sowieso hier den Browser steuern.

**24:40** · Und ja, das stimmt auch und für viele Use Cases reicht bestimmt auch diese Extension, aber wenn du mal intensiver mit dieser Extension gearbeitet hast, dann ist dir vielleicht mal aufgefallen, dass in bestimmten Fällen das Ganze auch nicht so gut funktioniert. Das heißt, es lädt sich manchmal sehr lange oder Claude kommt irgendwie nicht weiter oder er macht schlichtweg Sachen falsch und das Ganze ist auch noch in der Beta und anhand der Bewertungen sieht man auch, dass das Ganze noch nicht so gut funktioniert, aber wie gesagt, es ist noch in der Beta.

**25:04** · Das heißt, wenn du selbst auch mal Probleme mit der Claude Browser Extension hast oder auch die gar nicht nutzen kannst, weil das hier nur im Chrome läuft oder auch im Microsoft Edge, dann solltest du dir unbedingt mal die Playwright CLI anschauen. Microsoft hat jetzt eben auch ein CLI Tool veröffentlicht, weil es einfach viel effizienter ist mit CLI Tools zu arbeiten hinsichtlich Coding Agents und der wesentliche Unterschied von Playwright und der Claude Chrome Extension ist, dass Playwright den Browser steuert, indem es den Code analysiert und dann z.B.

**25:31** · schaut, wo welche Buttons vorkommen anhand des Codes und anhand irgendwelcher IDs und dann z.B. sagen kann, aha, hier ist die ID, das ist der Button, den muss ich anklicken oder hier ist das Feld, da kann ich was reinschreiben. Bei der Claude Extension ist es so, dass Claude die ganze Zeit Screenshots macht von der Seite und dann versucht herauszufinden, wo es hinklicken muss und das dauert nicht nur ziemlich lange, sondern es geht auch manchmal einfach schief und klappt nicht. Und weil Claude mit Hilfe von Playwright einfach den Code analysieren kann von der Seite und dann deutlich schneller sehen kann, wo es hinklicken muss, funktioniert das Ganze auch noch mal zuverlässiger und auch schneller.

**26:03** · Und noch ein Unterschied ist, dass die CLI von Playwright auch headless funktioniert by default. Das bedeutet, es wird nicht aktiv ein Browser Tab geöffnet und dann hin und her geklickt, sondern das Ganze passiert auch ohne den Browser Tab im Hintergrund. Du kannst aber natürlich auch aktivieren, dass du aktiv den Browser siehst und genau siehst, was passiert. Und du kannst auch gleichzeitig mehrere Sessions starten und verschiedene Browser Aktionen durchführen. Ich würde sagen, wir testen das Ganze einfach mal, dann siehst du, was ich meine.

**26:29** · Ich kopiere hier wieder den Link zum Repository, installiere die CLI und den Skill und dann hat er hier sowohl die CLI als auch den Skill erstellt und Playwright hat ja auch als Demo so eine Seite erstellt mit einer To-Do-Liste, wo man jetzt hier verschiedene Sachen eintragen kann und dann einfach testen kann, ob Claude jetzt hier z.B. das einfügen kann, was wir möchten oder auch die ganzen To-Dos hier anklicken kann und so weiter. Das heißt, wir testen das jetzt mal damit.

**26:55** · Nutze Playwright und erstelle zehn To-Dos für den Haushalt und hake sie nacheinander ab. Zeige den Browser an.

**27:01** · Und jetzt sehen wir, öffnet er hier den Browser-Tab. Und ich mache das mal hier ein bisschen größer. Und jetzt siehst du hier rechts, was Cloud Code macht. Er sieht die Referenz des Textfeldes im Code und kann jetzt hier die ganzen Einträge machen, nacheinander. To-Do 1, To-Do 2, To-Do 3 und so weiter. Und das macht er alles, indem er den Code versteht. Das bedeutet, er macht nicht Screenshots und versucht dann zu überlegen, okay, wo muss ich jetzt was einfügen, sondern er liest einfach nur den Code aus. Und dann sehen wir hier auch die einzelnen IDs von diesen Feldern, die dann abzuhaken sind. Ich meine, das hat jetzt hier nicht mal eine Minute gedauert und der ist schon fertig.

**27:32** · Das heißt, falls du irgendeinen Browser-Use-Case hast und unzufrieden bist mit der Cloud Chrome Extension, dann probier doch gerne mal die Playwright CLI als Alternative aus.

**27:40** · Kommen wir zu Nummer 10. Und zwar ist das das Obsidian-Plugin. Falls du Obsidian noch nicht kennst, das ist eine Notiz-App, die alles als Markdown-Datei speichert. Also einfach Textdateien auf deinem Rechner, keine Cloud, keine Datenbank, einfach nur Ordner mit Markdown-Dateien. Und du kannst Notizen untereinander verlinken, du kannst Tags setzen, du kannst Properties vergeben und dir so ein persönliches Wissenssystem aufbauen. Viele nennen das gerade auch ein zweites Gehirn. Und Obsidian gibt es schon seit Jahren, aber jetzt mit Cloud Code wird es richtig interessant.

### 7 Obsidian Skills

**28:11** · Denn überleg mal, Obsidian speichert alles als Markdown-Datei. Und Cloud Code arbeitet ja auch mit Markdown-Dateien. Das passt perfekt zusammen. Bei Obsidian ist es so, du hast hier wirklich einfach nur einen Vault, so heißt das. Das ist eigentlich nur ein Ordner, in dem dann z.B.

**28:26** · verschiedene Unterordner drin sein können und dann in diesen Unterordnern dann z.B. hier verschiedene Textdateien, ne, also Markdown-Dateien mit den Informationen zu z.B. jetzt hier Cloud Code. Und in diesen Texten kann man dann andere Dateien auch verlinkten, ne, also jetzt hier z.B. N8N. Wenn ich dann hier raufklicke, springe ich direkt zu N8N und kann hier auch wieder Sachen verlinken, z.B. hier DSGVO. Das bedeutet, man kann Wissen sehr gut vernetzen. Und diese Verlinkungen lassen sich dann auch hier in so einem Graphen darstellen.

**28:55** · Das heißt, du siehst ganz genau, welche Informationen mit welchen anderen Informationen in Verbindung stehen. Das heißt, du kannst all dein Wissen, das du jetzt hier über die Jahre ansammelst, auch abspeichern in so einem System wie Obsidian. Und guess what, seit einiger Zeit hat Obsidian auch ein CLI-Tool. Das bedeutet, man kann alle Dinge in Obsidian über das Terminal steuern. Das heißt, Claude Code kann auch für uns unser gesamtes Obsidian steuern. Das heißt, er hat direkten Zugriff auf unseren Vault, auf alle Ordner, alle Notizen.

**29:23** · Und er kann Notizen lesen, durchsuchen, zusammenfassen, neue Notizen mit Verlinkungen erstellen. Denn das war vorher wirklich anstrengend, dass man hier immer selbst diese Verlinkungen erstellt. Da musste man immer so ein paar Befehle eingeben bzw. halt einen Ausdruck. Und das ist einfach nur manuell ziemlich anstrengend. Aber das haben wir jetzt nicht mehr. Das kann nämlich jetzt Claude einfach für uns übernehmen. Und das Allerwichtigste ist, Claude kann ja dieses gesamte, gesammelte Wissen auch selber nutzen als Kontext. Denn stell dir vor, du hast hunderte Notizen zu Kunden, Projekten, Ideen, Meetings.

**29:55** · Und Claude kann dann, je nachdem, was du fragst, direkt auf diese Infos zugreifen und sich deutlich mehr Kontext holen. Das bedeutet eigentlich, wir erweitern einfach nur das Gedächtnis von Claude Code, indem wir ihm Zugriff auf unsere Notizen in Obsidian geben. Und damit wird er quasi viel mehr zu einem persönlichen Assistenten, der dir dann deutlich besser helfen kann, da er deutlich mehr über dich weiß. Das heißt, damit ist es nicht so, dass, wenn wir jetzt hier einen neuen Chat in Claude Code starten, dass wir komplett bei Null anfangen.

**30:20** · Sondern ich kann jetzt hier einfach mit ihm schreiben und je nach Situation kann er dann auf meinen Obsidian Vault zugreifen, auf Kontext über mich z.B.

**30:27** · zugreifen und daraufhin seine Antwort generieren und hier irgendwas machen.

**30:31** · Und ich muss ihm das nicht alles noch mal neu sagen. Oder auch hier jedes Mal in so eine Claude MD-Datei abspeichern.

**30:36** · Und es gibt, wie gesagt, ein Obsidian-Plugin. Das Repository heißt Obsidian Skills. Und wenn wir das von Claude Code lassen wird automatisch auch die Obsidian CLI installiert und weitere nützliche Skills, um mit Obsidian zu arbeiten und damit wir das jetzt richtig installieren, musst du zuerst natürlich Obsidian hier als Desktop App herunterladen.

**30:53** · In Obsidian musst du dann einen neuen Volt erstellen, also, das ist einfach nur der Überordner sozusagen, der wird dann einfach bei dir leer sein hier und diesen Ordner kannst du dann auch wie in jedem anderen Ordner auch hier in Visual Studio Code öffnen und hier kannst du dann Cloud sagen, er soll dieses Obsidian Plugin installieren. du kopierst dir einfach

**31:10** · wieder fügst es hier ein und sagst er soll das Obsidian Plugin hier für dich installieren und dann kannst du einfach mit dem Brainstorm und kannst ihn fragen, okay, was für eine Ordnerstruktur würde für mich Sinn ergeben, kannst du natürlich ein bisschen selber überlegen, denn das ist natürlich total individuell, wie du das hier gestalten möchtest, ich habe ein bisschen mit Cloudcode gebrainstormt in ein bisschen gefragt, was wäre für mich sinnvoll und ihm so meine Bereiche gesagt und dann hat er auch für die jeweiligen Ordner ein paar sinnvolle Unterordner erstellt und so weiter und dann habe ich ganz einfach nur mit diesem Whisper Tool hier, das ist so ein Transkriptionstool alles mögliche über

**31:41** · mal mich und meine Tätigkeiten und so weiter hier reingesprochen, dass er daraus ein paar Notizen erstellt und die auch verknüpft und das hat er natürlich dann alles für mich gemacht, hat echt lange geladen und ich bin jetzt selbst auch gerade dabei, das ganze noch viel weiter auszubauen, denn ich finde, das ist eine sehr sehr gute Möglichkeit, um Cloudcode eben noch mal zusätzliches Wissen zu geben über dich, das heißt nicht nur ist es für uns einfacher geworden mit Hilfe von Cloudcode hier

**32:02** · Informationen in Obsidian abzuspeichern und diese ganzen Dateien und Markdown Texte für uns hier zu erstellen und diese auch untereinander zu verlinken, sondern wir können jetzt eben auch Cloudcode Zugang geben zu all diesem Wissen über uns und über unsere Projekte und das ist der Punkt, wo Cloudcode dann wirklich zu einem persönlichen Assistenten wird, weil er jetzt nicht mehr im Vakuum arbeitet, sondern auf

**32:23** · dein gesammeltes Wissen zugreifen kann, denn er sieht dann genauso wie dieser Wissensgraf hier alle Connections zwischen den einzelnen Entitäten und kann dann von Markdown Datei zu Markdown Datei springen und dich ähnlich wie in einem Graph Rex System hier sehr gut unterstützen, weil er die ganzen Verbindungen hier zu den einzelnen Themen, die dich interessieren, deutlich besser versteht. Das heißt, falls du Obsidian noch nicht nutzt, schaust dir unbedingt an. Ich werde hierzu wahrscheinlich noch mal ein extra Video machen, weil ich finde, dass das sehr viel Potenzial hat und das Ganze jetzt hier in ein paar Minuten reinzuquetschen ist ein bisschen unpraktisch.

**32:51** · Deswegen, falls es dich auch interessiert, schreib's gerne in die Kommentare, dann mache ich noch mal ein Video dazu. Falls du auch einen oder anderen Skill noch interessant fandest, dann schreib auch das gerne in die Kommentare, dann kann ich das sehen und dementsprechend vielleicht auch noch dazu ein Video machen. Kommen wir zum achten Plugin das Feature Dev Plugin von Anthropic. Das Plugin hilft dir dabei, neue Features oder Inhalte in deiner App strukturiert anhand eines klaren Prozesses zu entwickeln. Und das Ganze in sieben klar voneinander getrennten Phasen, die nacheinander abgearbeitet werden, um das Feature wirklich sinnvoll zu entwickeln.

### 8 Feature Dev Plugin

**33:22** · Und ich will einmal mit dir kurz die Phasen durchgehen und übrigens, diese Abbildung wurde natürlich mithilfe von Claude Code generiert und dem Excalibur Skill. Die erste Phase ist die Discovery Phase. Das heißt, hier geht es erstmal darum, nur zu verstehen, was überhaupt gebaut werden soll. Claude klärt die Anforderungen, identifiziert irgendwelche Constraints und stellt sicher, dass er wirklich verstanden hat, was das Problem ist. Danach gehen wir in die Codebase Exploration. Das heißt, Claude schickt zwei bis drei parallele Explorer Agents los, die deinen bestehenden Code analysieren.

**33:50** · Das heißt, Claude versteht erstmal, was schon da ist, bevor er irgendwas Neues baut. In der dritten Phase werden Fragen geklärt.

**33:58** · Das heißt, Claude stellt einfach Rückfragen über bestimmte Edge Cases oder Fehlerbehandlungen oder Integrations- punkte, Performance-Anforderungen und so weiter.

**34:07** · Also alles, was noch unklar ist, wird hier geklärt. Und Claude wartet dann auch erstmal auf dein Feedback, bevor er irgendwas weitermacht. In Phase vier gehen wir dann in das Design der Architektur deines Features, das du einbauen möchtest, und dort schickt Claude dann zwei bis drei Architekt-Agenten los, die dann verschiedene Versionen des Features designen. Das heißt, verschiedene Varianten, wo Claude dann noch mal drüber schaut und dir dann eins empfiehlt, aber du selbst kannst selber noch mal sagen, welche du davon nehmen möchtest. Das heißt, es werden einfach mehrere Ansätze deines Features entworfen und du entscheidest einfach, was dir am meisten gefällt.

**34:37** · Und erst jetzt in Phase 5 kommt es zur Implementierung. Also, das ist jetzt die Implementierungsphase.

**34:44** · Jetzt wird gebaut und zwar nach dem Ansatz, den du vorher in Phase 4 gewählt hast. Nachdem das dann fertig gebaut wurde, geht es in Phase 6 über, dem Qualitätsreview. Drei parallele Review Agents prüfen dann den Code. Das heißt, es werden nach Bugs gesucht, es wird geschaut, ob die User Experience gut ist, ob der Code auch wirklich gut geschrieben ist, ob die Konventionen und die Muster, die vorher geplant wurden, auch wirklich eingehalten wurden. Und falls dann irgendwelche Sachen auffallen, dann kann man entscheiden, ob man das Ganze jetzt lösen möchte oder auch erst später. Und Phase 7 ist dann einfach nur eine Zusammenfassung des Implementierten.

**35:15** · Das heißt, Claude dokumentiert, was gebaut wurde, welche Entscheidungen getroffen wurden, welche Dateien geändert wurden und was auch die empfohlenen nächsten Schritte sind. Ich würde dir dringend empfehlen, wenn du an einer komplexen App sitzt, mal dieses Feature Dev Plugin hier auszuprobieren, wenn du jetzt neue Features einbauen möchtest in deine App. Also z.B. ein Loginsystem oder eine Bezahlfunktion mit Stripe oder auch ein Kontaktformular oder irgendwelche Suchfunktionen.

**35:40** · Installation genauso wie vorher, einfach den Browserlink in Claude eingeben und sagen, er soll Feature Dev für dich installieren. Probier das gerne mal aus für ein neues Feature in deiner App. Ich kann dir sagen, das ist sehr, sehr nützlich ist, weil es noch mal deutlich mehr Struktur in den gesamten Entwicklungsprozess gibt, ne? Es ist ja Planung, Implementierung, Review, alles in einem. Also, besonders bei komplexeren Projekten eine klare Empfehlung. Kommen wir jetzt zum neunten Plugin und das ist das Superpowers Plugin. Das ist auf Platz 2 der meist gedownloadetsten Plugins hier in Claude.

### 9 Superpowers plugin

**36:08** · Und wir hatten ja gerade das Feature Dev Plugin, das für einzelne Features in deiner App gedacht ist. Und Superpowers geht noch mal einen Schritt weiter und deckt den gesamten Entwicklungsprozess ab. Also, nicht nur baue dieses Features, sondern auch hilf mir erstmal rauszufinden, was ich überhaupt bauen soll. Es ist ein umfassendes Kompetenzrahmenwerk, das Claude strukturierte Softwareentwicklungsmethoden vermittelt.

**36:29** · Es bietet zusammensetzbare Kompetenzen für testgetriebene Entwicklung, systematisches Debugging, Brainstorming, Subagenten-gesteuerte Entwicklung und integrierte Code-Prüfung. Das heißt, wenn ich ganz am Anfang stehe und eine ganze App jetzt bauen möchte, dann kann mir Superpowers sehr gut dabei helfen, meine App, so wie ich sie mir vorstelle, wirklich dann auch zu implementieren.

**36:49** · Und nach jedem Schritt wird auch immer ein Review gemacht von dem, was implementiert wurde. Und was ich genial finde an dem Superpowers-Plugin ist, dass neben dem Brainstorming für deine App und dem strukturierten Debugging, was auch enthalten ist, eine testgetriebene Entwicklung dabei ist.

**37:03** · Normalerweise ist es so, dass Claude zuerst den Code für deine Anwendung schreibt und danach erst testet, ob der Code funktioniert. Mit der testgetriebenen Entwicklung dreht Superpowers das aber um. Das heißt, Claude beschreibt zuerst, was der Code am Ende können soll, also quasi die Anforderungen als automatischen Test, und dann schreibt Claude den Code so lange, bis er den Test besteht. Denn dadurch weiß Claude von Anfang an ganz genau, was das Ziel ist, und baut nicht an den Anforderungen vorbei.

**37:29** · Das heißt, zuerst Test schreiben, dann so lange coden, bis die Tests erfüllt werden, und danach wird der Code aufgeräumt, und das Ganze wird dann für jedes einzelne Feature in deiner App wiederholt. Um Superpowers zu installieren, auch wieder einfach den Browser-Link hier oben kopieren und einfach Claude geben und sagen, er soll es installieren. Du kannst übrigens hier auch unter dem Slash und dann hier bei Manage Plugins sehen, welche Plugins du hier bereits installiert hast, und diese kannst du dann noch aktivieren. Du kannst ja auch andere Plugins installieren, hier z.B.

**37:58** · Frontend-Design. Und ich sehe jetzt das Superpowers-Plugin, das ist aktiv. Und ich werde ihm mal kurz eine Anfrage stellen, dass er hier was baut, damit du siehst, was Superpowers genau macht. Und zwar soll er jetzt einfach ein Freelancer-CRM-System erstellen mit allen Funktionen, die so ein CRM-System braucht. Sehr basic Prompt, ich weiß.

**38:14** · Aber wenn ich das jetzt abschicke und ich habe ihn jetzt hier nicht in den Plan-Modus gepackt, dann nutzt er hier den Brainstorming-Skill als Erstes, um meine Anforderungen zu definieren.

**38:23** · Verwende Brainstorming, um das Freelancer CM systematisch zu designen.

**38:27** · Und wir sehen wir hier seine To-Dos. Er schaut sich zuerst unser Projekt an, dann gibt er uns auch die Möglichkeit gleich visuell etwas zu sehen, was er vielleicht implementieren möchte. Dann fragt er noch mal ein paar Fragen, um wirklich zu verstehen, was wir wollen.

**38:38** · Er gibt uns hier auch wieder verschiedene Vorgehensweisen, zwischen denen wir dann wählen kann. Er präsentiert uns das Design und so weiter. Also wirklich wieder Feature Dev Skill, aber noch mal in einem größeren Umfang. Einiges von dem, was wir besprechen werden, lässt sich besser visuell zeigen, z.B. Mockups für das Dashboard, UI Layouts oder Architektudiagramme. Ich kann dir während des Brainstormings Entwürfe im Browser anzeigen. Das Feature ist noch neu und kann tokenintensiv sein.

**39:01** · Möchtest du es ausprobieren? Ja. Und was er jetzt gemacht hat, er hat eine Seite erstellt, wo er jetzt gleich verschiedene Visualisierungen hochladen wird von meiner App. Er stellt er mir noch mal ein paar Fragen erstmal über meine App. Er fragt mich auch, welche CRM Module mir am wichtigsten sind. Und man merkt einfach, es ist noch mal viel mehr Austausch, also er stellt viel mehr Fragen als standardmäßig im Planmodus.

**39:22** · Wie soll die Authentifizierung funktionieren? Und dann fragt er mich, wie soll das UI Design aussehen? Schau mal im Browser nach, ich zeige dir drei Stilrichtungen. Denn oftmals ist es schwierig zu verstehen, was für ein Designer implementieren möchte anhand einer Textbeschreibung. Und wenn ich jetzt den Browser öffne, sehe ich drei Stilrichtungen. Wie cool ist das bitte?

**39:39** · Einmal so ein clean und minimalistisches Design, dann hier so dark und professional oder hier colorful and friendly. Und jetzt kann ich natürlich viel besser verstehen, wie es dann am Ende aussieht. Und ich möchte z.B. jetzt hier dark und professional. Und wenn wir jetzt hier im Terminal arbeiten würden, dann könnte man das auch einfach anklicken und dann würde das sofort merken, aber hier in dem VS Code Plugin muss ich ihm noch mal explizit sagen, dass es dark und professional sein soll.

**40:01** · Dann gibt er mir hier so ein Architekturansatz und eine Zusammenfassung und ich kann einfach jetzt sagen, ob mir der Ansatz, den er hier beschreibt, gefällt oder nicht oder ob er was anpassen soll. Mir gefällt der. Er präsentiert mir dann auch das Datenmodell. Und ich kann für jede einzelne Sache, die er sich jetzt hier überlegt, auch immer direkt Feedback geben, also z.B. jetzt auch zum Datenmodell. Das heißt, wenn du deine eigene App bauen möchtest, dann probier unbedingt Superpowers als Plugin aus.

### 10 CLAUDE.md Management Plugin

**40:23** · Kommen wir zum letzten Plugin und das ist auch eins von Anthropic, nämlich dem Claude MD Management Plugin. Die Claude MD Datei ist eine spezielle Datei in deinem Projektordner, die Claude immer in sein Gedächtnis lädt. Das heißt, die Informationen, die dort enthalten sind, fungieren so ein bisschen wie ein Systemprompt, den er immer wieder bekommt. Das heißt, dort sollten natürlich nur Informationen enthalten sein, die wirklich sehr wichtig sind und immer gelten. Und die meisten Leute erstellen einmal so eine Claude MD Datei und fassen sie danach nie wieder an, aber dein Projekt verändert sich ja im Laufe der Zeit.

**40:51** · Das heißt, es kommen vielleicht neue Anforderungen dazu, neue wichtige Regeln, die beachtet werden sollen oder bestimmte Probleme, auf die man achten sollte. Und dieses Plugin kann man dafür nutzen, um diese Claude MD Datei eben zu pflegen, zu aktualisieren, neue Erkenntnisse zu erfassen. Und das Plugin gibt dir zwei Funktionen, erstmal eine Auditfunktion, das sagt einfach, "Prüfe alle meine Claude MD Dateien oder ist meine Claude MD Datei noch aktuell?" Und Claude durchsucht dann deinen Ordner nach allen Claude MD Dateien, bewertet sie anhand von Qualitätskriterien, also ob z.B.

**41:22** · wichtige Befehle drin sind, wichtige Regeln und ganz wichtig, ob das Ganze auch kompakt genug ist. Denn eine Claude MD Datei sollte nicht ewig lang sein.

**41:30** · Und zusätzlich gibt es auch noch hier so einen revise Claude MD Befehl, den du am Ende deiner Sitzung nutzen kannst, um deine Claude MD Datei mit den neuesten Erkenntnissen aus der Sitzung zu aktualisieren. Und die Claude MD Datei wird natürlich nicht automatisch einfach verändert, sondern die Änderungen werden dir erstmal angezeigt und du kannst dann entscheiden, "Ja, mach das." oder "Mach das nicht." Und das heißt, man hat also eine Prüffunktion, ob die Claude MD Dateien noch aktuell sind und auch wirklich gut und kompakt geschrieben sind. Und man hat eine Methode, um nach einer Session seine neuen Erkenntnisse in der Claude MD Datei zu speichern.

**41:57** · Das heißt, wenn du deine Claude MD Datei etwas besser managen möchtest, über ein längeres Projekt hinweg z.B., dann nutz unbedingt dieses Plugin. Das war's auch schon mit dem Video. Es war ein etwas längeres Video, aber ich hoffe, du konntest vielleicht ein oder zwei Plugins für dich entdecken, die du jetzt auch für deine Projekte vielleicht nutzen möchtest. Ich finde die alle extrem nützlich und benutze auch viele davon in meinen eigenen Projekten. Falls dir das Video gefallen hat und dir weiterhelfen konnte, dann würde ich mich sehr darüber freuen, wenn du ein Like und auch ein Abo da lässt.

### Outro

**42:22** · Und falls dich das Thema KI-Automatisierung und Cloud Code wirklich interessiert und du es auch im Business-Kontext einsetzen möchtest, dann kannst du natürlich auch in meiner Community vorbeischauen. Hier behandeln wir das Thema, wie gesagt, deutlich intensiver, auch Themen wie n8n, Self-Hosting, DSGVO und du kannst dir ein sehr gutes Netzwerk Unternehmern und Selbstständigen in dem Bereich aufbauen. Link dazu findest du in der Videobeschreibung. Ich würde sagen, wir sehen uns dann beim nächsten Video wieder und bis dann.