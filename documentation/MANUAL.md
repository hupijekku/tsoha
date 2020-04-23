# Käyttöohje
## Kuinka käytät sovellusta
Sivun ylälaidassa on navigaatiopalkki, jonka avulla voit liikkua sovelluksen sisällä sivulta toiselle.  
Navigaatiopalkin oikeassa reunasta löydät napit sekä sovellukseen rekisteröitymiseen sekä sisäänkirjautumiseen.  

### Reseptin lisääminen
Kirjauduttuasi sisään, voit navigaatiopalkista painaa "Add a post", jolloin siirryt reseptinluontinäkymään.  
Anna reseptillesi sopiva otsikko ja sisältö, ja paina sitten "Add post", niin resepti tallentuu sovellukseen.  

### Reseptien katsominen, muokkaaminen ja poistaminen
Painamalla navigaatiopalkista "List posts", voit selata sovellukseen lisättyjä reseptejä.  
Mikäli olet kirjautunut sisään, voit myös äänestää reseptejä joista pidät painamalla vihreää "Vote" nappia.  
Voit myös muokata tai poistaa omia reseptejäsi tältä sivulta painamalla punaista "Delete" tai sinistä "Edit" nappia.  

## Asennusohje
Sovelluksen suorittamiseksi paikallisella koneella tarvitset Python 3:n.  
Sovelluksen riippuvuudet voit asentaa juurikansiossa komennolla  
```
pip install -r requirements.txt
```
Riippuvuuksien asentamisen jälkeen sovelluksen voi suorittaa ajamalla _run.py_-tiedoston.  
  
Mikäli haluat käyttää sovellusta esimerkiksi Herokussa, määritä herokuun ympäristömuuttuja
```
heroku config:set HEROKU=1
```
ja lisää sovellukselle tietokanta:
```
heroku addons:add heroku-postgresql:hobby-dev
```
