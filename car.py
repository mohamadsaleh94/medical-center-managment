class Car:
  """Car Object
  """      
  def __init__(self):
      self.name = 'Mercedes'
      self.model = '1998'
      self.velocity = 0


  def accelerate(self, acceleration, time):
    """increase the velocity of the car, by the value acceleration * time.
    Args:
        acceleration ([float]): the acceleration value
        time ([time]): the time of the acceleration

    """
    if not acceleration:
      raise ValueError('Acceleration should not be 0.')   
    self.velocity += acceleration * time   

# define a crv car.
crv = Car()
crv.accelerate(10, 10)

print(crv.velocity)






