from searchMovie import searchByCategory, searchByYear, searchByWinner, searchByName, data
import json

#test search by name

# x=searchByName("Titanic", data)
# jsonTest = [{'year': 1953, 'category': ['ART DIRECTION (Black-and-White)', 'WRITING (Story and Screenplay)', 'ACTRESS IN A LEADING ROLE', 'ACTRESS IN A SUPPORTING ROLE', 'ART DIRECTION', 'CINEMATOGRAPHY', 'COSTUME DESIGN', 'DIRECTING', 'FILM EDITING', 'MAKEUP', 'MUSIC (Original Dramatic Score)', 'MUSIC (Original Song)', 'BEST PICTURE', 'SOUND', 'SOUND EFFECTS EDITING', 'VISUAL EFFECTS'], 'name': 'Art Direction:  Lyle Wheeler, Maurice Ransford;  Set Decoration:  Stuart Reiss', 'film': 'Titanic', 'winner': False}]
# if( x == x ):     
    # resultsDict={}
    # arr=[]
    # for i in range(0,len(data)):
        # val = data[i]['film']
        # if "Titanic".upper() in val.upper():
            # if not val in resultsDict:
                # resultsDict[val]=data[i]
                # if not type(resultsDict[val]['category']) is list:
                    # resultsDict[val]['category']=[resultsDict[val]['category']]
                # arr.append(data[i])
    # if(jsonTest == x):
        # print("pass")
    # else:
        # print("fail")

x=searchByName("Titanic", data)
jsonTest = [{'year': 1953, 'category': ['ART DIRECTION (Black-and-White)', 'WRITING (Story and Screenplay)', 'ACTRESS IN A LEADING ROLE', 'ACTRESS IN A SUPPORTING ROLE', 'ART DIRECTION', 'CINEMATOGRAPHY', 'COSTUME DESIGN', 'DIRECTING', 'FILM EDITING', 'MAKEUP', 'MUSIC (Original Dramatic Score)', 'MUSIC (Original Song)', 'BEST PICTURE', 'SOUND', 'SOUND EFFECTS EDITING', 'VISUAL EFFECTS'], 'name': 'Art Direction:  Lyle Wheeler, Maurice Ransford;  Set Decoration:  Stuart Reiss', 'film': 'Titanic', 'winner': False}] 
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
