from data_science import calcular_alianzas, calcular_alianzas2, calcular_fortalezas, calcular_open_access, calcular_prestigio_author_de_una_institucion, data_ciencie
from paper import Paper
from procesador_papers import generar_paper
import random


def main():
    lista_papers = []
    lista_dict_papers = []
    for i in range(1000):
        title, author, category, email, country, date, institucion, open_access = generar_paper()
        paper = Paper(title, author, category, email, country, date, institucion, open_access)
        lista_papers.append(paper)
    for i in range(100000):
        paper = random.choice(lista_papers)
        paper2 = random.choice(lista_papers)
        if paper.title != paper2.title:
            paper.add_citations(paper2)
    for paper in lista_papers:
        lista_dict_papers.append(paper.__dict__)
    data_ciencie(lista_dict_papers)
    calcular_alianzas(lista_dict_papers)
    calcular_alianzas2(lista_dict_papers)
    calcular_fortalezas(lista_dict_papers)
    calcular_open_access(lista_dict_papers)
    calcular_prestigio_author_de_una_institucion(lista_dict_papers)


if __name__ == "__main__":
    main()
