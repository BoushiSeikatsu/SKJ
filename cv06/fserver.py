from xmlrpc.server import SimpleXMLRPCServer

class Forecast(object):
    """
    Reprezentuje predpoved. V instancnich promennych jsou reprezentovany hodnoty
    predpovedi.
    """

    def __init__(self, description, wind_force, temperature):
        """
        Konstuktor predpovedi. Instancni promenne reprezentuji predana data.
        """
        self.description = description
        self.wind_force = wind_force
        self.temperature = temperature
        pass

    def get_list(self):
        """
        Vraci trojici reprezentujici predpoved.
        """
        return (self.description, self.wind_force, self.temperature)
        pass

class ForecastCalendar(object):
    """
    Reprezentuje predpovedi pro nekolik dni. Data predpovedi jsou ulozena ve
    slovniku. Klicem je datum, hodnotou pak instance trody Forecast. Vkladani
    predpovedi metodou update_forecast je chraneno heslem, ktere je predano v
    konstruktoru. Startovaci data jsou tezz predana v konstruktoru.
    """
    
    def __init__(self, initial_values, password):
        """
        Konstruktor kalendare predpovedi. Instancni promenne reprezentuji predana data.
        """
        self.data = initial_values
        self.password = password
        pass

    def get_forecast(self, date):
        """
        Vrati predpoved pro zadane datum jako retezec. V pripade, ze pro dane
        datum neexistuje predpoved. Vrati se retezec "No focecast".
        """
        if(date in self.data.keys()):
            forecast = self.data[date].get_list()
            return date + ": dnesni predpoved je->" + forecast[0] + " " + str(forecast[1]) + " " + str(forecast[2])
        else:
            return "No forecast"

    def update_forecast(self, password, date, description, wind_force, temperature):
        """
        Aktualizuje predpoved pro zadane datum. Akce je chranena heslem. Pokud
        heslo nesouhlasi s heslem, ktere je zadano v konstruktoru, neni mozno
        aktualizovat predpoved. v takovm priapde metoda vrati retezec "No
        update". Metoda muze aktualizovat stavajici predpoved nebo pridat novou.
        """
        if(self.password == password):
            self.data[date] = Forecast(description, wind_force, temperature)
            return "updates"
        else:   
            return "No update"
        
def main():

    # TODO Pridat do initial_state data predpovedi tak, aby je mohl klient
    # precist.
    initial_state = {"2012-11-05": Forecast("Padaji trakare", 2, 15), "2012-11-06": Forecast("Padaji zaby", 7, 15)}

    fcalendar = ForecastCalendar(initial_state, password = "heslo")

    server_address = ('localhost', 10006)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(fcalendar)
    server.register_introspection_functions()
    print("Starting Weather XML-RPC server, use <Ctrl-C> to stop")
    server.serve_forever()

if __name__ == "__main__":
    main()