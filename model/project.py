from sys import maxsize


class Project:
    def __init__(self, projectname=None):
        self.id = None
        self.projectname = projectname

    def __repr__(self):
        return "%s" % self.projectname

    def __eq__(self, other):
        return self.projectname == other.projectname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
