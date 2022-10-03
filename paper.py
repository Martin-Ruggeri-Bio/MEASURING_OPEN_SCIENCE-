class Paper():
    def __init__(self, title, author, category, email, country, date, institution, open_access):
        self.title = title
        self.author = author
        self.email = email
        self.category = category
        self.country = country
        self.institution = institution
        self.date = date
        self.open_access = open_access

        self.citations = []
        self.count_citations = 0
        self.national_citations = []
        self.count_national_citations = 0
        self.international_citations = []
        self.count_international_citations = 0
        self.country_citations = []
        self.institution_citations = []

        self.citators = []
        self.count_citators = 0
        self.national_citators = []
        self.count_national_citators = 0
        self.international_citators = []
        self.count_international_citators = 0
        self.country_citators = []
        self.institution_citators = []

    def __str__(self):
        cadena=f""" Metrica del Paper
        title: {self.title}\n
        Author: {self.author}\n
        Category: {self.category}\n
        Country: {self.country}\n
        Institution: {self.institution}\n
        Fecha: {self.date}\n

        citations: \n{self.listar_citas()}\n
        National_citations: {self.national_citations}\n
        Cant National citations: {self.count_national_citations}\n
        International citations: {self.international_citations}\n
        Cant International citations: {self.count_international_citations}\n
        Pais de las citas {self.country_citations}\n
        Institucion de las citas {self.institution_citations}\n

        Was citationd: {self.citators}\n
        National_citations: {self.national_citators}\n
        Cant National was citationd: {self.count_national_citators}\n
        International was citationd: {self.international_citators}\n
        Cant International was citationd: {self.count_international_citators}\n
        Country Citators {self.country_citators}\n
        Institution Citators {self.institution_citators}\n

        """
        return cadena
    
    def add_citations(self, paper):
        self.citations.append(paper.title)
        self.count_citations += 1
        if paper.country == self.country:
            self.national_citations.append(paper.title)
            self.count_national_citations += 1
        else:
            self.international_citations.append(paper.title)
            self.count_international_citations += 1
        self.country_citations.append(paper.country)
        self.institution_citations.append(paper.institution)
        paper.increment_citators(self)

    def increment_citators(self, summoner):
        self.citators.append(summoner.title)
        self.count_citators += 1
        if summoner.country == self.country:
            self.national_citators.append(summoner.title)
            self.count_national_citators += 1
        else:
            self.international_citators.append(summoner.title)
            self.count_international_citators += 1
        self.country_citators.append(summoner.country)
        self.institution_citators.append(summoner.institution)

    def list_citations(self):
        citations = ""
        if len(self.citations) > 0:
            for citation in self.citations:
                if citation.title:
                    citations += f"\t{citation.title}\n"
                else:
                    citations += "\t\tNaN\n"
        else:
            citations += "\t\tNaN\n"
        return citations.title

    def list_citators(self):
        citators = ""
        if len(self.citators) > 0:
            for summoner in self.citators:
                if summoner.title:
                    citators += f"\t{summoner.title}\n"
                else:
                    citators += "\t\tNaN\n"
        else:
            citators += "\t\tNaN\n"
        return citators.title
