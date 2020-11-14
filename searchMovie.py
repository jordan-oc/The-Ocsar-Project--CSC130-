import json

with open('oscar.json') as f:
    data=json.load(f)

# with open('oscarCategories.json') as h:
    # a=json.load(h)
# print(len(a))

# pass in par and a dictionary of movies
# just returns array of dictionaries 
# the dictionaries hold info about a particular movie
# maybe change it so that it returns json instead
def searchByName(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['film']
        if par in val:
            if not nVal in resultsDict:
                resultsDict[nVal]=d[i]
                resultsDict[nVal]['category']=[resultsDict[nVal]['category']]
                arr.append(d[i])
            else:
                resultsDict[nVal]['category'].append(d[i]['category'])
                
    return arr
    
def searchByCategory(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['category']
        nVal = d[i]['film']
        
        if type(val) is list:
            for j in range(0,len(val)):
                if par in val[j]:
                    resultsDict[nVal]=d[i]
                    arr.append(d[i])
                    break
        else:
            if par in val and not nVal in resultsDict:
                resultsDict[nVal]=d[i]
                arr.append(d[i])
                
    return arr

#may need to get rid of name field (we dosent relly have any relevance now)   
def searchByYear(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['year']
        nVal = d[i]['film']
        if par == val:
            if not nVal in resultsDict:
                resultsDict[nVal]=d[i]
                resultsDict[nVal]['category']=[resultsDict[nVal]['category']]
                arr.append(d[i])
            else:
                resultsDict[nVal]['category'].append(d[i]['category'])
                
    return arr
    
# def searchByCategoryAndYear(category, year, d):
    # resultsDict={}
    # arr=[]
    # for i in range(0,len(d)):
        # val = d[i]['category']
        # nVal = d[i]['film']
        # if(category in val and not nVal in resultsDict):
            # resultsDict[nVal]=d[i]
            
    # newDict={}        
    # a=resultsDict.items()
    # for k,v in a:
        # if resultsDict[k]['year'] == year:
            # newDict[k]=v
    # return newDict

def searchByWinner(par, d):
    if type(par) != bool:
        print("error, value passed to searchByWinner must be a bool")
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['winner']
        nVal = d[i]['film']
        if par == val:
            if not nVal in resultsDict:
                resultsDict[nVal]=d[i]
                resultsDict[nVal]['category']=[resultsDict[nVal]['category']]
                arr.append(d[i])
            else:
                resultsDict[nVal]['category'].append(d[i]['category'])
                
    return arr

if __name__ == '__main__':
    # returns a dictionary with key name of film

    #manual tests   
    #print(searchByCategory("BEST PICTURE", data))
    #print(searchByYear(1934, data))
    #print(searchByWinner(True, data))
    #print(searchByCategoryAndYear("BEST PICTURE", 1989, data))
    #print(searchByName("Jo", data))

    print( json.dumps(searchByCategory("BEST PICTURE", searchByYear(1997, data))) ) 


    #get different categories
    # resultsDict={}
    # for i in range(0,len(d)):
        # movieName = d[i]['category']
        # if(not (movieName in resultsDict)):
            # resultsDict[movieName]=d[i]

    # arr=[]        
    # for k in resultsDict.keys():
        # arr.append(k)
    # arr.sort()
    # for i in arr:
        # print(i)

    # with open("oscarCategories.json", "w") as out:
        # json.dump(arr, out)
        
        
        
        
        
        
        
        

    # search = "Good Will Hunting"
    # results = []


    # for i in range(0,len(d)):
      # if(d[i]['entity']== search):
        # results.append(d[i])
        # break

    #prints out search results
    #print(str(results) + '\n')

    #prints out search results filtered by category
    #s =sorted(results, key = lambda t: t['category'])
    print("printing from searchMovie.py")
    