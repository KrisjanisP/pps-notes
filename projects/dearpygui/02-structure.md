## DPG (DearPyGUI) struktūra:

Main skriptam vienmēr:
* jāizveido & jāiznīcina konteksts
* jāizveido & jāparāda skats
* jāuzstāda & jāsāk DPG

```python
.create_context()
.create_viewport()
.setup_dearpygui()
.show_viewport()
.start_dearpygui()
.destroy_context()
```

## Konteksts

Ja `create_context` nebūs pirmā DPG komanda, tad DPG visdrīzāk uzmetīs kļūdu un python process nomirs.

Es, ja godīgi, nesaprotu, kāds ir tā pielietojums.

## Skats
Kas ir "skats"? Skats DPG ir pats logs, ko izveido operētājsistēma.

`show_viewport` jāizsauc pirms `start_dearpygui`.

## Zīmēšanas cikls
Zīmēšanas cikls ir atbildīgs par lietu parādīšanu, stāvokļa uzturēšanu.

Parasti zīmēšanas ciklu izveido `start_dearpygui` taču dažreiz ir nepieciešams to izveidot manuāli, lai izsaukt python komandas, kuras, iespējams, nepieciešams palaist katru kadru.

Zīmēšanas cikls jāveido pēc `setup_dearpygui` izsaukšanas.

## Elementi

Elementu izveides komanda vienmēr sākas ar `add_`.

Katrai lietai ir sava unikāla birka jeb `tag`.

## Galvenais logs
DPG vienam logam var piešķirt galvenā loga statusu.

Galvenais logs aizpilda visu skatu un vienmēr tiek zimēts aiz citiem logiem.

`set_primary_window(window, True)`