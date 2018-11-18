from docx.shared import Pt


# Editors and translators are tuples, version is an ordinal number. num is a tuple like vol, num.
class Citation(object):
    def __init__(self, **kwargs):
        self.currentCitation = None
        self.data = kwargs
        self.keys = self.data.keys()

    # Adds a part (text) to the citation (cit)
    def add(self, text, italic=False):
        assert(self.currentCitation is not None)
        a = self.currentCitation.add_run(text)
        a.font.name = "Times New Roman"
        a.font.size = Pt(12)
        if italic:
            a.italic = True

    def write(self, document):
        cit = document.add_paragraph()
        self.currentCitation = cit
        if "author" in self.keys:
            self.add(self.data["author"] + ". ")
        if "title" in self.keys:
            if self.data["title"][0] == '"':
                self.add(self.data["title"] + ". ")
            else:
                self.add(self.data["title"] + '. ', italic=True)
        if "container" in self.keys:
            self.add(self.data["container"] + ", ")

        # Not worth implementing editors and translators currently

        if "version" in self.keys:
            self.add(self.data["version"] + " ed., ")
        if "num" in self.keys:
            self.add("vol. " + self.data["num"][0] + ", no. " + self.data["num"][1] + ", ")
        if "publisher" in self.keys:
            self.add(self.data["publisher"] + ", ")
        if "pubdate" in self.keys:
            self.add(self.data["pubdate"] + ", ")
        if "location" in self.keys:
            self.add(self.data["location"] + ", ")
        if "url" in self.keys:
            if "//" in self.data["url"]:
                self.add(self.data["url"].split("//")[1] + ". ")
            else:
                self.add(self.data["url"] + ". ")
        if "accessdate" in self.keys:
            self.add("Accessed " + self.data["accessdate"] + ".")

    def getFirst(self):
        if "author" in self.keys:
            return self.data["author"] + " " + self.data["title"]
        else:
            return self.data["title"]
