from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.events import GoToEvent
from pydantic import BaseModel

# TO DO
class MyType(BaseModel):
  name: str
  icon: c.Image
my_object = MyType(name="meowzer", icon=c.Image(src="./assets/JB_pic.png"))

app = FastAPI()


def layout(*components: AnyComponent, title: str) -> list[AnyComponent]:
    return [
        c.PageTitle(text=""),
        c.Navbar(
            title="JONATHAN BOUCHET",
            title_event=GoToEvent(url="/about"),
            start_links=[
                c.Link(
                    components=[c.Text(text="About")],
                    on_click=GoToEvent(url="/about"),
                    active="startswith:/about",
                ),
                c.Link(
                    components=[
                        c.Markdown(text="Resume")
                        ],
                    on_click=GoToEvent(url="/resume"),
                    active="startswith:/resume",
                ),
                c.Link(
                    components=[
                        c.Markdown(text="Portfolio")
                        ],
                    on_click=GoToEvent(url="/data_analysis"),
                    active="startswith:/data_analysis",
                ),
                c.Link(
                    components=[
                        c.Markdown(text="Contact")
                        ],
                    on_click=GoToEvent(url="/contact"),
                    active="startswith:/contact",
                ),
            ],
        ),
        c.Page(components=components),
        c.Footer(
            links=[
                c.Link(components=[c.Text(text='Made with FastUI')], on_click=GoToEvent(url='https://docs.pydantic.dev/fastui/')),
            ],
        ),
    ]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return layout(
        c.Text(text="""
Customer oriented data scientist with proven ability of delivering valuable insights via data analytics.
7+ years of professional experience in developing cutting-edge machine learning solutions for insurance leaders.
"""), 
    title="home")


@app.get("/api/about", response_model=FastUI, response_model_exclude_none=True)
def page_about() -> list[AnyComponent]:
    return layout(
            c.Text(text="""
    Customer oriented data scientist with proven ability of delivering valuable insights via data analytics.                    
    7+ years of professional experience in developing cutting-edge machine learning solutions for insurance leaders.
    """),
title="About Me")


@app.get("/api/resume", response_model=FastUI, response_model_exclude_none=True)
def page_about() -> list[AnyComponent]:
    return layout(c.Markdown(text="""
# Work Experience
### Freelance, Aug 2024 - Nov 2024
Director of Data Science
- Market and Customer Research for a GenAI project
- Evaluation and experimentations of RAG system, Security and Compliance, Prompt Optimization, Voice Feature.

### Freelance, March 2024 - May 2024
Director of Data Science

- roadmap design around transforming customer technology landscape to better support their strategic goals and operational efficiency.

### Entefy, Jan 2023 - July 2023
Senior Data scientist                            

- Developed and deployed models for bitcoin prediction.
- Developed and deployed models to extract instructed data from documents.
- Developed and deployed OCR pipeline.
- Developed models for search query understanding.
                             
### Omniscience, May 2020 - June 2022
Lead Data Scientist                        
- Developed triage and classification models for life insurance underwriting (north American insurer)
- Developed classification models for life insurance underwriting (top 5 in Canada), including ETL, data exploration, features engineering, modeling and final reporting.
- Developed supervised machine learning model for data aggregation platform for worker compensation insurance (top 25 in the U.S. carriers), based on phonetic algorithms.
- Supported Sales team by prototyping machine learning models and use of internal optical character recognition model.
- Contributed to RiskOPs product development.
- Facilitated evaluations and coordination with data provider.
- Mentored team, created robust process resulting in constant inflow of PhDs from Stanford and Caltech.

### Omniscience, Oct 2017 – May 2020
Data Scientist                             
- Developed predictive model capabilities for U.S. Customs and Borders Protections for their Global Travel Assessment system
- Developed supervised machine learning model for data aggregation platform for worker compensation insurance (top 25 in the U.S. carriers), based on phonetic algorithms.
- Developed classification models for loan mortgages for a north American bank (top 10 banks in Canada)
- Facilitated evaluations and coordination with data provider.
                             
### Kent State University, April 2008 – Aug 2016
Research Scientist                            
- Software coordinator of the Silicon Strip Detector, responsible for developing and maintaining offline code used for raw data evaluation of SSD.
- Data analysis of the STAR experiment (Brookhaven National Laboratory, Long Island, NY) for particle identification with the use of machine learning algorithm.
                             
# Education
- Oct 2007 Doctor of Philosophy (Ph.D.) in Nuclear Physics 
FACULTÉ DES SCIENCES, UNIVERSITÉ DE NANTES, NANTES, FRANCE
                             
# Technical Skills
- Programming Languages: Python | R Programming | C++
- Data analysis: ROOT | NumPy, Scikit | Pandas
- Software: Linux | UNIX | R studio | Spark
- Databases: SQL(intermediate), MongoDb(intermediate)
- Front end: React(beginner to intermediate), Vue(beginner to intermediate)
- Back end: FastAPI, Google GCS
    """), title="resume")


@app.get("/api/contact", response_model=FastUI, response_model_exclude_none=True)
def page_contact() -> list[AnyComponent]:
    return layout(c.Markdown(text="""
- [Linkedin](https://www.linkedin.com/in/jonathanbouchet/)
- [Kaggle](https://www.kaggle.com/jonathanbouchet/)
- [GitHub](https://github.com/jonathanbouchet)
- [R Publications](https://rpubs.com/jonathanbouchet)                                                                 
"""), title="Contact Page!")


@app.get("/api/data_analysis",response_model=FastUI, response_model_exclude_none=True)
def page_contact() -> list[AnyComponent]:
    return layout(c.Markdown(text="""
# Kaggle
A list of selected data analysis published on `Kaggle`
                                                          
- [F1 Data analysis](https://www.kaggle.com/code/jonathanbouchet/f1-data-analysis):
    - data visualization, notebook in `R`                          
- [U.S. Commercial Flights Tracker Map](https://www.kaggle.com/code/jonathanbouchet/u-s-commercial-flights-tracker-map)
- data visualization, notebook in `R`  
- [GOOOOOAAAAALLLLLL !!!!!!!!!!!!](https://www.kaggle.com/code/jonathanbouchet/goooooaaaaallllll):
    - data visualization, ML for winner prediction, notebook in `R`  
- [Forecasting Beijing's housing](https://www.kaggle.com/code/jonathanbouchet/forecasting-beijing-s-housing):
    - data visualization, ML for price of House, notebook in `R`
- [Age of empire Winner prediction](https://www.kaggle.com/code/jonathanbouchet/base-dataset-winner-s-prediction):
    - data visualization, ML for AOE's games winner, ensemble of tuned classifiers, notebook in `python`
- [Recommendation systems for MetaQuest market places](https://www.kaggle.com/code/jonathanbouchet/recommendation-systems-for-metaquest-market-places):
    - data visualization, Recommendation systems, NLP, content based and collaborative filtering, notebook in `python`
- [League Of Legends data: 2 days snapshot on Korean server](https://www.kaggle.com/code/jonathanbouchet/lol-data-2-days-snapshot-on-kr-server):
    - data visualization, time series, LSTM, Keras, notebook in `python` 
- [Genshin Impact(patch 3.1) Voice lines analysis](https://www.kaggle.com/code/jonathanbouchet/genshin-impact-patch-3-1-voice-lines-analysis):
    - data visualization, NLP, Topic Modelling, notebook in `python`  
                             
# Apps.
                             
- [Pokemon App](https://jonathanbouchet.shinyapps.io/pokeData/):
    - mean characteristics of Pokemon (gen 1-6) with radarcharts, `R shiny`, data analysis 
- [Cities Transportation System](https://jonathanbouchet.shinyapps.io/transport_visualization/):
    - Visualization and historical data plots of Transportayion System from several world cities, data from Kaggle, via citylines.co data, `R shiny`, data analysis  
                             
# Scientific Publications
- [Identification of charmed mesons using Multivariate analysis in STAR](https://iopscience.iop.org/article/10.1088/1742-6596/396/2/022007/meta)
- [Charmed decay reconstruction using a microvertexing technique with the STAR Silicon Detectors](https://pos.sissa.it/cgi-bin/reader/contribution.cgi?id=135/031)
- [Heavy Flavor Tracker (HFT) : A new inner tracking device at STAR](https://arxiv.org/abs/0907.3407)
                                                                                                                                   
"""), title="portfolio")


@app.get("/{path:path}")
def root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Navigation"))