import json

with open('oscar.json') as f:
    data=json.load(f)

# with open('oscarCategories.json') as h:
    # a=json.load(h)
# print(len(a))

# pass in par and an array of dictionaries containing movie info
# returns array of dictionaries 
# the dictionaries hold info about a particular movie
# the movie category field are in upper case
def searchByName(par, d):
    resultsDict={}
    arr=[]
    for i in range(0,len(d)):
        val = d[i]['film']
        if par.upper() in val.upper():
            if not val in resultsDict:
                resultsDict[val]=d[i]
                if not type(resultsDict[val]['category']) is list:
                    resultsDict[val]['category']=[resultsDict[val]['category']]
                arr.append(d[i])
            else:
                resultsDict[val]['category'].append(d[i]['category'])
                
    return arr
    
def searchByCategory(par, d):
# ISSUE: want to try and include other categories as well
# right now, even though the movie may have won 2 oscar categories, only 1 category is being displayed for the movie 
    resultsDict={}
    arr=[]
    par=par.upper()
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
                if not type(resultsDict[nVal]['category']) is list:
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
                if not type(resultsDict[nVal]['category']) is list:
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
    
    #test search by name
    x=searchByName("Titanic", data)
    jsonTest = [{'year': 1953, 'category': ['ART DIRECTION (Black-and-White)', 'WRITING (Story and Screenplay)', 'ACTRESS IN A LEADING ROLE', 'ACTRESS IN A SUPPORTING ROLE', 'ART DIRECTION', 'CINEMATOGRAPHY', 'COSTUME DESIGN', 'DIRECTING', 'FILM EDITING', 'MAKEUP', 'MUSIC (Original Dramatic Score)', 'MUSIC (Original Song)', 'BEST PICTURE', 'SOUND', 'SOUND EFFECTS EDITING', 'VISUAL EFFECTS'], 'name': 'Art Direction:  Lyle Wheeler, Maurice Ransford;  Set Decoration:  Stuart Reiss', 'film': 'Titanic', 'winner': False}]
    if( x == x ):     
        resultsDict={}
        arr=[]
        for i in range(0,len(data)):
            val = data[i]['film']
            if "Titanic".upper() in val.upper():
                if not val in resultsDict:
                    resultsDict[val]=data[i]
                    if not type(resultsDict[val]['category']) is list:
                        resultsDict[val]['category']=[resultsDict[val]['category']]
                    arr.append(data[i])
        if(jsonTest == x):
            print("pass")
        else:
            print("fail")

    x=searchByName("Scooby doo", data)
    if( x == x ):     
        resultsDict={}
        arr=[]
        for i in range(0,len(data)):
            val = data[i]['film']
            if "Scooby doo".upper() in val.upper():
                if not val in resultsDict:
                    resultsDict[val]=data[i]
                    if not type(resultsDict[val]['category']) is list:
                        resultsDict[val]['category']=[resultsDict[val]['category']]
                    arr.append(data[i])
        if not x:
            print("pass")
        else:
            print("fail")  

#test searchByCategory





























    #print( json.dumps(searchByCategory("BEST PICTURE", searchByYear(1997, data))) ) 


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
    #print("printing from searchMovie.py")
    