import matplotlib.pyplot
import numpy

# Simple 2-D plot
y_axis = numpy.array([3, 5, 7, 9, 11, 13])
x_axis = numpy.array([0, 1, 2, 3, 4, 5])
print('X-Axis: ', x_axis)
print('Y-Axis: ', y_axis)

#matplotlib.pyplot.plot(data_on_x_axis, data_on_y_axis)
matplotlib.pyplot.plot(x_axis, y_axis)
matplotlib.pyplot.ylabel('Random numbers')
matplotlib.pyplot.xlabel('Index')
matplotlib.pyplot.show()
matplotlib.pyplot.close()

# Plotting styles
# matplotlib.pyplot.plot(data_on_x_axis, data_on_y_axis, '<color><character>')
# Refer https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html to
# learn more about the plotting styles
matplotlib.pyplot.plot(x_axis, y_axis, 'g*')
matplotlib.pyplot.ylabel('Random numbers')
matplotlib.pyplot.xlabel('Index')
matplotlib.pyplot.show()


# Plotting more than one plot at the same figure
new_array = numpy.arange(-10, 10, 2)
matplotlib.pyplot.plot(new_array, new_array, 'kx', new_array,
                       new_array*2, 'g*', new_array, new_array*3, 'r+')
matplotlib.pyplot.ylabel('A function of new_array')
matplotlib.pyplot.xlabel('Index')
matplotlib.pyplot.show()

# Line properties
# matplotlib.pyplot.plot(data_on_x_axis, data_on_y_axis, <property>=<value>)
# Refer https://matplotlib.org/2.0.1/api/lines_api.html to
# learn more about the line properties
matplotlib.pyplot.plot(new_array, new_array*3, linewidth=5.0)
matplotlib.pyplot.ylabel('A function of new_array')
matplotlib.pyplot.xlabel('Index')
matplotlib.pyplot.show()

# Adding text to plots


# Multiple figures(Subplots)
# Sinusoidal signals example
# func1(t) = sin(2 * pi * t)
# func2(t) = cos(2 * pi * t)
time_array = numpy.arange(0.0, 2.0, 0.01)
func1 = numpy.sin(2 * numpy.pi * time_array)
func2 = numpy.cos(2 * numpy.pi * time_array)
matplotlib.pyplot.figure(1)
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(time_array, func1)
matplotlib.pyplot.ylabel('$func_{1}(t) = sin(2 * \pi * t)$')
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(time_array, func2)
matplotlib.pyplot.ylabel('$func_{2}(t) = cos(2 * \pi * t)$')
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.show()
