---
title: "Soo kann jeder eine MacOS App bauen | Claude Code"
source: "https://www.youtube.com/watch?v=juNbNTutOJU"
author:
  - "[[Dennis Jan Vogt]]"
published: 2025-09-12
created: 2026-06-20
description: "In diesem Video zeige ich dir, wie ich mit Cloud Code und Electron eine eigene macOS App gebaut habe – und zwar einen Time Tracker, mit dem man seine Arbeitszeit super easy erfassen kann. ⏱️💻👉 Das"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=juNbNTutOJU)

In diesem Video zeige ich dir, wie ich mit Cloud Code und Electron eine eigene macOS App gebaut habe – und zwar einen Time Tracker, mit dem man seine Arbeitszeit super easy erfassen kann. ⏱️💻  
  
👉 Das Video ist perfekt für dich, wenn du:  
• lernen willst, wie man mit Electron Desktop-Apps erstellt  
• wissen möchtest, wie man Cloud Code für AI-gestützte Entwicklung nutzt  
• Inspiration für deine eigenen Productivity Tools suchst  
  
Wir gehen Schritt für Schritt durch den Prozess:  
1\. Electron Setup für macOS  
2\. Nutzung von Cloud Code für schnellen Code-Flow  
3\. Umsetzung des Time Tracker mit moderner UI  
4\. Erste Tests & Packaging für macOS  
  
Am Ende hast du nicht nur eine fertige App, sondern auch ein Gefühl dafür, wie stark Cloud Code in Kombination mit Electron deine Dev-Produktivität pushen kann. 🚀  
  
#Electron #ClaudeCode #MacOS #AppDevelopment #TimeTracker #ProductivityApps #CodingTutorial #AIcoding #JavaScript #DevWorkflow

## Transcript

**0:00** · So, hallo willkommen zu einem weiteren Video hier auf diesem Channel. Heute möchte ich mit euch eine MacOS App bauen und dies mit Cloud Code. Ich habe mir, glaube ich, zur persönlichen Aufgabe gemacht, euch Cloud Code bzw. alle Art von Agenten näher zu bringen, damit ihr auch davon profitieren könnt, weil es ist wirklich eine Art von Magie, wenn sie funktionieren. Das ist noch mal eine andere Sache. Cloud Code hatte beispielsweise jetzt eine Schwankung.

**0:23** · Ähm, aber Cloud Code ist wieder voll zurück und kann gefühlt alles programmieren. Im Hintergrund seht ihr z.B. auch eine App, die ich gebaut habe und das war jetzt mit Jengo HTML, CSS JavaScript, also relativ basic für mich, sage ich mal, äh mit recht coolen Funktionalitäten, z.B. hier dies kann man Board da kann man sich z.B.

**0:42** · irgendwelche Tod-Doos anlegen, wie irgendwie YouTube Video machen und hat das dann hier im Backlog, dann im Tod-Do und so weiter und so fort. Also im Business wird das so teilweise genutzt, um halt ähm ja Aufgaben zu tracken und ich dachte mir, ich hätte das gern vielleicht noch mal integriert in meinem MacOS und das habe ich dann einfach gemacht und jetzt habe ich hier rein theoretisch auch so ein Board und kann dann sagen hier auch irgendwie YouTube Video, erstellen und kann einfach tracken, was ich gerade heute oder sonst wann machen möchte.

**1:13** · Es ist wirklich cool und ich möchte euch wirklich einfach zeigen, wie ihr es selber machen könnt und mit Cloud Code ist es relativ trivial. Heute habe ich mir für das Video vorgenommen oder für uns einmal hier diese Timetracker App zu äh zu programmieren, um einfach zu zeigen, wie es funktioniert. Ähm vielleicht ist es für den einen interessant zu wissen, wie lange irgendwelche Aufgaben am Computer gedauert haben.

**1:33** · In meinem Kontext ist es relevant, weil dann ich darauf halt Abrechnung stelle in dem Sinne. Äh, auch für den einen oder anderen das ist vielleicht einfach nur interessant zu sehen, wie lange er wirklich am am Computer Zeit verbringt oder sonstiges und das dann direkt integriert zu haben im eigenen Mac, wenn ihr ein Mac habt, ist einfach cool. Ähm, es wird vielleicht nicht alle von euch heute interessieren. Die einen nutzen vielleicht eher Windows, die anderen Linux, aber das Tool, was wir verwenden, kann rein theoretisch für alle Plattformen Apps ja erstellen, rändern, wie auch immer. Wir nutzen nämlich heute Elektron.

**2:05** · Bedingung für Elektron ist, dass Node J installiert ist. Ist allgemein auch eine Bedingung für Cloud Code, weil Cloud Code in der Regel installiert wird mit Node GS als Package. Dementsprechend, wenn ihr das noch nicht habt, geht gerne auf die Seite, installiert es. Es ist relativ triviales runterzuladen, installieren, gar nichts Schwieriges. Wenn ihr doch irgendwie Hilfe braucht, schreibt mir gerne in die Kommentare. Ich helfe euch natürlich gerne. Wenn ihr noch mal ein separates Short wollt oder ein Video wollt, wie man DS installiert, schreibt mir auch in die Kommentare. Und das gleiche auch zu Cloud Code.

**2:35** · Bei Cloud Code bin ich immer überlegen, eine separate ähm Videoreihe noch mal dazu machen, wie man das richtig verwendet.

**2:43** · Kommt, denke ich auch noch, aber eins nach dem anderen. Wie gesagt, wir verwenden heute Elektron bzw. Also Cloud Code wird heute Elektron für uns verwenden, um unsere MacOS App zu bauen.

**2:52** · Das ist einfach so eine Art von ja Engine Framework, das einmal die Chromium AP bzw. das Chromium Engine nutzt, also so das die gleiche Engine, auf der auch Google Chrome und Microsoft Edge aufgebaut ist. Zugleich dann halt auch HTMLCS ist ein JavaScript, was das Ganze deutlich lesbarer und einfacher macht. Wir müssen da gar nicht so tief rein. Das ist gar nicht ein Tutorial diesbezüglich, sondern eher bezüglich Code Clode Cloud Code.

**3:19** · Das wird das heute verwenden. Ich wollte euch noch mal zeigen, was wir heute benutzen. Dementsprechend gehen wir direkt rein und lassen mal unseren Timetracker implementieren von Cloud Code, damit ich hier neben dieser App noch eine weitere App habe und wir legen los. So, wir befinden uns an einem ja vertrauten Ort, würde ich sagen, und zwar wie ist Code. Habt ihr wahrscheinlich auch in meinem letzten Video schon gesehen, wenn ihr es schon gesehen habt. Wenn nicht, checkt gerne noch mal ab. Ähm, und ich habe Cloud Code auch schon geöffnet in meine ID.

**3:47** · Dafür nutze ich auch hier diesmal wieder die Cloud Code Extension, weil damit Cloud Code noch mal ein bisschen ja stabiler, besser läuft, wie auch immer.

**3:54** · Ich habe ein komplett leeres Projekt, also ein leeren Ordner und wir geben Cloud Code einfach mal die Anweisung, die wir haben wollen. Ich nutze auch hierfür wieder Super Whisper, um halt über eine Spracheingabe das Ganze zu sagen, weil ich finde Prompting über eine Spracheingabe ist noch mal deutlich einfacher, weil man viel mehr Kontext mitgeben kann, weil sprechen geht einfach tendenziell immer noch schneller als schreiben. So, dementsprechend jetzt muss ich mir ein paar Gedanken machen und ich fange mal an.

**4:18** · Also, erstelle ein Pro äh Product Requirements Document bezüglich einer MacOS App, die du mit Elektron baust. Ziel dieser App ist ist, dass ich sie oben rechts in der ähm NAFB habe vom Macos, unten aber nicht auftauchend in der normalen Tableiste.

**4:46** · Ich möchte mit ihr meine Zeiten tracken.

**4:49** · Das heißt, ich muss einen Timer haben, den ich starten, stoppen und pausieren kann. Ich muss natürlich dann auch eintragen können, was ich zu dem Zeitpunkt gemacht habe. Möglicherweise wären Kategorien auch gar nicht mal so schlecht.

**5:04** · Und ich muss natürlich auch diese Zeiten einsehen können, vielleicht auch exportieren können. Also wäre ein übersichtliches und großes und gutes Fenster relativ schön zu sehen.

**5:15** · Ähm macht dir ausführliche Gedanken und erstelle mir am Ende dann auch die App, die ich dann installieren kann für mein Macgerät.

**5:26** · So, ist jetzt bearbeitet. Jetzt haben wir hier den gepasteten Text und jetzt habe ich ein ganz großes Pro. ist beim letzten Mal auch schon aufgefallen, dass ich teilweise da irgendwie dann so ein paar Fehler habe. Also wie gesagt, am Ende läuft da auch, ich weiß gar, ob es ein LM ist oder Model hinter, ich glaube, es ist sogar das Whisper Modell von Open AI ähm, das dann das einmal rum rändert, also von Speech to Text und das einmal reinschreibt.

**5:49** · Potenziell potenziell tendenziell ist Cloud, aber ja, Cloud Code relativ gnädig, was auch dann teilweise mal so Schreibfehler angeht oder sonstiges. Set hat mich eigentlich immer noch gut relativ gut verstanden. So für die, die Cloud Code nicht kennen, er hat jetzt zunächst einmal eine Liste erstellt. Ich habe jetzt gar nicht den ähm den den Planmodus benutzt. Normalerweise benutzt man auch den Planmodus, um einen größeren Plan zu machen. Aktuell bin ich aber so confident mit Cloud Code, dass ich ihm vertraue, dass er das locker in einem One Shot komplett abreißt und wir am Ende ein fertiges Produkt haben.

**6:21** · So, er fragt mich hier natürlich dann noch mal nach ähm Berechtigung, ob er dann auch Dinge erstellen kann, wie beispielsweise hier dieses Markt Document. Jetzt ist er sogar schon fertig mit seinem gesamten Plan. Hat hier sogar so ein Dropdown Übersicht, wie das ganze Fenster überhaupt aussehen soll. Erstellt. Mega cool. Und jetzt fängt das schon an zu programmieren und frag mich halt auch wieder nach den einzelnen Berechtigungen. Ich klick das einmal ein bisschen durch und wir sehen uns wieder, wenn er einmal durch ist und dann gucken wir direkt d mal, ob irgendwelche Bugs existieren.

**6:51** · Dementsprechend bis jetzt zum fertigen Produkt. So, da sind wir auch schon wieder. Für euch hat's jetzt vielleicht 2 Sekunden gedauert, für mich ungefähr 10 Minuten und ich möchte mit euch direkt den Live Test machen, ob alles auch so funktioniert hat, wie ich es mir am liebsten gewünscht hätte zum Beginn.

**7:07** · Und zwar er ist fertig, er ist auch komplett durchgelaufen, er hat keine Fehler geschmissen oder sonstiges, was ja schon mal super ist. So und er sagt uns, dass er jetzt hier eine DMG Installation vorbereitet hat und zwar im Ordner Bild. Und jetzt haben wir hier ICons hat er auch erstellt hier. Das öffnen wir einmal im Feinder.

**7:27** · Der ist auf der hier haben wir das da.

**7:30** · Doppelklick und dann haben wir unten, guck mal sogar mit Logo und allem drum und dran. Für die, die Mac nicht kennen, man muss das man installiert Apps, indem man sie in diesen Applications Ordner reinzieht. Okay. Genau. Und dann sind die tendenziell auch schon installiert.

**7:46** · Geht verrückt schnell. Und wenn ich jetzt den Timcker nicht den so den Timetracker einmal öffne, dann kriege ich einmal Developer Tools.

**7:59** · Das wollte ich nicht haben, aber wir haben hier oben in der Leiste einen Timetracker. Verrückt oder?

**8:08** · Jetzt hat sich das war will mal kurz hier den anderen Hintergrund packen. So, dann noch mal hier auf den Timetracker und jetzt starten wir ihn mit der Aufgabeneschreibung zufügen. Kein Problem. ähm YouTube Video machen für MacOS. Wir starten das Ganze. Ist es Arbeit? Ja, tendenziell. Können auch hier scrollen. Haben die Einträge, wir haben Einstellungen, die können wir jetzt gerade nicht betätigen. Hier Tracker Übersicht. Hier hat sich noch ein Popup geöffnet. Crazy. So, Moment, wir gucken ein mal hier. Der Tracker läuft gerade. Ist ja gerade grün.

**8:38** · Ich drücke mal auf Pause. Ist immer noch grün, aber der Tracker läuft nicht weiter.

**8:46** · Und ich drücke mal fortsetzen. Und ich drück Stopp. Und dann haben wir hier unten unseren Eintrag. Ich klick mal drauf. Passiert nichts. Ich gucke mal hier aufs Fenster. Hier passiert auch nichts. Okay, aber das ist jetzt schon mal, also es ist in Ordnung, würde ich sagen. Wir haben hier zumindest unsere Liste mit dem, was wir sehen. 0 Minuten, das passt auch. Einstellung haben wir noch nicht. Okay, teilweise UI Elemente integriert. die wir aber noch nicht nutzen können.

**9:11** · Das heißt, in den nächsten Schritten wir jetzt hingehen und sagen, okay, ähm überarbeite mir die Liste hier vielleicht noch einmal, weil das ein bisschen groß ist von diesen einzelnen Kachen her Kacheln her. Ähm, dann überarbeite ich hier diese Ansicht noch mal, weil theoretisch möchte er, glaube ich, hier drin so eine Liste auföffnen. Ähm, funktioniert aber noch nicht, kann aber gerne noch mal überarbeiten. Was ich aber cool finde, ist, dass er hier automatisch auch hier dieses Icon erstellt hat. Ähm, wir haben hier unten auch in der Leiste. Okay, hier hat er noch das dann geöffnet. Das möchte ich nicht haben.

**9:40** · Das habe ich bei dem anderen auch ausgestellt und ja, aber das also beispielsweise das hat er auch selbständig erstellt. Also ich finde, das ist gefühlt reinste Magie und wir haben halt nur einen Befehl abgesendet. Es ist verrückt. Also ich bin hart beeindruckt, wie einfach es heutzutage geht, gefühlt so eine App zu entwickeln. Natürlich ist sie jetzt nicht direkt irgendwie deliverable und keine Ahnung was und Production ready und verkaufen und hast du nicht gesehen, aber mal für sich selber so eine kleine App bauen, wie auch beispielsweise hier dieses Kanmanboard, das schon verrückt.

**10:11** · Also es ist schon schon fast zu einfach, schon fast ein Cheat Code diese Agents heutzutage. Ich hoffe, euch hat das Video gefallen. Moment, ich mache noch mal hier diesen klassischen Wo ist mein OBS? Ich ma mich noch mal klassischerweise ein bisschen größer.

**10:23** · Ah, warte mal Sekunde.

**10:26** · So, genau. Ich hoffe euch hat das Video gefallen. Lass mir gerne ein Like und ein Abo da und wir sehen uns beim nächsten Mal wieder, wenn ich euch weiterhin Cloud Code andere Agents oder sonstiges schmackhaft machen möchte.

**10:35** · Macht's gut. Bis zum nächsten Mal und ciao.