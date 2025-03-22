import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FiveSim:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {os.getenv("API_KEY")}",
            "Access": "application/json"
        }
    
    def get_balance(self):
        result = requests.get("https://5sim.net/v1/user/profile", headers=self.headers).json()
        return result["balance"]
    
    def purchase(self, country, operator, product):
        res = requests.get(f"https://5sim.net/v1/user/buy/activation/{country}/{operator}/{product}", headers=self.headers)
        result = res.json()
        if res.status_code == 200:
            return result["id"], result["phone"], result["operator"], result["price"]
        return self.handle_error(res)
        
    def get_code(self, id):
        res = requests.get(f"https://5sim.net/v1/user/check/{id}", headers=self.headers)
        result = res.json()
        if res.status_code == 200:
            try:
                return result["sms"]["code"]
            except:
                return None
        return self.handle_error(res)

    def cancel(self, id):
        res = requests.get(f"https://5sim.net/v1/user/cancel/{id}", headers=self.headers)
        if res.status_code == 200:
            return "Canceled"
        return self.handle_error(res)
    
    def ban(self, id):
        res = requests.get(f"https://5sim.net/v1/user/ban/{id}", headers=self.headers)
        if res.status_code == 200:
            return "Banned"
        return self.handle_error(res)
    
    def handle_error(self, res):
        match res.status_code:
            case 400:
                return "Bad Request"
            case 404:
                return "Order Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return "Something Went Wrong"