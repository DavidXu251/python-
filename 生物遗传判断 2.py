
disease_type=None
def exist(*args):
    return (None not in set(args))

class P:
    def __init__(self,sick=None,male=None,
                 gene={'AA','Aa','aa'}):
        self.sick=bool(sick)
        self.male=bool(male)
        if type(gene)==str:
            self.gene=set([gene])
        elif type(gene)==set:
            self.gene=gene


def family(father,mother,*args):
    global have_new_info
    possible_gene=set()
    for gene in father.gene:
        possible_gene.update(set(gene))
    for gene in mother.gene:
        possible_gene.update(set(gene))
    for kid in args:
        
    pass


a1=P(gene={'AA'})
a2=P(gene={'AA'})
a3=P(male=1)

def describe():
    family(a1,a2,a3)


have_new_info=False
while have_new_info:
    describe()
print(a3.gene)






