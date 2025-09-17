# Define a class representing a TV
class TV:
    def __init__(self):
        # TV starts off and on channel 5
        self.on = False
        self.channel = 5

    # Method to toggle the TV power
    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    # Method to increase and decrease the channel if TV is on
    def change_channel_up(self):
        if self.on and self.channel < 100:
            self.channel += 1

    def change_channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

# Create a TV object
television = TV()

# Print if the TV is on or off
print("Is television on?: {}" .format(television.on))

# Toggle power and print status
television.power()
print("Is television on?: {}" .format(television.on))
television.power()
print("Is television on?: {}" .format(television.on))
television.power()
print("Is television on?: {}" .format(television.on))

# Print current channel
print("canal: {}" .format(television.channel))

# Increase channel 4 times
television.change_channel_up()
television.change_channel_up()
television.change_channel_up()
television.change_channel_up()

# Print current channel
print("canal: {}" .format(television.channel))

# Decrease channel 3 times
television.change_channel_down()
television.change_channel_down()
television.change_channel_down()

# Print current channel
print("canal: {}" .format(television.channel))