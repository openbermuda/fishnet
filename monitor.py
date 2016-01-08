import sense_hat

def stats(hat):
    while True:
        yield "Temp: %4.1f" % hat.temp
        yield "humidity: %4.0f" % hat.humidity
        yield "pressure: %4.0f" % hat.pressure

hat = sense_hat.SenseHat()

for message in stats(hat):
    hat.show_message(message)
