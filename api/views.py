from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import Response as DRFResponse
from .views import Response
from bson import ObjectId
import pymongo

# Connect to MongoDB
url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)
db = client['FormGenerator']  # Replace 'your_database_name' with the actual name of your MongoDB database

# Endpoint to create a new form in the form collection
@api_view(['POST'])
def create_form(request):
    try:
        form_data = request.data
        form_title = form_data.get('formTitle')
        components = form_data.get('components')

        # Assuming 'forms' is the collection for form information
        forms_collection = db['forms']

        # Create a new document in the forms collection for the new form
        form_document = {
            'form_title': form_title,
            'components': components if components else [],  # Ensure components is not None
            # Add more form details as needed
        }
        inserted_document = forms_collection.insert_one(form_document)

        return Response({'message': f'Form {form_title} created successfully with ID: {inserted_document.inserted_id}'})
    except Exception as e:
        return Response({'message': f'Error creating form: {str(e)}'}, status=500)


# Endpoint to add responses to the responses collection
@api_view(['POST'])
def add_responses(request):
    form_id = request.data.get('form_id')  # Get the form ID
    responses = request.data.get('responses')  # Get responses data from frontend

    # Assuming 'responses' is the collection for responses
    responses_collection = db['responses']

    # Insert responses into the collection
    responses_collection.insert_one({
        'form_id': form_id,
        'responses': responses,
    })

    return Response({'message': f'Responses added for Form ID: {form_id} successfully'})
'''

@api_view(['POST'])
def add_responses(request):
    form_id = request.data.get('form_id')  # Get the form ID
    responses = request.data.get('responses')  # Get responses data from frontend

    # Assuming 'responses' is the collection for responses
    responses_collection = db['responses']

    # Transform responses data to store questions instead of types
    transformed_responses = []
    for response in responses:
        question = response.get('name')  # Assuming the question is stored in 'name'
        answer = response.get('value')
        transformed_responses.append({
            'question': question,
            'answer': answer,
        })

    # Insert transformed responses into the collection
    responses_collection.insert_one({
        'form_id': form_id,
        'responses': transformed_responses,
    })

    return Response({'message': f'Responses added for Form ID: {form_id} successfully'})
'''
@api_view(['DELETE'])
def delete_form(request, form_id):
    try:
        # Validate ObjectID
        if not ObjectId.is_valid(form_id):
            return DRFResponse({'message': 'Invalid ObjectID format'}, status=400)

        # Assuming 'forms' is the collection for form information
        forms_collection = db['forms']

        # Delete the form with the specified ID
        result = forms_collection.delete_one({'_id': ObjectId(form_id)})

        if result.deleted_count == 1:
            return DRFResponse({'message': f'Form with ID {form_id} deleted successfully'})
        else:
            return DRFResponse({'message': f'Form with ID {form_id} not found'}, status=404)

    except Exception as e:
        return DRFResponse({'message': f'Error deleting form: {str(e)}'}, status=500)