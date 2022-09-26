## DPG (DearPyGUI) struktūra:
* uzstādīšana
* konsteksts
* skats
* zīmēšanas cikls
* "lietas"
* primārais logs

Main skriptam vienmēr jāizpilda:
1. konteksta izveide `create_context`
2. skata izveide `create_viewport`
3. DPG uzstādīšana `setup_dearpygui`
4. DPG startēšana `start_dearpygui`
5. konteksta iznīcināšana `destroy_context`

To izklāstot savadāk, vienmēr:
* jāizveido & jāiznīcina konsteksts
* jāizveido & jāparāda skats
* jāuzstāda & jāsāk DPG

## Konteksts
Ja `create_context` nebūs pirmā DPG komanda, tad DPG visdrīzāk uzmetīs kļūdu un python process nomirs.

Es, ja godīgi, nesaprotu, kāds ir tā pielietojums.

## Skats
Kas ir "skats"? Skats ir logs, ko izveido operētājsistēma.

Ja `show_viewport` netiks izsaukts pirms `start_dearpygui`, tad DPG visdrīzāk uzmetīs kļūdu un python process nomirs.

## Zīmēšanas cikls
Zīmēšanas cikls ir atbildīgs par lietu parādīšanu, stāvokļa uzturēšanu.

Parasti zīmēšanas ciklu izveido `start_dearpygui` taču dažreiz ir nepieciešams to izveidot manuāli, lai izsaukt python komandas, kuras, iespējams, nepieciešams palaist katru kadru.

Zīmēšanas cikls jāveido pēc `setup_dearpygui` izsaukšanas.

## "Lietas"

DPG "lietas" tiek iedalītas trīs grupās: **Items**, **UI Items**, **Containers**.

**Items**: jebkas, kas ir bibliotēkā? es nez.

**UI Items**: lietas, kam piemīt vizuāls aspekts.

**Containers**: lietas, kas var saturēt citas lietas.

Man personīgi izskatās, ka *Items* iedalās *UI Items* un *Containers*.

Lietu izveides komandas vienmēr sākas ar `add_`.

Katrai lietai ir sava unikāla birka jeb *tag*.


## Galvenais logs
DPG var vienam logam piešķirt galvenā loga statusu.
Galvenais logs aizpildīs visu skatu un vienmēr tiks zimēts aiz citiem logiem.