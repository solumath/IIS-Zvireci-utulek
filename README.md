# IIS - Zvířecí útulek - Pes gang

## Hodnocení

| Hodnocení projektu | body  |
|--------------------|-------|
| Projekt            | 20/30 |

## Poznámky k hodnocení

- dokumentace:
  - ER/návrh DB: ok
  - instalace: ok
- zdrojové kódy:
  - inicializační skript DB: ok
  - architektura/struktura souborů: ok
  - uložení hesel: není hash

## Funkcionalita

### administrátor

- spravuje uživatele - ok

### pečovatel

- spravuje zvířata, vede jejich evidenci - ok
- vytváří rozvrhy pro venčení -- není možnost zadat vlastní rozvrh
- ověřuje dobrovolníky - ok
- schvaluje rezervace zvířat na venčení, eviduje zapůjčení a vrácení - ok
- vytváří požadavky na veterináře -- skoro

- vytváření požadavku skončil s hláškou internal error

### veterinář

- vyřizuje požadavky od pečovatele - ok
- udržuje zdravotní záznamy zvířat -- skoro
  - editace skončí s err 500

### dobrovolník

- rezervuje zvířata na venčení - ok
- vidí historii svých venčení - ok

### neregistrovaný uživatel

- prochází informace o útulku a zvířatech - ok

### použitelnost

- klientská validace formulářů:
  - datum nalezení/přijetí zvířete je možné zadat v budoucnosti
- oznámení o (ne)provedení akce:
- další:
  - pekně vytvořený souhlas s podmínkami používání :D

## Spuštění projektu

Postgress inicializacia:

```shell
docker run --name iis_utulek -dp 5432:5432 -e POSTGRES_PASSWORD=iispass -e POSTGRES_USER=iis -e POSTGRES_DB=iis postgres:latest
```

```python
pip3 install -r requirements.txt
```

Inicializacia db:

```python
python3
>>> import main
>>> main.reset_db()
```

Start main

```python
python3 main.py
```

## Popis

Úkolem zadání je vytvořit jednoduchý informační systém pro evidenci opuštěných zvířat zvířecím útulkem (např. králíků, koček nebo psů) a možnost jejich zapůjčení a venčení dobrovolníky. Každé zvíře je identifikováno jménem, druhem a dalšími vhodně zvolenými atributy (např. věk, fotky, případně se inspirujte např. popisem zvířat pana Zdeňka Srstky, apod.). Zvíře má dále svoji historii (např. informace o nalezení) a evidenci svého zdravotního stavu (např. informace o očkování) a průběžných prohlídkách veterinářem. Zvíře je možné přidat do rozvrhu pro možné venčení. Ověření dobrovolníci mohou tyto zvířata vyhledávat a provádět rezervace pro jejich zapůjčení dle volných termínů v rozvrhu. Konkrétně budou v systému vystupovat následující role:

---

## Uživatelé

1. administrátor:
    - [x] spravuje uživatele, jako jediný vytváří pečovatele a veterináře

2. pečovatel:
    - [x] spravuje zvířata, vede jejich evidenci
    - [x] vytváří rozvrhy pro venčení
    - [x] ověřuje dobrovolníky
    - [x] schvaluje rezervace zvířat na venčení, eviduje zapůjčení a vrácení
    - [x] vytváří požadavky na veterináře

3. veterinář:
    - [x] vyřizuje požadavky od pečovatele (plánuje vyšetření zvířat dle požadavků)
    - [x] udržuje zdravotní záznamy zvířat

4. dobrovolník:
    - [x] rezervuje zvířata na venčení
    - [x] vidí historii svých venčení

5. neregistrovaný uživatel
    - [x] prochází informace o útulku a zvířatech

---

## Tasks

- [x] Dokumentace
- [x] Video
- [x] Submitted

## Náměty na možná rozšíření

sestavování plánu pro medikaci léků zvířatům,
dle vlastní fantazie, popište v dokumentaci…

Dále postupujte dle všeobecného [zadání](https://moodle.vut.cz/mod/page/view.php?id=238239).
