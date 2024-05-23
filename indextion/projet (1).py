import math


def extract_document(corpus):
    document=""
    i=0
    while(i<len(corpus)-1):
        
        if(corpus[i]=="#" and document!=""):
            corpus=corpus[i:]
            return document,corpus
        if(corpus[i]!="#"):
            document+=corpus[i]
        i+=1
        if(corpus[i]==""):
            break
        


def extract_term(end_word):
    word=""
    term=[]
    i=0;j=0
    while(i<(len(document))):
        if((document[i] in end_word) |(document[i]==len(document)-1)):
            if(not(word in stopliste)):
                term.append(word)
            word=""
        else:
            word+=document[i]
        i=i+1
    return term

def term_freq(word,term):
    count=0
    for i in range(len(term)):
        if(word == term[i]):
            count +=1
    return count

def remove_occ(word):
    i=0
    while(i<len(term)):
        if(word == term[i]):
            del term[i]
        i+=1
    return i+1

def write_file_terms(term,min_freq,max_freq,f1,tf,n):
    df=[]

    i=0
    while(i<len(term)):
        f1 = open("terms.txt","a")
        if(min_freq<term_freq(term[i],term)<max_freq):
            ch=term[i]+" "+"document:"+str(n)+" " +"terme :"+str(term_freq(term[i],term))+"\n"
            f1.write(ch)
            df.append(term[i])
            tf.append(term_freq(term[i],term))
            remove_occ(term[i]) 
        i+=1

    f1.close
    return df

def document_freq(df):
    d_df={}
    for i in range (len(df)):
        d_df[df[i]]=term_freq(df[i],df)
        remove_occ(df[i])
    return d_df

def pond_global(pd,num_documents):
    idf = 1/(math.log10(num_documents / (pd) ))
    return idf

def term_count(df,trm):
    for i in range(len(df)):
        c=0
        for j in range(len(trm)):
            if(df[i]==trm[j]):
                c+=1
        df_count[i]=c
    return df_count
    

num_documents=5
end_word={".",","," ","'","0","1","2","3","4","5","6","7","8","9","\n","(",")","<",">"}
min_freq=1
max_freq=11
f = open("corpus.txt","r")
f1= open("terms.txt","w")
f2= open("pond_global.txt","w")
corpus = f.read()
corpus=corpus.lower()
stopliste=["l","d","le","les","des","de","la","dans","un","une","à","ces","ce","ca","sa","ses","se","en","au","est","en","et",""]
i=0
df=[]
tf=[]
trm=[]

d_df={}
df_count=[0]*100
while( i<num_documents):
    i+=1
    n=i
    document,corpus=extract_document(corpus)

    term=extract_term(end_word)
    trm=trm+term
    df+=write_file_terms(term,min_freq,max_freq,f1,tf,n)


df1 = set(df)
df0 = list(df1)
pd=[0]*len(df0)
n=0
f.close()
f = open("corpus.txt","r")
corpus = f.read()
for i in range(len(df0)):
    for j in range(len(df)):
        if(df0[i]==df[j]):
            pd[i]+=1

      


#df_count=term_count(df,trm)
pd_g=[0]*len(df0)
i=0
for i in range (len(df0)):
    f2= open("pond_global.txt","a")
    pd_g[i]=pond_global(pd[i],num_documents)
    ch=df0[i]+" "+" " +"pond_global : "+str(pd_g[i])+"\n"
    f2.write(ch)

f.close()
f1.close()
f2.close()


ch=""
rq=[]
req=str(input("saisir requete:")).lower()
f1= open("terms.txt","r")
f2= open("pond_global.txt","r")
req=req+" "
for i in range(len(req)):
    if(req[i]==" "):
        if(not(ch in stopliste)):
            rq.append(ch+" ")
        ch=""
    else:
        ch+=req[i]


for i in range(len(rq)):
    k=0
    with open("terms.txt","r") as file:
        for line in file:
            line1=line.lower()
            
            if (rq[i] in line1 and rq[i][0]==line1[0]):
                for j in range(len(df0)):
                    if (df0[j]+" "==rq[i]):
                        print(rq[i]," poids: ",pd_g[j]*tf[k])

            k+=1