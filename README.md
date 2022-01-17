MNIST with cookiecutter organisation
==============================

M6 exercise.

The way to run this project is as follow:

>make data
will do the data preprocessing. It will run `src/data/make_dataset.py` and will take the data from `data/raw` and process into `data/processed`.

>make train
will train the data in  `data/processed` and returns the model in `models/trained_model`. I'll think of a way to have multiple model and chose them in the argument.

>make evaluate
will make prediction on generated example from the test set `data/examples/example_images.npy`.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── .github
    │   └── workflows 
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │    └── trained_model    
    │    └── model.py
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── tests 
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
## Missing
### M6
- [] src/visualization/visualize.py
### M7
- [] Go over the most complicated file in your project. Be critical and add comments where the logic behind the code is not easily understandable.
- [] Add docstrings to at least two python function/methods.
### M8
- [] dvc

### M10
- [] hydra on mnist (same as vae)

### M13
- [] create report you can share

### M14
- [] Pytorchlignting (All)
### M15 
- [] Pytest that works
- [] Github action that works
- [] Auto linter that works


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
