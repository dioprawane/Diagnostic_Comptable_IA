# Diagnostic Comptable IA

Ce projet est une application web de diagnostic comptable utilisant l'API OpenAI pour détecter les anomalies dans les écritures comptables et analyser les états financiers. L'application est développée avec Flask et permet d'entrer les données soit par saisie directe, soit en téléchargeant des fichiers de différents formats (CSV, Excel, JSON).

## Fonctionnalités

- Analyse des écritures comptables pour détecter les anomalies.
- Analyse des états financiers pour fournir une analyse détaillée.
- Support de l'entrée des données via texte ou téléchargement de fichier (CSV, Excel, JSON).

## Prérequis

- Python 3.7 ou supérieur
- Un compte OpenAI avec une clé API

## Installation

1. Clonez le repository :

    ```bash
    git clone https://github.com/dioprawane/Diagnostic_Comptable_IA.git
    cd Diagnostic_Comptable_IA
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement :

    Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Utilisation

1. Lancez l'application Flask :

    ```bash
    python app.py
    ```

2. Ouvrez votre navigateur et allez à l'adresse suivante :

    ```
    http://127.0.0.1:5000
    ```

3. Utilisez l'interface web pour entrer vos données comptables ou téléchargez un fichier à analyser.

## Structure du Projet

- `app.py` : Le fichier principal de l'application Flask.
- `templates/` : Contient les fichiers HTML pour l'interface utilisateur.
  - `index.html` : Page principale pour entrer les données.
  - `result.html` : Page pour afficher les résultats de l'analyse.
- `static/` : Contient les fichiers statiques (CSS, JavaScript).
  - `style.css` : Fichier de style pour l'interface utilisateur.
- `.env` : Fichier pour stocker les variables d'environnement (clé API OpenAI).
- `requirements.txt` : Liste des dépendances Python nécessaires.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Fork le repository
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/new-feature`)
3. Commitez vos modifications (`git commit -m 'Ajouter une nouvelle fonctionnalité'`)
4. Poussez votre branche (`git push origin feature/new-feature`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- **Diop Rawane** - *Développeur principal* - [dioprawane](https://github.com/dioprawane)

---

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à me contacter directement.

