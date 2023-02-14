class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin="{:0.5f}".format(celsius+273.15)
        Fahrenheit = "{:0.5f}".format(celsius * 1.80 + 32.00)
        li=[float(Kelvin),float(Fahrenheit)]
        return li
