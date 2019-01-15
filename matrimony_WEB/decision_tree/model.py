import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import euclidean_distances
from app.models import Users

def get_match(info,prefrences):
    persons_data = pd.read_csv('./decision_tree/matrimony_labelled_data.csv')
    print(str(info.Gender).split('.')[1])
    if str(info.Gender).split('.')[1] == "Male":
        persons_data = persons_data[persons_data['gender']=='F']
    else: 
        persons_data = persons_data[persons_data['gender']=='F']
 
    attributes = ['marital_status','religion','language','country','food_preferences','drinks','smokes','skin_tone','build']
    for prefrence in str(prefrences).split(','):
        for a in attributes:
            if (a+"Didnt_Matter")==prefrence:
                attributes.remove(a)
    encoder = LabelEncoder()
    training_data = pd.DataFrame()
    category = persons_data.category
    classifier = DecisionTreeClassifier(criterion='entropy',min_samples_split=10,max_features='auto')
    testing_data = [str(info.Marital_Status).split('.')[1],str(info.Religion).split('.')[1],str(info.Language).split('.')[1],str(info.Country).split('.')[1],str(info.Language).split('.')[1],str(info.Drinks).split('.')[1],str(info.Smokes).split('.')[1],str(info.Skin_Tone).split('.')[1],str(info.Build).split('.')[1]]
    persons_data = persons_data[attributes]
    
    real_person_data = Users.query.all()

    print(info.First_Name)
    for person_ in real_person_data:
        temp = [str(person_.Marital_Status).split('.')[1], str(person_.Religion).split('.')[1], str(person_.Language).split('.')[1], str(person_.Country).split('.')[1], str(person_.Language).split('.')[1], str(person_.Drinks).split('.')[1], str(person_.Smokes).split('.')[1], str(person_.Skin_Tone).split('.')[1], str(person_.Build).split('.')[1]]
        if person_.First_Name != info.First_Name:
            persons_data.append(pd.Series(temp, index=attributes), ignore_index=True)

    persons_data = persons_data.append(pd.Series(testing_data,index=attributes),ignore_index=True)
    for attribute in attributes:
        training_data[attribute] = encoder.fit_transform(persons_data[attribute])
    classifier.fit(training_data.iloc[:-1,:],category)
    testing_data = training_data.iloc[-1,:]
    cat = classifier.predict(np.asarray(testing_data).reshape(1,-1))
    persons_data = pd.read_csv('./decision_tree/matrimony_labelled_data.csv')

    match = persons_data[persons_data['category']==cat[0]]
    training_data = training_data.iloc[:-1,:]
    match_data = training_data[category == cat[0]]
    '''
    for person_ in real_person_data:
        temp = [str(person_.Marital_Status).split('.')[1], str(person_.Religion).split('.')[1], str(person_.Language).split('.')[1], str(person_.Country).split('.')[1], str(person_.Language).split('.')[1], str(person_.Drinks).split('.')[1], str(person_.Smokes).split('.')[1], str(person_.Skin_Tone).split('.')[1], str(person_.Build).split('.')[1]]
        if person_.First_Name != info.First_Name:
            match.append(pd.Series(temp, index=attributes), ignore_index=True)'''
    distances =  euclidean_distances(np.asarray(match_data),np.asarray(testing_data).reshape(1,-1))
    
    distances = list(distances)
    print(distances)
    nearest_match = min(distances)
    index = list(distances).index(nearest_match)
    #v_match = pd.DataFrame()
    #v_match = match.iloc[index,:]

    return match
