import requests
try:
    Pokemon_Name= (str(input('Enter Pokemon name: '))).lower()
    url=f'https://pokeapi.co/api/v2/pokemon/{Pokemon_Name}'

    pokemondata = (requests.get(url)).json()
    
    print(f'\nPokemon Name: {Pokemon_Name} \n')
    
#'''TYPE'''
    type_pokemon=[]
    type_no=1
    for x in (range(len(pokemondata['types']))):
        type_pokemon.append(pokemondata['types'][x]['type']['name'])
    for j in (type_pokemon):
        print(f'Type {type_no}: {j}')
        type_no+=1
        
#'''IMAGE'''        
    Image=(pokemondata['sprites']['front_default'])
    print(f'\nTo see the pokemon, \nclick the link: \n{Image}\n')
    
#'''ABILITIES'''        
    abil=[]
    abil_no=1
    for x in (range(len(pokemondata['abilities']))):
        abil.append(pokemondata['abilities'][x]['ability']['name']) 
    for j in abil:
        print (f'Abilities {abil_no}: {j}')
        abil_no+=1

#'''POKEMON STATUS'''
    print('\n\nPokemon Status: ')   
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