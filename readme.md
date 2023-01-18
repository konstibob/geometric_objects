# Zeichentool

Eine Ansammlung von Programmen, die die Erstellung von Polygonen, Rechtecken und Kreisen in einem Koordinatensystem ermöglichen

## Installationanweisung

Für dieses Projekt sind die Module math und unittest, sowie python notwendig.  

## Ausführung

Das Projekt wird ausgeführt, indem man die main Datei ausführt.

```
python3 main.py 
```

Um die TestCases auszuführen, die sich im test.py befinden, muss man stattdessen 

```
python3 test.py 
```

Ausserhalb des lib Ordners ausführen

## Aufbau

![Alt text](images/UML.png?raw=true "UML Diagramm")

Man beachte, dass alle Funktionen und Attribute Public sind, da man diese in Python im Vergleich zu anderen Objekt Orientierten
Programmiersprachen nicht einschränken kann

Das Projekt ist in 6 Dateien aufgeteilt, von welchen 2 (test.py und main.py) zur Ausführung des Codes gedacht sind.

Die andern Dateien repräsentieren Klassen, die unten beschrieben werden. 

### Vector 

Die Klasse 'Vector' repräsentiert einen Vektor im 2D-Raum. Sie enthält Methoden zur Berechnung des Normalenvektors, des Skalarprodukts, der Länge und der Normalisierung.

### Projection 

Die Klasse 'Projection' repräsentiert die Projektion eines Objekts auf eine bestimmte Achse. 
Sie enthält Methoden zur Bestimmung des minimalen und maximalen Werts der Projektion auf der Achse, 
was hilft zu bestimmen, ob es einen Überlappung gibt oder nicht.

### Forms

In dieser Implementierung gibt es mehrere Objekte: 

Während es bei Kreisen, Polygonen und Rechtecken um Objekte handelt, die man erstellen kann,
handelt es sich bei 'Shape' um eine abstrakte Klasse, von der man keine Objekte erzeugen sollte. 
Diese habe ich dabei gewählt, damit alle Objekte (Polygon, Kreis aber auch Rechteck) auf die 
wichtigen 'Collision' und 'Project' Funktionen Zugreifen können.

### Koordinatensystem

Das Koordinatensystem dient dazu, Objekte auf diesem platzieren zu können. Es trackt die Objekte, kann 
aber auch prüfen, welche Objekte sich mit anderen Objekten überlappen und welche nicht.


## Anforderungsbestimmung und Designentscheidungen

```
a) Dafür gilt es, eine Klasse für das Koordinatensystem zu erstellen. Dieses muss Parameter wie maximale X und Y
Auslenkung und eine Liste von geometrischen Objekten innerhalb des Koordinatensystems
beinhalten.
```

Diese Teilaufgabe habe ich geschafft, da Klasse 'Coordinates' alle variablen 
wie min_x, max_x aber auch add_obj() und remove_obj(). 

```
b.) Geometrische Objekte sollen eine Klasse darstellen. Als geometrische Objekte sollen
zumindest Rechtecke und Kreise definierbar sein. Dabei empfiehlt es sich diese als
Unterklassen zu definieren

und 

b+.) Als optionale Aufgabe kann zusätzlich ein Polygon definiert werden. Dabei ist darauf zu
achten, ob es sinnvoll ist, die Anzahl der „Ecken“ zu beschränken.
```

Wir haben Klassen wie 'Rectangle' und 'Circle', aber auch 'Polygon'.

```
c.) Geometrische Objekte sollen einem Koordinatensystem mithilfe einer Funktion hinzugefügt
oder entnommen werden können. Außerdem soll es eine Funktion geben, die für die aktuelle
Liste von Objekten bestimmt, ob sich diese überlappen. Zusätzlich sollen die Objekte
ausgegeben werden, die die Bedingung verletzen. Es ist zu überlegen wie für den Nutzer die
geometrischen Objekte eindeutig identifizierbar gemacht werden kann.
```

Entnehmen und hinzufügen in das Koordinatensystem: 
Die Funktion overlap() habe ich hingegen nicht in der 'Coordinates' Funktion programmiert, da dies gegen das Prinzip der Objektorientierung sprechen würde. Es ergibt mehr Sinn für ein Objekt A zu prüfen, ob dieses sich mit Objekt B überschneidet, als dass das Koordinatensystem macht.

Die get_overlap Funktion in 'coordinates' gibt alle Elemente im Koordinatensystem zurück und gibt an, welche sich davon überlappen
und welche nicht, während Ich die Methode genommen habe die Objekte eindeutig identifizierbar zu machen, indem der Nutzer jedem Objekt einen Namen zuweist, und vom Koordinatensystem geprüft wird, ob dieser eindeutig ist.

```
d.) Für jede Operation ist zu prüfen, ob alle Vorbedingungen der Operation gegeben sind.
Objekte außerhalb des Koordinatensystems sowie entfernen von nicht existenten Objekten
sollten vermieden werden, ohne dass die Ausführung des Programms unterbrochen wird.
Hilfreiche Fehlermeldungen sind an dieser Stelle sinnvoll
```

Es wurden alle mir erdenklichen Fehlermeldungen eingebaut, inklusive der Fehlermeldung, falls ein Objekt sich
außerhalb des Koordinatensystems befindet. Dabei wurden nicht bei allen Fehlermeldungen die Ausführung eines Programmes nicht unterbrochen, da dies oft ansonsten keinen Sinn machen würde. 

Wenn wir bsp. bei einem Viereck mehr x als y Koordinaten haben, halte ich es für falsch eine beliebige Koordinate einzusetzen und einfach durch ein print auf den Fehler aufmerksam zu machen. Stattdessen habe ich einen Error Gerauised

## Separating Axes Theorem

Das Schwierigste an dieser Aufgabe war zu überlegen, wie genau man prüft, ob zwei Objekte sich überschneiden. Vorerst hatte ich 
es mit Punkten versucht, aber schnell gemerkt, dass Vektorrechnung hier sinnvoll ist und deshalb eine Vektoren klasse implementiert. 

Die Idee des Separating Axes Theorem, welcher für zwei beliebige Polygone löst, ob diese sich Überschneiden, ist , dass wir 
prüfen, ob man eine Grade durch die zwei Polygone ziehen könnte. 
Wenn dies geht, heißt dies, dass diese getrennt sind. 

1 Schritt: nehme von jeder Kante der beiden Polygone eine Senkrechte (im 90° Winkel) und speichere alle diese neue Kanten.

2 Schritt: Projiziere beide Figuren auf jede von diesen neuen Kanten. 
Dafür wird bei einem Polygon jeder einzelne Punkt auf die Achse projiziert, wobei die Projektionsfläche dem Punkt am weitesten
links bis zu dem Punkt am weitesten rechts auf der Achse entspricht.

Bei einem Kreis geht man vom Mittelpunkt aus her nach jeweils links oder rechts in Richtung der Kante, auf die man projizieren will (parallel) und projiziert nur diese beiden Punkte.

![Alt text](images/Kreisprojektion.png?raw=true "Kreisprojektion ")

3 Schritt: Wenn auf einer von diesen Kanten es eine Lücke zwischen den beiden Projektionen gibt, heißt das, dass man eine Grade
zwischen die beiden Körper ziehen und die berühren sich nicht.

![Alt text](images/projection.png?raw=true "Lücke Zwischen zwei Polygonen")


### Probleme mit SAT

Es gibt jedoch auch bsp ein kleines Problem mit dem Separating Axes Theorem 

![Alt text](images/problem.png?raw=true "Problem")

Bei der oberen Abbildung kann man zwischen beide Polygone (wir nehmen an das untere ist auch ein Polygone) keine Grade durchziehen
dies ist insbesondere bei unserem Programm ein Problem, da unser Programm solche Polygone zur Konstruktion zulässt. 
Um sowas zu verhindern, müsste man einfach die Konstruktion von nicht Konvexen Polygonen verhindern oder ein andern Algorithmus  benutzen, falls eins der benutzen Polygone Konvex ist.

## Kontaktmöglichkeit 

konsti.bobenko@gmail.com

## Quellen

use pretty hyperlinks here

[Wiki](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)

[Separating_Axes](https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169)

[Separating_Axes_with_code](https://hackmd.io/@US4ofdv7Sq2GRdxti381_A/ryFmIZrsl?type=view)