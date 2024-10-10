from flask import Flask, url_for, render_template, request 

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/input")
def render_main_q1():
    Q1 = request.args['Q1']
    Q2 = request.args['Q2']
    Q3 = request.args['Q3']
    # Hot meals
    if Q1 == "Meal" and Q2 == "Hot" and Q3 == "Sweet":
        answer = "Teriyaki Chicken"
        #image = "Teriyaki-Chicken.jfif"
        
    if Q1 == "Meal" and Q2 == "Hot" and Q3 == "Spicy":
        answer = "Chicken Kurry Katsu"   
     
    if Q1 == "Meal" and Q2 == "Hot" and Q3 == "Sour":
        answer = "Subata"
    
    if Q1 == "Meal" and Q2 == "Hot" and Q3 == "Bitter":
        answer = "Goya Champuru"
     
    if Q1 == "Meal" and Q2 == "Hot" and Q3 == "Salty":
        answer = "Ramen" 
        # Cold meals
    if Q1 == "Meal" and Q2 == "Cold" and Q3 == "Sweet":
        answer = "Soba Noodles with dipping sauce"  

    if Q1 == "Meal" and Q2 == "Cold" and Q3 == "Spicy":
        answer = "Sushi with wasabi"
        
    if Q1 == "Meal" and Q2 == "Cold" and Q3 == "Sour":
        answer = "Sushi with ginger"   
     
    if Q1 == "Meal" and Q2 == "Cold" and Q3 == "Bitter":
        answer = "Natto"
        
    if Q1 == "Meal" and Q2 == "Cold" and Q3 == "Salty":
        answer = "Uni Sushi"
     
     # Hot snacks
    if Q1 == "Snack" and Q2 == "Hot" and Q3 == "Sweet":
        answer = "Yakitori"
        
    if Q1 == "Snack" and Q2 == "Hot" and Q3 == "Spicy":
        answer = "Koikeya Karamucho Spicy Chips"   
     
    if Q1 == "Snack" and Q2 == "Hot" and Q3 == "Sour":
        answer = "Rice crackers with umeboshi"
    
    if Q1 == "Snack" and Q2 == "Hot" and Q3 == "Bitter":
        answer = "KushiKatsu with Matcha Salt"
     
    if Q1 == "Snack" and Q2 == "Hot" and Q3 == "Salty":
        answer = "Takoyaki" 
        # Cold snacks
    if Q1 == "Snack" and Q2 == "Cold" and Q3 == "Sweet":
        answer = "Tofu"  

    if Q1 == "Snack" and Q2 == "Cold" and Q3 == "Spicy":
        answer = "Onigiri with Spicy Tuna"
        
    if Q1 == "Snack" and Q2 == "Cold" and Q3 == "Sour":
        answer = "Onigiri with Umeboshi"   
     
    if Q1 == "Snack" and Q2 == "Cold" and Q3 == "Bitter":
        answer = "Sansai"
        
    if Q1 == "Snack" and Q2 == "Cold" and Q3 == "Salty":
        answer = "Pickled cucumbers with soy sauce"
    
    # Hot desserts
    if Q1 == "Dessert" and Q2 == "Hot" and Q3 == "Sweet":
        answer = "Japanese Cheesecake"
        
    if Q1 == "Dessert" and Q2 == "Hot" and Q3 == "Spicy":
        answer = "Ginger-spiced Dorayaki"   
     
    if Q1 == "Dessert" and Q2 == "Hot" and Q3 == "Sour":
        answer = "Yuzu Daifuku"
    
    if Q1 == "Dessert" and Q2 == "Hot" and Q3 == "Bitter":
        answer = "Kurogama Purin"
     
    if Q1 == "Dessert" and Q2 == "Hot" and Q3 == "Salty":
        answer = "Kurogama Zenzai" 
        # Cold desserts
    if Q1 == "Dessert" and Q2 == "Cold" and Q3 == "Sweet":
        answer = "Matcha Ice Cream"  

    if Q1 == "Dessert" and Q2 == "Cold" and Q3 == "Spicy":
        answer = "Wasabi Kit-Kat"
        
    if Q1 == "Dessert" and Q2 == "Cold" and Q3 == "Sour":
        answer = "Sour Japanese Candy"   
     
    if Q1 == "Dessert" and Q2 == "Cold" and Q3 == "Bitter":
        answer = "Meiji Dark Chocolate"
        
    if Q1 == "Dessert" and Q2 == "Cold" and Q3 == "Salty":
        answer = "Sakura Dark Chocolate"
          
      
    return render_template('input.html', response = answer, )
    
    

if __name__=="__main__":
    app.run(debug=True)
