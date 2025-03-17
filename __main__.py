import pulumi
import pulumi_docker as docker

network = docker.Network("escola-network")

def criar_container(nome, imagem, porta_interna, porta_externa):
    return docker.Container(
        nome,
        image=imagem,
        ports=[
            {
                "internal": porta_interna,
                "external": porta_externa,
            }
        ],
        networks_advanced=[{
            "name": network.name, 
        }]
    )

backend = criar_container("api-container", "gabiribeiro/api-escola:latest", 8000, 8000)
frontend = criar_container("web-container", "gabiribeiro/web-escola:latest", 80, 8042)
