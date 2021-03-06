#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 Fall 2018
# Assignment: Classwork 11
###

import numpy as np
import matplotlib.pyplot as plt

"""This module explores the different techniques of solving a differential equation with the initial condition v(0) = 0 and x(0) = 1 and x'(t) = v(t), v'(t) = -x'(t)
Techniques include Euler's method, Huen's method and both the 2nd and 4th order Runge-Kutta Methods
"""
def euler():
    """ Plots the solution to the differential equation with the given initial conditions to verify they equal sin(x) and cos(x) using Euler's Method
    """
    t = np.linspace(0.0, 5*2*np.pi, 1000, dtype = float)
    

    x = np.zeros_like(t)
    v = np.zeros_like(t)
    
    x[0]= 1
    v[0] = 0
    s = len(t)
    
    r = np.zeros((2,s))
    for i in range(s-1):
        x[i+1] = x[i] + (t[i+1]-t[i])*v[i]
        r[0,i]= x[i]
        v[i+1] = v[i] + (t[i+1]-t[i])*-x[i]
        r[1,i] = v[i]

    fig = plt.figure(figsize = (12,8))
    cartesian = plt.axes()
    
    cartesian.plot(t, r[0], 'b', label = "$u(t)$")
    cartesian.plot(t, r[1], 'r', label = "$v(t)$")

    cartesian.legend()
    plt.show()


def huen():
    """ Plots the solution to the differential equation with the given initial conditions to verify they equal sin(x) and cos(x) using Huen's Method
    """
    t = np.linspace(0, 5*2*np.pi, 1000, dtype = float)
    
    x = np.zeros_like(t)
    v = np.zeros_like(t)
    
    x[0] = 1
    v[0] = 0
    s = len(t)
    r = np.zeros((2, s))
    
    for i in range(s-1):
        ui = x[i] + (t[i+1]-t[i])*v[i]
        vi = v[i] + (t[i+1]-t[i])*-x[i]
        x[i+1] = x[i] + (t[i+1]/2 - t[i]/2)*(v[i]+vi)
        v[i+1] = v[i] + (t[i+1]/2 - t[i]/2)*(-x[i]-ui)
        r[0,i] = x[i]
        r[1,i] = v[i]

    fig = plt.figure(figsize = (12,8))
    cartesian = plt.axes()
    
    cartesian.plot(t, r[0], 'b', label = "$u(t)$")
    cartesian.plot(t, r[1], 'r', label = "$v(t)$")
    
    cartesian.set(ylim = (-2,2))
    cartesian.legend()
    plt.show()
    
def rk2():
    """ Plots the solution to the differential equation with the given initial conditions to verify they equal sin(x) and cos(x) using Runge-Kutta's 2nd Order Method
    """
    t = np.linspace(0, 5*2*np.pi, 1000, dtype = float)
    x = np.zeros_like(t)
    v = np.zeros_like(t)
    
    x[0] = 1
    v[0] = 0
    s = len(t)
    
    r = np.zeros((2, s))
    for i in range(s-1):
        k1x = (t[i+1]/2 - t[i]/2)*v[i]
        k1v = (t[i+1]/2 - t[i]/2)*(-x[i])
        k2x = (t[i+1]/2 - t[i]/2)*(v[i] + k1v/2)
        k2v = (t[i+1]/2 - t[i]/2)*(-x[i] + k1x/2)
        x[i+1] = x[i] + k2x
        v[i+1] = v[i] + k2v
        r[0,i] = x[i]
        r[1,i] = v[i]
        
    fig = plt.figure(figsize = (12,8))
    cartesian = plt.axes()
    
    cartesian.plot(t, r[0], 'b', label = "$u(t)$")
    cartesian.plot(t, r[1], 'r', label = "$v(t)$")

    cartesian.legend()
    plt.show()

        
def rk4():
    """ Plots the solution to the differential equation with the given initial conditions to verify they equal sin(x) and cos(x) using Runge-Kutta's 4th Order Method
    """
    t = np.linspace(0, 5*2*np.pi, 1000, dtype = float)
    x = np.zeros_like(t)
    v = np.zeros_like(t)
                    
    x[0] = 1
    v[0] = 0
    s = len(t)
    
    r = np.zeros((2, s))
    for i in range(s-1):
        k1x = (t[i+1]/2 - t[i]/2)*v[i]
        k1v = (t[i+1]/2 - t[i]/2)*(-x[i])
        k2x = (t[i+1]/2 - t[i]/2)*(v[i] + k1v/2)
        k2v = (t[i+1]/2 - t[i]/2)*(-x[i] + k1x/2)
        k3x = (t[i+1]/2 - t[i]/2)*(v[i] + k2v/2)
        k3v = (t[i+1]/2 - t[i]/2)*(-x[i] + k2x/2)
        k4x = (t[i+1]/2 - t[i]/2)*(v[i]+k3v)
        k4v = (t[i+1]/2 - t[i]/2)*(-x[i]+k3x)
        x[i+1] = x[i] + (k1x + 2*k2x + 2*k3x + k4x)/6
        v[i+1] = v[i] + (k1v + 2*k2v + 2*k3v +k4v)/6
        r[0,i] = x[i]
        r[1,i] = v[i]
        
        
    fig = plt.figure(figsize = (12,8))
    cartesian = plt.axes()
    
    cartesian.plot(t, r[0], 'b', label = "$u(t)$")
    cartesian.plot(t, r[1], 'r', label = "$v(t)$")

    cartesian.legend()
    plt.show()
