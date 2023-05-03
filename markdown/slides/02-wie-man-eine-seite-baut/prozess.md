---
title:
- Wie man eine funktionierende Seite baut
theme:
- Boadilla
---

# Ordnerstruktur
Angefangen wird mit der Ordnerstruktur in der man die anfangs zwei genutzten
Dateinen richtig abspeichern muss, sonst funktioniert auch der Rest nicht.

```
Ueberordner (Beliebiger Ordner)
|
|-css (ordner)
| |-style.css
|
|-index.html
```

Die verlinkung in der Html datei muss dann sein wie folgt:
```Html
<link href="css/style.css" rel="stylesheet">
```
Hier sagt `<link>` das etwas verlinkt werden solle, `href` gibt einen Dateipfad
an der zeigt wo es ist und `rel` gibt der Html bekannt das es sich um einen Stylesheet handle.

# Weiterer aufbau
Jetzt wird die html in seiner Struktur aufgebaut, angefangen mit der groben Aussenstruktur:
```HTML
<!DOCTYPE html>
<html>
    <head>

    </head>

    
    <body>




    </body>
</html>
```

# head
Im head sind drei sachen:

- title
- meta
- link

`title`:

Im `title` steht was dann auch im Browser oben angezeigt wird 
```HTML
<title>Beispiel Titel</title>
```

In `meta` gibt man das Charset also was fuer ein encoding genutzt wird. Bei uns ist das fuer
ae, oe, ue (*hab die tasten hier grad nicht*) **UTF-8**. Also:
```HTML
<meta charset="UTF-8">
```
Zuletzt braucht man die verlinkung zum Stylesheet, wie erklaert weiter oben:

```Html
<link href="css/style.css" rel="stylesheet">
```

# Body
Im body ist alles, andere.

Also Text, Bilder...

Der Rest halt.

# CSS
## Klassen
Klassen definiert man wie folgt:
```CSS
.test-klasse {
        color: #fff;
    }
```

Der '.' sagt das eine Klasse folgt, welche man selbst definiert, es muss an
einem teil sein wenn man mehrere Woerter benutzt, also `'test-klasse'` und nicht
etwas wie `'test klasse'` (*mit Lehrzeichen statt '-'*).

Was die Klasse dann macht macht man in den geschwungenen Klammern `{}`, die
bekommt man mit `AltGr+7`..

## IDs
IDs sind fast gleich, besonders ist aber das man sie nur ein mal pro Seite benutzten darf.

Dann definiert man sie:
```CSS
#test-id {
    background-color: #000;
}
```

**Wichtig ist auch noch das man bei mehreren CSS attributen sie mit ';' voneinander trennen muss.**  

# Wie man es in HTML benutzt
## Klassen
```HTML
<body class="test-klasse">
    <p>
      Inhalt, der sich an die test-klasse haelt. <br>
      <em>wenn sie richtig definiert wurde</em> 
    </p>
</body>
```



## IDs
```HTML
<body id="test-id">
    <p>
      Inhalt, der sich an die test-id haelt. <br>
      <em>wenn sie richtig definiert wurde</em> 
    </p>
</body>
```

# Erweiterte Verlinkung:
Gegben:

```
HTML(Beliebiger Ordner)
|
|_css (ordner)
| |_style.css
|
|_html (ordner)
| |_sub-1.html
|
|-index.html
```

## Stylesheet in die sub-html:
Den Stylesheet kann man nun nichtmehr normal mit '`<link href="css/style.css" rel="stylesheet">`'
verlinken.

### Zum Vorstellen
`<link>` ueberhalb greift erst runter in den css Ordner, dann die css.

Aber die sub-1.html kann nach unten keine css greifen, sondern muss erst einen Ordner hoch greifen.
Das macht man mit `..` zu beginn des `href`:
'`<link href="../css/style.css" rel="stylesheet">`'




# extra
### Wo kann man sie benutzen?
**Klassen** und **IDs** kann man jedem Tag geben.

### Wie viele Klassen kann man benutzen?
So oft man will.
```HTML
<body class="klasse-1 klasse-2 klasse-...">
```
Das ist nuetzlich wenn man z.B. eine Klasse hat fuer eine Schriftfarbe, eine
fuer Hintergrundfarbe...

Das ist so wie in Frameworks wie Bootstrap, oder ist allgemein ganz praktisch
wenn man grosse websiten hat.





