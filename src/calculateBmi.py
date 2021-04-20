class Person():
    """
    person class to calculate bmi , category and health
    """
    
    def __init__ ( self , height , weight ):
        self.height = height
        self.weight = weight
        self.category = None

    def calculate_bmi( self ):
        """
        bmi = weight / ( height ^ 2)
        given (
            height in cm
            weight in kg
        )     
        """
        self.bmi = ( 
            self.weight / ((0.01*self.height )**2)
        )
         
    def set_category_and_health_risk(self):
        """
        decides the value of category and
        health according to bmi value
        """
        if   self.bmi <= 18.4 :
             self.category = "Underweight"
             self.health = "malnutrition risk"

        elif 18.5 <= self.bmi <= 24.9:
             self.category = "Normal weight"
             self.health = "Low risk"

        elif 25 <= self.bmi <= 29.9:
             self.category = "Overweight"
             self.health = "Enhanced risk"

        elif 30 <= self.bmi <= 34.9:
             self.category = "Moderately obese"
             self.health = "Medium risk"

        elif 35 <= self.bmi <= 39.9:
             self.category  = "Severely obese"
             self.health = "High risk"

        elif self.bmi >= 40 :
             self.category = "Very severely obese"
             self.health = "Very high risk"


  
def count_overweight(bmi_objects_list):
    """
    count total overweight people
    """
    total_over_weight_count = 0
    for bmi in bmi_objects_list :
        if bmi.category == "Overweight":
            total_over_weight_count += 1

    return total_over_weight_count

  

def create_bmi_objects_list(json_objects_list):
    """
    takes list of person dictionaries
    and create list of objects after bmi calculation
    """
    bmi_objects_list = []

    for person in json_objects_list :
   
      person_obj = Person ( 
           height = person['HeightCm'] , 
           weight = person['WeightKg']
      )
     
      person_obj.calculate_bmi()
      person_obj.set_category_and_health_risk()
      
      bmi_objects_list.append (
          person_obj
      )
    
    return bmi_objects_list





     
  
    
            
        
               


           

