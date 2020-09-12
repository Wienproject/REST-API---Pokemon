import requests
try:
    Pokemon_Name= (str(input('Enter Pokemon name: '))).lower()
    url=f'https://pokeapi.co/api/v2/pokemon/{Pokemon_Name}'

    pokemondata = (requests.get(url)).json()
    
    print('\nPokemon Name:', Pokemon_Name)
    
    for x in pokemondata['types']:
        TYPE=(x['type']['name'])
        print(f'\nPokemon Type: {TYPE}\n')
        
    Image=(pokemondata['sprites']['front_default'])
    print(f'\nTo see the pokemon, \nclick the link: {Image}\n')
        
    abil=[]
    abil_no=1
    for x in (range(len(pokemondata['abilities']))):
        abil.append(pokemondata['abilities'][x]['ability']['name']) 
    for j in abil:
        print (f'Abilities {abil_no}: {j}')
        abil_no+=1

    print('\nPokemon Status: ')   
    HP= pokemondata['stats'][0]['base_stat']
    print(f'HP: {HP}')
    Attack=pokemondata['stats'][1]['base_stat']
    print(f'Attack: {Attack}')
    Defense=pokemondata['stats'][2]['base_stat']
    print(f'Defense: {Defense}')
    Speed=pokemondata['stats'][5]['base_stat']
    print(f'Speed: {Speed}')

except:
    print('Wrong Pokemon Name !!')