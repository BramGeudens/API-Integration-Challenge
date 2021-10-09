#!/usr/bin/env python3

#importeren van gebruikte libraries.
import requests 
import urllib.parse
from prettytable import PrettyTable

APIv4_key = <<plaats hier uw api key>> #api v4 token 
link = "https://api.themoviedb.org/3/search/movie?" # Dit is de originele link om met de API op te zoeken.

while True: # Het programma gaat door tot er een break komt.
    
    Movie_name = input("Geef de naam van de film die u wilt vinden (s of stop om het programma af te sluiten): ") # We vragen input van de gebruiker om een film te zoeken.
    if Movie_name == "stop" or Movie_name == "s": # Wanneer de gebruiker een s of stop typt, gaat het programma afsluiten.
            break
    else : # Indien er iets anders dan s of stop staat 
        headers = {'authorization': 'Bearer ' + APIv4_key} # Dit is een header die we nodig hebben voor de authentication met Bearer token.

        volledige_url = link + urllib.parse.urlencode({"query":Movie_name}) # Maken van de URL om data van de API op te vragen.

        json_data = requests.get(volledige_url, headers=headers) # We vragen data op van de API door een get request te doen naar onze gemaakte url. Deze word geauthenticeerd door de header met de bearer token.
        status_code = json_data.status_code #we vragen de status code van onze request op.
        json_data = json_data.json() 
        json_status = json_data["total_pages"] # We vragen op hoeveel pagina's er gevonden zijn.
        movie_data = json_data["results"] # We vragen naar de data van de films om hier nadien gegevens uit te halen.

        if json_status == 0: # Als er geen films gevonden zijn krijg je de melding dat er geen gegevens gevonden zijn.
            print('Er zijn geen resultaten gevonden in de TMDB voor: ' + Movie_name)
        else: # Als er gegevens gevonden zijn voor de naam van de film.
            
            myTable = PrettyTable(["Film naam", "Taal", "datum van publicatie", "aantal stemmen"])# We maken een tabel met verschillende kolommen.
            
            # We plaatsen gegevens in de tabel.
            i = 0
            while i < len(json_data["results"]): # We kijken hoeveel films er zijn gevonden en gaan zo voor elke film de gegevens uitlezen en in de tabel zetten.
                
                myTable.add_row([movie_data[i]['title'], movie_data[i]['original_language'], movie_data[i]['release_date'], movie_data[i]['vote_count']])
                i += 1
            print('we hebben ' + str(len(json_data["results"])) + ' films gevonden voor ' + Movie_name) # we zorgen ervoor dat de gebruiker een overzicht krijgt met wat er gevonden is.
            print(myTable) # We laten de tablel zien.
            




