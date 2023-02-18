class pizzaSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def preparePizza(self, pizza_style):
        if pizza_style == "bacon":
            print("Preparing bacon pizza")
        elif pizza_style == "salami":
            print("Preparing salami pizza")

pizza_Singleton = pizzaSingleton