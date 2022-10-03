from pandas import json_normalize
import pandas as pd
import json
import numpy as np


def data_ciencie(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    df.to_csv('dataframe_papers.csv')

def calcular_alianzas(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    mask = (df['date'] > 2010) & (df['date'] <= 2022) & (df['country'] == 'Argentina') 
    alianzas_arg=df.loc[mask]
    alianzas_arg= alianzas_arg.groupby(['category'])
    alianzas_arg = alianzas_arg.agg({'count_citations': 'sum','title': 'count'}).sort_values(by=['count_citations'], ascending=False)
    alianzas_arg = alianzas_arg.rename(columns={'title':'papers'})
    alianzas_arg.to_csv('alianzas_arg_1.csv')

def calcular_fortalezas(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    mask = (df['date'] > 2010) & (df['date'] <= 2022) & (df['category'] == 'Astronomy')
    fortalezas_astronomy=df.loc[mask]
    fortalezas_astronomy= fortalezas_astronomy.groupby(['country'])
    fortalezas_astronomy = fortalezas_astronomy.agg({'count_citations': 'sum', 'count_national_citations': 'sum', 'count_international_citations': 'sum','count_citators': 'sum', 'count_national_citators': 'sum', 'count_international_citators': 'sum',  'title': 'count'}).sort_values(by=['count_citators','count_international_citators'], ascending=False)
    fortalezas_astronomy = fortalezas_astronomy.rename(columns={'title':'papers'})
    fortalezas_astronomy['Indice_colaboracion_cientifica_internacional'] = fortalezas_astronomy['count_international_citators']/fortalezas_astronomy['papers']
    fortalezas_astronomy['Indice_colaboracion_cientifica_nacional']  = fortalezas_astronomy['count_national_citators']/fortalezas_astronomy['papers']
    fortalezas_astronomy['Tendencia_Global'] = fortalezas_astronomy['count_international_citators']/fortalezas_astronomy['count_national_citators']
    fortalezas_astronomy['Indice_Colaboracion_General'] = fortalezas_astronomy['count_international_citators']+fortalezas_astronomy['count_national_citators']
    fortalezas_astronomy.replace([np.inf, -np.inf], np.nan, inplace=True) 
    fortalezas_astronomy.to_csv('fortalezas_astronomy.csv')

def calcular_alianzas2(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    mask = (df['date'] > 2010) & (df['date'] <= 2022) & (df['country'] == 'Argentina') & (df['category'] == 'Astronomy')
    alianzas_arg_2=df.loc[mask]
    alianzas_arg_2.to_csv('alianzas_arg_2.csv')


def calcular_open_access(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    open_access = df.groupby(['country','open_access'])
    open_access = open_access.agg({'count_citations': 'sum', 'count_national_citations': 'sum', 'count_international_citations': 'sum','count_citators': 'sum', 'count_national_citators': 'sum', 'count_international_citators': 'sum',  'title': 'count'})
    open_access = open_access.rename(columns={'title':'papers'})
    open_access['Indice_colaboracion_cientifica_internacional'] = open_access['count_international_citators']/open_access['papers']
    open_access['Indice_colaboracion_cientifica_nacional']  = open_access['count_national_citators']/open_access['papers']
    open_access['Tendencia_Global'] = open_access['count_international_citators']/open_access['count_national_citators']
    open_access['Indice_Colaboracion_General'] = open_access['count_international_citators']+open_access['count_national_citators']
    open_access.replace([np.inf, -np.inf], np.nan, inplace=True) 
    open_access.to_csv('open_access.csv')

def calcular_prestigio_author_de_una_institucion(json_papers):
    json_papers = json.dumps(json_papers)
    json_papers = json.loads(json_papers)
    df = json_normalize(json_papers)
    mask = (df['country'] == 'Argentina')
    prestigio_author=df.loc[mask]
    prestigio_author = prestigio_author.groupby(['author', 'email', 'institution'])
    prestigio_author = prestigio_author.agg({'count_citators': 'sum', 'count_national_citators': 'sum', 'count_international_citators': 'sum',  'title': 'count'})
    prestigio_author = prestigio_author.rename(columns={'title':'papers'})
    prestigio_author['Indice_colaboracion_cientifica_internacional'] = prestigio_author['count_international_citators']/prestigio_author['papers']
    prestigio_author['Indice_colaboracion_cientifica_nacional']  = prestigio_author['count_national_citators']/prestigio_author['papers']
    prestigio_author['Tendencia_Global'] = prestigio_author['count_international_citators']/prestigio_author['count_national_citators']
    prestigio_author['Indice_Colaboracion_General'] = prestigio_author['count_international_citators']+prestigio_author['count_national_citators']
    prestigio_author.replace([np.inf, -np.inf], np.nan, inplace=True) 
    prestigio_author.to_csv('prestigio_author.csv')
