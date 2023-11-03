# Create virtual env

```
python -m venv cosmetic-organizers
```

# Activate virtual env

```
cosmetic-organizers\Scripts\activate.bat
```

# Install Requirements

```
pip install -r requirements.txt
```

# Run a local server 

```
uvicorn main:app --reload
```

# Reste à faire
3. Créer base de données en local
4. Faire la connection base de données avec API en local
5. Créer automatiquement les tables et insertions par défaut quand on lance l'application
6. Implémenter les services 
7. Vérifier tous les endpoints
8. Investiguer sur un projet avec FastAPI comment s'organise les dossiers et reproduire un modèle cohérent
9. Préparer un Docker Compose
10. Regarder Github Actions pour le déploiement avec CICD