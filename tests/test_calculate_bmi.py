from calculateBmi import Person , create_bmi_objects_list , count_overweight
import json
"""
unit tests for calculateBmi module
"""


def get_data():
    """
    get data from json file 'data.json' 
    """
    json_string = open('data.json','r')
    json_data = json_string.read(2000)
    json_string.close()
    return json.loads(json_data)



def test_person():

    height = get_data()[0]['HeightCm']                # person 1 height in cm
    weight = get_data()[0]['WeightKg']                # person 1 weight in kg
    person = Person ( 
        height,
        weight
    )
    
    person.calculate_bmi()
    person.set_category_and_health_risk()
    
    assert person.category == "Moderately obese" 
    assert person.health ==   "Medium risk"


 
def test_count_overweight():  
    json_objects_list = get_data()
    bmi_objects_list = create_bmi_objects_list(json_objects_list)
    assert count_overweight(bmi_objects_list) == 1
  
