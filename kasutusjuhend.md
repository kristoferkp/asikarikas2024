# II - Piletid
Piletite veebirakendus ASI Karikas võistluse jaoks.
Veebileht on ehitud [Nuxt3](https://nuxt.com) ja [Supabase](https://supabase.com) projektidega.
Supabase-iga tuleb kaasa PostgreSQL andmebaas, authentimise teenus jm.

# Demo
Kasutage ette tehtud demo:
[asi.kristoferp.com](https://asi.kristoferp.com)

Kasutage demo, kuna ise hostimine vajab terve Supabase'i uuseti konfigureerimist. 

## Ise hostimine

Liigu piletid kausta, kus on 2. ülesande failid
```
cd 'II - Piletid'
```

Ole kindel, et Node.js on installitud, kui ei ole installi see
```
F:\asikarikas2024\II - Piletid> winget install nodejs
```

```
F:\asikarikas2024\II - Piletid> node
Welcome to Node.js v21.6.0.
Type ".help" for more information.
>
```

Installi kõik vajalikud moodulid
```
npm install
```
## Supabase'i enda infrastruktuur
Üks võimalus (soovitatuslik) on kasutada Supabase'i enda infrastrukuuri AWS peal. Tasuta kasutajaga saab kaasa lõpmatult API päringuid ja 50,000 aktiivset kasutajat kuus, mis on piisav meie väikese veebilehe jaoks.

Kasutades [dokumentatsiooni](https://supabase.com/docs/reference/cli/supabase-db) on võimalik lisada remote Supabase'i schema.sql fail, mis asub supabase kaustas.

### Self-hosting
[Selle dokumendi](https://supabase.com/docs/guides/self-hosting) järgi peaks olema lihtne püstidada oma Supabase.

## Deployment, development
Erinevad hostingu pakkujad: [Nuxt Deploy](https://nuxt.com/deploy)

Development server
```
npm run dev -- -o
```

Deployment port 3000 peal
```
npm run build
```


# Kuidas kasutada

Minnes demo lehele on näha suurt teksti ja kahte nuppu, Osta pilet ja Kontrolli piletit. Navigatsiooni riba ja jalust.

### Navigeerida saab erinevate lehekülgede vahel kasutades navigatisooni menüüd. 

- Kodu - Viib tagasi põhilehele.
- Kontrolli piletit - Viib pileti kontrollimis lehele
- Osta pilet - Viib pileti ostmise lehele.
- Logi sisse/ Kasutaja - Oleneb sellest, kas kasutaja on sisse loginud või ei. Viib kasutaja lehele.
- Kuu/Päikese nupp - muudab veebilehe teemat, must või valge.

### Logi sisse
Vajutades logi sisse nuppu, tuleb ette sisse logimise leht. Sisse logimiseks on kaks võimalust, emaili maagiline link ja Github. Kui valida maagiline link, saadetakse sulle link, et sisse logida on vaja lihtsalt vajutada lingile, mis tuli emailile. Kui valida GitHub, pead sa sisse logima oma Github'i kasutajaga ning autoriseerima Piletirongi veebilehe.

Olles sisse loginud, muutub Logi sisse nupp Kasutaja nupuks, vajutades sellele, jõuad kasutaja lehele. Seal saad muuta oma emaili aadressi, kasutajanime. Saad näha oma ostetud pileteid, nende andmeid ning ka ostu numbreid. Siin lehel saad ka lisada kasutajale profiilipildi. Lõpuks saab ka välja logida.

### Kontrolli piletit
See lehekülge laseb sul kontrollida, kas pilet on süsteemis olemas või ei. Pileti numbri (tegelikult purchase_id) leiad oma kasutaja alt, selle pärast peab olema ostmisel sisse logitud kasutajasse, et siduda pileti ost kasutajaga.

### Osta pilet
Leheküljel on kaks kasti, esimene on sihtkoht, teine on lähtekoht. Sisesta linnad ning vajuta "Leia pilet". Kui andmebaasis on need olemas, lisandub tabelisse pilet kõikide andmetega. 

Funktsioon leiab kõik piletid, kus on tõene üks tingimustest: esimene tingimus kontrollib, kas muutuja “to_city” vastab sihtkoha väärtusele, ja kui “from_city” vastab lähtkoha väärtusele või kui “from_city” on olemas JSONB veerust nimega “stops”. Teine tingimus on sarnane, kuid kontrollib, kas “from_city” vastab määratud väärtusele, ja kui “to_city” vastab mõnele muule määratud väärtusele või kui “to_city” on samas “stops” massiivis olemas. 

Selle funktsiooniga on võimalik leida kõik piletid, mis lähevad ühest kohast teise, ning piletid millel on peatus, kuhu kasutaja soovib minna.

Kui kasutaja leiab pileti, millele ta soovib minna, saab ta vajutada osta nuppu, mis viib ta /pilet veebilehele, et oma ostu kinnitada.

Pileti info leheküljel on näha kõiki andmeid, k.a. peatuste listi. Vajutades Osta, küsib veebileht, kas kasutaja on kindel, et soovib selle pileti osta. Kui kasutaja vajutab jah, saab tema ost lisatud andmebaasi, tema kasutaja alla. Kasutaja saab ka enda kasutajaga seotud emailile kirja, et tema ost on kinnitatud.