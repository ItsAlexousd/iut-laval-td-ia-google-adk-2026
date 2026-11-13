"""
Agent conversationnel pour La Bonne Fourchette
Assistant de commande de restaurant utilisant Google ADK
"""

from typing import Optional

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext

# Load environment variables
load_dotenv()

# Menu du restaurant
MENU = {
    "burgers": {
        "burger_classique": {
            "nom": "Burger Classique",
            "prix": 12.50,
            "description": "Steak haché, salade, tomate, oignon, cornichons",
        },
        "burger_cheese": {
            "nom": "Cheeseburger",
            "prix": 13.50,
            "description": "Burger classique avec fromage cheddar",
        },
        "burger_veggie": {
            "nom": "Burger Végétarien",
            "prix": 11.50,
            "description": "Steak végétal, légumes frais",
        },
    },
    "boissons": {
        "coca": {"nom": "Coca-Cola", "prix": 3.50, "description": "Coca-Cola 33cl"},
        "coca_zero": {
            "nom": "Coca-Cola Zero",
            "prix": 3.50,
            "description": "Coca-Cola Zero 33cl",
        },
        "fanta": {"nom": "Fanta", "prix": 3.50, "description": "Fanta Orange 33cl"},
        "eau": {"nom": "Eau", "prix": 2.50, "description": "Eau minérale 50cl"},
        "biere": {
            "nom": "Bière pression",
            "prix": 4.50,
            "description": "Bière pression 25cl",
        },
    },
    "desserts": {
        "tiramisu": {"nom": "Tiramisu", "prix": 5.50, "description": "Tiramisu maison"},
        "fondant_chocolat": {
            "nom": "Fondant au chocolat",
            "prix": 6.00,
            "description": "Fondant au chocolat avec glace vanille",
        },
        "tarte_citron": {
            "nom": "Tarte au citron",
            "prix": 5.00,
            "description": "Tarte au citron meringuée",
        },
    },
    "accompagnements": {
        "frites": {"nom": "Frites", "prix": 4.00, "description": "Frites maison"},
        "frites_cheddar": {
            "nom": "Frites au cheddar",
            "prix": 5.50,
            "description": "Frites avec sauce cheddar",
        },
        "salade": {
            "nom": "Salade verte",
            "prix": 3.50,
            "description": "Salade verte avec vinaigrette",
        },
    },
}


# Création de l'agent racine
root_agent = LlmAgent(
    model="gemini-3.8-flash",
    name="restaurant_agent",
    description="",
    instruction="",
    tools=[],
)
