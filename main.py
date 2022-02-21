# diagram.py
from diagrams import Diagram,Cluster
from diagrams.azure.compute import VM
from diagrams.azure.database import SQLVM
from diagrams.azure.network import LoadBalancers

with Diagram("Simple AZ Diagram", show=False):
    lb1 = LoadBalancers("LB")
    lb2 = LoadBalancers("LB")

    with Cluster("Tier 1"):
        firstTier = [VM("Webserver 1"),VM("Webserver 2"), VM("Webserver 3"),]
    with Cluster("Tier 2"):
        secondTier = [VM("Logic 1"),VM("Logic 2"),VM("Logic 3"),]
    with Cluster("Tier 3"):
        thirdTier = [SQLVM("DB 1"),SQLVM("DB 2"),SQLVM("DB 3"),]
    
    firstTier >> lb1 >> secondTier >> lb2 >> thirdTier    
    
