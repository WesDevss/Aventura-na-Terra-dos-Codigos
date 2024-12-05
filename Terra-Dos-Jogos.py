import random
import math

# Dados do jogador
player = {
    "name": "",
    "health": 100,
    "inventory": [],
    "location": "casa"
}

# Mapear cenários
locations = {
    "casa": "Você está em casa. Quer sair para explorar?",
    "floresta": "Você chegou a uma floresta misteriosa. Algo está se mexendo nos arbustos.",
    "caverna": "Uma caverna escura. Você ouve sons estranhos.",
    "castelo": "Um castelo abandonado, cheio de tesouros... ou armadilhas?"
}

# Função: exibir status
def show_status():
    print(f"\n=== Status ===")
    print(f"Nome: {player['name']}")
    print(f"Vida: {player['health']}")
    print(f"Inventário: {', '.join(player['inventory']) if player['inventory'] else 'vazio'}")
    print(f"Localização: {player['location']}")
    print("================\n")

# Função: movimentar-se
def move():
    print("Escolha para onde ir: casa, floresta, caverna, castelo")
    choice = input("Digite o local: ").lower()
    if choice in locations:
        player["location"] = choice
        print(locations[choice])
    else:
        print("Local inválido!")

# Função: coletar itens
def collect_item():
    items = ["espada", "escudo", "poção", "ouro"]
    item = random.choice(items)
    player["inventory"].append(item)
    print(f"Você encontrou um(a) {item}!")

# Função: batalha simples
def battle():
    enemy_health = random.randint(20, 50)
    print(f"Um inimigo apareceu! Ele tem {enemy_health} de vida.")
    while enemy_health > 0 and player["health"] > 0:
        action = input("Quer atacar ou fugir? (atacar/fugir): ").lower()
        if action == "atacar":
            damage = random.randint(10, 30)
            enemy_damage = random.randint(5, 15)
            enemy_health -= damage
            player["health"] -= enemy_damage
            print(f"Você causou {damage} de dano. O inimigo causou {enemy_damage} de dano.")
        elif action == "fugir":
            print("Você fugiu!")
            break
        else:
            print("Comando inválido.")
    if enemy_health <= 0:
        print("Você derrotou o inimigo!")
        collect_item()
    elif player["health"] <= 0:
        print("Você morreu. Fim de jogo!")

# Função principal
def start_game():
    print("Bem-vindo à Terra dos Códigos!")
    player["name"] = input("Qual é o seu nome, aventureiro? ")
    while True:
        show_status()
        print("Escolha uma ação: mover, coletar, batalhar, sair")
        action = input("Digite sua ação: ").lower()
        if action == "mover":
            move()
        elif action == "coletar":
            collect_item()
        elif action == "batalhar":
            battle()
        elif action == "sair":
            print("Obrigado por jogar!")
            break
        else:
            print("Ação inválida.")

# Iniciar o jogo
if __name__ == "__main__":
    start_game()
