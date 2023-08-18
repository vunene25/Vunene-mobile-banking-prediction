
import streamlit as st
import pickle


#Function to load the selected model
def load_model(model_name): 
	model_path = f'{model_name}.pkl'
	with open(model_path, 'rb') as file: 
		model = pickle.load(file) 
	return model 


def main(): 
	# Title of the web app 
	st.title('Mobile Banking Prediction') 

# Subheader 
	st.subheader('Please select a model and input features for prediction.') 

# Dropdown to select the model 
model_options = ['LinearRegression', 'DecisionTreeRegressor', 'KNN'] 
selected_model = st.selectbox('Select Model', model_options)

# Load the selected model 
model = load_model(selected_model) 

# User input for features 
st.header('Feature Input') 
feature1 = st.number_input('Country_code', value=0.0) 
feature2 = st.number_input('Age', value=0.0) 
feature3 = st.number_input('Has debit card', value=0.0) 
feature4 = st.number_input('Informal Save', value=0.0)
feature5 = st.number_input('Salary for 12m', value=0.0) 
feature6 = st.number_input('Has bank a/c', value=0.0) 

# Button for predictions 
clicked = st.button('Get Predictions') 

# Perform predictions when the button is clicked 
if clicked: 
	# Perform predictions using the selected model 
	prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6]]) 

# Dummy value for testing
prediction = [1]

# Display the prediction result
st.header('Prediction')

# Convert the prediction to "Yes" or "No"
prediction_result = "Yes" if prediction[0] == 1 else "No"

# Display the result
st.write(f'Has mobile/internet banking? : {prediction_result}')


if __name__ == '__main__':
	main()

