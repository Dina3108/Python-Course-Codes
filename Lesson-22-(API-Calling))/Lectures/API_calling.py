import requests
base_url='https://pokeapi.co/api/v2/'
def api_calling(name):
    url=f'{base_url}/pokemon/{name}'
    #in requests module using the get function , HTTP from the server side will send us a response with HTTP status code as object and also retrives the data from the API server we have called
    response=requests.get(url)
    print(response)
api_calling('pikachu')


def api_data_retrival(name):
    response=requests.get(f'{base_url}/pokemon/{name}')
    #below status code attribute from the requests object will give us the HTTP status code from the server side
    #if HTTP code is 200 means the server is found, reponse was successful and data can be retrieved
    if response.status_code == 200:
        #using the json method we can fetch the data retrived as dictionary with keys and values
        return response.json()
    else:
        print(f'Failed to retrive data {response.status_code}')
#print(api_data_retrival('pikachu'))
name='pikachu'
api_data=api_data_retrival(name) 

#if api_data is fetched and got stored means
if api_data:
    #getting the particular data from the api using the keys from the dictionary
    print(f'Name : {api_data['name'].capitalize()}')
    print(f'ID : {api_data['id']}')
    print(f'Height : {api_data['height']}')
    print(f'Weight : {api_data['weight']}')

# Above is the base to fetch data from an API 