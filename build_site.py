#!/usr/bin/env python3
"""Builds Additives' standalone 12-locale Help & Privacy static site (Docket Paper & Brine palette)."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://hayriodabas.github.io/additives-help"
CONTACT_EMAIL = "hayriodabas@gmail.com"
BUNDLE_ID = "app.klarwerk.additives"

CSS = """\
:root {
  color-scheme: light dark;
  --paper: #f4f1e8;
  --sheet: #fffdf7;
  --well: #ebe6da;
  --hair: #dad4c6;
  --ink: #151b19;
  --ink2: #58615d;
  --brine: #0b6459;
  --brine-wash: #d7ebe5;
  --marker: #f5cf45;
  --on-marker: #141a1a;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #111413;
    --sheet: #1a1e1d;
    --well: #242928;
    --hair: #2f3634;
    --ink: #efebe1;
    --ink2: #a6aeaa;
    --brine: #5bbfb0;
    --brine-wash: #183631;
    --marker: #f5cf45;
    --on-marker: #141a1a;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16.5px/1.64 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
.docket-rule-wrap {
  max-width: 780px;
  margin: 0 auto;
  padding: 20px 20px 0;
}
.docket-rule-heavy {
  height: 6px;
  background: var(--ink);
}
.docket-rule-thin {
  height: 1px;
  margin-top: 3px;
  background: var(--ink);
  opacity: 0.7;
}
main {
  max-width: 780px;
  margin: 0 auto;
  padding: 20px 20px 68px;
}
.kicker {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  background: var(--marker);
  color: var(--on-marker);
}
h1 {
  font-size: 36px;
  line-height: 1.12;
  font-weight: 700;
  margin: 12px 0 8px;
  letter-spacing: -0.015em;
}
.lede {
  font-size: 18px;
  color: var(--ink2);
  margin: 0 0 22px;
}
nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 20px;
  padding: 12px 0;
  border-top: 2px solid var(--ink);
  border-bottom: 1px solid var(--hair);
  margin-bottom: 28px;
  font-size: 14.5px;
  font-weight: 600;
}
a {
  color: var(--brine);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 3px;
}
h2 {
  font-size: 20px;
  line-height: 1.25;
  margin: 30px 0 12px;
  font-weight: 700;
}
.card {
  background: var(--sheet);
  border: 1px solid var(--hair);
  border-radius: 14px;
  padding: 16px 18px;
  margin: 12px 0;
}
.card h3 {
  margin: 0 0 6px;
  font-size: 16px;
  font-weight: 700;
}
.card p {
  margin: 0;
  color: var(--ink2);
}
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--sheet);
  border: 1px solid var(--hair);
  border-radius: 14px;
  overflow: hidden;
  margin: 12px 0 24px;
}
td, th {
  padding: 13px 16px;
  border-bottom: 1px solid var(--hair);
  text-align: left;
  vertical-align: top;
}
tr:last-child td { border-bottom: none; }
td strong { color: var(--ink); font-weight: 600; }
ol {
  padding-left: 20px;
  margin: 12px 0 24px;
}
li { margin: 10px 0; }
ul.langs {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
}
ul.langs li {
  margin: 0;
  background: var(--sheet);
  border: 1px solid var(--hair);
  border-radius: 12px;
  padding: 13px 16px;
}
footer {
  margin-top: 44px;
  padding-top: 16px;
  border-top: 1px solid var(--hair);
  font-size: 13px;
  color: var(--ink2);
}
"""

LOCALES = {
    "en-US": {
        "name": "English",
        "html_lang": "en",
        "app": "Additives: E-Number Decoder",
        "nav_help": "Help",
        "nav_privacy": "Privacy Policy",
        "nav_langs": "All Languages",
        "contact_title": "Contact",
        "contact_body": f'Questions, corrections, or feedback about Additives: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Updated November 25, 2026 · Additives ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Help & Reference Guide",
            "lede": "Read any food ingredient list on-device, highlight the additives you watch, and inspect EU labelling rules without accounts or tracking.",
            "steps_title": "How Additives Works",
            "steps": [
                ("Read an ingredient list", "Open the Read tab and point the camera at the ingredients line on a food package. Codes such as E330, E 129, or e120 and additive names are outlined live on the image. Tap Read this label for a full breakdown, or pick a photo or type/paste text."),
                ("Highlight what you watch first", "Open Watch For (Shelf or Read) to select up to three single E-numbers for free, or entire additive groups with Additives Pro. Watched items appear at the top of every report with a yellow marker."),
                ("Review EU labelling notices", "Beneath your watch list, the report lists statutory package statements such as sulphite allergen emphasis (10 mg/kg SO2), the six children's activity/attention colours (Reg. (EC) No 1333/2008 Art. 24 & Annex V), aspartame phenylalanine notice, >10% polyols notice, and codes no longer on the EU food additive list (e.g. E171 titanium dioxide, E128 Red 2G)."),
                ("Browse 339 EU E-numbers offline", "Use Look Up to browse by number range or functional class, search by code or name in 12 languages, and check EU status and EU-specified origins (such as insects, egg, or milk sugar). No scores or medical advice are shown."),
                ("Additives Pro (one-time purchase)", "Unlocks whole Watch For groups and unlimited single E-numbers, saving named readings on your device, side-by-side label comparison, favourites, and plain-text export."),
            ],
            "faq_title": "Frequently Asked Questions",
            "faq": [
                ("Does Additives upload package photos?", "No. Camera frames and selected photos are processed exclusively on-device using Apple Vision text recognition and immediately discarded."),
                ("Does it give health scores or medical advice?", "No. Additives is an offline reference decoder built from the consolidated EU food additive register (Reg. (EC) No 1333/2008 Annex II, consolidated 18 August 2026) and EU labelling law. It presents factual entries so you can decide."),
                ("Can it read foreign packaging?", "Yes. It detects which of its 12 supported languages an ingredient list is printed in, matches names in that language, and shows results in your app language — including INS numbers printed without 'E' and US dye names like Red 40."),
                ("How do I restore Additives Pro?", "Open Settings (top left on Read, Look Up, or Shelf) and tap Restore Purchase while signed in with the same Apple Account. Refunds are handled by Apple at reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Privacy Policy",
            "lede": "Additives collects no personal data, creates no accounts, includes no analytics or ads, and runs offline on your device.",
            "summary_title": "Data Handling Summary",
            "rows": [
                ("Camera & Photos", "Processed entirely on-device to recognize ingredient text. Images are never uploaded or saved to disk or cloud."),
                ("Watch List & Saved Readings", "Stored locally inside the app container on your device (saved.json and UserDefaults). No account or cloud sync."),
                ("Analytics, Ads & Tracking", "None. Zero third-party analytics, advertising, crash reporting, or tracking SDKs are included."),
                ("Network Requests", "Apple StoreKit 2 only, used solely when fetching pricing, purchasing, or restoring Additives Pro."),
            ],
            "sections": [
                ("No Personal Data Collection", "Additives does not collect, store on external servers, transmit, sell, or share any personal information, identifiers, location data, or usage telemetry."),
                ("Camera & Photo Library Access", "Camera and photo access are optional and requested only when you tap Read or Choose a Photo. You can also type or paste text without granting media access. Selected photos and live video frames are analyzed in memory to extract additive names and E-numbers and are immediately discarded."),
                ("Local Storage & Deletion", "Your saved readings, favourites, watch list selections, and preferences stay solely on your iPhone or iPad (using UserDefaults for preference flags and the verified StoreKit unlock cache, plus an app sandbox JSON file). You can erase saved history anytime from Settings, or remove the app to delete all local data."),
                ("In-App Purchase", "Additives Pro is a single non-consumable purchase processed directly by Apple via StoreKit 2. We never receive payment details or your Apple Account information."),
            ],
        },
    },
    "de-DE": {
        "name": "Deutsch",
        "html_lang": "de",
        "app": "E-Nummern: Zusatzstoff-Leser",
        "nav_help": "Hilfe",
        "nav_privacy": "Datenschutz",
        "nav_langs": "Alle Sprachen",
        "contact_title": "Kontakt",
        "contact_body": f'Fragen, Hinweise oder Korrekturen zu E-Nummern: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Stand: 25. November 2026 · E-Nummern ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Hilfe & Referenzhandbuch",
            "lede": "Zutatenlisten offline auf dem Gerät lesen, eigene E-Nummern markieren und EU-Kennzeichnungshinweise ohne Konto oder Tracking prüfen.",
            "steps_title": "So funktioniert E-Nummern",
            "steps": [
                ("Zutatenliste lesen", "Öffne den Tab Lesen und halte die Kamera über die Zutatenliste. Codes wie E330, E 129 oder e120 sowie Namen werden live umrahmt. Tippe auf Dieses Etikett lesen oder wähle ein Foto bzw. füge Text ein."),
                ("Eigene Liste zuerst hervorheben", "Wähle unter Darauf achten bis zu drei E-Nummern kostenlos aus oder ganze Gruppen mit E-Nummern Pro. Treffer erscheinen im Bericht ganz oben in Gelb."),
                ("EU-Kennzeichnungshinweise ansehen", "Darunter zeigt der Bericht gesetzliche Hinweise samt Verordnung, z. B. Sulfite ab 10 mg/kg SO2, die sechs Farbstoffe mit Kinderhinweis (VO (EG) Nr. 1333/2008 Art. 24 & Anhang V), Aspartam, Polyole >10 % sowie gestrichene Codes wie E171 oder E128."),
                ("339 EU-E-Nummern offline nachschlagen", "Im Verzeichnis findest du Funktionsklassen, EU-Status, Namen in 12 Sprachen und EU-Spezifikationsangaben zur Herkunft. Es werden keine Noten oder medizinische Empfehlungen gegeben."),
                ("E-Nummern Pro (Einmalkauf)", "Schaltet ganze Beobachtungsgruppen und eine unbegrenzte Liste, benannte gespeicherte Lesungen, Etiketten-Vergleich, Favoriten und Klartext-Export frei."),
            ],
            "faq_title": "Häufige Fragen",
            "faq": [
                ("Werden Packungsfotos hochgeladen?", "Nein. Kamerabilder und Fotos werden ausschließlich lokal über Apple Vision ausgewertet und sofort verworfen."),
                ("Gibt es Gesundheitsbewertungen?", "Nein. Die App ist ein faktenbasiertes Nachschlagewerk auf Basis der konsolidierten EU-Zusatzstoffliste (18. August 2026) und des EU-Lebensmittelrechts."),
                ("Funktioniert die App im Ausland?", "Ja. Sie erkennt 12 Etikettsprachen automatisch, liest auch INS-Nummern ohne E sowie US-Farbstoffnamen wie Red 40 und antwortet in deiner Sprache."),
                ("Kauf wiederherstellen", "Öffne Einstellungen › Kauf wiederherstellen mit demselben Apple Account. Erstattungen erfolgen über reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Datenschutzerklärung",
            "lede": "E-Nummern erhebt keine personenbezogenen Daten, benötigt kein Konto und arbeitet vollständig offline auf deinem Gerät.",
            "summary_title": "Datenüberblick",
            "rows": [
                ("Kamera & Fotos", "Erkennung findet ausschließlich lokal statt. Es werden keine Fotos gespeichert oder übertragen."),
                ("Beobachtungsliste & Lesungen", "Lokal auf dem Gerät gespeichert (saved.json und UserDefaults). Kein Konto, keine Cloud."),
                ("Analyse, Werbung & Tracking", "Keine. Keine Tracking- oder Analyse-SDKs von Drittanbietern."),
                ("Netzwerkverkehr", "Ausschließlich StoreKit 2 (Apple) für Preisabruf, Einmalkauf und Wiederherstellung."),
            ],
            "sections": [
                ("Keine Datenerfassung", "E-Nummern sammelt, speichert, überträgt oder teilt keinerlei personenbezogene Daten, Nutzungsstatistiken oder Standortdaten."),
                ("Kamera- und Fotozugriff", "Berechtigungen sind optional und werden nur bei Nutzung von Kamera oder Fotoauswahl angefragt; Texte können auch eingetippt werden. Bilddaten werden nach der Texterkennung sofort verworfen."),
                ("Lokale Speicherung & Löschung", "Alle gespeicherten Etiketten und Einstellungen bleiben in deiner lokalen App-Sandbox und können jederzeit in den Einstellungen gelöscht werden."),
                ("In-App-Kauf", "E-Nummern Pro wird einmalig direkt über Apples StoreKit 2 abgewickelt. Zahlungsdaten erhalten wir nicht."),
            ],
        },
    },
    "fr-FR": {
        "name": "Français",
        "html_lang": "fr",
        "app": "Additifs : Codes E",
        "nav_help": "Aide",
        "nav_privacy": "Confidentialité",
        "nav_langs": "Toutes les langues",
        "contact_title": "Contact",
        "contact_body": f'Questions ou retours sur Additifs : <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Mise à jour : 25 novembre 2026 · Additifs ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Aide & Guide de référence",
            "lede": "Lisez toute liste d'ingrédients hors ligne sur votre appareil et vérifiez vos additifs ainsi que les mentions légales de l'UE.",
            "steps_title": "Comment fonctionne Additifs",
            "steps": [
                ("Lire une étiquette", "Pointez la caméra sur la liste d'ingrédients dans l'onglet Lire : les codes E et noms d'additifs sont encadrés en direct. Touchez Lire cette étiquette, choisissez une photo ou collez le texte."),
                ("Afficher vos alertes en premier", "Sélectionnez gratuitement jusqu'à 3 numéros E dans À surveiller, ou des groupes entiers avec Additifs Pro. Ils apparaissent d'abord, surlignés en jaune."),
                ("Mentions légales de l'UE", "Le compte rendu rappelle les mentions obligatoires (sulfites >10 mg/kg, six colorants pour enfants Règl. 1333/2008 art. 24 & annexe V, phénylalanine, polyols >10 %) et les codes retirés comme E171 ou E128."),
                ("Dictionnaire de 339 numéros E", "Consultez hors ligne les classes fonctionnelles, le statut UE, les noms en 12 langues et l'origine selon la spécification UE, sans note ni avis médical."),
                ("Additifs Pro (achat unique)", "Débloque les groupes complets À surveiller, l'historique nommé sur l'appareil, la comparaison côte à côte, les favoris et l'export texte."),
            ],
            "faq_title": "Questions fréquentes",
            "faq": [
                ("Les photos sont-elles envoyées sur un serveur ?", "Non. L'analyse optique Apple Vision fonctionne localement et aucune photo n'est conservée ni envoyée."),
                ("Y a-t-il des scores nutritionnels ou médicaux ?", "Non. Additifs présente uniquement les faits du registre européen consolidé au 18 août 2026."),
                ("Puis-je lire un emballage étranger ?", "Oui. L'app reconnaît 12 langues, les codes INS sans E et les colorants américains comme Red 40."),
                ("Restaurer l'achat", "Ouvrez Réglages › Restaurer l'achat avec le même identifiant Apple. Remboursements sur reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Politique de confidentialité",
            "lede": "Additifs ne collecte aucune donnée personnelle, ne nécessite aucun compte et fonctionne entièrement hors ligne.",
            "summary_title": "Résumé des données",
            "rows": [
                ("Caméra et photos", "Traités localement sur l'appareil ; aucune image n'est conservée ni transmise."),
                ("Listes et lectures enregistrées", "Stockées uniquement sur votre appareil (saved.json et UserDefaults)."),
                ("Analyse, pub et suivi", "Aucun SDK tiers de suivi, publicité ou télémétrie."),
                ("Réseau", "StoreKit 2 (Apple) uniquement pour le tarif, l'achat ou la restauration Pro."),
            ],
            "sections": [
                ("Aucune collecte personnelle", "Additifs ne collecte ni ne partage aucune donnée personnelle, identifiant ou donnée de localisation."),
                ("Accès caméra et photothèque", "Demandé uniquement lors de l'utilisation de la caméra ou de la galerie ; les images sont immédiatement écartées après lecture."),
                ("Stockage local et suppression", "Effacez l'historique dans Réglages à tout moment ou supprimez l'application."),
                ("Achat intégré", "Achat unique traité directement par Apple via StoreKit 2 sans accès à vos informations de paiement."),
            ],
        },
    },
    "es-ES": {
        "name": "Español",
        "html_lang": "es",
        "app": "Aditivos: Lector de códigos E",
        "nav_help": "Ayuda",
        "nav_privacy": "Privacidad",
        "nav_langs": "Todos los idiomas",
        "contact_title": "Contacto",
        "contact_body": f'Dudas o sugerencias sobre Aditivos: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Actualizado: 25 de noviembre de 2026 · Aditivos ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Ayuda y Guía",
            "lede": "Lee listas de ingredientes en el dispositivo, marca tus aditivos vigilados y consulta los avisos legales de la UE sin internet.",
            "steps_title": "Cómo funciona Aditivos",
            "steps": [
                ("Leer una etiqueta", "Apunta con la cámara a la lista de ingredientes en la pestaña Leer; los códigos E y nombres se marcan en directo. También puedes elegir una foto o pegar texto."),
                ("Priorizar lo que vigilas", "Elige hasta 3 códigos E gratis en Qué vigilar, o grupos enteros con Aditivos Pro. Siempre aparecen primero y en amarillo."),
                ("Avisos legales de la UE", "Muestra requisitos legales (sulfitos >10 mg/kg, seis colorantes infantiles Reg. (CE) 1333/2008 art. 24 y anexo V, fenilalanina, polioles >10 %) y códigos fuera de la lista UE (E171, E128)."),
                ("Diccionario de 339 números E", "Consulta funciones, estado en la UE, nombres en 12 idiomas y origen sin puntuaciones ni consejos médicos."),
                ("Aditivos Pro (compra única)", "Añade grupos completos, lecturas guardadas con nombre, comparación lado a lado, favoritos y exportación de texto."),
            ],
            "faq_title": "Preguntas frecuentes",
            "faq": [
                ("¿Se suben las fotos a internet?", "No. Todo el reconocimiento se hace en el dispositivo y las imágenes se descartan de inmediato."),
                ("¿Ofrece notas o consejos de salud?", "No. Solo muestra información objetiva del registro de la UE consolidado al 18 de agosto de 2026."),
                ("¿Lee etiquetas extranjeras?", "Sí. Detecta 12 idiomas, números INS sin la letra E y colorantes estadounidenses como Red 40."),
                ("Restaurar compra", "Entra en Ajustes › Restaurar compra con la misma cuenta de Apple. Reembolsos en reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Política de privacidad",
            "lede": "Aditivos no recopila datos personales, no requiere cuenta y guarda toda tu información localmente.",
            "summary_title": "Resumen de datos",
            "rows": [
                ("Cámara y fotos", "Procesamiento local en el dispositivo; no se guardan ni se envían imágenes."),
                ("Listas y lecturas", "Solo en tu dispositivo (saved.json y UserDefaults)."),
                ("Analítica y anuncios", "Ninguno. Sin SDKs de rastreo ni publicidad."),
                ("Conexión de red", "Únicamente Apple StoreKit 2 para consultar precio, comprar o restaurar Pro."),
            ],
            "sections": [
                ("Sin recopilación de datos", "No recolectamos ni compartimos datos personales, métricas ni ubicación."),
                ("Permisos multimedia", "Opcionales al usar cámara o fotos; las imágenes se descartan tras leer el texto."),
                ("Eliminación", "Puedes borrar el historial desde Ajustes o desinstalando la aplicación."),
                ("Compra única", "Gestionada por Apple StoreKit 2 sin acceso a tus datos bancarios."),
            ],
        },
    },
    "it": {
        "name": "Italiano",
        "html_lang": "it",
        "app": "Additivi: Numeri E",
        "nav_help": "Guida",
        "nav_privacy": "Privacy",
        "nav_langs": "Tutte le lingue",
        "contact_title": "Contatti",
        "contact_body": f'Domande o segnalazioni su Additivi: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Aggiornato al 25 novembre 2026 · Additivi ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Guida e Riferimento",
            "lede": "Leggi gli ingredienti sul dispositivo, evidenzia ciò che tieni d'occhio e verifica le norme UE senza account né tracciamento.",
            "steps_title": "Come funziona Additivi",
            "steps": [
                ("Leggi un'etichetta", "Inquadra la lista ingredienti in Leggi: codici E e nomi vengono evidenziati dal vivo. Puoi anche scegliere una foto o incollare il testo."),
                ("Metti in cima i tuoi additivi", "Scegli gratis fino a 3 numeri E in Tieni d'occhio, oppure interi gruppi con Additivi Pro. Compaiono per primi in giallo."),
                ("Obblighi di etichettatura UE", "Elenca gli obblighi di legge (solfiti >10 mg/kg, sei coloranti per bambini Reg. 1333/2008 art. 24 e allegato V, fenilalanina, polialcoli >10 %) e i codici esclusi (E171, E128)."),
                ("Dizionario offline di 339 numeri E", "Funzioni, stato UE, nomi in 12 lingue e origine specificata dall'UE, senza punteggi né pareri medici."),
                ("Additivi Pro (acquisto unico)", "Sblocca gruppi completi, storico salvato sul dispositivo, confronto affiancato, preferiti ed esportazione testo."),
            ],
            "faq_title": "Domande frequenti",
            "faq": [
                ("Le foto vengono inviate online?", "No. Tutto il riconoscimento avviene sul dispositivo e le immagini vengono scartate subito."),
                ("Ci sono punteggi sanitari?", "No. Solo riferimenti oggettivi dall'elenco UE consolidato al 18 agosto 2026."),
                ("Legge etichette estere?", "Sì, riconosce 12 lingue, codici INS e coloranti USA come Red 40."),
                ("Ripristina acquisto", "Vai su Impostazioni › Ripristina acquisto con lo stesso Apple Account. Rimborsi su reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Informativa sulla privacy",
            "lede": "Additivi non raccoglie dati personali, non richiede account e conserva tutto in locale.",
            "summary_title": "Riepilogo dati",
            "rows": [
                ("Fotocamera e foto", "Analisi esclusivamente locale; nessuna immagine salvata o trasmessa."),
                ("Elenchi e letture", "Salvati solo sul dispositivo (saved.json e UserDefaults)."),
                ("Analisi e pubblicità", "Nessuno SDK di tracciamento o pubblicità."),
                ("Rete", "Solo Apple StoreKit 2 per prezzo, acquisto o ripristino Pro."),
            ],
            "sections": [
                ("Nessuna raccolta dati", "Nessun dato personale, telemetria o posizione viene raccolto o condiviso."),
                ("Accesso fotocamera", "Richiesto solo per scansionare o importare foto; i fotogrammi vengono scartati immediatamente."),
                ("Cancellazione", "Puoi cancellare la cronologia dalle Impostazioni o eliminando l'app."),
                ("Acquisto in-app", "Acquisto singolo gestito da Apple StoreKit 2."),
            ],
        },
    },
    "pt-BR": {
        "name": "Português",
        "html_lang": "pt-BR",
        "app": "Aditivos: Leitor de Códigos E",
        "nav_help": "Ajuda",
        "nav_privacy": "Privacidade",
        "nav_langs": "Todos os idiomas",
        "contact_title": "Contato",
        "contact_body": f'Dúvidas ou sugestões sobre o Aditivos: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Atualizado em 25 de novembro de 2026 · Aditivos ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Ajuda e Referência",
            "lede": "Leia listas de ingredientes no aparelho, destaque seus códigos observados e confira avisos da legislação da UE sem internet.",
            "steps_title": "Como usar o Aditivos",
            "steps": [
                ("Ler um rótulo", "Aponte a câmera para a lista de ingredientes na aba Ler; códigos E e nomes são marcados ao vivo. Também aceita foto ou texto colado."),
                ("Destacar o que você observa", "Escolha até 3 números E grátis em Observar, ou grupos completos no Aditivos Pro, para vê-los primeiro em amarelo."),
                ("Regras de rotulagem da UE", "Mostra exigências legais (sulfitos >10 mg/kg, seis corantes infantis Reg. 1333/2008 art. 24 e anexo V, fenilalanina, polióis >10 %) e códigos fora da lista da UE (E171, E128)."),
                ("Dicionário de 339 números E", "Consulte funções, status na UE, nomes em 12 idiomas e origem offline, sem notas ou conselho médico."),
                ("Aditivos Pro (compra única)", "Libera grupos inteiros, histórico salvo no aparelho, comparação lado a lado, favoritos e exportação em texto."),
            ],
            "faq_title": "Perguntas frequentes",
            "faq": [
                ("As fotos saem do aparelho?", "Não. Todo reconhecimento ocorre localmente e as imagens são descartadas imediatamente."),
                ("O app dá pontuação de saúde?", "Não. Traz apenas dados objetivos da lista consolidada da UE de 18 de agosto de 2026."),
                ("Lê embalagens estrangeiras?", "Sim. Reconhece 12 idiomas, códigos INS sem E e corantes dos EUA como Red 40."),
                ("Restaurar compra", "Abra Ajustes › Restaurar compra com a mesma Conta Apple. Reembolsos via reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Política de Privacidade",
            "lede": "O Aditivos não coleta dados pessoais, dispensa conta e mantém tudo apenas no seu aparelho.",
            "summary_title": "Resumo de dados",
            "rows": [
                ("Câmera e fotos", "Processados localmente no dispositivo; nada é salvo ou enviado."),
                ("Listas e leituras", "Apenas no armazenamento local do app (saved.json e UserDefaults)."),
                ("Rastreamento e anúncios", "Nenhum SDK de análise, rastreamento ou publicidade."),
                ("Rede", "Apenas Apple StoreKit 2 para preço, compra ou restauração Pro."),
            ],
            "sections": [
                ("Sem coleta de dados", "Não coletamos nem compartilhamos dados pessoais, telemetria ou localização."),
                ("Câmera e fototeca", "Solicitados apenas ao usar câmera ou foto; as imagens são descartadas logo após a leitura."),
                ("Exclusão de dados", "Apague o histórico em Ajustes ou remova o aplicativo."),
                ("Compra única", "Processada diretamente pela Apple via StoreKit 2."),
            ],
        },
    },
    "nl-NL": {
        "name": "Nederlands",
        "html_lang": "nl",
        "app": "E-nummers: Etikettenlezer",
        "nav_help": "Hulp",
        "nav_privacy": "Privacybeleid",
        "nav_langs": "Alle talen",
        "contact_title": "Contact",
        "contact_body": f'Vragen of feedback over E-nummers: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Bijgewerkt: 25 november 2026 · E-nummers ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Hulp & Handleiding",
            "lede": "Lees ingrediëntenlijsten lokaal op je apparaat, markeer waar je op let en bekijk EU-etiketteringsregels zonder account.",
            "steps_title": "Zo werkt E-nummers",
            "steps": [
                ("Een etiket lezen", "Richt de camera op de ingrediëntenlijst in Lezen; E-nummers en namen worden live omlijnd. Je kunt ook een foto kiezen of tekst plakken."),
                ("Jouw lijst bovenaan", "Kies gratis tot 3 E-nummers onder Waar je op let, of hele groepen met E-nummers Pro. Ze verschijnen bovenaan in het geel."),
                ("EU-etiketteringsregels", "Toont verplichte meldingen (sulfieten >10 mg/kg, zes kleurstoffen met kinderwaarschuwing Verordening 1333/2008 art. 24 & bijlage V, fenylalanine, polyolen >10 %) en geweerde codes zoals E171 of E128."),
                ("Offline woordenboek (339 codes)", "Functies, EU-status, namen in 12 talen en oorsprong zonder scores of medisch advies."),
                ("E-nummers Pro (eenmalig)", "Ontgrendelt hele groepen, bewaarde metingen op dit apparaat, twee etiketten naast elkaar, favorieten en tekstexport."),
            ],
            "faq_title": "Veelgestelde vragen",
            "faq": [
                ("Worden foto's geüpload?", "Nee. Herkenning gebeurt volledig op het apparaat en foto's worden direct gewist."),
                ("Geeft de app gezondheidsscores?", "Nee. Alleen feitelijke gegevens uit de geconsolideerde EU-lijst van 18 augustus 2026."),
                ("Leest de app buitenlandse pakken?", "Ja, 12 talen, INS-nummers zonder E en Amerikaanse kleurstoffen zoals Red 40."),
                ("Aankoop herstellen", "Ga naar Instellingen › Aankoop herstellen met dezelfde Apple Account. Terugbetaling via reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Privacybeleid",
            "lede": "E-nummers verzamelt geen persoonsgegevens, gebruikt geen accounts en werkt volledig offline.",
            "summary_title": "Gegevensoverzicht",
            "rows": [
                ("Camera en foto's", "Lokaal verwerkt; geen foto's bewaard of verzonden."),
                ("Lijsten en metingen", "Alleen lokaal opgeslagen (saved.json en UserDefaults)."),
                ("Analytics en reclame", "Geen enkele tracking-, reclame- of analyse-SDK."),
                ("Netwerk", "Alleen Apple StoreKit 2 voor prijs, aankoop en herstel."),
            ],
            "sections": [
                ("Geen gegevensverzameling", "Er worden geen persoonsgegevens, locatiegegevens of statistieken opgeslagen of gedeeld."),
                ("Camera en foto's", "Alleen op aanvraag gebruikt om tekst te lezen en daarna onmiddellijk weggegooid."),
                ("Verwijderen", "Wis je geschiedenis in Instellingen of verwijder de app."),
                ("Eenmalige aankoop", "Verwerkt door Apple via StoreKit 2."),
            ],
        },
    },
    "ja": {
        "name": "日本語",
        "html_lang": "ja",
        "app": "食品添加物：E番号リーダー",
        "nav_help": "ヘルプ",
        "nav_privacy": "プライバシー",
        "nav_langs": "すべての言語",
        "contact_title": "お問い合わせ",
        "contact_body": f'ご質問・ご要望はこちら：<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"更新日：2026年11月25日 · 食品添加物 ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "ヘルプ＆ガイド",
            "lede": "原材料表示を端末内で読み取り、チェックしたい添加物やEUの表示ルールをオフラインで確認できます。",
            "steps_title": "主な機能と使い方",
            "steps": [
                ("ラベルを読み取る", "「読む」タブで原材料表示にカメラを向けると、E番号や添加物名がリアルタイムに枠で囲まれます。写真を選ぶ、または文字の入力・貼り付けにも対応します。"),
                ("チェック対象を先頭に表示", "「注目リスト」に無料の3件まで、または食品添加物 Proでグループ全体を追加すると、該当項目が黄色のハイライトで先頭に出ます。"),
                ("EUの表示ルールを確認", "亜硫酸塩（10 mg/kg超）、子ども向け警告が必要な6色の着色料（規則(EC) No 1333/2008 第24条・付属書V）、アスパルテーム、ポリオール（10%超）、E171やE128などEU非承認コードを表示します。"),
                ("339件のEU添加物辞典", "用途分類、EUの許可状況、12言語の名称、EU規格の由来をオフラインで検索できます。スコア判定や医療アドバイスは行いません。"),
                ("食品添加物 Pro（買い切り）", "グループ単位の注目設定、端末内での読み取り保存、2つのラベルの比較、お気に入り、テキスト書き出しを追加します。"),
            ],
            "faq_title": "よくある質問",
            "faq": [
                ("写真は外部サーバーに送られますか？", "いいえ。Apple Visionによりすべて端末内で文字認識され、画像は保存・送信されません。"),
                ("健康スコアや点数は出ますか？", "いいえ。2026年8月18日時点のEU食品添加物統合リストの事実情報のみを示します。"),
                ("海外のパッケージも読めますか？", "はい。12言語のラベル自動判別、INS番号、米国着色料名（Red 40等）に対応しています。"),
                ("購入の復元方法", "同じApple Accountで「設定 › 購入を復元」をタップしてください。返金は reportaproblem.apple.com にて行われます。"),
            ],
        },
        "privacy": {
            "title": "プライバシーポリシー",
            "lede": "本アプリは個人情報を収集せず、アカウント不要・完全オフラインで動作します。",
            "summary_title": "データの取り扱い",
            "rows": [
                ("カメラと写真", "端末内での文字認識のみに使用し、保存・送信しません。"),
                ("リストと保存履歴", "端末内（saved.json / UserDefaults）のみに保存されます。"),
                ("解析・広告・追跡", "第三者のトラッキング、広告、解析SDKは一切含まれません。"),
                ("通信", "食品添加物 Proの価格確認・購入・復元の際のApple StoreKit 2のみ。"),
            ],
            "sections": [
                ("個人情報の非収集", "氏名、位置情報、利用統計、識別子等を収集・送信・第三者提供することはありません。"),
                ("カメラ・写真アクセス", "読み取り時のみ任意で求められ、文字抽出後の画像は即座に破棄されます。"),
                ("データの削除", "設定から履歴を消去するか、アプリを削除することで端末内の全データが削除されます。"),
                ("アプリ内課金", "Apple StoreKit 2による買い切り処理のみを利用します。"),
            ],
        },
    },
    "ko": {
        "name": "한국어",
        "html_lang": "ko",
        "app": "식품첨가물: E-번호 리더",
        "nav_help": "도움말",
        "nav_privacy": "개인정보 처리방침",
        "nav_langs": "모든 언어",
        "contact_title": "문의",
        "contact_body": f'문의 및 의견 보내기: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"업데이트: 2026년 11월 25일 · 식품첨가물 ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "도움말 및 안내",
            "lede": "식품 원재료명을 기기에서 직접 읽고, 확인하려는 첨가물과 EU 표시 규정을 계정 없이 오프라인으로 확인하세요.",
            "steps_title": "사용 방법",
            "steps": [
                ("라벨 읽기", "읽기 탭에서 원재료명에 카메라를 대면 E 번호와 첨가물 이름이 실시간으로 표시됩니다. 사진 선택 또는 텍스트 붙여넣기도 지원합니다."),
                ("확인할 항목 우선 표시", "내 목록에서 무료 3개까지 또는 Pro에서 그룹 전체를 선택하면 모든 결과 상단에 노란색으로 표시됩니다."),
                ("EU 표시 의무 확인", "아황산염(10 mg/kg 초과), 어린이 주의 색소 6종(규정 1333/2008 제24조 및 부속서 V), 아스파탐, 폴리올(10% 초과), E171·E128 등 미허용 코드를 안내합니다."),
                ("339개 EU 첨가물 사전", "기능 분류, EU 상태, 12개 언어 이름 및 원료 유래를 점수나 의학적 조언 없이 객관적으로 제공합니다."),
                ("식품첨가물 Pro(일회성 구매)", "전체 그룹 알림, 이름별 읽기 기록 보관, 두 라벨 나란히 비교, 즐겨찾기, 텍스트 내보내기를 제공합니다."),
            ],
            "faq_title": "자주 묻는 질문",
            "faq": [
                ("사진이 서버로 전송되나요?", "아니요. 모든 인식은 Apple Vision으로 기기 내부에서 처리되며 이미지는 저장되거나 전송되지 않습니다."),
                ("점수나 등급을 매기나요?", "아니요. 2026년 8월 18일 기준 EU 통합 목록의 사실 정보만 표시합니다."),
                ("해외 제품도 읽을 수 있나요?", "네. 12개 언어 자동 판별, E 없는 INS 번호, 미국식 색소 이름(Red 40 등)을 지원합니다."),
                ("구매 복원", "같은 Apple 계정으로 설정 › 구매 복원을 누르세요. 환불은 reportaproblem.apple.com에서 진행됩니다."),
            ],
        },
        "privacy": {
            "title": "개인정보 처리방침",
            "lede": "식품첨가물은 개인정보를 수집하지 않으며, 계정이나 추적 없이 기기에서만 작동합니다.",
            "summary_title": "데이터 처리 요약",
            "rows": [
                ("카메라 및 사진", "기기 내 문자 인식에만 사용되며 저장되거나 전송되지 않습니다."),
                ("목록 및 보관 기록", "기기 내부(saved.json 및 UserDefaults)에만 저장됩니다."),
                ("분석·광고·추적", "제3자 추적, 광고, 분석 SDK가 전혀 없습니다."),
                ("네트워크 통신", "Pro 가격 조회·구매·복원을 위한 Apple StoreKit 2 통신만 사용합니다."),
            ],
            "sections": [
                ("개인정보 비수집", "개인정보, 기기 식별자, 위치 정보 또는 사용 통계를 수집하거나 공유하지 않습니다."),
                ("카메라 및 사진 권한", "사용자가 촬영이나 사진 선택을 누를 때만 요청되며, 인식 후 이미지는 즉시 폐기됩니다."),
                ("데이터 삭제", "설정에서 기록을 지우거나 앱을 삭제하면 모든 로컬 데이터가 제거됩니다."),
                ("인앱 결제", "Apple StoreKit 2를 통해 처리되는 일회성 구매입니다."),
            ],
        },
    },
    "zh-Hans": {
        "name": "简体中文",
        "html_lang": "zh-Hans",
        "app": "食品添加剂：E 编号识别",
        "nav_help": "帮助",
        "nav_privacy": "隐私政策",
        "nav_langs": "全部语言",
        "contact_title": "联系我们",
        "contact_body": f'使用反馈或问题咨询：<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"更新日期：2026年11月25日 · 食品添加剂 ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "帮助与参考指南",
            "lede": "完全在设备端离线识别食品配料表，高亮标记您关注的 E 编号，并查看欧盟标签法规要求。",
            "steps_title": "功能说明",
            "steps": [
                ("读取配料表", "在“读取”页面将相机对准配料表，E 编号和添加剂名称会在实时画面中框出；也支持选取照片或粘贴文字。"),
                ("优先标出关注项", "免费可关注 3 个单个 E 编号，开通食品添加剂 Pro 可按整组关注，所有结果顶部将以黄色优先标出。"),
                ("查看欧盟法规要求", "列出亚硫酸盐（超 10 mg/kg）、六种儿童警示着色剂（法规 (EC) No 1333/2008 第 24 条及附件 V）、阿斯巴甜、多元醇（超 10%）以及未列入欧盟清单的编码（如 E171、E128）。"),
                ("339 条欧盟添加剂词典", "离线浏览用途分类、欧盟状态、12 种语言名称与欧盟规格原料来源，不打分，不提供医疗建议。"),
                ("食品添加剂 Pro（一次性购买）", "解锁整组关注清单、本地命名保存记录、双标签并排对比、收藏及纯文本导出。"),
            ],
            "faq_title": "常见问题",
            "faq": [
                ("包装照片会上传吗？", "不会。所有文字识别均通过设备端 Apple Vision 完成，图像不会保存或上传。"),
                ("是否会给食品打分或提供健康建议？", "不会。仅展示截至 2026 年 8 月 18 日欧盟食品添加剂汇总清单与法规客观条文。"),
                ("支持国外包装吗？", "支持。自动识别 12 种语言配料表、无 E 前缀的 INS 编号及美国色素名称（如 Red 40）。"),
                ("如何恢复购买？", "使用同一 Apple 账户在“设置 › 恢复购买”操作即可；退款请访问 reportaproblem.apple.com。"),
            ],
        },
        "privacy": {
            "title": "隐私政策",
            "lede": "本应用不收集任何个人数据，无需账号，无广告与追踪，全部运算均在本地进行。",
            "summary_title": "数据处理说明",
            "rows": [
                ("相机与照片", "仅在设备端用于文字识别，识别后立即丢弃，不保存或上传。"),
                ("关注清单与保存记录", "仅保存在本设备应用沙盒内（saved.json 与 UserDefaults）。"),
                ("分析、广告与追踪", "无任何第三方追踪、广告或统计 SDK。"),
                ("网络连接", "仅在获取价格、购买或恢复食品添加剂 Pro 时连接 Apple StoreKit 2。"),
            ],
            "sections": [
                ("不收集个人信息", "本应用不收集、传输、出售或共享任何个人身份、位置或使用遥测数据。"),
                ("相机与相册权限", "仅在您触发扫描或选图时请求权限；也可直接键入配料文本而无需授权媒体权限。"),
                ("本地存储与删除", "您可随时在设置中清除本地记录，或卸载应用彻底删除全部数据。"),
                ("应用内购买", "由 Apple StoreKit 2 直接处理的一次性买断项目。"),
            ],
        },
    },
    "ru": {
        "name": "Русский",
        "html_lang": "ru",
        "app": "Пищевые добавки: E-коды",
        "nav_help": "Справка",
        "nav_privacy": "Конфиденциальность",
        "nav_langs": "Все языки",
        "contact_title": "Контакты",
        "contact_body": f'Вопросы и замечания о приложении: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Обновлено: 25 ноября 2026 · Пищевые добавки ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Справка и руководство",
            "lede": "Распознавание состава продуктов на устройстве, выделение нужных E-кодов и требования маркировки ЕС без аккаунта и интернета.",
            "steps_title": "Как устроено приложение",
            "steps": [
                ("Чтение этикетки", "Наведите камеру на список ингредиентов на вкладке «Чтение» — E-коды и названия обводятся в реальном времени. Также можно выбрать фото или вставить текст."),
                ("Важные коды первыми", "Выберите до 3 отдельных E-кодов бесплатно или целые группы в версии Pro — они всегда будут первыми и выделены жёлтым."),
                ("Требования закона ЕС", "Обязательные уведомления (сульфиты >10 мг/кг, шесть красителей с предупреждением для детей по Регл. 1333/2008 ст. 24 и прил. V, фенилаланин, полиолы >10 %) и коды вне списка ЕС (E171, E128)."),
                ("Справочник на 339 E-кодов", "Функции, статус в ЕС, названия на 12 языках и сырьё по спецификации ЕС без оценок и медицинских советов."),
                ("Версия Pro (разовая покупка)", "Открывает группы наблюдения, сохранение чтений на устройстве, сравнение двух этикеток, избранное и экспорт текста."),
            ],
            "faq_title": "Частые вопросы",
            "faq": [
                ("Загружаются ли фото на сервер?", "Нет. Распознавание выполняется локально средствами Apple Vision, снимки не сохраняются и не передаются."),
                ("Ставит ли приложение баллы продуктам?", "Нет. Показываются только факты из сводного перечня ЕС от 18 августа 2026 года."),
                ("Читает ли зарубежные упаковки?", "Да: 12 языков, номера INS без E и американские красители вроде Red 40."),
                ("Восстановление покупки", "Откройте Настройки › Восстановить покупку с тем же Apple Account. Возврат средств — через reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Политика конфиденциальности",
            "lede": "Приложение не собирает персональные данные, не требует аккаунта и работает офлайн.",
            "summary_title": "Обработка данных",
            "rows": [
                ("Камера и фото", "Обработка только на устройстве; кадры не сохраняются и не отправляются."),
                ("Списки и чтения", "Хранятся локально (saved.json и UserDefaults)."),
                ("Аналитика и реклама", "Отсутствуют полностью."),
                ("Сеть", "Только Apple StoreKit 2 для цены, покупки или восстановления Pro."),
            ],
            "sections": [
                ("Без сбора данных", "Мы не собираем и не передаём персональные сведения, телеметрию или геолокацию."),
                ("Доступ к камере и фото", "Запрашивается только по вашему выбору; изображения удаляются сразу после распознавания."),
                ("Удаление данных", "Историю можно очистить в Настройках или удалить приложением."),
                ("Покупка в приложении", "Разовая покупка обрабатывается напрямую Apple через StoreKit 2."),
            ],
        },
    },
    "tr": {
        "name": "Türkçe",
        "html_lang": "tr",
        "app": "Katkı Maddeleri: E-Kodu",
        "nav_help": "Yardım",
        "nav_privacy": "Gizlilik",
        "nav_langs": "Tüm Diller",
        "contact_title": "İletişim",
        "contact_body": f'Sorular, düzeltmeler ve geri bildirimler için: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Güncelleme: 25 Kasım 2026 · Katkı Maddeleri ({BUNDLE_ID}) · Hayri Odabaş",
        "help": {
            "title": "Yardım ve Kılavuz",
            "lede": "İçindekiler listesini cihaz üzerinde çevrimdışı okuyun, dikkat ettiklerinizi öne çıkarın ve AB etiketleme kurallarını görün.",
            "steps_title": "Nasıl Çalışır?",
            "steps": [
                ("Etiketi okuma", "Oku sekmesinde kamerayı içindekiler kısmına tutun; E330, E 129 gibi kodlar ve katkı adları canlı görüntüde çerçevelenir. İsterseniz fotoğraf seçebilir ya da metin yapıştırabilirsiniz."),
                ("Önce dikkat ettikleriniz", "Dikkat listesine ücretsiz olarak 3 tekil E-kodu veya Pro ile tüm grupları ekleyin. Her raporda sarıyla en üstte gösterilir."),
                ("AB etiketleme kuralları", "10 mg/kg üzeri sülfit uyarısı, çocuklar için dikkat uyarılı altı renklendirici (1333/2008 Md. 24 ve Ek V), aspartam, %10 üzeri polioller ile AB gıda listesinde olmayan kodlar (E171, E128) belirtilir."),
                ("339 E-kodluk çevrimdışı sözlük", "İşlev sınıfları, AB durumu, 12 dildeki adlar ve AB şartnamesindeki köken notları. Puanlama veya tıbbi tavsiye verilmez."),
                ("Katkı Maddeleri Pro (tek ödeme)", "Tam gruplar, cihazda adlandırılmış okumalar, iki etiketi yan yana karşılaştırma, favoriler ve düz metin dışa aktarımı açılır."),
            ],
            "faq_title": "Sık Sorulan Sorular",
            "faq": [
                ("Fotoğraflar internete yüklenir mi?", "Hayır. Metin tanıma tamamen cihaz üzerinde Apple Vision ile çalışır ve görseller kaydedilmez."),
                ("Sağlık puanı veriyor mu?", "Hayır. Yalnızca 18 Ağustos 2026 tarihli birleştirilmiş AB listesi ve mevzuat metinlerini nesnel biçimde gösterir."),
                ("Yurt dışı paketleri okur mu?", "Evet. 12 dili otomatik tanır, E'siz INS kodlarını ve Red 40 gibi ABD boya adlarını da okur."),
                ("Satın alımı geri yükleme", "Aynı Apple Hesabı ile Ayarlar › Satın Alımı Geri Yükle'ye dokunun. İadeler reportaproblem.apple.com üzerinden yapılır."),
            ],
        },
        "privacy": {
            "title": "Gizlilik Politikası",
            "lede": "Katkı Maddeleri kişisel veri toplamaz, hesap gerektirmez ve her şeyi yalnızca cihazınızda tutar.",
            "summary_title": "Veri Özeti",
            "rows": [
                ("Kamera ve Fotoğraflar", "Yalnızca cihazda metin okumak için işlenir; saklanmaz ve gönderilmez."),
                ("Liste ve Okuma Geçmişi", "Sadece kendi cihazınızda tutulur (saved.json ve UserDefaults)."),
                ("Analiz, Reklam ve İzleme", "Hiçbir üçüncü taraf izleme, analiz veya reklam SDK'sı içermez."),
                ("Ağ Trafiği", "Yalnızca Pro fiyat bilgisi, satın alma ve geri yükleme için Apple StoreKit 2."),
            ],
            "sections": [
                ("Veri Toplanmaz", "Kişisel bilgi, konum verisi, kimlik bilgisi veya kullanım istatistiği toplanmaz ve paylaşılmaz."),
                ("Kamera ve Galeri Erişimi", "İsteğe bağlıdır; görüntüler okunduktan hemen sonra bellekten atılır."),
                ("Veri Silme", "Ayarlar üzerinden geçmişi silebilir veya uygulamayı kaldırarak tüm yerel verileri temizleyebilirsiniz."),
                ("Uygulama İçi Satın Alma", "Apple StoreKit 2 aracılığıyla işlenen tek seferlik satın almadır."),
            ],
        },
    },
}


def render_shell_header() -> str:
    return (
        '<div class="docket-rule-wrap" aria-hidden="true">'
        '<div class="docket-rule-heavy"></div>'
        '<div class="docket-rule-thin"></div>'
        '</div>'
    )


def render_help(locale: str, data: dict) -> str:
    h = data["help"]
    steps_html = "".join(
        f"<li><strong>{html.escape(title)}</strong> — {html.escape(body)}</li>"
        for title, body in h["steps"]
    )
    faq_html = "".join(
        f'<div class="card"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>'
        for q, a in h["faq"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(h['title'])}</title>
<link rel="canonical" href="{BASE_URL}/{locale}/help.html">
<style>{CSS}</style>
</head>
<body>
{render_shell_header()}
<main>
  <div class="kicker">{html.escape(data['app'])}</div>
  <h1>{html.escape(h['title'])}</h1>
  <p class="lede">{html.escape(h['lede'])}</p>
  <nav>
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="../index.html">{html.escape(data['nav_langs'])}</a>
  </nav>
  <h2>{html.escape(h['steps_title'])}</h2>
  <ol>{steps_html}</ol>
  <h2>{html.escape(h['faq_title'])}</h2>
  {faq_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_privacy(locale: str, data: dict) -> str:
    p = data["privacy"]
    rows_html = "".join(
        f"<tr><td><strong>{html.escape(k)}</strong></td><td>{html.escape(v)}</td></tr>"
        for k, v in p["rows"]
    )
    sec_html = "".join(
        f"<h2>{html.escape(title)}</h2><p>{html.escape(body)}</p>"
        for title, body in p["sections"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(p['title'])}</title>
<link rel="canonical" href="{BASE_URL}/{locale}/privacy.html">
<style>{CSS}</style>
</head>
<body>
{render_shell_header()}
<main>
  <div class="kicker">{html.escape(data['app'])}</div>
  <h1>{html.escape(p['title'])}</h1>
  <p class="lede">{html.escape(p['lede'])}</p>
  <nav>
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="../index.html">{html.escape(data['nav_langs'])}</a>
  </nav>
  <h2>{html.escape(p['summary_title'])}</h2>
  <table><tbody>{rows_html}</tbody></table>
  {sec_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_root_copy(page_html: str) -> str:
    return page_html.replace('href="../index.html"', 'href="index.html"')


def render_index() -> str:
    items = "".join(
        f'<li><strong>{html.escape(d["name"])}</strong><br>'
        f'<a href="{loc}/help.html">{html.escape(d["nav_help"])}</a> · '
        f'<a href="{loc}/privacy.html">{html.escape(d["nav_privacy"])}</a></li>'
        for loc, d in LOCALES.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Additives: E-Number Decoder — Help &amp; Privacy</title>
<link rel="canonical" href="{BASE_URL}/">
<style>{CSS}</style>
</head>
<body>
{render_shell_header()}
<main>
  <div class="kicker">Additives · E-Number Decoder</div>
  <h1>Help &amp; Privacy</h1>
  <p class="lede">On-device EU E-number ingredient reader and offline reference built around Regulation (EC) No 1333/2008. Select your language below.</p>
  <ul class="langs">{items}</ul>
  <footer>Effective November 25, 2026 · Additives ({BUNDLE_ID}) · Hayri Odabaş · <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></footer>
</main>
</body>
</html>
"""


def main() -> None:
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    for locale, data in LOCALES.items():
        loc_dir = ROOT / locale
        loc_dir.mkdir(parents=True, exist_ok=True)
        (loc_dir / "help.html").write_text(render_help(locale, data), encoding="utf-8")
        (loc_dir / "privacy.html").write_text(render_privacy(locale, data), encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    (ROOT / "help.html").write_text(render_root_copy(render_help("en-US", LOCALES["en-US"])), encoding="utf-8")
    (ROOT / "privacy.html").write_text(render_root_copy(render_privacy("en-US", LOCALES["en-US"])), encoding="utf-8")
    print(f"Generated {len(LOCALES) * 2 + 3} HTML pages in {ROOT}")


if __name__ == "__main__":
    main()
