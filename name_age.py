from flask import request, jsonify , Flask

app = Flask(__name__)


#Function to return a take the 'Name' from th payload and store in a local file

@app.route("/name", methods=["POST"]) # exposing this function to the route with POST method
def get_name():
    data = request.get_json()

    Name = data['Name']     #Taking the name from payload
    Age = data['Age']       #Taking the Age from payload    

    print("Name from payload is :", Name, "and type is ", type(Name))
    print("Age from payload is :", Age, "and type is ", type(Age))


    with open("names.txt", "a") as f:   #storing the name in a Names file
        f.write(Name + " and " + str(Age) + "\n")            #Writes the name in a new line in the file

# return a text message with name and age details
    return jsonify({"message": "Name and Age saved successfully"}), 200


# defining the main function
if __name__ == "__main__":
    app.run(debug=True)