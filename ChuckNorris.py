import requests
import json
from datetime import datetime
from database import JokeDatabase

class ChuckNorrisAPI:
    def __init__(self):
        self.base_url = "https://api.chucknorris.io/jokes"

    def get_random_joke(self, category=None):
        endpoint = f"{self.base_url}/random"
        if category:
            endpoint += f"?category={category}"

        print("Calling endpoint:", endpoint)
        response = requests.get(endpoint)
        data = response.json()

        return data

    def get_categories(self):
        endpoint = f"{self.base_url}/categories"
        print("Calling endpoint:", endpoint)
        response = requests.get(endpoint)
        categories = response.json()

        return categories

    def search_jokes(self, query):
        endpoint = f"{self.base_url}/search?query={query}"
        print("Calling endpoint:", endpoint)
        response = requests.get(endpoint)
        data = response.json()

        return data


def main():
    chuck_norris_api = ChuckNorrisAPI()
    joke_database = JokeDatabase()

    while True:
        print("Press 1 to get a random joke")
        print("Press 2 to get a random joke from a category")
        print("Press 3 to get categories")
        print("Press 4 to search for jokes")
        print("Press 5 to display saved jokes")
        print("Press 6 to exit")

        input_option = input()

        if input_option == "1":
            joke = chuck_norris_api.get_random_joke()
            print(joke["created_at"])
            print(joke["value"])
            print(joke["url"])
            joke_database.insert_joke(joke["value"])

        elif input_option == "2":
            category = input("Enter a category: ")
            joke = chuck_norris_api.get_random_joke(category)
            print(joke["created_at"])
            print(joke["value"])
            print(joke["url"])
            joke_database.insert_joke(joke["value"])

        elif input_option == "3":
            categories = chuck_norris_api.get_categories()
            print("Available categories:")
            for category in categories:
                print(category)

        elif input_option == "4":
            search_query = input("Enter a search query: ")
            search_results = chuck_norris_api.search_jokes(search_query)
            print(f"Found {search_results['total']} matching jokes:")
            for joke in search_results['result']:
                print(joke['value'])
                joke_database.insert_joke(joke["value"])

        elif input_option == "5":
            jokes = joke_database.get_jokes()
            for joke in jokes:
                print(joke)

        elif input_option == "6":
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
