from Card import *


# Initialization


def initialize_stack():
    stack = []
    stack += (Card("Big Daddy", "Deine Kugel wird zu Big Daddy.",
                    """Die Kugel, die in
                    diesem Zug auf dem Aktionsfeld gelandet
                    ist, wird zu Big Daddy. Tausche
                    die Kugel mit der Big Daddy Kugel.
                    Die Kugel behält den Status so lange
                    bis eine andere Kugel zu Big DaddyA
                    wird. Big Daddy kann nicht von einem
                    gegnerischen Spieler getauscht werden.
                    Wer auf dem selben Feld wie Big Daddy
                    landet schickt nicht Big Daddy in den
                    Zwinger zurück, sondern sich selbst.
                    Big Daddy kann Barrieren überlaufen.
                    Er darf jedoch nicht auf dem
                    selben Feld landen und eine Barriere
                    nicht mit einer 7 überlaufen. Big
                    Daddy kann in seinem Haus Kugeln
                    überlaufen. Big Daddy ist immun
                    gegenüber Effekten von Aktionskarten
                    gegnerischer Spieler (mit Ausnahme
                    der Karte Mutz und Schwiegermutter).""", 12))
    stack += (Card("Mutz", "Schicke Big Daddy in den Zwinger.",
                    """Big Daddy wird nicht
                    in den Zwinger geschickt, wenn er
                    bereits im Haus angekommen ist. Die
                    Kugel bleibt Big Daddy, wenn sie
                    nach Hause geschickt wird.""", 1))
    stack += (Card("Who’s your Daddy", "Big Daddy zieht jedem Spieler eine Karte. Diese muss im nächsten Zug gespielt werden.",
                    """Big Daddy
                    zieht jedem Mitspieler eine Karte.
                    Jeder Mitspieler legt die gezogene
                    Karte offen vor sich hin. Im nächsten
                    Zug muss diese ausgespielt werden. Es
                    dürfen keine Aktionskarten gezogen
                    werden. Tandem darf nicht zusammen
                    mit der offenen Karte gespielt
                    werden. Hat ein Spieler keine Karte
                    mehr, passiert ihm nichts. Ist zu diesem
                    Zeitpunkt niemand Big Daddy,
                    passiert nichts.""", 2))
    stack += (Card("Auge um Auge", "Würfle. Laufe soviele Einzelschritte vorwärts oder rückwärts.",
                    """Du darfst entscheiden,
                    ob du vorwärts oder rückwärts
                    gehen willst. Wird Big Daddy
                    oder eine Barriere getroffen, muss
                    deine Kugel in den Zwinger zurück.""", 2))
    stack += (Card("Chuehandel", "Tausche eine Karte mit deinem Partner.",
                    """Du und dein Partner
                    legen eine Karte verdeckt vor ihren
                    Partner. Diese Karte darf erst aufgenommen
                    werden, wenn beide Spieler
                    eine Karte gelegt haben. Hat einer der
                    betroffenen Spieler keine Karten mehr,
                    wird nicht getauscht.""", 4))
    stack += (Card("Frühgeburt", "Bewege eine Kugel von dir und deinem Partner vom Zwinger auf das Startfeld.",
                    """Die Aktion muss
                    durchgeführt werden, sofern ein Spieler
                    deines Teams eine Kugel im Zwinger
                    hat. Wenn bereits eine Kugel auf
                    dem Startfeld ist, muss diese zurück
                    in den Zwinger. Ist diese Kugel Big
                    Daddy, passiert nichts.""", 4))
    stack += (Card("Hot Swap", "Würfle. Tausche deine Kugel mit der x-ten Kugel in Spielrichtung.",
                    """Bei einer Eins tausche
                    deine Kugel mit der nächsten Kugel in
                    Laufrichtung. Bei einer Zwei die Übernächste.
                    Geschützte Kugeln werden
                    nicht mitgezählt. Wird Big Daddy
                    getroffen, passiert nichts. Wird deine
                    eigene Kugel, die in diesem Zug auf
                    dem Aktionsfeld gelandet ist, getroffen,
                    muss diese in den Zwinger zurück.""", 2))
    stack += (Card("Ice Age", "Würfle. Friere die x-te Kugel ein.",
                    """Bei einer Eins friere die
                    nächste Kugel in Laufrichtung ein.
                    Bei einer Zwei die Übernächste. Wird
                    Big Daddy getroffen, passiert nichts.
                    Eine gefrorene Kugel kann sich nicht
                    selbst bewegen. Die Kugel kann nicht
                    getauscht werden. Der Effekt wird
                    aufgehoben, sobald die Kugel überholt
                    oder nach Hause geschickt wird,
                    spätestens aber am Ende der Runde.""", 2))
    stack += (Card("Kommunismus", "Die Spieler des gegnerischen Teams müssen gleichviele Kugeln auf dem Spielfeld haben.",
                    """Beide gegnerischen
                    Spieler müssen gleichviele
                    Kugeln auf dem Feld haben. Kugeln
                    im Haus oder im Zwinger zählen
                    nicht. Der Spieler mit mehr Kugeln
                    muss soviele seiner Kugeln in den
                    Zwinger schicken, bis er gleichviele
                    auf dem Feld hat wie sein Partner. Der
                    Spieler darf selbst entscheiden, welche
                    seiner Kugeln er wählt. Big Daddy
                    kann auf diese Weise nicht in den
                    Zwinger geschickt werden.""", 2))
    stack += (Card("Putzfrau", "Räume dein Haus und das deines Partners auf.",
                    """Bewege alle Kugeln
                    in deinem Haus soweit nach vorne
                    wie möglich. Auch Big Daddy darf
                    bewegt werden.""", 4))
    stack += (Card("Raucherpause", "Nimm diese Karte auf die Hand. Spiele sie, um eine Runde auszusetzen.",
                    """Diese Karte ist
                    jetzt eine Handkarte. Sie kann allerdings
                    weder getauscht noch gezogen
                    werden. Wird die Karte bis am Ende
                    der Runde nicht ausgespielt, verfällt
                    der Effekt und die Karte muss abgegeben
                    werden.""", 3))
    stack += (Card("Richtungswechsel", "Spiel- und Laufrichtung werden gewechselt.",
                    """Die Richtung,
                    in welcher die Spieler eine Runde
                    beginnen, wird auch geändert. Dies
                    kann dazu führen das manche Spieler
                    mehr Karten haben als Andere.""", 7))
    stack += (Card("Schwiegermutter", "Bringe Unordnung in die Häuser deiner Gegner.",
                    """Bewege alle
                    Kugeln in den Häusern deiner Gegner
                    soweit nach hinten wie möglich. Auch
                    Big Daddy darf bewegt werden.""", 2))
    stack += (Card("Tandem", "Nimm diese karte auf die Hand. Spiele sie mit einer Karte, um diese auch auf deinen Partner anzuwenden.",
                    """Diese Karte ist jetzt eine
                    Handkarte. Sie kann weder getauscht
                    noch gezogen werden. Wird die Karte
                    bis zum Ende der Runde nicht ausgespielt,
                    verfällt der Effekt und die
                    Karte muss abgegeben werden. Wenn
                    du die Karte ausspielst, bestimmst du
                    den Spielzug für deinen Partner.""", 4))
    stack += (Card("Tornado", "Alle Handkarten werden neu verteilt.",
                    """Der Spieler, der die
                    Aktionskarte gezogen hat, sammelt
                    die Handkarten aller Spieler ein. Er
                    mischt die Karten und verteilt sie neu,
                    beginnend beim Spieler rechts von
                    ihm. Hat ein Spieler seine Karten bereits
                    abgeworfen, bekommt er trotzdem
                    neue Karten.""", 1))
    stack += (Card("Towanda", "Alle nicht geschützten Kugeln müssen in den Zwinger.",
                    """Eine Kugel ist geschützt,
                    wenn sie Big Daddy ist, eine
                    Barriere bildet oder im Haus ist. Eine
                    Kugel ist nicht geschützt, wenn sie
                    eingefroren ist.""", 1))
    stack += (Card("Weihnachten", "Alle Spieler geben eine Handkarte in Spielrichtung weiter.",
                    """Aktionskarten
                    können nicht weitergegeben werden.
                    Wer keine Karten mehr hat erhält
                    trotzdem eine Karte, muss aber keine
                    weitergeben.""", 3))
    return stack