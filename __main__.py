import pulumi 
import pulumi_docker as docker 

frontend = docker.Container( 
    "web-container", 
    image="gabiribeiro/web-escola:latest", 
    ports=[ 
        { 
            "internal": 80,       
            "external": 8042,    
        } 
    ] 
) 
